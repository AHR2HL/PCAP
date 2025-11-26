..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Section 5: Advanced Techniques
===============================

.. index:: advanced closures, decorator chains, introspection, functional programming

Introduction
------------

You've mastered closure basics, state management, encapsulation, and practical patterns. Now it's time to explore **advanced techniques** that professional Python developers use.

This section covers the sophisticated aspects of closures:

- **Decorators with arguments** — creating configurable decorators
- **Decorator stacking** — combining multiple decorators
- **Class decorators** — ``@property``, ``@staticmethod``, ``@classmethod``
- **Closure introspection** — examining closure internals with ``__closure__``
- **Performance considerations** — memory usage and optimization
- **Functional programming** — closures in map/filter/reduce pipelines
- **Best practices** — when to use closures vs. classes

By the end, you'll have **master-level understanding** of closures and be able to use them in sophisticated, production-ready code!

---

Decorators with Arguments
--------------------------

.. index:: parametrized decorators, decorator arguments, decorator factories

So far, we've seen simple decorators like ``@timer``. But what if you want a decorator that takes arguments, like ``@repeat(3)`` or ``@retry(max_attempts=5)``?

**The Pattern: Decorator Factory**

To create a decorator that accepts arguments, you need **three layers** of functions:

1. **Outer function** — takes decorator arguments, returns a decorator
2. **Middle function** — the actual decorator, takes the function to decorate
3. **Inner function** — the wrapper that executes when the decorated function is called

.. activecode:: closure_adv_decorator_with_args
   :language: python
   :caption: Decorator with Arguments Pattern

   def repeat(times):
       """Outer: takes decorator arguments"""

       def decorator(func):
           """Middle: the actual decorator"""

           def wrapper(*args, **kwargs):
               """Inner: executes when function is called"""
               results = []
               for i in range(times):
                   print(f"  Execution {i+1}/{times}")
                   result = func(*args, **kwargs)
                   results.append(result)
               return results

           return wrapper
       return decorator

   # Usage
   @repeat(3)
   def greet(name):
       return f"Hello, {name}!"

   results = greet("Alice")
   print(f"\nResults: {results}")

   print("\n" + "="*40 + "\n")

   # What's actually happening:
   # Step 1: repeat(3) returns decorator
   # Step 2: decorator(greet) returns wrapper
   # Step 3: greet = wrapper (greet is now the wrapper function)
   # Step 4: greet("Alice") calls wrapper("Alice")

   # Manual version (equivalent):
   def say_hi(name):
       return f"Hi, {name}!"

   say_hi = repeat(3)(say_hi)  # Two function calls!
   results = say_hi("Bob")
   print(f"Results: {results}")

**Output:**

::

     Execution 1/3
     Execution 2/3
     Execution 3/3

   Results: ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']

   ========================================

     Execution 1/3
     Execution 2/3
     Execution 3/3
   Results: ['Hi, Bob!', 'Hi, Bob!', 'Hi, Bob!']

.. important::
   **Three Layers of Closures**

   - ``@repeat(3)`` calls ``repeat(3)`` → returns ``decorator``
   - ``decorator`` wraps the function → returns ``wrapper``
   - ``wrapper`` executes when you call the decorated function

   Each layer creates a closure that captures variables from its enclosing scope!

---

**Practical Example: Configurable Retry**

.. activecode:: closure_adv_retry_with_config
   :language: python
   :caption: Retry Decorator with Configuration

   import time
   import random

   def retry(max_attempts=3, delay=0, exceptions=(Exception,)):
       """Decorator that retries on failure

       Args:
           max_attempts: Maximum number of attempts
           delay: Seconds to wait between attempts
           exceptions: Tuple of exceptions to catch
       """

       def decorator(func):
           def wrapper(*args, **kwargs):
               for attempt in range(1, max_attempts + 1):
                   try:
                       return func(*args, **kwargs)
                   except exceptions as e:
                       if attempt == max_attempts:
                           print(f"❌ Failed after {max_attempts} attempts: {e}")
                           raise
                       print(f"⚠️  Attempt {attempt} failed: {e}. Retrying...")
                       if delay > 0:
                           time.sleep(delay)
           return wrapper
       return decorator

   # Use with different configurations
   @retry(max_attempts=5, delay=0.1, exceptions=(ValueError,))
   def flaky_function():
       if random.random() < 0.6:  # 60% failure rate
           raise ValueError("Random failure!")
       return "Success! 🎉"

   @retry(max_attempts=3, exceptions=(ZeroDivisionError,))
   def divide(a, b):
       return a / b

   # Test flaky function
   result = flaky_function()
   print(result)

   # Test divide (will succeed)
   print(f"\n10 / 2 = {divide(10, 2)}")

**Output (varies due to randomness):**

::

   ⚠️  Attempt 1 failed: Random failure!. Retrying...
   ⚠️  Attempt 2 failed: Random failure!. Retrying...
   Success! 🎉

   10 / 2 = 5.0

---

**Practical Example: Configurable Cache**

.. activecode:: closure_adv_cache_with_config
   :language: python
   :caption: Cache Decorator with Size Limit

   def cache(max_size=None):
       """Decorator that caches results with optional size limit

       Args:
           max_size: Maximum cache size (None = unlimited)
       """

       def decorator(func):
           cache_dict = {}
           access_order = []  # Track access order for LRU

           def wrapper(*args):
               # Check cache
               if args in cache_dict:
                   # Move to end (most recently used)
                   access_order.remove(args)
                   access_order.append(args)
                   print(f"💾 Cache hit: {func.__name__}{args}")
                   return cache_dict[args]

               # Compute result
               print(f"⚙️  Computing: {func.__name__}{args}")
               result = func(*args)

               # Add to cache
               cache_dict[args] = result
               access_order.append(args)

               # Enforce size limit (LRU eviction)
               if max_size and len(cache_dict) > max_size:
                   evicted = access_order.pop(0)
                   del cache_dict[evicted]
                   print(f"🗑️  Evicted: {evicted}")

               return result

           return wrapper
       return decorator

   @cache(max_size=3)
   def expensive(x):
       return x ** 2

   # Fill cache
   print(expensive(1))
   print(expensive(2))
   print(expensive(3))

   # Cache hits
   print(expensive(1))
   print(expensive(2))

   # Overflow cache (should evict 3)
   print(expensive(4))

   # Try to access evicted item (cache miss)
   print(expensive(3))

**Output:**

::

   ⚙️  Computing: expensive(1,)
   1
   ⚙️  Computing: expensive(2,)
   4
   ⚙️  Computing: expensive(3,)
   9
   💾 Cache hit: expensive(1,)
   1
   💾 Cache hit: expensive(2,)
   4
   ⚙️  Computing: expensive(4,)
   🗑️  Evicted: (3,)
   16
   ⚙️  Computing: expensive(3,)
   9

.. note::
   **Python's Built-in LRU Cache**

   Python's standard library includes ``functools.lru_cache`` with this exact functionality:

   .. code-block:: python

      from functools import lru_cache

      @lru_cache(maxsize=128)
      def expensive_function(x):
          return x ** 2

   But understanding how it works with closures is valuable!

---

Decorator Stacking and Chains
------------------------------

.. index:: decorator stacking, decorator chains, multiple decorators

You can apply **multiple decorators** to a single function. They're applied **bottom-to-top** (closest to the function first).

**Basic Stacking**

