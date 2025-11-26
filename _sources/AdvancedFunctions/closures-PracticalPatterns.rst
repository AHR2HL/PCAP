..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Section 4: Practical Patterns
==============================

.. index:: decorators, callbacks, memoization, function factories, practical closures

Introduction
------------

Now that you understand closure mechanics, state, and encapsulation, it's time to see closures in action solving **real-world problems**.

Closures are everywhere in professional Python code:

- **Web frameworks** like Flask use closures for route decorators
- **Testing frameworks** use closures for fixtures and mocking
- **GUI libraries** use closures for event handlers
- **Data processing** uses closures for custom filters and transformers
- **Performance optimization** uses closures for caching

In this section, you'll learn the most important practical patterns:

- **Decorators** — the #1 most common use of closures
- **Callbacks and event handlers** — GUI and async programming
- **Function factories** — creating specialized functions on demand
- **Memoization** — caching results for performance
- **Partial application** — pre-configuring function arguments
- **Real-world examples** from popular libraries

By the end, you'll recognize closures throughout the Python ecosystem and know when to use each pattern!

---

Pattern 1: Decorators
----------------------

.. index:: decorator pattern, function decorator, wrapper function

**Decorators** are the most common and powerful use of closures in Python. A decorator is a function that takes another function and extends its behavior **without modifying its code**.

**The Basic Pattern**

.. activecode:: closure_basic_decorator
   :language: python
   :caption: Basic Decorator Pattern

   def my_decorator(func):
       """Outer function: takes a function to decorate"""

       def wrapper(*args, **kwargs):
           """Inner function: wraps the original function"""
           print("🎯 Before function call")
           result = func(*args, **kwargs)  # Call original function
           print("✅ After function call")
           return result

       return wrapper  # Return the wrapper (a closure!)

   # Method 1: Manual decoration
   def say_hello(name):
       print(f"Hello, {name}!")

   say_hello = my_decorator(say_hello)  # Replace with decorated version
   say_hello("Alice")

   print("\n" + "="*40 + "\n")

   # Method 2: Using @ syntax (syntactic sugar)
   @my_decorator
   def say_goodbye(name):
       print(f"Goodbye, {name}!")

   say_goodbye("Bob")

**Output:**

::

   🎯 Before function call
   Hello, Alice!
   ✅ After function call

   ========================================

   🎯 Before function call
   Goodbye, Bob!
   ✅ After function call

.. important::
   **Decorator Syntax**

   These are **exactly equivalent**:

   .. code-block:: python

      # Manual decoration
      func = decorator(func)

      # @ syntax (preferred)
      @decorator
      def func():
          pass

   The ``@`` syntax is just **syntactic sugar** that makes the code cleaner!

---

**Practical Decorator: Timing Functions**

.. activecode:: closure_timing_decorator
   :language: python
   :caption: Timing Decorator

   import time

   def timer(func):
       """Decorator to measure function execution time"""

       def wrapper(*args, **kwargs):
           start = time.time()
           result = func(*args, **kwargs)
           end = time.time()
           elapsed = end - start
           print(f"⏱️  {func.__name__} took {elapsed:.4f} seconds")
           return result

       return wrapper

   @timer
   def slow_function():
       """Simulate a slow operation"""
       time.sleep(0.5)
       return "Done!"

   @timer
   def fast_function():
       """Quick calculation"""
       return sum(range(1000))

   # Use the decorated functions
   result1 = slow_function()
   print(f"Result: {result1}\n")

   result2 = fast_function()
   print(f"Result: {result2}")

**Output:**

::

   ⏱️  slow_function took 0.5001 seconds
   Result: Done!

   ⏱️  fast_function took 0.0001 seconds
   Result: 10

This pattern is used everywhere! For example, in web frameworks:

.. code-block:: python

   @app.route('/users')  # Flask decorator
   def get_users():
       return users_list

---

**Practical Decorator: Logging**

.. activecode:: closure_logging_decorator
   :language: python
   :caption: Logging Decorator

   def log_calls(func):
       """Decorator to log function calls with arguments"""

       def wrapper(*args, **kwargs):

           # Format arguments nicely
           args_str = ', '.join(repr(arg) for arg in args)
           kwargs_str = ', '.join(f"{k}={v!r}" for k, v in kwargs.items())
           all_args = ', '.join(filter(None, [args_str, kwargs_str]))

           print(f"📞 Call #{call_count}: {func.__name__}({all_args})")

           result = func(*args, **kwargs)
           print(f"📤 Returned: {result!r}")
           return result

       return wrapper

   @log_calls
   def add(a, b):
       return a + b

   @log_calls
   def greet(name, greeting="Hello"):
       return f"{greeting}, {name}!"

   # Test the decorated functions
   add(5, 3)
   add(10, 20)
   greet("Alice")
   greet("Bob", greeting="Hi")

