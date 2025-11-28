..  Copyright (C)  Alpha School

.. qnum::
   :prefix: test-ex-
   :start: 1

Chapter Assessment - Test Cases
================================

**Multiple Choice Questions**

.. mchoice:: tc_ex_mcq1
   :answer_a: assert type(x) == int
   :answer_b: assert x == int
   :answer_c: assert int(x)
   :answer_d: assert x is int
   :correct: a
   :feedback_a: Correct! This checks if x's type is int.
   :feedback_b: This checks if x equals the int type object, not if x is an integer.
   :feedback_c: This converts x to int but doesn't check its original type.
   :feedback_d: 'is' checks identity, not type equality.
   :practice: T

   Which assertion correctly checks if variable ``x`` is an integer?

.. mchoice:: tc_ex_mcq2
   :answer_a: Only test with typical values
   :answer_b: Test with typical values, boundary values, and edge cases
   :answer_c: Only test boundary values
   :answer_d: Testing is optional for simple functions
   :correct: b
   :feedback_a: This misses important edge cases where bugs often hide.
   :feedback_b: Correct! Comprehensive testing requires typical cases, boundaries, and edge cases.
   :feedback_c: Typical values are also important to verify normal operation.
   :feedback_d: Even simple functions need testing to prevent bugs.
   :practice: T

   When writing test cases for a function, what is the best approach?

.. mchoice:: tc_ex_mcq3
   :answer_a: assert process_list([])
   :answer_b: assert len(my_list) > 0 before processing
   :answer_c: Both a and b
   :answer_d: Neither - empty lists don't need testing
   :correct: c
   :feedback_a: This is one way to test empty list handling.
   :feedback_b: This prevents errors by checking before processing.
   :feedback_c: Correct! Both are valid approaches - testing the edge case and preventing errors.
   :feedback_d: Empty lists are critical edge cases that must be tested.
   :practice: T

   Which approach helps test or prevent errors when a function receives an empty list?

.. mchoice:: tc_ex_mcq4
   :answer_a: Only test when the parameter is provided
   :answer_b: Only test when the parameter is omitted
   :answer_c: Test both with the parameter omitted and with different provided values
   :answer_d: Optional parameters don't need testing
   :correct: c
   :feedback_a: You must also test that the default value works correctly.
   :feedback_b: You must also test that providing values works correctly.
   :feedback_c: Correct! Test the default behavior and various provided values including edge cases.
   :feedback_d: Optional parameters create multiple code paths that all need testing.
   :practice: T

   When testing a function with optional parameters, you should:

.. mchoice:: tc_ex_mcq5
   :answer_a: A test that checks a function's return value
   :answer_b: A test that checks if a function modified a mutable object
   :answer_c: A test that checks if a function printed output
   :answer_d: A test that checks function execution time
   :correct: b
   :feedback_a: That's a return value test, not a side effect test.
   :feedback_b: Correct! Side effect tests verify changes to mutable objects like lists or dictionaries.
   :feedback_c: Print output tests are beyond the scope of this testing framework.
   :feedback_d: Performance tests are different from side effect tests.
   :practice: T

   What is a side effect test?

.. mchoice:: tc_ex_mcq6
   :answer_a: Test only the if block
   :answer_b: Test only the else block
   :answer_c: Test both the if and else blocks
   :answer_d: Test all branches including elif and else, plus boundary conditions
   :correct: d
   :feedback_a: You must test all possible paths through the conditional.
   :feedback_b: You must test all possible paths through the conditional.
   :feedback_c: This is closer but doesn't mention elif or boundaries.
   :feedback_d: Correct! Complete testing requires all branches and boundary values where conditions change.
   :practice: T

   When testing a function with if/elif/else statements, you should:

.. mchoice:: tc_ex_mcq7
   :answer_a: Groups of inputs that should all be handled the same way by the function
   :answer_b: Different types of output the function can produce
   :answer_c: Different programming languages
   :answer_d: Different versions of the function
   :correct: a
   :feedback_a: Correct! Equivalence classes group similar inputs that should be processed identically.
   :feedback_b: These are output categories, not equivalence classes of inputs.
   :feedback_c: Equivalence classes relate to function inputs, not languages.
   :feedback_d: Equivalence classes relate to inputs, not function versions.
   :practice: T

   What are "equivalence classes" in the context of testing?

.. mchoice:: tc_ex_mcq8
   :answer_a: 0 <= discount <= 1
   :answer_b: start_date <= end_date
   :answer_c: len(items) > 0
   :answer_d: All of the above
   :correct: d
   :feedback_a: Yes, discount rates must be valid percentages.
   :feedback_b: Yes, date ranges must be logical.
   :feedback_c: Yes, non-empty collections prevent division by zero and similar errors.
   :feedback_d: Correct! All of these are valuable assertions that catch common errors.
   :practice: T

   Which of the following assertions tests a valuable assumption about data?