.. activecode:: closure_adv_stacking_basic
   :language: python
   :caption: Stacking Multiple Decorators

   def bold(func):
       """Wrap result in **bold**"""
       def wrapper(*args, **kwargs):
           result = func(*args, **kwargs)
           return f"**{result}**"
       return wrapper

   def italic(func):
       """Wrap result in *italic*"""
       def wrapper(*args, **kwargs):
           result = func(*args, **kwargs)
           return f"*{result}*"
       return wrapper

   def uppercase(func):
       """Convert result to uppercase"""
       def wrapper(*args, **kwargs):
           result = func(*args, **kwargs)
           return result.upper()
       return wrapper

   # Stack decorators
   @bold
   @italic
   @uppercase
   def greet(name):
       return f"hello, {name}"

   print(greet("Alice"))

   # What's happening:
   # Step 1: greet = uppercase(greet)  -> returns "HELLO, ALICE"
   # Step 2: greet = italic(greet)     -> returns "*HELLO, ALICE*"
   # Step 3: greet = bold(greet)       -> returns "***HELLO, ALICE***"

**Output:**

::

   ***HELLO, ALICE***

.. important::
   **Decorator Application Order**

   Decorators are applied **bottom-to-top**:

   .. code-block:: python

      @decorator1
      @decorator2
      @decorator3
      def func():
          pass

      # Equivalent to:
      func = decorator1(decorator2(decorator3(func)))

   The decorator **closest to the function** is applied first!

---

**Practical Stacking: Timing + Logging + Caching**

.. activecode:: closure_adv_stacking_practical
   :language: python
   :caption: Combining Timing, Logging, and Caching

   import time

   def timer(func):
       """Time function execution"""
       def wrapper(*args, **kwargs):
           start = time.time()
           result = func(*args, **kwargs)
           elapsed = time.time() - start
           print(f"⏱️  {func.__name__} took {elapsed:.4f}s")
           return result
       return wrapper

   def logger(func):
       """Log function calls"""
       def wrapper(*args, **kwargs):
           print(f"📞 Calling {func.__name__}{args}")
           result = func(*args, **kwargs)
           print(f"📤 {func.__name__} returned {result}")
           return result
       return wrapper

   def memoize(func):
       """Cache results"""
       cache = {}
       def wrapper(*args):
           if args in cache:
               print(f"💾 Cache hit!")
               return cache[args]
           result = func(*args)
           cache[args] = result
           return result
       return wrapper

   @timer
   @logger
   @memoize
   def fibonacci(n):
       """Compute Fibonacci (slow without memoization)"""
       if n <= 1:
           return n
       return fibonacci(n - 1) + fibonacci(n - 2)

   print("First call to fibonacci(5):")
   print(fibonacci(5))
   print("\n" + "="*40 + "\n")

   print("Second call to fibonacci(5):")
   print(fibonacci(5))

**Output:**

::

   First call to fibonacci(5):
   📞 Calling fibonacci(5,)
   📞 Calling fibonacci(4,)
   📞 Calling fibonacci(3,)
   📞 Calling fibonacci(2,)
   📞 Calling fibonacci(1,)
   📤 fibonacci returned 1
   📞 Calling fibonacci(0,)
   📤 fibonacci returned 0
   📤 fibonacci returned 1
   💾 Cache hit!
   📤 fibonacci returned 2
   💾 Cache hit!
   📤 fibonacci returned 3
   💾 Cache hit!
   📤 fibonacci returned 5
   ⏱️  fibonacci took 0.0001s
   5

   ========================================

   Second call to fibonacci(5):
   📞 Calling fibonacci(5,)
   💾 Cache hit!
   📤 fibonacci returned 5
   ⏱️  fibonacci took 0.0000s
   5

The decorators work together: memoization speeds it up, logger shows what's happening, timer measures total time!

---

Class Decorators
----------------

.. index:: class decorators, @property, @staticmethod, @classmethod

Python has built-in class decorators that modify how class methods behave. Understanding these is crucial for writing clean, professional Python code.

---

@property — Computed Attributes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: property decorator, computed properties, getters and setters

**What is @property?**

The ``@property`` decorator allows you to define methods that act like attributes. Instead of calling ``obj.get_radius()``, you can write ``obj.radius`` — it looks like an attribute but runs method code behind the scenes!

**Why use @property?**

✅ **Clean syntax** - Access computed values like attributes
✅ **Validation** - Control what values can be set
✅ **Computed values** - Calculate on-the-fly without storing
✅ **Backwards compatibility** - Can add logic to existing attributes later

**How it works:**

.. code-block:: python

   class Example:
       @property
       def my_attr(self):
           # Getter: called when reading obj.my_attr
           return some_value

       @my_attr.setter
       def my_attr(self, value):
           # Setter: called when writing obj.my_attr = value
           # Can validate or transform the value
           pass

**Full Example:**

.. activecode:: closure_adv_property_decorator
   :language: python
   :caption: @property Decorator

   class Circle:
       def __init__(self, radius):
           self._radius = radius  # Private variable (by convention)

       @property
       def radius(self):
           """Get radius - looks like attribute access!"""
           return self._radius

       @radius.setter
       def radius(self, value):
           """Set radius with validation"""
           if value <= 0:
               raise ValueError("Radius must be positive")
           self._radius = value

       @property
       def diameter(self):
           """Computed property - calculated on demand"""
           return self._radius * 2

       @property
       def area(self):
           """Another computed property"""
           return 3.14159 * self._radius ** 2

   # Use like attributes (but they're actually methods!)
   c = Circle(5)
   print(f"Radius: {c.radius}")      # Calls radius getter
   print(f"Diameter: {c.diameter}")  # Computed on-the-fly
   print(f"Area: {c.area:.2f}")      # Not stored, calculated each time

   # Setter works too
   c.radius = 10  # Calls radius setter (with validation!)
   print(f"\nAfter changing radius to 10:")
   print(f"Diameter: {c.diameter}")  # Automatically updates!
   print(f"Area: {c.area:.2f}")

   # Validation in action
   try:
       c.radius = -5  # Setter rejects invalid value
   except ValueError as e:
       print(f"\n❌ {e}")

**Output:**

::

   Radius: 5
   Diameter: 10
   Area: 78.54

   After changing radius to 10:
   Diameter: 20
   Area: 314.16

   ❌ Radius must be positive

**Key Insights:**

.. important::

   **@property creates a closure!**

   Behind the scenes, ``@property`` stores the getter, setter, and deleter functions in a closure. When you access ``obj.radius``, Python:

   1. Looks up the property object
   2. Calls the getter function from the closure
   3. Returns the result

   This is closure-based encapsulation in action!

**When to use @property:**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - **Use @property When:**
     - **Don't Use @property When:**
   * - Value needs computation (area from radius)
     - Simple attribute storage with no logic
   * - You need validation on setting
     - Value is expensive to compute (cache instead)
   * - Converting old code (public attr → property)
     - Method takes arguments (use regular method)
   * - Read-only attributes (no setter)
     - Complex multi-step operations

---

@staticmethod — No Instance Required
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: staticmethod decorator, static methods

**What is @staticmethod?**

A ``@staticmethod`` is a method that doesn't need access to the instance (``self``) or the class (``cls``). It's just a regular function that happens to live inside a class namespace.

**Why use @staticmethod?**