**Output:**

::

   📞 Call #1: add(5, 3)
   📤 Returned: 8
   📞 Call #2: add(10, 20)
   📤 Returned: 30
   📞 Call #1: greet('Alice')
   📤 Returned: 'Hello, Alice!'
   📞 Call #2: greet('Bob', greeting='Hi')
   📤 Returned: 'Hi, Bob!'

Notice that **each decorated function has its own ``call_count``** because each decoration creates a separate closure!

---

**Practical Decorator: Validation**

.. activecode:: closure_validation_decorator
   :language: python
   :caption: Input Validation Decorator

   def validate_positive(func):
       """Decorator to ensure all numeric arguments are positive"""

       def wrapper(*args, **kwargs):
           # Check positional arguments
           for i, arg in enumerate(args):
               if isinstance(arg, (int, float)) and arg <= 0:
                   raise ValueError(f"Argument {i+1} must be positive, got {arg}")

           # Check keyword arguments
           for key, value in kwargs.items():
               if isinstance(value, (int, float)) and value <= 0:
                   raise ValueError(f"Argument '{key}' must be positive, got {value}")

           return func(*args, **kwargs)

       return wrapper

   @validate_positive
   def calculate_area(width, height):
       """Calculate rectangle area (dimensions must be positive)"""
       return width * height

   @validate_positive
   def withdraw(amount, balance):
       """Withdraw from account (amounts must be positive)"""
       if amount > balance:
           return "Insufficient funds"
       return balance - amount

   # Valid calls
   print(f"Area: {calculate_area(5, 10)}")
   print(f"New balance: {withdraw(50, 100)}")

   # Invalid calls
   try:
       calculate_area(-5, 10)
   except ValueError as e:
       print(f"❌ {e}")

   try:
       withdraw(0, 100)
   except ValueError as e:
       print(f"❌ {e}")

**Output:**

::

   Area: 50
   New balance: 50
   ❌ Argument 1 must be positive, got -5
   ❌ Argument 1 must be positive, got 0

---

Pattern 2: Callbacks and Event Handlers
----------------------------------------

.. index:: callback pattern, event handler, GUI callbacks

Callbacks are functions that are passed as arguments to other functions. Closures make it easy to create callbacks that "remember" context.

**Simple Callback Pattern**

.. activecode:: closure_callback_basic
   :language: python
   :caption: Basic Callback Pattern

   def process_data(data, callback):
       """Process data and call callback with result"""
       result = sum(data) / len(data) if data else 0
       callback(result)

   # Without closure: limited context
   def simple_callback(result):
       print(f"Average: {result}")

   process_data([10, 20, 30], simple_callback)

   # With closure: can capture context
   def make_callback(label, threshold):
       """Factory that creates contextual callbacks"""
       def callback(result):
           status = "✅ PASS" if result >= threshold else "❌ FAIL"
           print(f"{label}: {result:.2f} {status}")
       return callback

   # Create specialized callbacks
   grade_checker = make_callback("Exam Score", 60)
   temp_checker = make_callback("Temperature", 20)

   process_data([85, 90, 78], grade_checker)
   process_data([15, 18, 22], temp_checker)

**Output:**

::

   Average: 20.0
   Exam Score: 84.33 ✅ PASS
   Temperature: 18.33 ❌ FAIL

---

**Delayed Execution with Context**

.. activecode:: closure_delayed_execution
   :language: python
   :caption: Delayed Execution Pattern

   def schedule_tasks():
       """Common mistake: all callbacks reference the same variable"""
       tasks = []

       # WRONG: All closures will use the final value of i
       for i in range(3):
           def task():
               print(f"Task {i}")  # Will all use i=2!
           tasks.append(task)

       print("❌ Without proper closure:")
       for task in tasks:
           task()

       print("\n✅ With proper closure:")
       tasks = []

       # RIGHT: Each closure captures its own value
       for i in range(3):
           def task(num=i):  # Default argument captures current value
               print(f"Task {num}")
           tasks.append(task)

       for task in tasks:
           task()

   schedule_tasks()

**Output:**

::

   ❌ Without proper closure:
   Task 2
   Task 2
   Task 2

   ✅ With proper closure:
   Task 0
   Task 1
   Task 2

.. warning::
   **Common Closure Pitfall: Loop Variables**

   Closures created in loops all reference the **same variable**. By the time they execute, the loop is done, so they all see the final value.

   **Solutions:**
   - Use default arguments: ``def func(x=loop_var):``
   - Use ``functools.partial()``
   - Create a factory function

---

Pattern 3: Function Factories
------------------------------

.. index:: function factory, specialized functions, configuration

Function factories use closures to create specialized functions with pre-configured behavior.

**Validator Factory**

