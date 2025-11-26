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

.. mchoice:: pcap_vocab_stderr
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

.. mchoice:: pcap_vocab_finally
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

.. mchoice:: pcap_concept_assert_production
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

**Exception with Finally**

.. parsonsprob:: pcap_parsons_finally
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


.. activecode:: ac_exceptions_01
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :autograde: unittest
   :topics: Exceptions/intro-exceptions.rst

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


.. activecode:: ac_exceptions_011
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


.. activecode:: ac_exceptions_02
   :tags:Exceptions/intro-exceptions.rst
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

.. activecode:: ac_exceptions_021
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :topics: Exceptions/intro-exceptions.rst
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


.. activecode:: ac_exceptions_03
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :autograde: unittest
   :topics: Exceptions/intro-exceptions.rst

   Write code so that the buggy code provided works using a try/except. When the codes does not work in the try, have it append to the list ``attempt`` the string "Error".
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

.. activecode:: ac_exceptions_031
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :topics: Exceptions/intro-exceptions.rst
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


.. activecode:: ac_exceptions_04
   :tags:Exceptions/intro-exceptions.rst
   :practice: T
   :topics: Exceptions/intro-exceptions.rst
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


.. activecode:: ac_exceptions_041
   :tags: Exceptions/intro-exceptions.rst
   :practice: T
   :topics: Exceptions/intro-exceptions.rst
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
**Debug: Broken Exception Handling**

.. activecode:: pcap_debug_exception
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
       def test_normal_division(self):
           """Should correctly divide two numbers"""
           result = divide_numbers(10, 2)
           self.assertEqual(result, 5.0, "10 / 2 should equal 5.0")

       def test_division_with_floats(self):
           """Should handle float division"""
           result = divide_numbers(7, 2)
           self.assertEqual(result, 3.5, "7 / 2 should equal 3.5")

       def test_zero_division_returns_value(self):
           """Should return a value (not crash) when dividing by zero"""
           result = divide_numbers(10, 0)
           self.assertIsNotNone(result, "Should return None instead of crashing")

       def test_zero_division_does_not_crash(self):
           """Should not raise exception when dividing by zero"""
           try:
               result = divide_numbers(10, 0)
               crashed = False
           except:
               crashed = True
           self.assertFalse(crashed, "Should handle division by zero without crashing")

       def test_catches_specific_exception(self):
           """Should catch ZeroDivisionError specifically"""
           source = self.getEditorText()
           func_code = source.split('def divide_numbers(')[1].split('\n\n')[0]
           self.assertIn('ZeroDivisionError', func_code,
                        "Should catch ZeroDivisionError specifically, not bare except")

       def test_no_bare_except(self):
           """Should not use bare except:"""
           source = self.getEditorText()
           func_code = source.split('def divide_numbers(')[1].split('\n\n')[0]

           # Check for bare except (except: with no exception type)
           lines = func_code.split('\n')
           for line in lines:
               if 'except' in line and ':' in line:
                   # Make sure there's something between 'except' and ':'
                   except_part = line.split('except')[1].split(':')[0].strip()
                   if except_part == '':
                       self.fail("Should not use bare 'except:' - specify exception type")

       def test_negative_numbers(self):
           """Should handle negative numbers"""
           result = divide_numbers(-10, 2)
           self.assertEqual(result, -5.0)

       def test_type_error_handled(self):
           """Should handle invalid types gracefully"""
           result = divide_numbers("10", 2)
           # Should return None or handle gracefully, not crash
           self.assertTrue(result is None or isinstance(result, (int, float)),
                         "Should handle type errors gracefully")

       def test_returns_none_on_error(self):
           """Should return None when error occurs"""
           result = divide_numbers(10, 0)
           self.assertIsNone(result, "Should return None when division by zero occurs")

   myTests().main()