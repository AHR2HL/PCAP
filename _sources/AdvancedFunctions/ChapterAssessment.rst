..  Copyright (C)  Alpha Schools

.. qnum::
   :prefix: advfunc-assess-
   :start: 1

Chapter Assessment: Advanced Functions
=======================================

Part 1: Multiple Choice Questions
----------------------------------

.. mchoice:: advfunc_assess_mc1
   :answer_a: add = lambda x: x + y
   :answer_b: add = lambda x, y: x + y
   :answer_c: add = lambda(x, y): x + y
   :answer_d: lambda add(x, y): return x + y
   :correct: b
   :feedback_a: This lambda only takes one parameter (x). You need two parameters.
   :feedback_b: Correct! Lambda syntax is: lambda parameters: expression
   :feedback_c: Parameters should not be in parentheses after lambda
   :feedback_d: Lambda doesn't use 'def' syntax or 'return' keyword

   Which of the following correctly defines a lambda function that adds two numbers?


.. mchoice:: advfunc_assess_mc2
   :answer_a: The outer function's local variables
   :answer_b: Only global variables
   :answer_c: Only its own parameters
   :answer_d: Nothing - it has no memory
   :correct: a
   :feedback_a: Correct! A closure "remembers" variables from its enclosing scope
   :feedback_b: Closures can access global variables, but more importantly they remember local variables from the enclosing function
   :feedback_c: Closures can access their own parameters AND variables from the outer function
   :feedback_d: This is the key feature of closures - they DO remember their environment

   What does a closure "remember" from its enclosing function?


.. mchoice:: advfunc_assess_mc3
   :answer_a: Before the function definition
   :answer_b: After the function definition
   :answer_c: Inside the function definition
   :answer_d: At the function call site
   :correct: a
   :feedback_a: Correct! Decorators use @ syntax before the function: @decorator followed by def function()
   :feedback_b: Decorators must come before the function definition
   :feedback_c: Decorators are applied outside, not inside the function
   :feedback_d: Decorators are applied at definition time, not call time

   Where is the ``@decorator`` syntax placed?