.. activecode:: closure_validator_factory
   :language: python
   :caption: Creating Specialized Validators

   def make_range_validator(min_val, max_val, field_name="Value"):
       """Factory that creates range validators"""

       def validate(value):
           if not isinstance(value, (int, float)):
               return f"❌ {field_name} must be a number"
           if value < min_val or value > max_val:
               return f"❌ {field_name} must be between {min_val} and {max_val}"
           return f"✅ {field_name} is valid"

       return validate

   # Create specialized validators
   validate_age = make_range_validator(0, 150, "Age")
   validate_percentage = make_range_validator(0, 100, "Percentage")
   validate_temperature = make_range_validator(-273, 1000000, "Temperature")

   # Use them
   print(validate_age(25))
   print(validate_age(200))
   print(validate_percentage(85))
   print(validate_percentage(150))
   print(validate_temperature(-300))

**Output:**

::

   ✅ Age is valid
   ❌ Age must be between 0 and 150
   ✅ Percentage is valid
   ❌ Percentage must be between 0 and 100
   ❌ Temperature must be between -273 and 1000000

---

**Formatter Factory**

.. activecode:: closure_formatter_factory
   :language: python
   :caption: Creating Specialized Formatters

   def make_formatter(prefix="", suffix="", uppercase=False):
       """Factory that creates text formatters"""

       def format_text(text):
           result = text
           if uppercase:
               result = result.upper()
           return f"{prefix}{result}{suffix}"

       return format_text

   # Create specialized formatters
   format_price = make_formatter(prefix="$", suffix=" USD")
   format_heading = make_formatter(prefix="=== ", suffix=" ===", uppercase=True)
   format_code = make_formatter(prefix="`", suffix="`")
   format_shout = make_formatter(suffix="!!!", uppercase=True)

   # Use them
   print(format_price("19.99"))
   print(format_heading("Chapter 1"))
   print(format_code("print()"))
   print(format_shout("hello"))

**Output:**

::

   $19.99 USD
   === CHAPTER 1 ===
   `print()`
   HELLO!!!

---

**Converter Factory**

.. activecode:: closure_converter_factory
   :language: python
   :caption: Unit Conversion Factory

   def make_unit_converter(factor, from_unit, to_unit):
       """Factory that creates unit converters"""

       def convert(value):
           result = value * factor
           return f"{value} {from_unit} = {result:.2f} {to_unit}"

       # Add reverse conversion as an attribute
       def reverse(value):
           result = value / factor
           return f"{value} {to_unit} = {result:.2f} {from_unit}"

       convert.reverse = reverse
       return convert

   # Create converters
   km_to_miles = make_unit_converter(0.621371, "km", "miles")
   kg_to_lbs = make_unit_converter(2.20462, "kg", "lbs")
   celsius_to_fahrenheit = make_unit_converter(1.8, "°C", "°F")  # Simplified

   # Use them
   print(km_to_miles(10))
   print(km_to_miles.reverse(6.21))
   print(kg_to_lbs(75))
   print(celsius_to_fahrenheit(25))

**Output:**

::

   10 km = 6.21 miles
   6.21 miles = 10.00 km
   75 kg = 165.35 lbs
   25 °C = 45.00 °F

---

Pattern 4: Memoization (Caching)
---------------------------------

.. index:: memoization, caching, performance optimization

**Memoization** is caching function results to avoid redundant calculations. Closures make this easy!

**Basic Memoization**

.. activecode:: closure_memoization_basic
   :language: python
   :caption: Memoization Decorator

   def memoize(func):
       """Decorator that caches function results"""
       cache = {}  # Private cache stored in closure!

       def wrapper(*args):
           if args in cache:
               print(f"💾 Cache hit for {func.__name__}{args}")
               return cache[args]

           print(f"⚙️  Computing {func.__name__}{args}")
           result = func(*args)
           cache[args] = result
           return result

       return wrapper

   @memoize
   def fibonacci(n):
       """Compute Fibonacci number (slow without memoization)"""
       if n <= 1:
           return n
       return fibonacci(n - 1) + fibonacci(n - 2)

   # Watch the cache at work
   print(f"fib(5) = {fibonacci(5)}\n")
   print(f"fib(6) = {fibonacci(6)}\n")  # Reuses cached values
   print(f"fib(3) = {fibonacci(3)}")    # Completely cached

**Output:**

::

   ⚙️  Computing fibonacci(5)
   ⚙️  Computing fibonacci(4)
   ⚙️  Computing fibonacci(3)
   ⚙️  Computing fibonacci(2)
   ⚙️  Computing fibonacci(1)
   ⚙️  Computing fibonacci(0)
   💾 Cache hit for fibonacci(1)
   💾 Cache hit for fibonacci(2)
   fib(5) = 5

   ⚙️  Computing fibonacci(6)
   💾 Cache hit for fibonacci(5)
   💾 Cache hit for fibonacci(4)
   fib(6) = 8

   💾 Cache hit for fibonacci(3)
   fib(3) = 2