**Active Code Problems**

.. activecode:: tc_ex_ac1
   :nocodelens:

   Write a function ``is_valid_age(age)`` that returns True if age is between 0 and 150 (inclusive), 
   False otherwise. Then write assert statements to test it with at least 4 different test cases 
   including edge cases.
   ~~~~
   def is_valid_age(age):
       # Your code here
       pass
   
   # Write your test cases here
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(is_valid_age(25), True, "Testing age 25")
           self.assertEqual(is_valid_age(0), True, "Testing age 0 (boundary)")
           self.assertEqual(is_valid_age(150), True, "Testing age 150 (boundary)")
           self.assertEqual(is_valid_age(-5), False, "Testing negative age")
           self.assertEqual(is_valid_age(200), False, "Testing age over 150")
   
   myTests().main()

.. activecode:: tc_ex_ac2
   :nocodelens:

   Write a function ``find_max(numbers)`` that returns the maximum value in a list. Include an 
   assertion to check that the list is not empty. Test it with normal cases and the empty list 
   edge case (which should trigger your assertion).
   ~~~~
   def find_max(numbers):
       # Your code here
       pass
   
   # Test with a normal list
   assert find_max([3, 7, 2, 9, 1]) == 9
   
   # Test with a single element
   assert find_max([5]) == 5
   
   # Uncomment to test empty list (should raise AssertionError)
   # find_max([])
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(find_max([3, 7, 2, 9, 1]), 9, "Testing normal list")
           self.assertEqual(find_max([5]), 5, "Testing single element")
           self.assertEqual(find_max([-5, -2, -10]), -2, "Testing negative numbers")
   
   myTests().main()

.. activecode:: tc_ex_ac3
   :nocodelens:

   Write a function ``classify_temperature(temp)`` that returns "Cold" if temp < 50, "Moderate" if 
   50 <= temp < 80, and "Hot" if temp >= 80. Write assert statements to test all branches and 
   boundary values.
   ~~~~
   def classify_temperature(temp):
       # Your code here
       pass
   
   # Write comprehensive tests here
   # Make sure to test: typical values, boundaries (50, 80), and extremes
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(classify_temperature(30), "Cold", "Testing cold temp")
           self.assertEqual(classify_temperature(50), "Moderate", "Testing boundary 50")
           self.assertEqual(classify_temperature(65), "Moderate", "Testing moderate temp")
           self.assertEqual(classify_temperature(80), "Hot", "Testing boundary 80")
           self.assertEqual(classify_temperature(95), "Hot", "Testing hot temp")
   
   myTests().main()

.. activecode:: tc_ex_ac4
   :nocodelens:

   Write a function ``filter_numbers(numbers, threshold=10)`` with an optional threshold parameter. 
   It should return a list of numbers greater than the threshold. Write tests that include 
   omitting the parameter, providing different thresholds, and edge cases.
   ~~~~
   def filter_numbers(numbers, threshold=10):
       # Your code here
       pass
   
   test_nums = [5, 10, 15, 20, 25]
   
   # Test with default threshold (10)
   
   # Test with explicit threshold
   
   # Test with threshold of 0
   
   # Test with very large threshold
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           test_nums = [5, 10, 15, 20, 25]
           self.assertEqual(filter_numbers(test_nums), [15, 20, 25], "Testing default threshold")
           self.assertEqual(filter_numbers(test_nums, 15), [20, 25], "Testing threshold 15")
           self.assertEqual(filter_numbers(test_nums, 0), [5, 10, 15, 20, 25], "Testing threshold 0")
           self.assertEqual(filter_numbers(test_nums, 100), [], "Testing large threshold")
   
   myTests().main()

.. activecode:: tc_ex_ac5
   :nocodelens:

   Write a function ``add_to_dict(d, key, value)`` that adds a key-value pair to dictionary d. 
   It should update the value if the key already exists. Write a side effect test that verifies 
   the dictionary is modified correctly.
   ~~~~
   def add_to_dict(d, key, value):
       # Your code here
       pass
   
   # Side effect test for adding new key
   test_dict1 = {'a': 1}
   add_to_dict(test_dict1, 'b', 2)
   assert test_dict1 == {'a': 1, 'b': 2}
   
   # Side effect test for updating existing key
   test_dict2 = {'x': 10}
   add_to_dict(test_dict2, 'x', 20)
   # Write your assertion here
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           test_dict = {'a': 1}
           add_to_dict(test_dict, 'b', 2)
           self.assertEqual(test_dict, {'a': 1, 'b': 2}, "Testing add new key")
           add_to_dict(test_dict, 'a', 5)
           self.assertEqual(test_dict, {'a': 5, 'b': 2}, "Testing update existing key")
   
   myTests().main()

