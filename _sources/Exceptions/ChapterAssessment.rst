..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Chapter Assessment
==================

Multiple Choice Questions
--------------------------

.. mchoice:: exceptions_ca_mc1
   :answer_a: Standard input stream
   :answer_b: Standard output stream
   :answer_c: Standard error stream
   :answer_d: A type of exception
   :correct: c
   :feedback_a: That's stdin.
   :feedback_b: That's stdout.
   :feedback_c: Correct! stderr is the standard error stream for error messages and logging.
   :feedback_d: It's a stream, not an exception.

   What is ``sys.stderr``?

.. mchoice:: exceptions_ca_mc2
   :answer_a: Runs only if an exception occurs
   :answer_b: Runs only if no exception occurs
   :answer_c: Always runs, regardless of exceptions
   :answer_d: Never runs
   :correct: c
   :feedback_a: That's the except clause.
   :feedback_b: That's the else clause.
   :feedback_c: Correct! finally ALWAYS runs—perfect for cleanup code.
   :feedback_d: finally always runs!

   When does the ``finally`` clause execute?

.. mchoice:: exceptions_ca_mc3
   :answer_a: Always use assert in production
   :answer_b: Never use assert in production
   :answer_c: assert is fine for production validation
   :answer_d: assert is required for error handling
   :correct: b
   :feedback_a: assert can be disabled with -O flag!
   :feedback_b: Correct! Don't use assert in production—it can be disabled and raises AssertionError.
   :feedback_c: Use proper exceptions for validation, not assert.
   :feedback_d: Use try/except for error handling, not assert.

   Should you use ``assert`` for production input validation?

.. mchoice:: exceptions_ca_mc4
   :answer_a: Runs if an exception occurs
   :answer_b: Runs if NO exception occurs
   :answer_c: Always runs
   :answer_d: Runs before the try block
   :correct: b
   :feedback_a: That's the except block.
   :feedback_b: Correct! The else clause only executes if the try block completed without raising an exception.
   :feedback_c: That's finally.
   :feedback_d: else comes after try/except, not before.

   When does the ``else`` clause in try/except execute?

.. mchoice:: exceptions_ca_mc5
   :answer_a: BaseException
   :answer_b: Error
   :answer_c: Exception
   :answer_d: StandardError
   :correct: c
   :feedback_a: You can, but Exception is the standard base for user-defined exceptions.
   :feedback_b: There's no Error base class in Python.
   :feedback_c: Correct! Custom exceptions should inherit from Exception (or a subclass of it).
   :feedback_d: StandardError doesn't exist in Python 3.

   What should custom exception classes inherit from?

.. mchoice:: exceptions_ca_mc6
   :answer_a: raise NewError() from original
   :answer_b: raise NewError() with original
   :answer_c: raise NewError() and original
   :answer_d: raise NewError(original)
   :correct: a
   :feedback_a: Correct! Use 'from' to chain exceptions and preserve the original cause.
   :feedback_b: That's not valid Python syntax for chaining.
   :feedback_c: That's not valid Python syntax for chaining.
   :feedback_d: That passes original as an argument, not chaining.

   How do you chain exceptions in Python?

.. mchoice:: exceptions_ca_mc7
   :answer_a: try, except, else, finally
   :answer_b: try, except, finally, else
   :answer_c: try, finally, except, else
   :answer_d: try, else, except, finally
   :correct: a
   :feedback_a: Correct! The order is: try, one or more except clauses, optional else, optional finally.
   :feedback_b: else must come before finally.
   :feedback_c: except must come immediately after try.
   :feedback_d: else requires at least one except clause before it.

   What is the correct order of exception handling clauses?

.. mchoice:: exceptions_ca_mc8
   :answer_a: To catch all exceptions including system exits
   :answer_b: To make code shorter
   :answer_c: To handle any type of error
   :answer_d: You should never use bare except
   :correct: d
   :feedback_a: This is why it's BAD - it catches too much!
   :feedback_b: Shorter code that hides errors is worse code.
   :feedback_c: You can't handle different errors appropriately if you don't know what they are.
   :feedback_d: Correct! Always catch specific exceptions so you can handle them appropriately.

   When should you use a bare ``except:`` clause?

.. mchoice:: exceptions_ca_mc9
   :answer_a: assert is for testing; raise is for validation
   :answer_b: assert is faster than raising exceptions
   :answer_c: assert is for user input; exceptions are for programmer errors
   :answer_d: They are equivalent and interchangeable
   :correct: a
   :feedback_a: Correct! assert is for debugging (can be disabled); exceptions are for runtime validation.
   :feedback_b: Performance is not the key difference.
   :feedback_c: This is backwards! assert is for assumptions; exceptions are for validation.
   :feedback_d: They are NOT equivalent - assert can be disabled with python -O.

   What's the difference between ``assert`` and raising an exception?