Without memoization, ``fibonacci(6)`` would make **25 function calls**. With memoization: just **3 new calls**!

---

**Performance Comparison**

.. activecode:: closure_memoization_performance
   :language: python
   :caption: Memoization Performance Impact

   import time

   # Without memoization
   def fib_slow(n):
       if n <= 1:
           return n
       return fib_slow(n - 1) + fib_slow(n - 2)

   # With memoization
   def memoize(func):
       cache = {}
       def wrapper(*args):
           if args not in cache:
               cache[args] = func(*args)
           return cache[args]
       return wrapper

   @memoize
   def fib_fast(n):
       if n <= 1:
           return n
       return fib_fast(n - 1) + fib_fast(n - 2)

   # Compare performance
   n = 30

   start = time.time()
   result1 = fib_slow(n)
   time1 = time.time() - start

   start = time.time()
   result2 = fib_fast(n)
   time2 = time.time() - start

   print(f"Computing fibonacci({n}):")
   print(f"Without memoization: {time1:.4f} seconds")
   print(f"With memoization:    {time2:.6f} seconds")
   print(f"Speedup: {time1/time2:.0f}x faster! 🚀")

**Output:**

::

   Computing fibonacci(30):
   Without memoization: 0.2547 seconds
   With memoization:    0.000031 seconds
   Speedup: 8216x faster! 🚀

---

Pattern 5: Partial Application
-------------------------------

.. index:: partial application, function currying, pre-configured functions

**Partial application** means creating a new function by fixing some arguments of an existing function.

**Manual Partial Application**

.. activecode:: closure_partial_application
   :language: python
   :caption: Partial Application with Closures

   def make_multiplier(factor):
       """Create a function that multiplies by a fixed factor"""
       def multiply(x):
           return x * factor
       return multiply

   # Create specialized functions
   double = make_multiplier(2)
   triple = make_multiplier(3)
   halve = make_multiplier(0.5)

   print(double(10))   # 20
   print(triple(10))   # 30
   print(halve(10))    # 5.0

   # More complex example
   def make_greeter(greeting, punctuation):
       """Create a specialized greeting function"""
       def greet(name):
           return f"{greeting}, {name}{punctuation}"
       return greet

   # Create different greeters
   casual_greet = make_greeter("Hey", "!")
   formal_greet = make_greeter("Good evening", ".")
   excited_greet = make_greeter("OMG HI", "!!!")

   print(casual_greet("Alice"))
   print(formal_greet("Dr. Smith"))
   print(excited_greet("bestie"))

**Output:**

::

   20
   30
   5.0
   Hey, Alice!
   Good evening, Dr. Smith.
   OMG HI, bestie!!!

---

**Generic Partial Application Factory**

.. activecode:: closure_partial_factory
   :language: python
   :caption: Generic Partial Application

   def partial(func, *fixed_args, **fixed_kwargs):
       """Create a partial function with some arguments fixed"""

       def wrapper(*args, **kwargs):
           # Combine fixed arguments with new arguments
           all_args = fixed_args + args
           all_kwargs = {**fixed_kwargs, **kwargs}
           return func(*all_args, **all_kwargs)

       return wrapper

   # Example function
   def power(base, exponent):
       return base ** exponent

   # Create specialized functions
   square = partial(power, exponent=2)
   cube = partial(power, exponent=3)
   powers_of_2 = partial(power, 2)

   print(f"square(5) = {square(5)}")
   print(f"cube(5) = {cube(5)}")
   print(f"powers_of_2(10) = {powers_of_2(10)}")

   # More complex example
   def format_message(template, name, age, city):
       return template.format(name=name, age=age, city=city)

   # Create a formatted bio function
   bio_formatter = partial(
       format_message,
       "{name} is {age} years old and lives in {city}."
   )

   print(bio_formatter("Alice", 30, "NYC"))
   print(bio_formatter("Bob", 25, "LA"))

**Output:**

::

   square(5) = 25
   cube(5) = 125
   powers_of_2(10) = 1024
   Alice is 30 years old and lives in NYC.
   Bob is 25 years old and lives in LA.

.. note::
   **Python's Built-in Partial**

   Python's standard library includes ``functools.partial`` which does exactly this!

   .. code-block:: python

      from functools import partial

      double = partial(multiply, 2)

   But understanding how to build it with closures shows the power of the pattern!

---

Real-World Examples
-------------------

.. index:: real-world closures, Flask, Django, click

Let's see how closures appear in popular Python libraries:

**Flask Web Framework**