✅ **Organization** - Group related functions with a class
✅ **No instance needed** - Can call without creating an object
✅ **Clear intent** - Signals "this doesn't modify instance/class state"
✅ **Utility functions** - Helper functions that belong conceptually to the class

**Comparison:**

.. code-block:: python

   class Example:
       # Regular instance method
       def instance_method(self, x):
           return self.value + x  # Needs self!

       # Static method
       @staticmethod
       def static_method(x, y):
           return x + y  # No self or cls needed!

**Think of it as:** A function that logically belongs to a class but doesn't need instance or class data.

---

@classmethod — Receives the Class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: classmethod decorator, class methods

**What is @classmethod?**

A ``@classmethod`` receives the **class itself** (not an instance) as its first argument, conventionally named ``cls``. This allows it to access class-level data and create instances.

**Why use @classmethod?**

✅ **Alternative constructors** - Create instances in different ways
✅ **Factory methods** - Build objects from different data formats
✅ **Access class attributes** - Read/modify class-level variables
✅ **Inheritance-friendly** - Works correctly in subclasses

**Common Pattern: Alternative Constructors**

.. code-block:: python

   class Date:
       def __init__(self, year, month, day):
           self.year = year
           self.month = month
           self.day = day

       @classmethod
       def from_string(cls, date_string):
           """Alternative constructor from string"""
           year, month, day = map(int, date_string.split('-'))
           return cls(year, month, day)  # cls is Date (or subclass!)

       @classmethod
       def today(cls):
           """Create instance with today's date"""
           import datetime
           today = datetime.date.today()
           return cls(today.year, today.month, today.day)

---

**Complete Comparison:**

.. activecode:: closure_adv_class_method_decorators
   :language: python
   :caption: All Three Method Types

   class MathUtils:
       pi = 3.14159  # Class attribute

       def __init__(self, name):
           self.name = name  # Instance attribute

       # INSTANCE METHOD - needs self
       def instance_method(self):
           """Has access to instance data (self)"""
           return f"Instance method called by {self.name}"

       # STATIC METHOD - needs nothing
       @staticmethod
       def add(a, b):
           """No access to instance or class - just a utility function"""
           return a + b

       # CLASS METHOD - needs cls (the class)
       @classmethod
       def circle_area(cls, radius):
           """Has access to class data (cls.pi)"""
           return cls.pi * radius ** 2

       @classmethod
       def create_default(cls):
           """Alternative constructor - returns new instance"""
           return cls("Default")

   print("="*50)
   print("STATIC METHOD - No instance needed")
   print("="*50)
   result = MathUtils.add(5, 3)  # Call directly on class
   print(f"5 + 3 = {result}")

   print("\n" + "="*50)
   print("CLASS METHOD - Uses class data")
   print("="*50)
   area = MathUtils.circle_area(5)  # Uses cls.pi
   print(f"Circle area (radius=5): {area:.2f}")

   print("\n" + "="*50)
   print("CLASS METHOD - Alternative constructor")
   print("="*50)
   obj = MathUtils.create_default()  # Creates instance
   print(f"Created: {obj.name}")

   print("\n" + "="*50)
   print("INSTANCE METHOD - Needs instance")
   print("="*50)
   obj = MathUtils("Alice")
   print(obj.instance_method())

   print("\n" + "="*50)
   print("Can call static/class methods on instance too")
   print("="*50)
   print(f"obj.add(10, 20) = {obj.add(10, 20)}")
   print(f"obj.circle_area(3) = {obj.circle_area(3):.2f}")

**Output:**

::

   ==================================================
   STATIC METHOD - No instance needed
   ==================================================
   5 + 3 = 8

   ==================================================
   CLASS METHOD - Uses class data
   ==================================================
   Circle area (radius=5): 78.54

   ==================================================
   CLASS METHOD - Alternative constructor
   ==================================================
   Created: Default

   ==================================================
   INSTANCE METHOD - Needs instance
   ==================================================
   Instance method called by Alice

   ==================================================
   Can call static/class methods on instance too
   ==================================================
   obj.add(10, 20) = 30
   obj.circle_area(3) = 28.27

---

**Visual Comparison:**

.. list-table:: Method Types at a Glance
   :widths: 20 25 25 30
   :header-rows: 1

   * - Method Type
     - First Argument
     - Access To
     - Common Use Cases
   * - **Instance Method**
     - ``self``
     - Instance & class data
     - Modify object state, use instance variables
   * - **@staticmethod**
     - (none)
     - Nothing special
     - Utility functions, helpers, pure functions
   * - **@classmethod**
     - ``cls``
     - Class data & can create instances
     - Alternative constructors, factory methods

**Decision Flowchart:**

::

   Does the method need access to instance data (self.something)?
   ├─ YES → Use regular instance method
   └─ NO ↓

      Does it need access to class data (cls.something)?
      ├─ YES → Use @classmethod
      └─ NO ↓

         Does it logically belong to this class?
         ├─ YES → Use @staticmethod
         └─ NO → Make it a module-level function

---

**Real-World Example:**

.. activecode:: closure_adv_class_decorators_real_world
   :language: python
   :caption: Real-World: Date Class

   class Date:
       def __init__(self, year, month, day):
           self.year = year
           self.month = month
           self.day = day

       # INSTANCE METHOD - uses self
       def format(self):
           """Format this date as string"""
           return f"{self.year}-{self.month:02d}-{self.day:02d}"

       # CLASS METHOD - alternative constructor
       @classmethod
       def from_string(cls, date_str):
           """Create Date from '2024-03-15' format"""
           year, month, day = map(int, date_str.split('-'))
           return cls(year, month, day)

       # CLASS METHOD - factory method
       @classmethod
       def today(cls):
           """Create Date with current date"""
           # In real code, would use datetime module
           return cls(2024, 3, 15)

       # STATIC METHOD - utility
       @staticmethod
       def is_leap_year(year):
           """Check if year is leap year"""
           return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

   # Regular constructor
   d1 = Date(2024, 3, 15)
   print(f"Regular: {d1.format()}")

   # Alternative constructor (class method)
   d2 = Date.from_string("2024-12-25")
   print(f"From string: {d2.format()}")

   # Factory method (class method)
   d3 = Date.today()
   print(f"Today: {d3.format()}")

   # Static method (no instance needed)
   print(f"Is 2024 leap year? {Date.is_leap_year(2024)}")
   print(f"Is 2023 leap year? {Date.is_leap_year(2023)}")

**Output:**

::

   Regular: 2024-03-15
   From string: 2024-12-25
   Today: 2024-03-15
   Is 2024 leap year? True
   Is 2023 leap year? False

---

**Practice: Understanding Method Types**

.. mchoice:: class_decorator_property_purpose
   :answer_a: To create private attributes
   :answer_b: To make methods look like attributes
   :answer_c: To make attributes immutable
   :answer_d: To speed up attribute access
   :correct: b
   :feedback_a: @property doesn't make attributes private (use _ convention for that)
   :feedback_b: Correct! @property lets you write methods that are accessed like attributes: obj.radius instead of obj.radius()
   :feedback_c: Properties can have setters, so they're not necessarily immutable
   :feedback_d: Properties are actually slightly slower than regular attributes (they call functions)

   What is the main purpose of ``@property``?