.. mchoice:: exceptions_ca_mc10
   :answer_a: So you can catch all related errors with one except clause
   :answer_b: To make code more complex
   :answer_c: Python requires it
   :answer_d: To avoid using Exception class
   :correct: a
   :feedback_a: Correct! A hierarchy lets you catch specific errors OR all related errors via the base class.
   :feedback_b: The purpose is organization and flexibility, not complexity.
   :feedback_c: Python doesn't require this - it's a best practice.
   :feedback_d: Your custom exceptions should still ultimately inherit from Exception.

   Why create a custom exception hierarchy?

Parsons Problems
----------------

.. parsonsprob:: exceptions_ca_parsons1
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to create proper exception handling with finally clause.
   -----
   def process_file(filename):
   =====
       f = None
   =====
       try:
   =====
           f = open(filename, 'r')
   =====
           content = f.read()
   =====
           return content
   =====
       except FileNotFoundError:
   =====
           print("File not found")
   =====
           return None
   =====
       finally:
   =====
           if f is not None:
   =====
               f.close()

.. parsonsprob:: exceptions_ca_parsons2
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to create a custom exception with proper structure.
   -----
   class ValidationError(Exception):
   =====
   class ValidationError: #distractor
   =====
       def __init__(self, field, message):
   =====
           self.field = field
   =====
           self.message = message
   =====
           super().__init__(f"{field}: {message}")
   =====
           Exception.__init__(f"{field}: {message}") #distractor

.. parsonsprob:: exceptions_ca_parsons3
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to create try/except with else clause.
   -----
   def safe_convert(text):
   =====
       try:
   =====
           number = int(text)
   =====
       except ValueError:
   =====
           print("Invalid number")
   =====
           return None
   =====
       else:
   =====
           print("Conversion successful")
   =====
           return number
   =====
       finally: #distractor
   =====
           return number #distractor

.. parsonsprob:: exceptions_ca_parsons4
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to create exception chaining.
   -----
   def process_data(data):
   =====
       try:
   =====
           result = int(data)
   =====
           return result * 2
   =====
       except ValueError as e:
   =====
           raise DataProcessingError("Cannot process data") from e
   =====
           raise DataProcessingError("Cannot process data", e) #distractor
   =====
           raise DataProcessingError("Cannot process data") #distractor

.. parsonsprob:: exceptions_ca_parsons5
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to create proper assert usage.
   -----
   def calculate_discount(price, rate):
   =====
       assert isinstance(price, (int, float)), "Price must be numeric"
   =====
       assert price > 0, "Price must be positive"
   =====
       assert 0 <= rate <= 1, "Rate must be between 0 and 1"
   =====
       if price <= 0: #distractor
   =====
           raise ValueError("Price must be positive") #distractor
   =====
       return price * (1 - rate)

Active Code Challenges
----------------------

.. activecode:: exceptions_ca_ac1
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :autograde: unittest

   The code below takes the list of country, ``country``, and searches to see if it is in the dictionary ``gold`` which shows some countries who won gold during the Olympics. However, this code currently does not work. Correctly add try/except clause in the code so that it will correctly populate the list, ``country_gold``, with either the number of golds won or the string "Did not get gold".
   ~~~~
   gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
   country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
   country_gold = []

   for x in country:
       country_gold.append(gold[x])
       country_gold.append("Did not get gold")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOneA(self):
           self.assertEqual(country_gold, [1, 'Did not get gold', 'Did not get gold', 10, 'Did not get gold', 46], "Testing that country_gold is assigned to correct values")

   myTests().main()

.. activecode:: exceptions_ca_ac2
   :tags: Exceptions/intro-exceptions.rst
   :autograde: unittest

   Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes.
   ~~~~
   di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
   total = 0
   for diction in di:
       total = total + diction['Puppies']

   print("Total number of puppies:", total)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(total, 130, "Testing that total has the correct value.")

   myTests().main()

.. activecode:: exceptions_ca_ac3
   :tags: Exceptions/intro-exceptions.rst
   :autograde: unittest

   The list, ``numb``, contains integers. Write code that populates the list ``remainder`` with the remainder of 36 divided by each number in ``numb``. For example, the first element should be 0, because 36/6 has no remainder. If there is an error, have the string "Error" appear in the ``remainder``.
   ~~~~
   numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

   remainder = []

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOneA(self):
           self.assertEqual(remainder, [0, 'Error', 0, 4, 0, 0, 'Error', 0, 36, 'Error', 36, 'Error', 0, 13], "Testing that remainder is assigned to correct values.")

   myTests().main()