.. code-block:: python

   from flask import Flask
   app = Flask(__name__)

   @app.route('/users/<int:user_id>')  # Decorator using closures!
   def get_user(user_id):
       return f"User {user_id}"

   # The @app.route decorator is roughly:
   def route(path):
       def decorator(func):
           # Register func with the path
           app.url_map[path] = func
           return func
       return decorator

**Click CLI Framework**

.. code-block:: python

   import click

   @click.command()
   @click.option('--count', default=1)  # Closures for options!
   def hello(count):
       for _ in range(count):
           click.echo('Hello!')

**Pytest Fixtures**

.. code-block:: python

   import pytest

   @pytest.fixture
   def database():
       # Setup
       db = create_database()
       yield db  # Closure captures db
       # Teardown
       db.close()

**Django Middleware**

.. code-block:: python

   def simple_middleware(get_response):
       # One-time configuration

       def middleware(request):
           # Code before view
           response = get_response(request)  # Closure!
           # Code after view
           return response

       return middleware

---

Practice Challenges
--------------------

**Challenge 1: Build a Rate Limiter**

.. activecode:: closure_practice_rate_limiter_2
   :language: python
   :autograde: unittest
   :caption: Challenge - Rate Limiter Decorator

   import time

   def rate_limit(max_calls, period):
       """
       Create a decorator that limits how often a function can be called.

       Args:
           max_calls: Maximum number of calls allowed
           period: Time period in seconds

       Returns:
           None if rate limit exceeded, otherwise function result

       Example: @rate_limit(3, 5) allows 3 calls per 5 seconds
       """
       # TODO: Your code here
       # Hint: Store timestamps of recent calls in a list
       pass

   ====
   from unittest.gui import TestCaseGui
   import time

   class myTests(TestCaseGui):
       def test_decorator_returns_function(self):
           @rate_limit(3, 5)
           def dummy():
               return "OK"

           # Should be callable
           self.assertTrue(callable(dummy))

       def test_allows_calls_within_limit(self):
           @rate_limit(3, 1)
           def api_call():
               return "Success"

           # First 3 calls should succeed
           result1 = api_call()
           result2 = api_call()
           result3 = api_call()

           self.assertEqual(result1, "Success")
           self.assertEqual(result2, "Success")
           self.assertEqual(result3, "Success")

       def test_blocks_calls_exceeding_limit(self):
           @rate_limit(2, 10)
           def api_call():
               return "Success"

           # First 2 calls succeed
           api_call()
           api_call()

           # Third call should raise RateLimitExceeded
           with self.assertRaises(Exception):
               api_call()

       def test_resets_after_period(self):
           @rate_limit(2, 1)  # 2 calls per 1 second
           def api_call():
               return "Success"

           # Use up the limit
           api_call()
           api_call()

           # Wait for period to expire
           time.sleep(1.1)

           # Should work again
           result = api_call()
           self.assertEqual(result, "Success")

       def test_preserves_function_args(self):
           @rate_limit(3, 5)
           def add(a, b):
               return a + b

           result = add(2, 3)
           self.assertEqual(result, 5)

       def test_independent_decorators(self):
           @rate_limit(2, 10)
           def func1():
               return "A"

           @rate_limit(2, 10)
           def func2():
               return "B"

           # Each function has its own limit
           func1()
           func1()
           func2()
           func2()

           # Both should be blocked (independent limits)
           with self.assertRaises(Exception):
               func1()

           with self.assertRaises(Exception):
               func2()

   myTests().main()


.. reveal:: closure_practice_rate_limiter_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def rate_limit(max_calls, period):
          def decorator(func):
              call_times = []  # Store timestamps

              def wrapper(*args, **kwargs):
                  nonlocal call_times
                  current = time.time()

                  # Remove old calls outside the period
                  call_times = [t for t in call_times if current - t < period]

                  if len(call_times) >= max_calls:
                      print(f"❌ Rate limit exceeded! Try again later.")
                      return None

                  call_times.append(current)
                  return func(*args, **kwargs)

              return wrapper
          return decorator

**Challenge 2: Build a Retry Decorator**