.. mchoice:: class_decorator_staticmethod_when
   :answer_a: When the method needs to modify instance variables
   :answer_b: When the method doesn't need access to instance or class data
   :answer_c: When the method should be private
   :answer_d: When the method needs to be faster
   :correct: b
   :feedback_a: If you need self, use a regular instance method, not @staticmethod
   :feedback_b: Correct! @staticmethod is for utility functions that logically belong to the class but don't need self or cls
   :feedback_c: @staticmethod doesn't affect visibility/privacy
   :feedback_d: @staticmethod doesn't improve performance

   When should you use ``@staticmethod``?

.. mchoice:: class_decorator_classmethod_constructor
   :answer_a: To make the constructor private
   :answer_b: To create alternative ways to construct instances
   :answer_c: To prevent instantiation
   :answer_d: To automatically call __init__
   :correct: b
   :feedback_a: @classmethod doesn't affect visibility
   :feedback_b: Correct! A common pattern is using @classmethod for alternative constructors like Date.from_string() or Date.today()
   :feedback_c: @classmethod doesn't prevent instantiation
   :feedback_d: You still need to call __init__ (via cls())

   Why use ``@classmethod`` for alternative constructors?

.. mchoice:: class_decorator_which_receives_class
   :answer_a: Instance methods receive cls
   :answer_b: Static methods receive cls
   :answer_c: Class methods receive cls
   :answer_d: Property methods receive cls
   :correct: c
   :feedback_a: Instance methods receive self (the instance), not cls
   :feedback_b: Static methods don't automatically receive any special arguments
   :feedback_c: Correct! Class methods receive cls (the class) as their first argument
   :feedback_d: Property methods receive self (the instance)

   Which method type receives the class itself as an argument?

---

**Key Takeaways:**

.. important::

   **Class Decorator Summary**

   **@property**
   - Makes methods look like attributes
   - Great for computed values and validation
   - Uses closures to store getter/setter/deleter

   **@staticmethod**
   - No access to instance (``self``) or class (``cls``)
   - Just a utility function grouped with the class
   - Use when logic belongs to class but doesn't need data

   **@classmethod**
   - Receives class (``cls``) as first argument
   - Perfect for alternative constructors
   - Works correctly with inheritance

   **Decision Guide:**
   - Need instance data? → Instance method
   - Need class data or to create instances? → ``@classmethod``
   - Need neither? → ``@staticmethod``
   - Want method-like-attribute? → ``@property``

---

Closure Introspection
----------------------

.. index:: closure introspection, __closure__, cell_contents, debugging closures

Python lets you **inspect closures** at runtime to see captured variables!

**The __closure__ Attribute**

Python functions have a ``__closure__`` attribute that lets you inspect captured variables. Here's how it works:

.. code-block:: python

   def make_counter(start=0, step=1):
       count = [start]  # Use list to avoid nonlocal

       def increment():
           count[0] += step
           return count[0]

       return increment

   counter = make_counter(10, 5)

   # Inspect the closure
   print(f"Is it a closure? {counter.__closure__ is not None}")
   print(f"Number of captured variables: {len(counter.__closure__)}")

   # Examine each captured variable
   for i, cell in enumerate(counter.__closure__):
       print(f"Variable {i}: {cell.cell_contents}")

   print("\nAfter calling counter():")
   result = counter()
   print(f"Result: {result}")

   # Check captured variables again
   print("\nCaptured variables after call:")
   for i, cell in enumerate(counter.__closure__):
       print(f"Variable {i}: {cell.cell_contents}")

**Output:**

::

   Is it a closure? True
   Number of captured variables: 2
   Variable 0: [10]
   Variable 1: 5

   After calling counter():
   Result: 15

   Captured variables after call:
   Variable 0: [15]
   Variable 1: 5

.. note::
   **Closure Cells**

   - ``__closure__`` is a tuple of ``cell`` objects
   - Each ``cell`` wraps a captured variable
   - Access the value with ``cell.cell_contents``
   - ``__closure__`` is ``None`` for non-closures

**Try it yourself:**

Save this code as ``inspect_closure.py`` and run it on your local Python installation to see closure introspection in action!

---

**Practice: Understanding Closure Introspection**

