..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

:skipreading:`True`

.. qnum::
   :prefix: sort-8-
   :start: 1

Exercises
---------

.. activecode:: ac18_8_1
   :autograde: unittest

   You're going to write a function that takes a string as a parameter and returns a list of the five most frequent characters in the string. We'll build this step by step.

   Eventually, the function will:
   1. Count character frequencies using a dictionary
   2. Sort the (key, value) pairs
   3. Take a slice to get the top five
   4. Return that slice

   **Step 1:** Suppose you had this list ``[8, 7, 6, 6, 4, 4, 3, 1, 0]`` already sorted in descending order. Create a variable called ``top_five`` that contains just the first 5 elements using a slice.
   ~~~~
   L = [8, 7, 6, 6, 4, 4, 3, 1, 0]

   # Create top_five using a slice of L

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(top_five, [8, 7, 6, 6, 4], "Testing that top_five contains the first 5 elements")

       def testTwo(self):
           self.assertEqual(len(top_five), 5, "Testing that top_five has exactly 5 elements")

       def testThree(self):
           code = self.getEditorText()
           self.assertIn('[', code.split('=')[-1], "Testing that you used slicing (Don't worry about actual and expected values)")
           self.assertIn(':', code.split('=')[-1], "Testing that you used slicing (Don't worry about actual and expected values)")

   myTests().main()


.. activecode:: ac18_8_2
   :autograde: unittest

   **Step 2:** Now suppose the list wasn't sorted yet. Create a variable called ``top_five`` that contains the five highest values from the unsorted list ``L``. You'll need to sort it first, then take a slice.
   ~~~~
   L = [0, 1, 6, 7, 3, 6, 8, 4, 4]

   # Create top_five by sorting L and taking the first 5 elements

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(top_five, [8, 7, 6, 6, 4], "Testing that top_five contains the five highest values")

       def testTwo(self):
           self.assertEqual(len(top_five), 5, "Testing that top_five has exactly 5 elements")

       def testThree(self):
           self.assertEqual(L, [0, 1, 6, 7, 3, 6, 8, 4, 4], "Testing that original list L was not modified")

       def testFour(self):
           code = self.getEditorText()
           self.assertTrue('sorted' in code or '.sort' in code, "Testing that you used sorting (Don't worry about actual and expected values)")

   myTests().main()

.. activecode:: ac18_8_3
   :autograde: unittest

   **Step 3:** Take the list L and create a dictionary called ``counts`` that maps each number to how many times it appears in the list. Use the accumulator pattern.
   ~~~~
   L = [0, 1, 6, 7, 3, 6, 8, 4, 4, 6, 1, 6, 6, 5, 4, 4, 3, 35, 4, 11]

   # Create counts dictionary

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(type(counts), dict, "Testing that counts is a dictionary")

       def testTwo(self):
           self.assertEqual(counts[4], 5, "Testing that 4 appears 5 times")

       def testThree(self):
           self.assertEqual(counts[6], 5, "Testing that 6 appears 5 times")

       def testFour(self):
           self.assertEqual(counts[1], 2, "Testing that 1 appears 2 times")

       def testFive(self):
           self.assertEqual(counts[0], 1, "Testing that 0 appears 1 time")

       def testSix(self):
           self.assertEqual(counts[35], 1, "Testing that 35 appears 1 time")

       def testSeven(self):
           self.assertEqual(len(counts), 10, "Testing that counts has 10 unique numbers")

   myTests().main()


.. activecode:: ac18_8_4
   :autograde: unittest

   **Step 4:** Create a frequency dictionary from the list L. Then sort the keys (numbers) based on their frequencies in descending order. Keep just the top five keys and store them in a variable called ``top_five``.

   Hint: Review *Sorting a Dictionary* - you'll need to use `sorted()` with the `.get()` method as the key parameter.
   ~~~~
   L = [0, 1, 6, 7, 3, 6, 8, 4, 4, 6, 1, 6, 6, 5, 4, 4, 3, 35, 4, 11]

   # Create frequency dictionary
   # Sort keys by frequency (descending)
   # Keep top 5 and store in top_five

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           self.assertEqual(len(top_five), 5, "Testing that top_five has exactly 5 elements")

       def testTwo(self):
           self.assertIn(4, top_five, "Testing that 4 is in top_five (appears 5 times)")

       def testThree(self):
           self.assertIn(6, top_five, "Testing that 6 is in top_five (appears 5 times)")

       def testFour(self):
           self.assertIn(1, top_five, "Testing that 1 is in top_five (appears 2 times)")

       def testFive(self):
           self.assertIn(3, top_five, "Testing that 3 is in top_five (appears 2 times)")

       def testSix(self):
           # The 5th element should be one of the numbers that appears once
           # Check that at least 4 of the top 5 are the most frequent
           freq_5_count = sum([1 for x in top_five if x in [4, 6]])
           freq_2_count = sum([1 for x in top_five if x in [1, 3]])
           self.assertEqual(freq_5_count, 2, "Testing that both numbers with frequency 5 are included")
           self.assertEqual(freq_2_count, 2, "Testing that both numbers with frequency 2 are included")

   myTests().main()

.. activecode:: ac18_8_5
   :autograde: unittest

   **Step 5 (Final):** Now generalize what you've done. Write a function called ``top_five_characters`` that takes a string as a parameter and returns a list of the five most frequent characters in the string.

   Your function should:
   1. Count the frequency of each character in the string
   2. Sort the characters by frequency (highest first)
   3. Return a list of the top 5 most frequent characters
   ~~~~
   def top_five_characters(s):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           result = top_five_characters("hello world")
           self.assertEqual(len(result), 5, "Testing that result has 5 elements")

       def testTwo(self):
           result = top_five_characters("hello world")
           self.assertIn('l', result, "Testing that 'l' is in top 5 (appears 3 times)")

       def testThree(self):
           result = top_five_characters("hello world")
           self.assertIn('o', result, "Testing that 'o' is in top 5 (appears 2 times)")

       def testFour(self):
           result = top_five_characters("mississippi")
           self.assertIn('i', result, "Testing that 'i' is in top 5 for 'mississippi'")
           self.assertIn('s', result, "Testing that 's' is in top 5 for 'mississippi'")

       def testFive(self):
           result = top_five_characters("aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiiiii")
           self.assertEqual(len(result), 5, "Testing with string that has clear top 5")
           # All of these appear 5 times, so all should be in result
           for char in ['a', 'b', 'c', 'd', 'e']:
               self.assertIn(char, result, f"Testing that '{char}' is in top 5")

       def testSix(self):
           result = top_five_characters("python programming")
           self.assertEqual(type(result), list, "Testing that function returns a list")

       def testSeven(self):
           # Test with a longer, more realistic string
           result = top_five_characters("the quick brown fox jumps over the lazy dog")
           self.assertEqual(len(result), 5, "Testing length with longer string")
           # Space appears most (8 times), 'o' appears 4 times
           self.assertIn(' ', result, "Testing that space is in top 5")
           self.assertIn('o', result, "Testing that 'o' is in top 5")

   myTests().main()

Contributed Exercises
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    {% for q in questions: %}
        <div class='oneq full-width'>
            {{ q['htmlsrc']|safe }}
        </div>
    {% endfor %}