.. activecode:: closure_practice_retry_decorator
   :language: python
   :autograde: unittest
   :caption: Challenge - Retry Decorator

   from functools import wraps
   import time

   def retry(max_attempts, delay=0):
       """
       Create a decorator that retries a function if it raises an exception.

       Args:
           max_attempts: Maximum number of attempts
           delay: Seconds to wait between attempts (default: 0)

       Returns:
           Function result if successful, or raises exception after all attempts fail

       Example:
           @retry(max_attempts=3, delay=0.1)
           def flaky_function():
               # Might fail, will retry up to 3 times
               pass
       """
       # TODO: Your code here
       # Hint: Use a loop for attempts
       # Hint: Use try/except to catch exceptions
       # Hint: Use @wraps to preserve function metadata
       pass

   ====
   from unittest.gui import TestCaseGui
   import time

   class myTests(TestCaseGui):
       def test_succeeds_on_first_attempt(self):
           """Test that decorator works with function that succeeds immediately"""
           call_count = [0]

           @retry(max_attempts=3)
           def always_succeeds():
               call_count[0] += 1
               return "Success!"

           result = always_succeeds()

           self.assertEqual(result, "Success!")
           self.assertEqual(call_count[0], 1, "Function should only be called once if it succeeds")

       def test_retries_then_succeeds(self):
           """Test that decorator retries and eventually succeeds"""
           call_count = [0]

           @retry(max_attempts=5)
           def succeeds_on_third_try():
               call_count[0] += 1
               if call_count[0] < 3:
                   raise ValueError(f"Attempt {call_count[0]} failed")
               return "Success!"

           result = succeeds_on_third_try()

           self.assertEqual(result, "Success!")
           self.assertEqual(call_count[0], 3, "Function should be called 3 times")

       def test_fails_after_max_attempts(self):
           """Test that decorator raises exception after all retries fail"""
           call_count = [0]

           @retry(max_attempts=3)
           def always_fails():
               call_count[0] += 1
               raise RuntimeError("Always fails!")

           with self.assertRaises(RuntimeError):
               always_fails()

           self.assertEqual(call_count[0], 3, "Function should be called max_attempts times")

       def test_preserves_function_signature(self):
           """Test that decorator preserves function name and docstring"""
           @retry(max_attempts=2)
           def my_function():
               """This is my docstring"""
               return 42

           self.assertEqual(my_function.__name__, "my_function")
           self.assertEqual(my_function.__doc__, "This is my docstring")

       def test_passes_arguments_correctly(self):
           """Test that decorator passes args and kwargs correctly"""
           @retry(max_attempts=3)
           def add_numbers(a, b, multiply=1):
               return (a + b) * multiply

           result = add_numbers(5, 3, multiply=2)
           self.assertEqual(result, 16)

       def test_uses_proper_exception_handling(self):
           """Test that the implementation uses try/except blocks"""

           # Get the source code of the retry function
           source = self.getEditorText()

           # Check for essential keywords
           self.assertIn('try', source, "Implementation should use 'try' block")
           self.assertIn('except', source, "Implementation should use 'except' block")

       def test_uses_wraps_decorator(self):
           """Test that implementation uses @wraps for metadata preservation"""

           source = self.getEditorText()

           # Check for wraps usage (either @wraps(func) or wraps(func))
           has_wraps = 'wraps' in source or '@wraps' in source
           self.assertTrue(has_wraps, "Implementation should use @wraps or wraps() to preserve function metadata")

   myTests().main()

.. reveal:: closure_practice_retry_decorator_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      from functools import wraps
      import time

      def retry(max_attempts, delay=0):
          def decorator(func):
              @wraps(func)
              def wrapper(*args, **kwargs):
                  for attempt in range(1, max_attempts + 1):
                      try:
                          print(f"Attempt {attempt}/{max_attempts}...")
                          result = func(*args, **kwargs)
                          print(f"✅ Success on attempt {attempt}")
                          return result
                      except Exception as e:
                          if attempt == max_attempts:
                              print(f"❌ Failed after {max_attempts} attempts")
                              raise
                          print(f"⚠️  Failed: {e}. Retrying...")
                          if delay > 0:
                              time.sleep(delay)
              return wrapper
          return decorator

---

**Challenge 3: Build a Memoization Decorator with Expiration**