.. mchoice:: closure_introspection_q1
   :answer_a: True
   :answer_b: False
   :answer_c: None
   :answer_d: An empty tuple ()
   :correct: a
   :feedback_a: Correct! A closure's __closure__ attribute is not None (it's a tuple of cells).
   :feedback_b: __closure__ is a tuple (which is truthy), not False.
   :feedback_c: __closure__ is None only for non-closures (functions that don't capture variables).
   :feedback_d: Even if empty, () is not None, so the expression would be True. But in this case, it captures variables so it's a non-empty tuple.

   Given ``counter = make_counter(10, 5)``, what does ``counter.__closure__ is not None`` evaluate to?

.. mchoice:: closure_introspection_q2
   :answer_a: 0
   :answer_b: 1
   :answer_c: 2
   :answer_d: 3
   :correct: c
   :feedback_a: There are captured variables: count and step!
   :feedback_b: There are two captured variables, not just one.
   :feedback_c: Correct! The closure captures two variables: count (the list [10]) and step (5).
   :feedback_d: Only two variables are captured from the enclosing scope.

   How many variables does the ``increment`` closure capture in the example above?

.. mchoice:: closure_introspection_q3
   :answer_a: [10] and 5
   :answer_b: [15] and 5
   :answer_c: 10 and 5
   :answer_d: 15 and 5
   :correct: b
   :feedback_a: After calling counter(), count[0] becomes 15, so count is [15].
   :feedback_b: Correct! After increment runs, count becomes [15] (was [10], added 5), and step remains 5.
   :feedback_c: count is a list [15], not just the integer 15.
   :feedback_d: count is stored as a list [15], not just 15.

   After calling ``counter()`` once, what are the values in ``cell.cell_contents``?

.. mchoice:: closure_introspection_q4
   :answer_a: Regular functions that don't capture variables
   :answer_b: Functions that have syntax errors
   :answer_c: Functions defined at module level
   :answer_d: Both A and C
   :correct: d
   :feedback_a: Correct! If a function doesn't capture anything, __closure__ is None.
   :feedback_b: Functions with syntax errors wouldn't be created in the first place.
   :feedback_c: Correct! Module-level functions usually don't capture variables from an enclosing scope.
   :feedback_d: Correct! Both module-level functions and functions that don't capture variables have __closure__ = None.

   When is ``function.__closure__`` equal to ``None``?

---

Performance Considerations
---------------------------

.. index:: closure performance, memory usage, optimization

Closures have performance implications you should understand:

**Memory Usage**

Closures require extra memory to store captured variables. Here's a comparison:

.. code-block:: python

   import sys

   # Regular function
   def regular_add(x, y):
       return x + y

   # Closure
   def make_adder(x):
       def add(y):
           return x + y
       return add

   add_five = make_adder(5)

   # Compare sizes
   print("Memory usage:")
   print(f"  Regular function: {sys.getsizeof(regular_add)} bytes")
   print(f"  Closure:          {sys.getsizeof(add_five)} bytes")

   # The closure also stores the cell
   if add_five.__closure__:
       cell_size = sum(sys.getsizeof(cell) for cell in add_five.__closure__)
       print(f"  Closure cells:    {cell_size} bytes")
       print(f"  Total closure:    {sys.getsizeof(add_five) + cell_size} bytes")

**Output:**

::

   Memory usage:
     Regular function: 136 bytes
     Closure:          136 bytes
     Closure cells:    48 bytes
     Total closure:    184 bytes

**What This Tells Us:**

.. list-table:: Closure Memory Breakdown
   :widths: 40 30 30
   :header-rows: 1

   * - Component
     - Size
     - Purpose
   * - Function object itself
     - ~136 bytes
     - Function metadata, code object
   * - Closure cells (per variable)
     - ~48 bytes each
     - Storage for captured variables
   * - **Total overhead**
     - **~48 bytes per captured var**
     - **Extra cost vs regular function**

**Key Insights:**

✅ **Closure overhead is small** - ~48 bytes per captured variable
✅ **Usually negligible** - Modern computers have gigabytes of RAM
✅ **Matters only at scale** - Creating thousands/millions of closures
✅ **Benefits often outweigh cost** - Cleaner code, encapsulation

---

**Performance: Closures vs. Classes**

.. activecode:: closure_adv_performance_comparison
   :language: python
   :caption: Speed Comparison

   import time

   # Closure implementation
   def make_counter_closure():
       count = {"hits":0}
       def increment():
           count["hits"] += 1
           return count["hits"]
       return increment

   # Class implementation
   class Counter:
       def __init__(self):
           self.count = 0
       def increment(self):
           self.count += 1
           return self.count

   # Benchmark
   iterations = 1000000

   # Test closure
   counter_closure = make_counter_closure()
   start = time.time()
   for _ in range(iterations):
       counter_closure()
   closure_time = time.time() - start

   # Test class
   counter_class = Counter()
   start = time.time()
   for _ in range(iterations):
       counter_class.increment()
   class_time = time.time() - start

   print(f"Performance ({iterations:,} iterations):")
   print(f"  Closure: {closure_time:.4f} seconds")
   print(f"  Class:   {class_time:.4f} seconds")
   print(f"  Winner:  {'Closure' if closure_time < class_time else 'Class'} "
         f"(~{max(closure_time, class_time) / min(closure_time, class_time):.1f}x faster)")

**Output (varies by system):**

::

   Performance (1,000,000 iterations):
     Closure: 0.0842 seconds
     Class:   0.0895 seconds
     Winner:  Closure (~1.1x faster)

Closures are typically **slightly faster** than classes for simple state, but the difference is minimal!

.. important::
   **When to Use Closures vs. Classes**

   **Use Closures when:**
   - Simple state (1-3 variables)
   - Single primary operation
   - Need true privacy
   - Creating function factories
   - Working with decorators

   **Use Classes when:**
   - Complex state (many attributes)
   - Multiple related methods
   - Need inheritance
   - Need clear structure and readability
   - Building reusable components

---

Functional Programming Patterns
--------------------------------

.. index:: functional programming, map, filter, reduce, lambda with closures

Closures enable functional programming patterns in Python:

**Map/Filter with Closures**

.. activecode:: closure_adv_functional_map_filter
   :language: python
   :caption: Closures in Map/Filter

   # Traditional functions
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   # Using lambda (anonymous closures!)
   doubled = list(map(lambda x: x * 2, numbers))
   print(f"Doubled: {doubled}")

   evens = list(filter(lambda x: x % 2 == 0, numbers))
   print(f"Evens: {evens}")

   # Using closure factories for more flexibility
   def make_multiplier(factor):
       return lambda x: x * factor

   def make_divisibility_checker(divisor):
       return lambda x: x % divisor == 0

   # Create specialized functions
   triple = make_multiplier(3)
   divisible_by_3 = make_divisibility_checker(3)

   tripled = list(map(triple, numbers))
   print(f"\nTripled: {tripled}")

   div_by_3 = list(filter(divisible_by_3, numbers))
   print(f"Divisible by 3: {div_by_3}")

**Output:**

::

   Doubled: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
   Evens: [2, 4, 6, 8, 10]

   Tripled: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
   Divisible by 3: [3, 6, 9]

---

**Reduce with Closures**

.. activecode:: closure_adv_functional_reduce
   :language: python
   :caption: Closures with functools.reduce

   from functools import reduce

   numbers = [1, 2, 3, 4, 5]

   # Built-in reduce patterns
   total = reduce(lambda acc, x: acc + x, numbers)
   print(f"Sum: {total}")

   product = reduce(lambda acc, x: acc * x, numbers)
   print(f"Product: {product}")

   # Custom reducer with closure
   def make_custom_reducer(operation, initial=0):
       """Factory that creates custom reducers"""
       def reducer(acc, x):
           return operation(acc, x)
       return reducer, initial

   # Create custom reducers
   max_reducer, _ = make_custom_reducer(lambda a, b: a if a > b else b)
   concat_reducer, _ = make_custom_reducer(lambda a, b: f"{a},{b}")

   maximum = reduce(max_reducer, numbers)
   print(f"\nMaximum: {maximum}")

   words = ['apple', 'banana', 'cherry']
   concatenated = reduce(concat_reducer, words)
   print(f"Concatenated: {concatenated}")

**Output:**

::

   Sum: 15
   Product: 120

   Maximum: 5
   Concatenated: apple,banana,cherry

---

**Pipeline Pattern**

.. activecode:: closure_adv_functional_pipeline
   :language: python
   :caption: Function Pipelines with Closures

   def compose(*functions):
       """Compose functions right-to-left: compose(f, g, h)(x) = f(g(h(x)))"""
       def inner(arg):
           result = arg
           for func in reversed(functions):
               result = func(result)
           return result
       return inner

   # Individual operations
   def double(x):
       return x * 2

   def add_ten(x):
       return x + 10

   def square(x):
       return x ** 2

   # Create pipeline
   pipeline = compose(square, add_ten, double)

   # Test: double(5) = 10, then 10 + 10 = 20, then 20^2 = 400
   result = pipeline(5)
   print(f"Pipeline result: {result}")

   # More complex example: data processing pipeline
   def make_transformer(operation, description):
       """Factory for labeled transformations"""
       def transform(data):
           print(f"  {description}")
           return operation(data)
       return transform

   # Build data processing pipeline
   data_pipeline = compose(
       make_transformer(lambda data: [x for x in data if x > 0], "Filter positives"),
       make_transformer(lambda data: [x ** 2 for x in data], "Square values"),
       make_transformer(lambda data: sorted(data), "Sort")
   )

   print("\nData processing:")
   input_data = [-2, 5, -1, 3, 8, -3, 1]
   output = data_pipeline(input_data)
   print(f"Input:  {input_data}")
   print(f"Output: {output}")

**Output:**

::

   Pipeline result: 400

   Data processing:
     Sort
     Square values
     Filter positives
   Input:  [-2, 5, -1, 3, 8, -3, 1]
   Output: [1, 9, 25, 64]

---

Best Practices and Patterns
----------------------------

.. index:: closure best practices, when to use closures

**Checklist: When to Use Closures**

.. code-block:: text

   ✅ Use closures when:
      □ Creating decorators
      □ Need true private state (not accessible from outside)
      □ Building function factories
      □ Simple state (1-3 variables)
      □ Single primary operation
      □ Callbacks need context
      □ Functional programming patterns

   ⚠️  Consider alternatives when:
      □ Complex state (many variables)
      □ Multiple related methods needed
      □ Need inheritance or polymorphism
      □ Team unfamiliar with closures
      □ Need clear OOP structure

---

**Code Style Guidelines**

.. code-block:: python

   # ✅ GOOD: Clear naming
   def make_validator(min_value, max_value):
       """Clear purpose and good names"""
       def validate(value):
           return min_value <= value <= max_value
       return validate

   # ❌ BAD: Unclear naming
   def f(a, b):
       def g(c):
           return a <= c <= b
       return g

   # ✅ GOOD: Docstrings
   def rate_limit(calls, period):
       """
       Rate limiter decorator.

       Args:
           calls: Maximum calls allowed
           period: Time period in seconds

       Returns:
           Decorator function
       """
       def decorator(func):
           # Implementation...
           pass
       return decorator

   # ✅ GOOD: Comments for complex closures
   def memoize_with_ttl(ttl):
       def decorator(func):
           cache = {}  # {args: (result, timestamp)}

           def wrapper(*args):
               # Check if cached value is still valid
               if args in cache:
                   result, timestamp = cache[args]
                   if time.time() - timestamp < ttl:
                       return result  # Use cached

               # Compute and cache
               result = func(*args)
               cache[args] = (result, time.time())
               return result

           return wrapper
       return decorator

---

Practice Challenges
--------------------

**Challenge 1: Build a Chaining Decorator**

.. activecode:: closure_adv_practice_chaining
   :language: python
   :autograde: unittest
   :caption: Challenge - Method Chaining with Closures

   from functools import wraps

   def chainable(func):
       """
       Decorator that makes a function chainable.
       The function should return self to allow method chaining.

       Example:
           @chainable
           def add_item(self, item):
               self.items.append(item)
               # return self automatically added!
       """
       # TODO: Your code here
       # Hint: Wrapper should call the function, then return self
       # Hint: Use @wraps to preserve function metadata
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_decorator_exists(self):
           """Test that chainable decorator is defined"""
           self.assertTrue(callable(chainable), "chainable should be a callable decorator")

       def test_basic_chaining(self):
           """Test that decorator enables chaining"""
           class Builder:
               def __init__(self):
                   self.items = []

               @chainable
               def add(self, item):
                   self.items.append(item)

           b = Builder()
           result = b.add(1)

           # Should return self for chaining
           self.assertIs(result, b, "Decorated method should return self")

       def test_multiple_chains(self):
           """Test chaining multiple method calls"""
           class Builder:
               def __init__(self):
                   self.items = []

               @chainable
               def add(self, item):
                   self.items.append(item)

           b = Builder()
           b.add(1).add(2).add(3)

           self.assertEqual(b.items, [1, 2, 3], "Multiple chained calls should all execute")

       def test_function_still_executes(self):
           """Test that the original function logic still runs"""
           class Counter:
               def __init__(self):
                   self.count = 0

               @chainable
               def increment(self):
                   self.count += 1

           c = Counter()
           c.increment().increment().increment()

           self.assertEqual(c.count, 3, "Original function logic should execute")

       def test_with_arguments(self):
           """Test that decorator passes arguments correctly"""
           class Builder:
               def __init__(self):
                   self.items = []

               @chainable
               def add(self, item):
                   self.items.append(item)

               @chainable
               def remove(self, item):
                   self.items.remove(item)

           b = Builder()
           b.add(1).add(2).add(3).remove(2)

           self.assertEqual(b.items, [1, 3], "Should handle args correctly")

       def test_complex_chaining(self):
           """Test full builder pattern with chaining"""
           class Builder:
               def __init__(self):
                   self.items = []

               @chainable
               def add(self, item):
                   self.items.append(item)

               @chainable
               def remove(self, item):
                   self.items.remove(item)

               def build(self):
                   return self.items.copy()

           result = Builder().add(1).add(2).add(3).remove(2).build()

           self.assertEqual(result, [1, 3], "Complex chaining should work correctly")

       def test_with_kwargs(self):
           """Test that decorator handles keyword arguments"""
           class Config:
               def __init__(self):
                   self.settings = {}

               @chainable
               def set(self, key, value):
                   self.settings[key] = value

           c = Config()
           c.set('host', 'localhost').set('port', 8080)

           self.assertEqual(c.settings, {'host': 'localhost', 'port': 8080})

       def test_preserves_function_name(self):
           """Test that decorator preserves function metadata"""
           class Example:
               @chainable
               def my_method(self):
                   """This is my docstring"""
                   pass

           self.assertEqual(Example.my_method.__name__, "my_method")
           self.assertEqual(Example.my_method.__doc__, "This is my docstring")

       def test_uses_wraps(self):
           """Test that implementation uses @wraps"""
           source = self.getEditorText()

           has_wraps = 'wraps' in source or '@wraps' in source
           self.assertTrue(has_wraps, "Implementation should use @wraps to preserve metadata")

   myTests().main()

.. reveal:: closure_adv_practice_chaining_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      from functools import wraps

      def chainable(func):
          @wraps(func)
          def wrapper(self, *args, **kwargs):
              func(self, *args, **kwargs)
              return self  # Always return self for chaining
          return wrapper

---

**Challenge 2: Build a Throttle Decorator**

.. activecode:: closure_adv_practice_throttle
   :language: python
   :autograde: unittest
   :caption: Challenge - Throttle Decorator

   import time

   def throttle(min_interval):
       """
       Decorator that prevents a function from being called
       more frequently than min_interval seconds.

       If called too soon, should return None and skip execution.

       Args:
           min_interval: Minimum seconds between calls

       Example: @throttle(2) allows calls at most every 2 seconds
       """
       # TODO: Your code here
       # Hint: Store the timestamp of the last successful call
       # Hint: Use time.time() to get current time
       # Hint: Compare elapsed time with min_interval
       pass

   ====
   from unittest.gui import TestCaseGui
   import time

   class myTests(TestCaseGui):
       def test_decorator_exists(self):
           """Test that throttle decorator is defined"""
           self.assertTrue(callable(throttle), "throttle should be a callable decorator")

       def test_first_call_succeeds(self):
           """Test that first call always succeeds"""
           call_count = [0]

           @throttle(1.0)
           def counter():
               call_count[0] += 1
               return "success"

           result = counter()

           self.assertEqual(result, "success", "First call should succeed")
           self.assertEqual(call_count[0], 1, "Function should execute on first call")

       def test_immediate_second_call_throttled(self):
           """Test that immediate second call is throttled"""
           call_count = [0]

           @throttle(1.0)
           def counter():
               call_count[0] += 1
               return "success"

           counter()  # First call
           result = counter()  # Immediate second call

           self.assertIsNone(result, "Throttled call should return None")
           self.assertEqual(call_count[0], 1, "Function should not execute when throttled")

       def test_call_after_interval_succeeds(self):
           """Test that call after interval succeeds"""
           call_count = [0]

           @throttle(0.5)  # Short interval for faster testing
           def counter():
               call_count[0] += 1
               return "success"

           counter()  # First call
           time.sleep(0.6)  # Wait longer than interval
           result = counter()  # Should succeed

           self.assertEqual(result, "success", "Call after interval should succeed")
           self.assertEqual(call_count[0], 2, "Function should execute after waiting")

       def test_multiple_throttles_sequence(self):
           """Test sequence of throttled and successful calls"""
           call_count = [0]

           @throttle(0.3)
           def counter():
               call_count[0] += 1
               return call_count[0]

           result1 = counter()  # Should work
           result2 = counter()  # Should be throttled
           result3 = counter()  # Should be throttled

           self.assertEqual(result1, 1)
           self.assertIsNone(result2)
           self.assertIsNone(result3)
           self.assertEqual(call_count[0], 1, "Only first call should execute")

           time.sleep(0.35)
           result4 = counter()  # Should work now

           self.assertEqual(result4, 2)
           self.assertEqual(call_count[0], 2)

       def test_preserves_arguments(self):
           """Test that decorator passes arguments correctly"""
           @throttle(0.5)
           def add(a, b):
               return a + b

           result = add(5, 3)
           self.assertEqual(result, 8, "Arguments should pass through correctly")

       def test_preserves_kwargs(self):
           """Test that decorator passes keyword arguments"""
           @throttle(0.5)
           def greet(name, greeting="Hello"):
               return f"{greeting}, {name}!"

           result = greet("Alice", greeting="Hi")
           self.assertEqual(result, "Hi, Alice!", "Kwargs should pass through correctly")

       def test_independent_throttles(self):
           """Test that different decorated functions have independent throttles"""
           @throttle(1.0)
           def func1():
               return "A"

           @throttle(1.0)
           def func2():
               return "B"

           # Both should work (independent counters)
           result1 = func1()
           result2 = func2()

           self.assertEqual(result1, "A")
           self.assertEqual(result2, "B")

           # Both should be throttled independently
           self.assertIsNone(func1())
           self.assertIsNone(func2())

       def test_different_intervals(self):
           """Test that different intervals work correctly"""
           count_fast = [0]
           count_slow = [0]

           @throttle(0.2)
           def fast():
               count_fast[0] += 1
               return "fast"

           @throttle(0.5)
           def slow():
               count_slow[0] += 1
               return "slow"

           fast()
           slow()

           time.sleep(0.25)

           # Fast should work now (0.2s interval)
           result_fast = fast()
           # Slow should still be throttled (0.5s interval)
           result_slow = slow()

           self.assertEqual(result_fast, "fast")
           self.assertIsNone(result_slow)

       def test_uses_time_module(self):
           """Test that implementation uses time.time()"""
           source = self.getEditorText()

           self.assertIn('time.time()', source, "Implementation should use time.time() for timestamps")

       def test_stores_last_call_time(self):
           """Test that implementation stores timestamp of last call"""
           source = self.getEditorText()

           # Look for timestamp storage pattern
           has_timestamp = 'last' in source or 'time' in source or 'timestamp' in source
           self.assertTrue(has_timestamp, "Implementation should store timestamp of last call")

       def test_compares_elapsed_time(self):
           """Test that implementation checks elapsed time"""
           source = self.getEditorText()

           # Should have comparison with min_interval
           has_comparison = ('min_interval' in source and '<' in source) or 'elapsed' in source
           self.assertTrue(has_comparison, "Implementation should compare elapsed time with min_interval")

   myTests().main()

.. reveal:: closure_adv_practice_throttle_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      import time

      def throttle(min_interval):
          def decorator(func):
              last_called = [0]  # Use list to avoid nonlocal

              def wrapper(*args, **kwargs):
                  current = time.time()
                  elapsed = current - last_called[0]

                  if elapsed < min_interval:
                      # Too soon - throttle the call
                      return None

                  # Enough time has passed - allow the call
                  last_called[0] = current
                  return func(*args, **kwargs)

              return wrapper
          return decorator

----

**Challenge 3: Build a Call Counter with Reset**

.. activecode:: closure_adv_practice_call_counter
   :language: python
   :autograde: unittest
   :caption: Challenge - Call Counter with Reset

   def counted(func):
       """
       Decorator that counts function calls.
       Adds a 'call_count' attribute and 'reset_count()' method to the function.

       Example:
           @counted
           def greet():
               return "Hello!"

           greet()
           greet()
           print(greet.call_count)  # 2
           greet.reset_count()
           print(greet.call_count)  # 0
       """
       # TODO: Your code here
       # Hint: Create wrapper function that increments counter
       # Hint: Add call_count as an attribute on the wrapper
       # Hint: Add reset_count as a method on the wrapper
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_decorator_exists(self):
           """Test that counted decorator is defined"""
           self.assertTrue(callable(counted), "counted should be a callable decorator")

       def test_has_call_count_attribute(self):
           """Test that decorated function has call_count attribute"""
           @counted
           def dummy():
               return "OK"

           self.assertTrue(hasattr(dummy, 'call_count'), "Decorated function should have call_count attribute")

       def test_call_count_starts_at_zero(self):
           """Test that call_count starts at 0"""
           @counted
           def dummy():
               return "OK"

           self.assertEqual(dummy.call_count, 0, "call_count should start at 0")

       def test_call_count_increments(self):
           """Test that call_count increments with each call"""
           @counted
           def dummy():
               return "OK"

           dummy()
           self.assertEqual(dummy.call_count, 1)
           dummy()
           self.assertEqual(dummy.call_count, 2)
           dummy()
           self.assertEqual(dummy.call_count, 3)

       def test_function_still_executes(self):
           """Test that original function logic still runs"""
           results = []

           @counted
           def append_value(val):
               results.append(val)
               return val

           result1 = append_value(1)
           result2 = append_value(2)

           self.assertEqual(result1, 1, "Function should return correct value")
           self.assertEqual(result2, 2, "Function should return correct value")
           self.assertEqual(results, [1, 2], "Function logic should execute")

       def test_has_reset_count_method(self):
           """Test that decorated function has reset_count method"""
           @counted
           def dummy():
               return "OK"

           self.assertTrue(hasattr(dummy, 'reset_count'), "Should have reset_count method")
           self.assertTrue(callable(dummy.reset_count), "reset_count should be callable")

       def test_reset_count_works(self):
           """Test that reset_count resets the counter to 0"""
           @counted
           def dummy():
               return "OK"

           dummy()
           dummy()
           dummy()
           self.assertEqual(dummy.call_count, 3)

           dummy.reset_count()
           self.assertEqual(dummy.call_count, 0, "reset_count should reset counter to 0")

       def test_count_after_reset(self):
           """Test that counting works correctly after reset"""
           @counted
           def dummy():
               return "OK"

           dummy()
           dummy()
           dummy.reset_count()
           dummy()
           dummy()

           self.assertEqual(dummy.call_count, 2, "Should count correctly after reset")

       def test_multiple_resets(self):
           """Test multiple reset cycles"""
           @counted
           def dummy():
               return "OK"

           dummy()
           dummy()
           self.assertEqual(dummy.call_count, 2)

           dummy.reset_count()
           dummy()
           self.assertEqual(dummy.call_count, 1)

           dummy.reset_count()
           dummy()
           dummy()
           dummy()
           self.assertEqual(dummy.call_count, 3)

       def test_preserves_arguments(self):
           """Test that decorator passes arguments correctly"""
           @counted
           def add(a, b):
               return a + b

           result = add(5, 3)
           self.assertEqual(result, 8)
           self.assertEqual(add.call_count, 1)

       def test_preserves_kwargs(self):
           """Test that decorator passes keyword arguments"""
           @counted
           def greet(name, greeting="Hello"):
               return f"{greeting}, {name}!"

           result = greet("Alice", greeting="Hi")
           self.assertEqual(result, "Hi, Alice!")
           self.assertEqual(greet.call_count, 1)

       def test_independent_counters(self):
           """Test that different decorated functions have independent counters"""
           @counted
           def func1():
               return "A"

           @counted
           def func2():
               return "B"

           func1()
           func1()
           func2()

           self.assertEqual(func1.call_count, 2)
           self.assertEqual(func2.call_count, 1)

           func1.reset_count()
           self.assertEqual(func1.call_count, 0)
           self.assertEqual(func2.call_count, 1, "Other function counter should be unaffected")

       def test_wrapper_function_created(self):
           """Test that implementation creates a wrapper function"""
           source = self.getEditorText()

           has_wrapper = 'def wrapper' in source or 'def inner' in source
           self.assertTrue(has_wrapper, "Implementation should create a wrapper function")

       def test_increments_counter(self):
           """Test that implementation increments the counter"""
           source = self.getEditorText()

           has_increment = '+= 1' in source or '+=' in source or '+ 1' in source
           self.assertTrue(has_increment, "Implementation should increment call_count")

       def test_sets_attributes_on_wrapper(self):
           """Test that implementation sets attributes on wrapper"""
           source = self.getEditorText()

           has_attribute_setting = 'wrapper.call_count' in source or '.call_count =' in source
           self.assertTrue(has_attribute_setting, "Implementation should set call_count as wrapper attribute")

   myTests().main()

.. reveal:: closure_adv_practice_call_counter_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Simple approach using function attributes:**

   .. code-block:: python

      def counted(func):
          def wrapper(*args, **kwargs):
              wrapper.call_count += 1
              return func(*args, **kwargs)

          # Initialize attributes
          wrapper.call_count = 0
          wrapper.reset_count = lambda: setattr(wrapper, 'call_count', 0)

          return wrapper

----

Check Your Understanding
-------------------------

.. mchoice:: closure_adv_decorator_args
   :answer_a: One layer: the decorator function
   :answer_b: Two layers: decorator and wrapper
   :answer_c: Three layers: factory, decorator, and wrapper
   :answer_d: It depends on how many arguments the decorator takes
   :correct: c
   :feedback_a: A decorator with arguments needs more layers!
   :feedback_b: You need an outer layer to receive the decorator arguments.
   :feedback_c: Correct! Factory (takes args) → Decorator (takes func) → Wrapper (replaces func).
   :feedback_d: It's always three layers for decorators with arguments.

   How many function layers do you need for a decorator that takes arguments like ``@retry(max_attempts=3)``?

.. mchoice:: closure_adv_nested_decorators
   :answer_a: Top to bottom (farthest from function first)
   :answer_b: Bottom to top (closest to function first)
   :answer_c: Randomly, depending on Python version
   :answer_d: All at once, in parallel
   :correct: b
   :feedback_a: The opposite! Decorators apply from bottom to top.
   :feedback_b: Correct! The decorator closest to the function is applied first.
   :feedback_c: Decorator order is deterministic and consistent.
   :feedback_d: Decorators are applied sequentially, not in parallel.

   When multiple decorators are stacked, in what order are they applied?

.. mchoice:: closure_adv_introspection
   :answer_a: __closure__ and cell_contents
   :answer_b: __dict__ and __slots__
   :answer_c: __code__ and __name__
   :answer_d: __vars__ and __locals__
   :correct: a
   :feedback_a: Correct! __closure__ contains cells, each with cell_contents.
   :feedback_b: These are for general object attributes, not closures specifically.
   :feedback_c: These provide code and name info, but not captured variables.
   :feedback_d: __vars__ doesn't exist, and __locals__ isn't for closures.

   Which attributes let you inspect captured variables in a closure?

.. mchoice:: closure_adv_memory
   :answer_a: Closures always use significantly more memory than classes
   :answer_b: Classes always use significantly more memory than closures
   :answer_c: Closures and classes have similar memory usage for simple state
   :answer_d: Closures can't be compared to classes in terms of memory
   :correct: c
   :feedback_a: Closures actually have slightly less overhead than classes.
   :feedback_b: The difference is small, not significant.
   :feedback_c: Correct! For simple state, memory usage is comparable (closures slightly smaller).
   :feedback_d: They can and should be compared when choosing between them!

   What's the memory overhead of closures compared to classes?

.. mchoice:: closure_adv_functional
   :answer_a: Closures can't be used with map() and filter()
   :answer_b: Lambda functions are closures when they capture variables
   :answer_c: Functional programming in Python doesn't use closures
   :answer_d: Only named functions can be closures, not lambdas
   :correct: b
   :feedback_a: Closures work perfectly with map() and filter()!
   :feedback_b: Correct! Lambdas are anonymous functions and can be closures if they capture variables.
   :feedback_c: Closures are fundamental to functional programming!
   :feedback_d: Both lambda and named functions can be closures.

   How do closures relate to functional programming in Python?

---

Key Takeaways
-------------

.. important::
   **Section 5 Summary: Advanced Techniques**

   ✅ **Decorators with Arguments**
      - Need **three layers**: factory (args) → decorator (func) → wrapper (execution)
      - Pattern: ``@decorator(arg)`` calls ``decorator(arg)`` first, then decorates
      - Examples: ``@retry(max=3)``, ``@cache(size=100)``, ``@rate_limit(calls=5)``

   ✅ **Decorator Stacking**
      - Applied **bottom-to-top** (closest to function first)
      - Each decorator wraps the result of the previous one
      - Combine timing + logging + caching for powerful effects

   ✅ **Class Decorators**
      - ``@property`` — computed attributes with getters/setters
      - ``@staticmethod`` — no class or instance access
      - ``@classmethod`` — receives class as first argument
      - All use closures internally!

   ✅ **Closure Introspection**
      - ``func.__closure__`` — tuple of cell objects
      - ``cell.cell_contents`` — the captured value
      - ``func.__code__.co_freevars`` — variable names
      - Useful for debugging and understanding closure behavior

   ✅ **Performance**
      - Closures have small memory overhead (cells)
      - Slightly faster than classes for simple operations
      - **Use closures for:** simple state, single operation, privacy
      - **Use classes for:** complex state, multiple methods, inheritance

   ✅ **Functional Programming**
      - Closures enable map/filter/reduce patterns
      - Lambda functions are closures when they capture variables
      - Function composition and pipelines
      - Factory pattern for creating specialized functions

   ✅ **Best Practices**
      - Clear naming and docstrings
      - Avoid loop variable capture pitfall (use default arguments)
      - Remember ``nonlocal`` for modifying captured variables
      - Choose closures vs. classes based on complexity

---

What's Next?
------------

**Congratulations! You've completed the Closures and Advanced Functions chapter!** 🎉

You now have **expert-level knowledge** of:

- ✅ Closure fundamentals (definition, free variables, scope)
- ✅ State management and the ``nonlocal`` keyword
- ✅ Encapsulation and data privacy
- ✅ Practical patterns (decorators, callbacks, factories, memoization)
- ✅ Advanced techniques (introspection, performance, functional programming)

**You can now:**

- Build sophisticated decorators with arguments
- Create function factories for code reuse
- Optimize performance with memoization
- Use closures for true data privacy
- Recognize closure patterns in professional Python libraries
- Make informed decisions about when to use closures vs. classes

**Next in your PCAP journey:**

- **Chapter 29: PCAP Power Topics** — Advanced exception handling, file I/O, and string methods
- **Real-world projects** — Apply your closure skills to build production-ready applications!

Keep coding, and remember: closures are a **superpower** in Python! 🚀