.. activecode:: tc_ex_ac6
   :nocodelens:

   Write a function ``sum_positive(numbers)`` that sums only the positive numbers in a list. 
   Include type checking assertions to ensure all elements are numbers. Write comprehensive 
   tests including empty list, all positive, all negative, and mixed cases.
   ~~~~
   def sum_positive(numbers):
       # Add type checking for all elements
       # Sum only positive numbers
       pass
   
   # Write your test cases
   
   ====
   from unittest.gui import TestCaseGui
   
   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(sum_positive([1, 2, 3]), 6, "Testing all positive")
           self.assertEqual(sum_positive([-1, -2, -3]), 0, "Testing all negative")
           self.assertEqual(sum_positive([1, -2, 3, -4, 5]), 9, "Testing mixed")
           self.assertEqual(sum_positive([]), 0, "Testing empty list")
   
   myTests().main()


**Debugging Problems**

.. activecode:: tc_ex_debug1
   :nocodelens:

   This function should check if all elements in a list are positive, but the tests are failing. 
   Fix the function and add appropriate assertions.
   ~~~~
   def all_positive(numbers):
       assert len(numbers) > 0
       for num in numbers:
           if num < 0:
               return True
       return False
   
   assert all_positive([1, 2, 3]) == True
   assert all_positive([1, -2, 3]) == False
   assert all_positive([-1, -2]) == False

.. activecode:: tc_ex_debug2
   :nocodelens:

   This function should calculate the average but doesn't handle edge cases properly. 
   Add the missing assertion and fix the logic.
   ~~~~
   def calculate_average(scores):
       # Missing assertion for empty list
       total = 0
       for score in scores:
           total = total + score
       return total / len(scores)
   
   assert calculate_average([80, 90, 85]) == 85.0
   # This should fail without the assertion:
   # calculate_average([])

.. activecode:: tc_ex_debug3
   :nocodelens:

   This function has incorrect type checking. Fix the assertions and the logic.
   ~~~~
   def multiply_numbers(a, b):
       assert type(a) == int
       assert type(b) == int
       return a * b
   
   # Should work with floats too
   result = multiply_numbers(2.5, 4.0)
   assert result == 10.0


**Parsons Problems**

.. parsonsprob:: tc_ex_parsons1
   :numbered: left
   :adaptive:

   Arrange the code to create a function that finds the minimum value in a list with proper 
   error checking. Include an assertion for non-empty lists and proper logic.
   -----
   def find_min(numbers):
   =====
       assert len(numbers) > 0, "List cannot be empty"
   =====
       assert len(numbers) >= 0, "List cannot be empty" #distractor
   =====
       min_val = numbers[0]
   =====
       min_val = 0 #distractor
   =====
       for num in numbers:
   =====
           if num < min_val:
   =====
           if num > min_val: #distractor
   =====
               min_val = num
   =====
       return min_val

.. parsonsprob:: tc_ex_parsons2
   :numbered: left
   :adaptive:

   Arrange the code to create a function that counts how many times a target value appears in a list, 
   with optional case sensitivity for strings. Include proper default parameter and tests.
   -----
   def count_occurrences(items, target, case_sensitive=True):
   =====
   def count_occurrences(items, target, case_sensitive): #distractor
   =====
       count = 0
   =====
       for item in items:
   =====
           if case_sensitive:
   =====
               if item == target:
   =====
                   count += 1
   =====
           else:
   =====
               if str(item).lower() == str(target).lower():
   =====
               if item.lower() == target.lower(): #distractor
   =====
                   count += 1
   =====
       return count

.. parsonsprob:: tc_ex_parsons3
   :numbered: left
   :adaptive:

   Arrange the code to test a function that validates if a password meets requirements 
   (length >= 8, has digit, has uppercase). Include comprehensive test cases.
   -----
   def is_valid_password(password):
   =====
       if len(password) < 8:
   =====
           return False
   =====
       has_digit = any(c.isdigit() for c in password)
   =====
       has_digit = any(c.isalpha() for c in password) #distractor
   =====
       has_upper = any(c.isupper() for c in password)
   =====
       return has_digit and has_upper
   =====
   assert is_valid_password("Pass123") == True
   =====
   assert is_valid_password("password") == False
   =====
   assert is_valid_password("Pass") == False
   =====
   assert is_valid_password("pass123") == False