..  Copyright (C)  Jaclyn Cohen, Lauren Murphy, Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. qnum::
   :prefix: test-4-
   :start: 1

Chapter Assessment
==================

Multiple Choice Questions
-------------------------

.. mchoice:: test_assess_mc1
   :multiple_answers:
   :answer_a: an empty list
   :answer_b: a list with one item
   :answer_c: a list with more than one item
   :feedback_a: Correct, 0 is not returned if the function is given an empty list.
   :feedback_b: Incorrect, a list with one item returns the correct value.
   :feedback_c: Correct, a list with more than one item does not provide the correct response.
   :correct: a, c
   :practice: T

   Which of the following cases fail for the mySum function?

.. mchoice:: test_assess_mc2
   :answer_a: Yes
   :answer_b: No
   :feedback_a: Incorrect. Though it is possible that the function could have more issues, we can't tell if other cases would fail (such as combining integers and floats) due to the current issues.
   :feedback_b: Correct. At the moment we can't tell if other cases would fail (such as combining integers and floats), but it is possible that the function could have more issues once the current issues are fixed.
   :correct: b
   :practice: T

   Are there any other cases, that we can determine based on the current structure of the function, that also fail for the mySum function?

.. mchoice:: test_assess_mc3
   :multiple_answers:
   :answer_a: the method study does not return None
   :answer_b: the optional integer in the constructor is not optional
   :answer_c: the attributes/instance variables are not correctly assigned in the constructor
   :answer_d: the method study does not increase self.knowledge correctly
   :answer_e: the method year_at_umich does not return the value of self.years_UM
   :feedback_a: Incorrect, the method study does return a value (when it shouldn't).
   :feedback_b: Incorrect, the integer for number of years is optional.
   :feedback_c: Correct! The constructor does not actually use the optional integer that is provided. Instead it always uses 1 regardless of the parameter value.
   :feedback_d: Correct! Study has unusual behavior with how it modifies self.knowledge.
   :feedback_e: Incorrect, year_at_umich does return the value assigned to self.years_UM.
   :correct: c, d
   :practice: T

   Which of the following issues exist in the Student class?

.. mchoice:: test_assess_mc4
   :answer_a: Yes
   :answer_b: No
   :feedback_a: Correct! There could be issues with methods like getKnowledge() that may not work as expected depending on the state of the object.
   :feedback_b: Incorrect, there may be more cases that fail. Try testing all the methods thoroughly!
   :correct: a
   :practice: T

   Are there any other cases, that we can determine based on the current structure of the class, that also fail for the Student class?

Programming Problems
--------------------

.. activecode:: test_assess_hidden
   :hidecode:

   **Starter Code** This code is merely for use in the subsequent questions. Please do not read these functions.

   ~~~~
   def lr(n): return list(range(n))

   # THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
   # PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
   # READING THEM.
   def mySum(a):
       if type(a) is type(''.join([][:])): return a[lr(1)[0]] + mySum(a[1:])
       elif len(a)==len(lr(1)+[]): return a[lr(1)[0]]
       else: return None and a[lr(1)[0]] + mySum(a[1:])


   # THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
   # PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
   # READING THEM.
   class Student():
       def __init__(s,a,b=1): s.name,s.years_UM,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
       def study(s):
           for _ in lr(s.knowledge): s.knowledge = s.knowledge + 1
       def getKnowledge(s):
           for i in lr(s.knowledge): return s.knowledge
       def year_at_umich(s): return s.years_UM

.. activecode:: test_assess_ac1
   :include: test_assess_hidden
   :autograde: unittest

   **Problem 1:** Testing the mySum Function

   The function ``mySum`` is supposed to return the sum of a list of numbers (and 0 if that list is empty), but it has one or more errors in it. Your task is to write test cases using assertions to discover what the bugs are.

   **Requirements:**
   - Write at least 4 different test cases using ``assert`` statements
   - Your assertions should catch the bugs in the function

   **Hints for test cases to write:**
   - Test with an empty list
   - Test with a list of one element
   - Test with a list of multiple elements
   - Test with different types of values (positive, negative, zero)

   ~~~~
   # The buggy function mySum is already defined (included from above)
   # Write your test cases here using assert statements

   # Example test case:
   # assert mySum([1, 2, 3]) == 6, "Testing sum of [1, 2, 3]"

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           code = self.getEditorText()
           self.assertIn('assert', code, "Testing that you wrote at least one assertion")

       def testTwo(self):
           code = self.getEditorText()
           num_asserts = code.count('assert')
           self.assertGreaterEqual(num_asserts, 4, "Testing that you wrote at least 4 assertions")

       def testThree(self):
           code = self.getEditorText()
           self.assertTrue('[]' in code, "Testing that you test the empty list case")

       def testFour(self):
           code = self.getEditorText()
           has_single = '[' in code and any(str(i) + ']' in code for i in range(10))
           self.assertTrue(has_single, "Testing that you test with single element lists")

       def testFive(self):
           code = self.getEditorText()
           has_multi = any(f'[{i}, {j}' in code or f'[{i},{j}' in code for i in range(1, 6) for j in range(1, 6))
           self.assertTrue(has_multi, "Testing that you test with multiple element lists")

       def testSix(self):
           try:
               exec(self.getEditorText())
               self.fail("Your assertions should catch the bugs in mySum. At least one assertion should fail.")
           except (AssertionError, TypeError):
               self.assertTrue(True, "Good! Your assertions caught at least one bug")

   myTests().main()

.. activecode:: test_assess_ac2
   :include: test_assess_hidden
   :autograde: unittest

   **Problem 2:** Testing the Student Class

   The ``Student`` class is supposed to work as follows:

   **Constructor:** ``Student(name, years_UM=1)``
     - ``name``: A string for the student's name
     - ``years_UM``: An optional integer for years at Michigan (default: 1)

   **Instance Variables:**
     - ``self.name``: Set to the name provided
     - ``self.years_UM``: Set to the number of years provided (or 1 if not provided)
     - ``self.knowledge``: Initialized to 0

   **Methods:**
     - ``.study()``: Should increase ``self.knowledge`` by 1 and return ``None``
     - ``.getKnowledge()``: Should return the current value of ``self.knowledge``
     - ``.year_at_umich()``: Should return the value of ``self.years_UM``

   There are one or more errors in the class. Your task is to write test cases using assertions to discover what the bugs are.

   **Requirements:**
   - Write at least 5 different test cases using ``assert`` statements
   - Your assertions should catch the bugs in the class

   **Hints for test cases to write:**
   - Test creating a student with just a name (using default years)
   - Test creating a student with both name and years
   - Test the ``study()`` method and what it returns
   - Test ``getKnowledge()`` after calling ``study()``
   - Test ``year_at_umich()`` with different year values
   - Try calling ``study()`` multiple times

   ~~~~
   # The buggy Student class is already defined (included from above)
   # Write your test cases here using assert statements

   # Example test case:
   # s = Student("Jane")
   # assert s.name == "Jane", "Testing name attribute"

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           code = self.getEditorText()
           self.assertIn('assert', code, "Testing that you wrote at least one assertion")

       def testTwo(self):
           code = self.getEditorText()
           num_asserts = code.count('assert')
           self.assertGreaterEqual(num_asserts, 5, "Testing that you wrote at least 5 assertions")

       def testThree(self):
           code = self.getEditorText()
           self.assertIn('Student(', code, "Testing that you create Student instances")

       def testFour(self):
           code = self.getEditorText()
           has_study = '.study()' in code
           self.assertTrue(has_study, "Testing that you call the study() method")

       def testFive(self):
           code = self.getEditorText()
           has_year_test = 'year_at_umich()' in code or 'years_UM' in code
           self.assertTrue(has_year_test, "Testing that you test the years_UM attribute or year_at_umich() method")

       def testSix(self):
           code = self.getEditorText()
           study_count = code.count('.study()')
           self.assertGreaterEqual(study_count, 2, "Testing that you call study() multiple times to test incremental behavior")

       def testSeven(self):
           try:
               exec(self.getEditorText())
               self.fail("Your assertions should catch the bugs in Student. At least one assertion should fail.")
           except (AssertionError, AttributeError):
               self.assertTrue(True, "Good! Your test cases caught at least one bug")

   myTests().main()