.. activecode:: exceptions_ca_ac4
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :autograde: unittest

   Provided is buggy code, insert a try/except so that the code passes.
   ~~~~
   lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]

   lst_three = []

   for num in lst:
       if 3 % num == 0:
           lst_three.append(num)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(lst_three, [1,3], "Testing that lst_three has the correct values.")

   myTests().main()

.. activecode:: exceptions_ca_ac5
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :autograde: unittest

   Write code so that the buggy code provided works using a try/except. When the code does not work in the try, have it append to the list ``attempt`` the string "Error".
   ~~~~
   full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

   attempt = []

   for elem in full_lst:
       attempt.append(elem[1])

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(attempt, ['b', 'd', 'g', 'Error', 'k', 'o', 'r', 'Error', 'v', 'x', 'Error'], "Testing that attempt has the correct values.")

   myTests().main()

.. activecode:: exceptions_ca_ac6
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :autograde: unittest

   The following code tries to append the third element of each list in ``conts`` to the new list ``third_countries``. Currently, the code does not work. Add a try/except clause so the code runs without errors, and the string 'Continent does not have 3 countries' is appended to ``third_countries`` instead of producing an error.
   ~~~~
   conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'], ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'], ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'], ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopia', 'South Africa'], ['Antarctica']]

   third_countries = []

   for c in conts:
       third_countries.append(c[2])

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(third_countries, ['Greece', 'Canada', 'Korea', 'Brazil', 'Continent does not have 3 countries', 'Kenya', 'Continent does not have 3 countries'], "Testing that third_countries is created correctly.")

   myTests().main()

.. activecode:: exceptions_ca_ac7
   :tags:Exceptions/intro-exceptions.rst
   :practice: T
   :autograde: unittest

   The buggy code below prints out the value of the sport in the list ``sport``. Use try/except so that the code will run properly. If the sport is not in the dictionary, ``ppl_play``, add it in with the value of 1.
   ~~~~
   sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

   ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

   for x in sport:
       print(ppl_play[x])

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOneA(self):
           self.assertEqual(sorted(ppl_play.items()), [('baseball', 1), ('basketball', 1), ('football', 15), ('hockey', 4), ('soccer', 10), ('tennis', 8)], "Testing that ppl_play is assigned to correct values.")

   myTests().main()

.. activecode:: exceptions_ca_ac8
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :autograde: unittest

   Provided is a buggy for loop that tries to accumulate some values out of some dictionaries. Insert a try/except so that the code passes. If the key is not there, initialize it in the dictionary and set the value to zero.
   ~~~~
   di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
   total = 0
   for diction in di:
       total = total + diction['Puppies']

   print("Total number of puppies:", total)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           accum = 0
           for diction in di:
               if 'Puppies' in diction:
                   accum += 1
           self.assertEqual(accum, 4, "Testing that every dictionary in di has the key 'Puppies'.")

   myTests().main()

.. activecode:: exceptions_ca_ac9
   :language: python
   :autograde: unittest

   Write a function ``safe_divide(a, b)`` that divides two numbers. If division is successful, use the else clause to print "Division successful" and return the result. If there's an error, print an error message and return None. Use finally to print "Operation complete".
   ~~~~
   def safe_divide(a, b):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = safe_divide(10, 2)
           self.assertEqual(result, 5.0)

       def testTwo(self):
           result = safe_divide(10, 0)
           self.assertIsNone(result)

   myTests().main()

.. activecode:: exceptions_ca_ac10
   :language: python
   :autograde: unittest

   Create a custom exception class ``NegativeValueError`` that inherits from Exception. Then write a function ``calculate_square_root(n)`` that raises this exception if n is negative, otherwise returns the square root (use ``n ** 0.5``).
   ~~~~
   # Define your custom exception class here

   def calculate_square_root(n):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = calculate_square_root(16)
           self.assertEqual(result, 4.0)

       def testTwo(self):
           try:
               calculate_square_root(-4)
               self.fail("Should raise NegativeValueError")
           except Exception as e:
               self.assertEqual(type(e).__name__, "NegativeValueError")

   myTests().main()

.. activecode:: exceptions_ca_ac11
   :language: python
   :autograde: unittest

   Write a function ``validate_age(age)`` that uses assert statements to check: 1) age is an integer, 2) age is not negative, 3) age is less than 150. If all checks pass, return True.
   ~~~~
   def validate_age(age):
       # Your code here with assert statements
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = validate_age(25)
           self.assertTrue(result)

       def testTwo(self):
           try:
               validate_age(-5)
               self.fail("Should raise AssertionError")
           except AssertionError:
               pass

   myTests().main()