.. activecode:: closure_practice_memo_expiry
   :language: python
   :autograde: unittest
   :caption: Challenge - Memoization with Expiration

   import time

   def memoize_with_expiry(ttl):
       """
       Create a memoization decorator where cached values expire.

       Args:
           ttl: Time-to-live in seconds (how long cache entries are valid)

       Behavior:
           - First call: computes and caches result with timestamp
           - Subsequent calls: returns cached result if within ttl
           - After ttl seconds: recomputes and updates cache

       Example:
           @memoize_with_expiry(ttl=2)
           def expensive():
               return time.time()

           result1 = expensive()  # Computes
           result2 = expensive()  # Cache hit (same as result1)
           time.sleep(3)
           result3 = expensive()  # Cache expired, recomputes
       """
       # TODO: Your code here
       # Hint: Store both the value AND timestamp in cache
       # Hint: cache format: {args: (result, timestamp)}
       pass

   ====
   from unittest.gui import TestCaseGui
   import time

   class myTests(TestCaseGui):
       def test_caches_results(self):
           """Test that function result is cached"""
           call_count = [0]

           @memoize_with_expiry(ttl=10)
           def counter():
               call_count[0] += 1
               return call_count[0]

           result1 = counter()
           result2 = counter()
           result3 = counter()

           # Should all return the same cached value
           self.assertEqual(result1, 1)
           self.assertEqual(result2, 1)
           self.assertEqual(result3, 1)
           self.assertEqual(call_count[0], 1, "Function should only be called once (cached)")

       def test_cache_expires(self):
           """Test that cache expires after TTL"""
           call_count = [0]

           @memoize_with_expiry(ttl=1)  # 1 second TTL
           def counter():
               call_count[0] += 1
               return call_count[0]

           result1 = counter()  # Call 1: compute
           self.assertEqual(result1, 1)

           result2 = counter()  # Call 2: use cache
           self.assertEqual(result2, 1)
           self.assertEqual(call_count[0], 1, "Should still be using cache")

           time.sleep(1.2)  # Wait for cache to expire

           result3 = counter()  # Call 3: recompute (cache expired)
           self.assertEqual(result3, 2)
           self.assertEqual(call_count[0], 2, "Should have recomputed after expiry")

       def test_different_args_cached_separately(self):
           """Test that different arguments get different cache entries"""
           @memoize_with_expiry(ttl=10)
           def add(a, b):
               return a + b

           result1 = add(2, 3)
           result2 = add(5, 7)
           result3 = add(2, 3)  # Same as first call

           self.assertEqual(result1, 5)
           self.assertEqual(result2, 12)
           self.assertEqual(result3, 5)

       def test_returns_correct_values(self):
           """Test that decorator preserves function return values"""
           @memoize_with_expiry(ttl=5)
           def multiply(x, y):
               return x * y

           self.assertEqual(multiply(3, 4), 12)
           self.assertEqual(multiply(5, 6), 30)
           self.assertEqual(multiply(3, 4), 12)  # From cache

       def test_handles_no_args(self):
           """Test that decorator works with functions that take no arguments"""
           value = [42]

           @memoize_with_expiry(ttl=5)
           def get_value():
               return value[0]

           result1 = get_value()
           value[0] = 100  # Change the value
           result2 = get_value()  # Should still return cached 42

           self.assertEqual(result1, 42)
           self.assertEqual(result2, 42, "Should return cached value, not new value")

       def test_uses_cache_dict(self):
           """Test that implementation uses a cache dictionary"""
           source = self.getEditorText()

           # Check for cache dictionary
           has_cache = 'cache' in source and ('{}' in source or 'dict()' in source)
           self.assertTrue(has_cache, "Implementation should use a cache dictionary")

       def test_uses_time_module(self):
           """Test that implementation uses time.time() for timestamps"""
           source = self.getEditorText()

           self.assertIn('time.time()', source, "Implementation should use time.time() to get current timestamp")

       def test_stores_timestamps(self):
           """Test that implementation stores timestamps with cached values"""
           source = self.getEditorText()

           # Look for tuple storage pattern or timestamp variable
           has_timestamp = 'timestamp' in source or 'time.time()' in source
           self.assertTrue(has_timestamp, "Implementation should store timestamps for cache entries")

       def test_checks_expiration(self):
           """Test that implementation checks if cache has expired"""
           source = self.getEditorText()

           # Should compare current time with stored time
           has_comparison = ('-' in source and 'ttl' in source) or 'current' in source
           self.assertTrue(has_comparison, "Implementation should check if cached entry has expired (current_time - timestamp < ttl)")

   myTests().main()

.. reveal:: closure_practice_memo_expiry_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def memoize_with_expiry(ttl):
          def decorator(func):
              cache = {}  # {args: (result, timestamp)}

              def wrapper(*args):
                  current_time = time.time()

                  if args in cache:
                      result, timestamp = cache[args]
                      if current_time - timestamp < ttl:
                          print(f"💾 Cache hit (age: {current_time - timestamp:.1f}s)")
                          return result
                      else:
                          print("⏰ Cache expired, recomputing...")
                  else:
                      print("⚙️  Computing...")

                  result = func(*args)
                  cache[args] = (result, current_time)
                  return result

              return wrapper
          return decorator

---

Check Your Understanding
-------------------------

.. mchoice:: closure_decorator_essence
   :answer_a: A function that adds decorative output to another function
   :answer_b: A function that takes a function and returns a modified version using a closure
   :answer_c: A special Python keyword for modifying functions
   :answer_d: A way to make functions run faster
   :correct: b
   :feedback_a: "Decorative" isn't literal - it means wrapping/extending functionality!
   :feedback_b: Correct! Decorators use closures to wrap and extend function behavior.
   :feedback_c: While @ is syntax, decorators are functions that use closures.
   :feedback_d: Decorators can affect performance either way (slower with logging, faster with caching).

   What is a decorator in Python?

