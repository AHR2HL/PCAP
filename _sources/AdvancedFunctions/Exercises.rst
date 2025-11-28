..  Copyright (C)  Alpha Schools

.. qnum::
   :prefix: advfunc-ex-
   :start: 1

Exercises: Advanced Functions
==============================

Lambda Expressions
------------------

.. activecode:: advfunc_ex_lambda1
   :practice: T

   **Exercise 1:** Write a function ``sort_by_last_letter(words)`` that takes a list of words and returns them sorted by their last letter (not alphabetically).

   Use ``sorted()`` with a lambda expression for the ``key`` parameter.

   Example: ``sort_by_last_letter(['apple', 'banana', 'cherry'])`` → ``['banana', 'apple', 'cherry']``
   (sorted by last letters: 'a', 'e', 'y')

   ~~~~
   def sort_by_last_letter(words):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(sort_by_last_letter(['apple', 'banana', 'cherry']), ['banana', 'apple', 'cherry'], "Test 1")
           self.assertEqual(sort_by_last_letter(['dog', 'cat', 'bird']), ['bird', 'dog', 'cat'], "Test 2")
           self.assertEqual(sort_by_last_letter(['python', 'java', 'ruby']), ['java', 'ruby', 'python'], "Test 3")

   myTests().main()


.. activecode:: advfunc_ex_lambda2
   :practice: T

   **Exercise 2:** Write a function ``filter_long_strings(strings, min_length)`` that returns a new list containing only strings that are at least ``min_length`` characters long.

   Use ``filter()`` with a lambda expression.

   Example: ``filter_long_strings(['a', 'hello', 'hi', 'world'], 4)`` → ``['hello', 'world']``

   ~~~~
   def filter_long_strings(strings, min_length):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(filter_long_strings(['a', 'hello', 'hi', 'world'], 4), ['hello', 'world'], "Test 1")
           self.assertEqual(filter_long_strings(['cat', 'dog', 'elephant', 'ant'], 5), ['elephant'], "Test 2")
           self.assertEqual(filter_long_strings(['Python', 'is', 'awesome'], 3), ['Python', 'awesome'], "Test 3")

   myTests().main()


Closures
--------

.. activecode:: advfunc_ex_closure1
   :practice: T

   **Exercise 3:** Create a closure function ``make_greeter(greeting)`` that returns a function. The returned function should take a name and return a greeting message.

   Example:

   * ``hello = make_greeter("Hello")``
   * ``hello("Alice")`` → ``"Hello, Alice!"``
   * ``hi = make_greeter("Hi")``
   * ``hi("Bob")`` → ``"Hi, Bob!"``

   ~~~~
   def make_greeter(greeting):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           hello = make_greeter("Hello")
           hi = make_greeter("Hi")
           self.assertEqual(hello("Alice"), "Hello, Alice!", "Test 1")
           self.assertEqual(hi("Bob"), "Hi, Bob!", "Test 2")
           self.assertEqual(hello("World"), "Hello, World!", "Test 3")

   myTests().main()


.. activecode:: advfunc_ex_closure2
   :practice: T

   **Exercise 4:** Create a closure ``make_counter(start=0)`` that returns a function. Each time the returned function is called, it should return the next number in sequence.

   Example:

   * ``counter = make_counter()``
   * ``counter()`` → ``0``
   * ``counter()`` → ``1``
   * ``counter()`` → ``2``
   * ``counter2 = make_counter(100)``
   * ``counter2()`` → ``100``
   * ``counter2()`` → ``101``

   ~~~~
   def make_counter(start=0):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           counter = make_counter()
           self.assertEqual(counter(), 0, "Test 1")
           self.assertEqual(counter(), 1, "Test 2")
           self.assertEqual(counter(), 2, "Test 3")

           counter2 = make_counter(100)
           self.assertEqual(counter2(), 100, "Test 4")
           self.assertEqual(counter2(), 101, "Test 5")

   myTests().main()


.. activecode:: advfunc_ex_closure3
   :practice: T

   **Exercise 5:** Create a closure ``make_power(exponent)`` that returns a function. The returned function should take a number and raise it to the specified exponent.

   Example:

   * ``square = make_power(2)``
   * ``square(5)`` → ``25``
   * ``cube = make_power(3)``
   * ``cube(2)`` → ``8``

   ~~~~
   def make_power(exponent):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           square = make_power(2)
           cube = make_power(3)
           self.assertEqual(square(5), 25, "Test 1: 5^2")
           self.assertEqual(square(10), 100, "Test 2: 10^2")
           self.assertEqual(cube(2), 8, "Test 3: 2^3")
           self.assertEqual(cube(3), 27, "Test 4: 3^3")

   myTests().main()


Decorators
----------

.. activecode:: advfunc_ex_decorator1
   :practice: T

   **Exercise 6:** Write a decorator ``uppercase_result`` that converts the return value of a function to uppercase.

   Example:

   .. code-block:: python

      @uppercase_result
      def greet(name):
          return f"hello {name}"

      greet("alice")  # Returns "HELLO ALICE"

   ~~~~
   def uppercase_result(func):
       # Your code here
       pass

   @uppercase_result
   def greet(name):
       return f"hello {name}"

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(greet("alice"), "HELLO ALICE", "Test 1")
           self.assertEqual(greet("bob"), "HELLO BOB", "Test 2")

   myTests().main()


.. activecode:: advfunc_ex_decorator2
   :practice: T

   **Exercise 7:** Write a decorator ``double_result`` that doubles the numeric return value of a function.

   Example:

   .. code-block:: python

      @double_result
      def add(a, b):
          return a + b

      add(3, 4)  # Returns 14 (not 7)

   ~~~~
   def double_result(func):
       # Your code here
       pass

   @double_result
   def add(a, b):
       return a + b

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(add(3, 4), 14, "Test 1: (3+4)*2")
           self.assertEqual(add(10, 5), 30, "Test 2: (10+5)*2")
           self.assertEqual(add(0, 0), 0, "Test 3: (0+0)*2")

   myTests().main()


.. activecode:: advfunc_ex_decorator3
   :practice: T

   **Exercise 8 (Challenge):** Write a decorator ``call_counter`` that counts how many times a function has been called. The decorator should add a ``.call_count`` attribute to the function.

   Example:

   .. code-block:: python

      @call_counter
      def say_hello():
          return "Hello"

      say_hello()
      say_hello()
      print(say_hello.call_count)  # 2

   ~~~~
   def call_counter(func):
       # Your code here
       pass

   @call_counter
   def say_hello():
       return "Hello"

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           say_hello()
           say_hello()
           say_hello()
           self.assertEqual(say_hello.call_count, 3, "Test 1: called 3 times")
           say_hello()
           self.assertEqual(say_hello.call_count, 4, "Test 2: called 4 times")

   myTests().main()