.. activecode:: exceptions_ca_ac12
   :language: python
   :autograde: unittest

   Write a function ``process_numbers(numbers)`` that attempts to convert each string in the list to an integer. Use exception chaining: if conversion fails, raise a ValueError with message "Cannot process list" chained from the original error.
   ~~~~
   def process_numbers(numbers):
       # Your code here with exception chaining
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = process_numbers(["1", "2", "3"])
           self.assertEqual(result, [1, 2, 3])

       def testTwo(self):
           try:
               process_numbers(["1", "abc", "3"])
               self.fail("Should raise ValueError")
           except ValueError as e:
               self.assertIsNotNone(e.__cause__)

   myTests().main()

Debugging Exercises
-------------------

.. activecode:: exceptions_ca_debug1
   :language: python
   :autograde: unittest

   This code doesn't handle exceptions properly. Fix it!
   ~~~~
   def divide_numbers(a, b):
       try:
           result = a / b
       except:
           print("Error occurred")

       return result

   print(divide_numbers(10, 2))
   print(divide_numbers(10, 0))

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = divide_numbers(10, 2)
           self.assertEqual(result, 5.0)

       def testTwo(self):
           result = divide_numbers(10, 0)
           self.assertIsNone(result)

   myTests().main()

.. activecode:: exceptions_ca_debug2
   :language: python
   :autograde: unittest

   This code uses assert incorrectly for validation. Fix it to use proper exception handling instead.
   ~~~~
   def withdraw_money(balance, amount):
       assert amount > 0, "Amount must be positive"
       assert amount <= balance, "Insufficient funds"
       return balance - amount

   print(withdraw_money(100, 50))
   print(withdraw_money(100, 150))

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = withdraw_money(100, 50)
           self.assertEqual(result, 50)

       def testTwo(self):
           try:
               withdraw_money(100, 150)
               self.fail("Should raise ValueError")
           except ValueError:
               pass

   myTests().main()

.. activecode:: exceptions_ca_debug3
   :language: python
   :autograde: unittest

   This code doesn't properly use the else clause. Fix it so success code only runs when no exception occurs.
   ~~~~
   def read_number(text):
       try:
           number = int(text)
           print("Conversion successful")
           return number
       except ValueError:
           print("Invalid number")
           return None

   read_number("42")
   read_number("abc")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = read_number("42")
           self.assertEqual(result, 42)

       def testTwo(self):
           result = read_number("abc")
           self.assertIsNone(result)

   myTests().main()

.. activecode:: exceptions_ca_debug4
   :language: python
   :autograde: unittest

   This code doesn't use finally for cleanup. Fix it to ensure the resource is always closed.
   ~~~~
   def process_data(data):
       resource = "opened"
       try:
           if data < 0:
               raise ValueError("Negative value")
           result = data * 2
           resource = "closed"
           return result
       except ValueError:
           return None

   print(process_data(10))
   print(process_data(-5))

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = process_data(10)
           self.assertEqual(result, 20)

       def testTwo(self):
           result = process_data(-5)
           self.assertIsNone(result)

   myTests().main()

.. activecode:: exceptions_ca_debug5
   :language: python
   :autograde: unittest

   This custom exception doesn't follow best practices. Fix it to properly inherit from Exception and include useful attributes.
   ~~~~
   class MyError:
       def __init__(self, msg):
           self.msg = msg

   def risky_operation(value):
       if value < 0:
           raise MyError("Negative value")
       return value * 2

   print(risky_operation(5))
   print(risky_operation(-5))

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = risky_operation(5)
           self.assertEqual(result, 10)

       def testTwo(self):
           try:
               risky_operation(-5)
               self.fail("Should raise exception")
           except Exception as e:
               self.assertTrue(isinstance(e, Exception))

   myTests().main()

Quick Reference Guide
---------------------

.. important:: **Exception Handling Patterns**

   **Basic Try/Except**

   ::

      try:
          risky_operation()
      except SpecificError:
          handle_error()

   **With Else (success code)**

   ::

      try:
          risky_operation()
      except SpecificError:
          handle_error()
      else:
          success_code()  # Only runs if no exception

   **With Finally (cleanup)**

   ::

      try:
          risky_operation()
      except SpecificError:
          handle_error()
      finally:
          cleanup()  # ALWAYS runs

   **Complete Structure**

   ::

      try:
          risky_operation()
      except SpecificError:
          handle_error()
      else:
          success_code()
      finally:
          cleanup()

   **Custom Exception**

   ::

      class CustomError(Exception):
          def __init__(self, message, data):
              super().__init__(message)
              self.data = data

   **Exception Chaining**

   ::

      try:
          operation()
      except OriginalError as e:
          raise NewError("Context") from e

   **Assert Statement**

   ::

      # For debugging only!
      assert condition, "Error message"