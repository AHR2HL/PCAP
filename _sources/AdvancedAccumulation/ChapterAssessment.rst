..  Copyright (C)  Alpha Schools. Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. qnum::
   :prefix: AdAccum-7-
   :start: 1

Chapter Assessment
==================

Part 1: Multiple Choice Questions
----------------------------------

.. mchoice:: adaccum_assess_mc1
   :practice: T
   :answer_a: [1, 4, 9, 16, 25]
   :answer_b: <map object at 0x...>
   :answer_c: map(lambda x: x**2, [1, 2, 3, 4, 5])
   :answer_d: An error occurs
   :correct: b
   :feedback_a: map() returns a map object (iterator), not a list. You'd need list(map(...)) to get this.
   :feedback_b: Correct! map() returns a map object (an iterator), not a list. You need to convert it with list() to see the values.
   :feedback_c: This is the expression, not what it returns
   :feedback_d: No error occurs; map() returns an iterator

   What does ``map(lambda x: x**2, [1, 2, 3, 4, 5])`` return when printed?


.. mchoice:: adaccum_assess_mc2
   :practice: T
   :answer_a: List comprehension is always faster
   :answer_b: map() is more readable for simple transformations
   :answer_c: List comprehension is considered more Pythonic for simple cases
   :answer_d: map() uses less memory
   :correct: c
   :feedback_a: Performance is similar; this isn't the main reason to choose one
   :feedback_b: List comprehensions are generally considered MORE readable
   :feedback_c: Correct! The Python community generally prefers list comprehensions for their readability
   :feedback_d: Both create lists (unless you use a generator expression)

   When should you prefer a list comprehension over map()?


.. mchoice:: adaccum_assess_mc3
   :practice: T
   :answer_a: [('a', 1), ('b', 2), ('c', 3)]
   :answer_b: [('a', 1), ('b', 2)]
   :answer_c: [('a', 1), ('b', 2), ('c', 3), ('d', None)]
   :answer_d: An error occurs
   :correct: b
   :feedback_a: zip() stops at the shortest iterable
   :feedback_b: Correct! zip() stops when the shortest iterable is exhausted
   :feedback_c: zip() doesn't fill in missing values with None
   :feedback_d: No error occurs; zip() handles unequal lengths

   What does ``list(zip(['a', 'b', 'c', 'd'], [1, 2]))`` produce?


.. mchoice:: adaccum_assess_mc4
   :practice: T
   :answer_a: A list
   :answer_b: A generator object
   :answer_c: A tuple
   :answer_d: A set
   :correct: b
   :feedback_a: Lists use square brackets []
   :feedback_b: Correct! Parentheses with comprehension syntax create a generator expression
   :feedback_c: Tuples would need tuple(), and don't use comprehension syntax
   :feedback_d: Sets use curly braces {}

   What type of object does ``(x**2 for x in range(10))`` create?


.. mchoice:: adaccum_assess_mc5
   :practice: T
   :answer_a: {1: 1, 2: 4, 3: 9}
   :answer_b: {1, 4, 9}
   :answer_c: [1, 4, 9]
   :answer_d: An error occurs
   :correct: a
   :feedback_a: Correct! This creates a dictionary mapping numbers to their squares
   :feedback_b: This would be a set comprehension: {x**2 for x in [1,2,3]}
   :feedback_c: This would be a list comprehension: [x**2 for x in [1,2,3]]
   :feedback_d: No error; this is valid dictionary comprehension syntax

   What does ``{x: x**2 for x in [1, 2, 3]}`` produce?


.. mchoice:: adaccum_assess_mc6
   :practice: T
   :answer_a: When working with large datasets and you only iterate once
   :answer_b: When you need to iterate multiple times
   :answer_c: When you need to use list methods like .append()
   :answer_d: When the dataset is small
   :correct: a
   :feedback_a: Correct! Generators save memory by generating values on-demand, perfect for large datasets with single iteration
   :feedback_b: Generators are exhausted after one iteration; use list comprehensions for multiple iterations
   :feedback_c: Generators don't have list methods; use list comprehensions
   :feedback_d: For small datasets, the memory benefit is minimal; use list comprehensions for clarity

   When should you use a generator expression instead of a list comprehension?


Part 2: Active Code Problems
-----------------------------