.. mchoice:: advfunc_assess_mc4
   :answer_a: lambda x: if x > 0: return x else: return 0
   :answer_b: lambda x: x if x > 0 else 0
   :answer_c: lambda x: return x if x > 0 else 0
   :answer_d: lambda x: (x > 0) ? x : 0
   :correct: b
   :feedback_a: Lambda doesn't use if:/else: blocks or return keyword
   :feedback_b: Correct! Use ternary operator: value_if_true if condition else value_if_false
   :feedback_c: Lambda doesn't use 'return' keyword
   :feedback_d: Python uses 'if/else', not '?' ternary operator (that's from C/Java)

   How do you write a conditional in a lambda expression?


.. mchoice:: advfunc_assess_mc5
   :answer_a: To allow functions to modify global state
   :answer_b: To create data hiding and encapsulation without classes
   :answer_c: To make functions run faster
   :answer_d: To avoid using function parameters
   :correct: b
   :feedback_a: While closures can access outer variables, their main purpose is encapsulation
   :feedback_b: Correct! Closures provide a way to create private state and factory functions
   :feedback_c: Closures don't improve performance; they provide encapsulation
   :feedback_d: Closures still use parameters; they additionally remember outer scope variables

   What is the primary purpose of using closures in Python?

.. mchoice:: advfunc_assess_mc6
   :answer_a: To capture all positional arguments as a tuple
   :answer_b: To capture all keyword arguments as a dictionary
   :answer_c: To pass a list to a function
   :answer_d: To create a pointer
   :correct: a
   :feedback_a: Correct! *args collects extra positional arguments into a tuple
   :feedback_b: That's **kwargs
   :feedback_c: *args captures arguments, doesn't pass lists
   :feedback_d: Python doesn't have pointers like C

   What does ``*args`` do in a function definition?

.. mchoice:: advfunc_assess_mc7
   :answer_a: To capture all positional arguments
   :answer_b: To capture all keyword arguments as a dictionary
   :answer_c: To create a double pointer
   :answer_d: To multiply arguments
   :correct: b
   :feedback_a: That's *args
   :feedback_b: Correct! **kwargs collects extra keyword arguments into a dict
   :feedback_c: Python doesn't have pointers
   :feedback_d: ** in function definition is for keyword arguments

   What does ``**kwargs`` do in a function definition?

.. mchoice:: advfunc_assess_mc8
   :answer_a: To modify global variables
   :answer_b: To modify variables in the enclosing scope
   :answer_c: To create new variables
   :answer_d: To delete variables
   :correct: b
   :feedback_a: That's global keyword
   :feedback_b: Correct! nonlocal allows modifying variables from outer (not global) scope
   :feedback_c: You don't need nonlocal to create variables
   :feedback_d: Use del to delete variables

   What is the ``nonlocal`` keyword used for?


Part 2: Active Code Problems
-----------------------------

.. activecode:: advfunc_assess_ac1

   **Problem 1:** Write a function ``sort_by_second(tuples)`` that sorts a list of tuples by the second element of each tuple using a lambda expression.

   Example: ``sort_by_second([(1, 3), (4, 1), (2, 2)])`` → ``[(4, 1), (2, 2), (1, 3)]``

   ~~~~
   def sort_by_second(tuples):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(sort_by_second([(1, 3), (4, 1), (2, 2)]), [(4, 1), (2, 2), (1, 3)], "Test 1")
           self.assertEqual(sort_by_second([('a', 5), ('b', 2), ('c', 8)]), [('b', 2), ('a', 5), ('c', 8)], "Test 2")
           self.assertEqual(sort_by_second([(10, 100), (20, 50), (30, 75)]), [(20, 50), (30, 75), (10, 100)], "Test 3")

   myTests().main()


.. activecode:: advfunc_assess_ac2

   **Problem 2:** Create a closure ``make_accumulator(initial=0)`` that returns a function. Each time the returned function is called with a number, it should add that number to the running total and return the new total.

   Example:

   * ``acc = make_accumulator()``
   * ``acc(5)`` → ``5``
   * ``acc(3)`` → ``8``
   * ``acc(2)`` → ``10``

   ~~~~
   def make_accumulator(initial=0):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           acc = make_accumulator()
           self.assertEqual(acc(5), 5, "Test 1")
           self.assertEqual(acc(3), 8, "Test 2")
           self.assertEqual(acc(2), 10, "Test 3")

           acc2 = make_accumulator(100)
           self.assertEqual(acc2(10), 110, "Test 4")
           self.assertEqual(acc2(5), 115, "Test 5")

   myTests().main()


.. activecode:: advfunc_assess_ac8

   **Problem 8:** Use ``reduce()`` from functools to find the product of all numbers in a list.

   Write ``product(numbers)`` that returns the product of all numbers.

   ~~~~
   from functools import reduce

   def product(numbers):
       # Your code here (use reduce and lambda)
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(product([1, 2, 3, 4]), 24, "Test 1: 1*2*3*4")
           self.assertEqual(product([2, 5, 10]), 100, "Test 2: 2*5*10")
           self.assertEqual(product([5]), 5, "Test 3: single element")

   myTests().main()

.. activecode:: advfunc_assess_ac9

   **Problem 9:** Create a decorator factory ``repeat(n)`` that makes a function execute n times.

   Example:

   .. code-block:: python

      @repeat(3)
      def greet(name):
          print(f"Hello, {name}!")

      greet("Alice")
      # Prints:
      # Hello, Alice!
      # Hello, Alice!
      # Hello, Alice!

   ~~~~
   def repeat(n):
       # Your code here (return a decorator)
       pass

   @repeat(3)
   def greet(name):
       print(f"Hello, {name}!")

   # This should print 3 times
   greet("Alice")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           # Test with counter
           call_count = []

           @repeat(3)
           def counter():
               call_count.append(1)

           counter()
           self.assertEqual(len(call_count), 3, "Should be called 3 times")

       def testTwo(self):
           @repeat(5)
           def adder(x):
               return x + 1

           # Should still return last result
           result = adder(10)
           self.assertEqual(result, 11, "Should return result from function")

   myTests().main()

.. activecode:: advfunc_assess_ac3

   **Problem 3:** Use ``map()`` and a lambda to convert a list of temperatures in Celsius to Fahrenheit. Formula: F = (C * 9/5) + 32

   Write a function ``celsius_to_fahrenheit(temps_c)`` that returns a list of Fahrenheit temperatures.

   ~~~~
   def celsius_to_fahrenheit(temps_c):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(celsius_to_fahrenheit([0, 100, -40]), [32.0, 212.0, -40.0], "Test 1")
           self.assertEqual(celsius_to_fahrenheit([20, 25, 30]), [68.0, 77.0, 86.0], "Test 2")

   myTests().main()


.. activecode:: advfunc_assess_ac4

   **Problem 4:** Create a closure ``make_validator(min_val, max_val)`` that returns a function. The returned function should take a number and return ``True`` if it's in range [min_val, max_val], ``False`` otherwise.

   Example:

   * ``check_age = make_validator(18, 65)``
   * ``check_age(25)`` → ``True``
   * ``check_age(70)`` → ``False``

   ~~~~
   def make_validator(min_val, max_val):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           check_age = make_validator(18, 65)
           self.assertEqual(check_age(25), True, "Test 1")
           self.assertEqual(check_age(70), False, "Test 2")
           self.assertEqual(check_age(18), True, "Test 3: boundary")
           self.assertEqual(check_age(65), True, "Test 4: boundary")
           self.assertEqual(check_age(17), False, "Test 5")

   myTests().main()


.. activecode:: advfunc_assess_ac5

   **Problem 5:** Write a decorator ``ensure_list`` that converts the return value of a function to a list (using ``list()``).

   Example:

   .. code-block:: python

      @ensure_list
      def get_range(n):
          return range(n)

      get_range(5)  # Returns [0, 1, 2, 3, 4], not range object

   ~~~~
   def ensure_list(func):
       # Your code here
       pass

   @ensure_list
   def get_range(n):
       return range(n)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = get_range(5)
           self.assertEqual(result, [0, 1, 2, 3, 4], "Test 1")
           self.assertEqual(type(result), list, "Test 2: Should be a list")

   myTests().main()


Part 3: Debugging Exercises
----------------------------

.. activecode:: advfunc_assess_debug1

   **Debug Exercise 1:** This closure should create a multiplier function, but it's not working correctly. Find and fix the bug.

   ~~~~
   def make_multiplier(factor):
       def multiply(x):
           factor = factor * x
           return factor
       return multiply

   times_2 = make_multiplier(2)
   print(times_2(5))  # Should print 10
   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           times_2 = make_multiplier(2)
           times_3 = make_multiplier(3)
           self.assertEqual(times_2(5), 10, "Test 1")
           self.assertEqual(times_3(4), 12, "Test 2")

   myTests().main()


.. activecode:: advfunc_assess_debug2

   **Debug Exercise 2:** This decorator should add 10 to the result, but it's broken. Find and fix the bug.

   ~~~~
   def add_ten(func):
       def wrapper(a, b):  # Simplified - explicit parameters
           result = func(a, b)
           return result
       return result  # Bug: should return wrapper, not result

   @add_ten
   def add(a, b):
       return a + b

   print(add(5, 3))  # Should print 18 (5+3+10)
   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(add(5, 3), 18, "Test 1: 5+3+10")
           self.assertEqual(add(0, 0), 10, "Test 2: 0+0+10")

   myTests().main()


.. activecode:: advfunc_assess_debug3

   **Debug Exercise 3:** This lambda should filter out even numbers, but it's doing the opposite. Fix it.

   ~~~~
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   odd_numbers = list(filter(lambda x: x % 2 == 0, numbers))
   print(odd_numbers)  # Should print [1, 3, 5, 7, 9]
   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(odd_numbers, [1, 3, 5, 7, 9], "Test: should contain only odd numbers")

   myTests().main()


Part 4: Parson's Problems
--------------------------

.. parsonsprob:: advfunc_assess_parsons1
   :numbered: left
   :adaptive:

   Arrange the code blocks to create a closure that makes a function remember a prefix string and adds it to any string passed in.

   Example: ``add_prefix = make_prefix("Hello, ")`` then ``add_prefix("World")`` returns ``"Hello, World"``
   -----
   def make_prefix(prefix):
   =====
   def make_prefix(prefix) #paired
   =====
       def add(text):
   =====
       def add(text) #paired
   =====
           return prefix + text
   =====
           return prefix.text #paired
   =====
       return add
   =====
       return add() #paired


.. parsonsprob:: advfunc_assess_parsons4
   :numbered: left
   :adaptive:

   Arrange the blocks to use reduce() to find the maximum value in a list.
   -----
   from functools import reduce
   =====
   from itertools import reduce #paired
   =====
   numbers = [3, 7, 2, 9, 1]
   =====
   max_val = reduce(lambda a, b: a if a > b else b, numbers)
   =====
   max_val = reduce(lambda a, b: max(a, b), numbers) #paired
   =====
   max_val = map(lambda a, b: a if a > b else b, numbers) #paired

.. parsonsprob:: advfunc_assess_parsons5
   :numbered: left
   :adaptive:

   Arrange the blocks to create a function that accepts any arguments with ``*args`` and ``**kwargs``.
   -----
   def flexible_func(*args, **kwargs):
   =====
   def flexible_func(args, kwargs): #paired
   =====
       print(f"Positional: {args}")
   =====
       print(f"Keyword: {kwargs}")
   =====
       return len(args) + len(kwargs)
   =====
       return args + kwargs #paired

.. parsonsprob:: advfunc_assess_parsons2
   :numbered: left
   :adaptive:

   Arrange the code blocks to create a decorator that prints "Starting..." before a function runs and "Done!" after it completes.
   -----
   def debug_decorator(func):
   =====
       def wrapper(*args, **kwargs):
   =====
       def wrapper(func): #paired
   =====
           print("Starting...")
   =====
           result = func(*args, **kwargs)
   =====
           result = func() #paired
   =====
           print("Done!")
   =====
           return result
   =====
       return wrapper
   =====
       return wrapper() #paired


.. parsonsprob:: advfunc_assess_parsons3
   :numbered: left
   :adaptive:

   Arrange the code blocks to use filter() and lambda to keep only strings longer than 5 characters.
   -----
   words = ["hi", "hello", "hey", "goodbye", "yo"]
   =====
   long_words = list(filter(lambda w: len(w) > 5, words))
   =====
   long_words = list(filter(lambda w: len(w) < 5, words)) #paired
   =====
   long_words = filter(lambda w: len(w) > 5, words) #paired
   =====
   long_words = list(map(lambda w: len(w) > 5, words)) #paired


Summary & Self-Check
---------------------

After completing this assessment, you should be able to:

✅ Write and use lambda expressions for simple operations

✅ Understand when lambda is appropriate vs regular ``def`` functions

✅ Create closures that remember values from their enclosing scope

✅ Explain the difference between closures and global variables

✅ Write decorators that modify function behavior

✅ Use the ``@`` syntax to apply decorators

✅ Combine lambda with ``map()``, ``filter()``, and ``sorted()``

✅ Debug common mistakes with lambda, closures, and decorators

**Struggling with any of these?** Review the relevant sections:

* **Lambda Expressions** - If you struggle with lambda syntax or usage
* **Closures** (all 5 lessons) - If closures are still unclear
* **Decorators** - If decorator syntax or mechanics are confusing
* **Programming Style** - If you're unsure when to use each technique

**Ready to continue?** These advanced function techniques are used throughout professional Python code and are essential for the PCAP certification!