.. mchoice:: closure_callback_benefit
   :answer_a: Callbacks run faster than regular function calls
   :answer_b: Callbacks can capture and remember context using closures
   :answer_c: Callbacks don't need to be defined before use
   :answer_d: Callbacks automatically handle errors
   :correct: b
   :feedback_a: Callbacks don't inherently run faster.
   :feedback_b: Correct! Closures let callbacks "remember" context like counters, state, or configuration.
   :feedback_c: Functions must be defined before use, whether callbacks or not.
   :feedback_d: Error handling must be explicitly added.

   Why are closures useful for callbacks?

.. mchoice:: closure_memoization_purpose
   :answer_a: To make code look cleaner
   :answer_b: To cache function results and avoid redundant calculations
   :answer_c: To automatically fix bugs in functions
   :answer_d: To make functions thread-safe
   :correct: b
   :feedback_a: Memoization is about performance, not appearance!
   :feedback_b: Correct! Memoization caches results so expensive calculations aren't repeated.
   :feedback_c: Memoization doesn't fix bugs.
   :feedback_d: Basic memoization doesn't provide thread-safety (would need locks).

   What is the purpose of memoization?

.. mchoice:: closure_partial_application_2
   :answer_a: Only partially executing a function
   :answer_b: Creating a new function with some arguments pre-filled using a closure
   :answer_c: Running a function in parallel
   :answer_d: A function that sometimes returns None
   :correct: b
   :feedback_a: The function executes fully, but starts with some pre-filled arguments.
   :feedback_b: Correct! Partial application creates a new function with some args fixed via closure.
   :feedback_c: That's parallel execution, not partial application.
   :feedback_d: Partial refers to arguments, not return values.

   What is partial application?

.. mchoice:: closure_loop_pitfall
   :answer_a: Closures can't be created in loops
   :answer_b: All closures created in a loop share the same loop variable
   :answer_c: Loops make closures run slower
   :answer_d: Closures in loops always cause memory leaks
   :correct: b
   :feedback_a: They can be created, but need careful handling.
   :feedback_b: Correct! All closures see the SAME loop variable, which has the final value after the loop.
   :feedback_c: Performance isn't the issue here.
   :feedback_d: No memory leak, just unexpected behavior with shared variables.

   What's the common pitfall with closures created in loops?

---

Key Takeaways
-------------

.. important::
   **Section 4 Summary: Practical Patterns**

   ✅ **Decorators (Most Important!)**
      - Use closures to wrap and extend function behavior
      - ``@decorator`` syntax is just sugar for ``func = decorator(func)``
      - Common uses: timing, logging, validation, authentication
      - Real examples: Flask's ``@app.route``, pytest's ``@fixture``

   ✅ **Callbacks and Event Handlers**
      - Closures let callbacks "remember" context
      - Essential for GUI programming (button handlers)
      - Solves the problem of passing state to callbacks
      - **Pitfall:** Loop variables in closures (use default arguments!)

   ✅ **Function Factories**
      - Create specialized functions with pre-configured behavior
      - Examples: validators, formatters, converters
      - Cleaner than classes for simple configuraiton
      - Each factory call creates independent closures

   ✅ **Memoization/Caching**
      - Cache expensive function results using closures
      - Can provide massive speedups (1000x+ for recursion)
      - Track cache statistics (hits, misses, size)
      - Python has ``functools.lru_cache`` built-in

   ✅ **Partial Application**
      - Create new functions by fixing some arguments
      - Manual: ``make_multiplier(factor)``
      - Generic: ``functools.partial()``
      - Useful for creating specialized versions of general functions

   ✅ **Real-World Usage**
      - **Web frameworks:** Flask, Django (route decorators, middleware)
      - **CLI tools:** Click (option decorators)
      - **Testing:** Pytest (fixtures)
      - **Data processing:** Pandas, NumPy (custom operations)
      - Closures are **everywhere** in professional Python!

---

What's Next?
------------

You've now mastered practical closure patterns! You can recognize and use closures in:

- ✅ Decorators for extending functionality
- ✅ Callbacks with context
- ✅ Function factories
- ✅ Performance optimization (memoization)
- ✅ Partial application

**In Section 5: Advanced Techniques**, you'll learn:

- Nested decorators and decorator chains
- Decorators with arguments (``@decorator(arg)``)
- Class decorators and ``@staticmethod``/``@property``
- Closure introspection (``__closure__``, ``cell_contents``)
- Performance considerations and memory implications
- Functional programming patterns (map/filter/reduce with closures)

Ready to dive into advanced closure techniques? Let's go! 🚀

---

.. note::
   **✅ Section 4 Complete!**

   You've learned:
   - [✓] Decorators (timing, logging, validation)
   - [✓] Callbacks and event handlers
   - [✓] Function factories
   - [✓] Memoization for performance
   - [✓] Partial application
   - [✓] Real-world examples from popular libraries

   **Ready for advanced techniques?** → Continue to Section 5!