.. activecode:: ac21_7_1
   :language: python
   :autograde: unittest
   :chatcodes:
   :practice: T
   :topics: AdvancedAccumulation/map

   Write code to assign to the variable ``map_testing`` all the elements in lst_check while adding the string "Fruit: " to the beginning of each element using mapping.
   ~~~~
   lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(map_testing, ['Fruit: plums', 'Fruit: watermelon', 'Fruit: kiwi', 'Fruit: strawberries', 'Fruit: blueberries', 'Fruit: peaches', 'Fruit: apples', 'Fruit: mangos', 'Fruit: papaya'], "Testing that map_testing has the correct values.")
         self.assertIn('map(', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()


.. activecode:: ac21_7_2
   :language: python
   :autograde: unittest
   :chatcodes:
   :practice: T
   :topics: AdvancedAccumulation/filter

   Below, we have provided a list of strings called ``countries``. Use filter to produce a list called ``b_countries`` that only contains the strings from ``countries`` that begin with B.
   ~~~~
   countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(b_countries, ['Brazil', 'Botswana', 'Britain', 'Bangladesh', 'Belarus', 'Belgium'], "Testing that b_countries is correct.")
         self.assertIn('filter(', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()


.. activecode:: ac21_7_3
   :language: python
   :autograde: unittest
   :chatcodes:
   :practice: T
   :topics: AdvancedAccumulation/listcomp

   Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, create a list of strings called ``first_names`` that contains only the first names of everyone in the original list.
   ~~~~
   people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(first_names, ['Jon', 'Cersei', 'Arya', 'Robb', 'Jamie', 'Daenerys', 'Sansa', 'Margaery', 'Eddard', 'Tyrion', 'Joffrey', 'Ramsey', 'Peter'], "Testing that first_names is correct.")

   myTests().main()


.. activecode:: ac21_7_4
   :language: python
   :autograde: unittest
   :chatcodes:
   :practice: T
   :topics: AdvancedAccumulation/listcomp

   Use list comprehension to create a list called ``lst2`` that doubles each element in the list, ``lst``.
   ~~~~
   lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFiveA(self):
         self.assertEqual(lst2, [['hi', 'bye', 'hi', 'bye'], 'hellohello', 'goodbyegoodbye', [9, 2, 9, 2], 8], "Testing that lst2 is assigned to correct values")

   myTests().main()


.. activecode:: ac21_7_5
   :language: python
   :autograde: unittest
   :chatcodes:
   :practice: T
   :topics: AdvancedAccumulation/listcomp

   Below, we have provided a list of tuples that contain students' names and their final grades in PYTHON 101. Using list comprehension, create a new list ``passed`` that contains the names of students who passed the class (had a final grade of 70 or greater).
   ~~~~
   students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(passed, ['Tommy', 'Carl', 'Bob', 'Sue'], "Testing that passed is correct.")

   myTests().main()


.. activecode:: ac21_7_6
   :language: python
   :autograde: unittest
   :chatcodes:
   :practice: T
   :topics: AdvancedAccumulation/zip

   Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable ``opposites`` if they are both longer than 3 characters each.
   ~~~~

   l1 = ['left', 'up', 'front']
   l2 = ['right', 'down', 'back']

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(opposites, [('left','right'), ('front','back')], "Testing that opposites has the correct list of tuples.")
         self.assertIn('filter(', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
         self.assertIn('zip(', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()


.. activecode:: ac21_7_7
   :language: python
   :autograde: unittest
   :chatcodes:
   :practice: T
   :topics: AdvancedAccumulation/zip

   Below, we have provided a ``species`` list and a ``population`` list. Use zip to combine these lists into one list of tuples called ``pop_info``. From this list, create a new list called ``endangered`` that contains the names of species whose populations are below 2500.
   ~~~~
   species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

   population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(pop_info, [('golden retriever', 10000), ('white tailed deer', 90000), ('black rhino', 1000), ('brown squirrel', 2000000), ('field mouse', 500000), ('orangutan', 500), ('sumatran elephant', 1200), ('rainbow trout', 8000), ('black bear', 12000), ('blue whale', 2300), ('water moccasin', 7500), ('giant panda', 100), ('green turtle', 1800), ('blue jay', 9500), ('japanese beetle', 125000)], "Testing that pop_info was created correctly.")
      def testTwo(self):
         self.assertEqual(endangered, ['black rhino', 'orangutan', 'sumatran elephant', 'blue whale', 'giant panda', 'green turtle'], "Testing that endangered was created correctly.")
      def testThree(self):
         self.assertIn('zip(', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()


.. activecode:: ac21_7_8
   :language: python
   :autograde: unittest
   :practice: T
   :topics: AdvancedAccumulation/dictcomp

   Create a dictionary comprehension that maps each fruit name to its length. Assign it to the variable ``fruit_lengths``.
   ~~~~
   fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(fruit_lengths, {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4, 'elderberry': 10, 'fig': 3}, "Testing that fruit_lengths is correct.")

   myTests().main()


.. activecode:: ac21_7_9
   :language: python
   :autograde: unittest
   :practice: T
   :topics: AdvancedAccumulation/setcomp

   Use a set comprehension to create a set of all unique word lengths in the sentence. Assign it to the variable ``unique_lengths``.
   ~~~~
   sentence = "the quick brown fox jumps over the lazy dog"
   words = sentence.split()

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(unique_lengths, {3, 4, 5}, "Testing that unique_lengths is correct.")

   myTests().main()


.. activecode:: ac21_7_10
   :language: python
   :autograde: unittest
   :practice: T
   :topics: AdvancedAccumulation/genexp

   Create a generator expression that generates squares of numbers from 1 to 100, then use sum() to find the total. Assign the sum to ``total_squares``.

   **Hint:** Use () for generator expressions, not [].
   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(total_squares, 338350, "Testing that total_squares is correct.")
         self.assertNotIn('[', self.getEditorText(), "Should use generator expression (), not list []")

   myTests().main()


.. activecode:: ac21_7_11
   :language: python
   :autograde: unittest
   :practice: T
   :topics: AdvancedAccumulation/nested

   Use a nested list comprehension to flatten the matrix into a single list. Assign it to ``flattened``.
   ~~~~
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(flattened, [1, 2, 3, 4, 5, 6, 7, 8, 9], "Testing that flattened is correct.")

   myTests().main()


Part 3: Debugging Exercises
----------------------------

.. activecode:: adaccum_debug_1
   :language: python
   :autograde: unittest
   :practice: T

   **Debug Exercise** This code should use filter() to keep only positive numbers, but it's not working. Find and fix the bug.
   ~~~~
   numbers = [3, -1, 5, -7, 0, 9, -2]

   # Should keep only positive numbers
   positives = list(filter(lambda x: x < 0, numbers))

   print(positives)  # Should print [3, 5, 9]

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      def testOne(self):
         self.assertEqual(positives, [3, 5, 9], "Testing that positives contains only positive numbers")

   myTests().main()


.. activecode:: adaccum_debug_2
   :language: python
   :autograde: unittest
   :practice: T

   **Debug Exercise** This dictionary comprehension should create a mapping of numbers to their squares, but it has a syntax error. Fix it.
   ~~~~
   numbers = [1, 2, 3, 4, 5]

   # Should create {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
   squares = {x, x**2 for x in numbers}

   print(squares)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      def testOne(self):
         self.assertEqual(squares, {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}, "Testing that squares is correct")

   myTests().main()


.. activecode:: adaccum_debug_3
   :language: python
   :autograde: unittest
   :practice: T

   **Debug Exercise** This code should use zip() to combine names and scores into a dictionary, but it's creating a list instead. Fix it.
   ~~~~
   names = ['Alice', 'Bob', 'Charlie']
   scores = [95, 87, 92]

   # Should create {'Alice': 95, 'Bob': 87, 'Charlie': 92}
   results = list(zip(names, scores))

   print(results)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      def testOne(self):
         self.assertEqual(results, {'Alice': 95, 'Bob': 87, 'Charlie': 92}, "Testing that results is a dictionary")
         self.assertEqual(type(results), dict, "Testing that results is a dictionary type")

   myTests().main()


Part 4: Parson's Problems
--------------------------

.. parsonsprob:: adaccum_parsons_1
   :numbered: left
   :adaptive:

   Arrange the code blocks to use map() to convert a list of strings to integers.
   -----
   strings = ['1', '2', '3', '4', '5']
   =====
   numbers = list(map(int, strings))
   =====
   numbers = list(map(lambda x: int(x), strings)) #paired
   =====
   numbers = map(int, strings) #paired
   =====
   numbers = filter(int, strings) #paired


.. parsonsprob:: adaccum_parsons_2
   :numbered: left
   :adaptive:

   Arrange the code blocks to create a dictionary comprehension that maps names to their lengths, but only for names longer than 4 characters.
   -----
   names = ['Alice', 'Bob', 'Charlie', 'Dan', 'Elizabeth']
   =====
   long_names = {name: len(name) for name in names if len(name) > 4}
   =====
   long_names = {name: len(name) for name in names} #paired
   =====
   long_names = [name: len(name) for name in names if len(name) > 4] #paired
   =====
   long_names = {len(name) for name in names if len(name) > 4} #paired


.. parsonsprob:: adaccum_parsons_3
   :numbered: left
   :adaptive:

   Arrange the code blocks to use zip() and a list comprehension to find the maximum value at each position from three lists.
   -----
   L1 = [1, 5, 3]
   L2 = [4, 2, 6]
   L3 = [3, 7, 1]
   =====
   maxs = [max(triple) for triple in zip(L1, L2, L3)]
   =====
   maxs = [max(L1, L2, L3) for triple in zip(L1, L2, L3)] #paired
   =====
   maxs = [max(triple) for triple in L1, L2, L3] #paired
   =====
   maxs = max([triple for triple in zip(L1, L2, L3)]) #paired


Summary & Self-Check
---------------------

After completing this assessment, you should be able to:

✅ Use map() to transform sequences with functions

✅ Use filter() to select elements meeting criteria

✅ Use zip() to combine multiple sequences

✅ Write list, dictionary, and set comprehensions

✅ Understand when to use generator expressions for memory efficiency

✅ Choose the appropriate technique (comprehension vs map/filter/zip)

✅ Work with nested data structures using comprehensions

✅ Debug common mistakes with these advanced techniques

**Struggling with any of these?** Review the relevant sections before continuing to the next chapter.