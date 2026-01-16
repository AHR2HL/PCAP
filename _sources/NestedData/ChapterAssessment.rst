..  Copyright (C) Lauren Murphy, Susan Doong, Haley Yaremych, Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. qnum::
   :prefix: nested-6-
   :start: 1

Chapter Assessment
==================

Multiple Choice Questions
-------------------------

.. mchoice:: nested_assess_mc1
   :answer_a: 2
   :answer_b: 3
   :answer_c: 4
   :answer_d: 5
   :correct: c
   :feedback_a: Count each [] or for loop as one level.
   :feedback_b: Don't forget the outer list level.
   :feedback_c: Correct! data['items'] (1), for item in... (2), item['values'] (3), [0] (4).
   :feedback_d: There are only 4 levels of nesting here.
   :practice: T

   How many levels deep is the nesting in this expression: ``data['items'][0]['values'][0]``?

.. mchoice:: nested_assess_mc2
   :answer_a: json.loads()
   :answer_b: json.dumps()
   :answer_c: json.parse()
   :answer_d: json.stringify()
   :correct: a
   :feedback_a: Correct! loads converts a JSON string to a Python object (load from string).
   :feedback_b: dumps converts a Python object to a JSON string (dump to string).
   :feedback_c: This is a JavaScript function, not Python.
   :feedback_d: This is a JavaScript function, not Python.
   :practice: T

   Which function converts a JSON-formatted string into a Python dictionary or list?

.. mchoice:: nested_assess_mc3
   :answer_a: original and copy are completely independent
   :answer_b: Changes to sublists in original will affect copy
   :answer_c: Changes to the outer list affect copy but not sublists
   :answer_d: copy is just an alias for original
   :correct: b
   :feedback_a: Shallow copy only copies the outer level.
   :feedback_b: Correct! [:] creates a shallow copy - sublists are still shared references.
   :feedback_c: It's the opposite - the outer list is copied but sublists are shared.
   :feedback_d: [:] creates a new list object, not an alias.
   :practice: T

   Given ``original = [['a', 'b'], ['c', 'd']]`` and ``copy = original[:]``, what happens?

.. mchoice:: nested_assess_mc4
   :multiple_answers:
   :answer_a: nested[0][2]
   :answer_b: nested[0][-1]
   :answer_c: nested[0][len(nested[0])-1]
   :answer_d: nested[-1][0]
   :correct: a,b,c
   :feedback_a: Correct! Direct indexing to position 2 in first sublist.
   :feedback_b: Correct! -1 gets the last element of the first sublist.
   :feedback_c: Correct! len(nested[0])-1 calculates the last index.
   :feedback_d: This gets the first element of the last sublist, not 'cat'.
   :practice: T

   Given ``nested = [['dog', 'bird', 'cat'], ['fish', 'hamster']]``, which expressions return ``'cat'``? (Select all)

.. mchoice:: nested_assess_mc5
   :answer_a: Use copy.deepcopy()
   :answer_b: Use the [:] slice operator
   :answer_c: Use list() constructor
   :answer_d: Assign with = operator
   :correct: a
   :feedback_a: Correct! deepcopy() recursively copies all nested levels.
   :feedback_b: [:] only does shallow copy - nested lists will still be shared.
   :feedback_c: list() also only does shallow copy.
   :feedback_d: This creates an alias, not a copy at all.
   :practice: T

   What's the best way to make a completely independent copy of a nested list with 3+ levels?

.. mchoice:: nested_assess_mc6
   :answer_a: A list
   :answer_b: A dictionary
   :answer_c: A tuple
   :answer_d: Any of the above
   :correct: b
   :feedback_a: Lists are mutable and cannot be dictionary keys.
   :feedback_b: Correct! Dictionary keys must be immutable (numbers, strings, tuples only).
   :feedback_c: Tuples are immutable and CAN be dictionary keys.
   :feedback_d: Only immutable types can be dictionary keys.
   :practice: T

   Which of the following CANNOT be used as a key in a dictionary?

.. mchoice:: nested_assess_mc7
   :answer_a: 1 for loop
   :answer_b: 2 for loops
   :answer_c: 3 for loops
   :answer_d: No for loops needed
   :correct: c
   :feedback_a: You need one for loop per level of list nesting.
   :feedback_b: Count the nesting levels carefully.
   :feedback_c: Correct! Three levels of lists require three nested for loops.
   :feedback_d: You need for loops to iterate through lists.
   :practice: T

   How many for loops do you need to iterate through every element in ``data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]``?

.. mchoice:: nested_assess_mc8
   :answer_a: Print the type and keys if it's a dictionary
   :answer_b: Try to extract everything at once
   :answer_c: Start coding without examining the structure
   :answer_d: Use complex nested indexing immediately
   :correct: a
   :feedback_a: Correct! Understanding the structure first is crucial.
   :feedback_b: You should go level by level, not all at once.
   :feedback_c: Always examine the structure first.
   :feedback_d: Build up gradually, don't jump to complex indexing.
   :practice: T

   When extracting data from a complex nested structure, what should you do FIRST?

.. mchoice:: nested_assess_mc9
   :answer_a: Always use the same data types at each level
   :answer_b: Mix lists and dictionaries freely for variety
   :answer_c: Use different key names in each dictionary
   :answer_d: Change structure based on individual items
   :correct: a
   :feedback_a: Correct! Consistent structure means less special-case code.
   :feedback_b: Mixing types requires more special case handling.
   :feedback_c: Consistent key names make iteration easier.
   :feedback_d: Changing structure requires type checking and conditionals.
   :practice: T

   What's a best practice when structuring nested data?

.. mchoice:: nested_assess_mc10
   :answer_a: for item in my_list[:1]
   :answer_b: for item in my_list[0]
   :answer_c: for item in my_list[0:1]
   :answer_d: Both a and c
   :correct: d
   :feedback_a: Correct! [:1] creates a slice with just the first item.
   :feedback_b: This tries to iterate over the first item itself, not a list containing it.
   :feedback_c: Correct! [0:1] also creates a slice with just the first item.
   :feedback_d: Correct! Both a and c create a list with one item to iterate over.
   :practice: T

   When debugging nested iteration, which is a good way to work with just the first item of a list?

.. mchoice:: nested_assess_mc11
   :answer_a: res['data']['items'][0]['name']
   :answer_b: res.data.items[0].name
   :answer_c: res['data'][0]['name']
   :answer_d: res['items'][0]['name']
   :correct: a
   :feedback_a: Correct! Each level descends with ['key'] for dictionaries.
   :feedback_b: Python dictionaries use brackets, not dot notation for keys.
   :feedback_c: This skips the 'items' level.
   :feedback_d: This doesn't start with 'data'.
   :practice: T

   Given ``res = {'data': {'items': [{'name': 'Alice'}, {'name': 'Bob'}]}}``, which correctly extracts 'Alice'?

.. mchoice:: nested_assess_mc12
   :answer_a: null
   :answer_b: None
   :answer_c: undefined
   :answer_d: nil
   :correct: a
   :feedback_a: Correct! JSON uses 'null' instead of Python's 'None'.
   :feedback_b: This is Python's representation, not JSON.
   :feedback_c: This is JavaScript's concept, not JSON.
   :feedback_d: This is used in some other languages, not JSON.
   :practice: T

   What does JSON use to represent a null/empty value?

Parsons Problems
----------------

.. parsonsprob:: nested_assess_pp1
   :numbered: left
   :adaptive:

   Arrange the code blocks to iterate through a nested list and print each element at the deepest level.
   -----
   nested = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
   =====
   for outer in nested:
   =====
   for outer in nested[0]: #paired
   =====
       for middle in outer:
   =====
       for middle in outer[0]: #paired
   =====
           for inner in middle:
   =====
               print(inner)
   =====
               print(middle) #paired

.. parsonsprob:: nested_assess_pp2
   :numbered: left
   :adaptive:

   Arrange the code blocks to extract all values from a nested dictionary and add them to a list.
   -----
   data = {'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}}
   values_list = []
   =====
   for outer_key in data:
   =====
   for outer_key in data.keys: #paired
   =====
       inner_dict = data[outer_key]
   =====
       for inner_key in inner_dict:
   =====
           values_list.append(inner_dict[inner_key])
   =====
           values_list.append(inner_key) #paired

.. parsonsprob:: nested_assess_pp3
   :numbered: left
   :adaptive:

   Arrange the code blocks to extract the screen names from a list of user dictionaries (like Twitter data).
   -----
   tweets = [{'user': {'screen_name': 'alice'}}, {'user': {'screen_name': 'bob'}}]
   names = []
   =====
   for tweet in tweets:
   =====
       user_info = tweet['user']
   =====
       user_info = tweet.user #paired
   =====
       names.append(user_info['screen_name'])
   =====
       names.append(user_info[screen_name]) #paired

.. parsonsprob:: nested_assess_pp4
   :numbered: left
   :adaptive:

   Arrange the code blocks to create a deep copy of a nested list using the copy module.
   -----
   import copy
   =====
   original = [[1, 2], [3, 4], [5, 6]]
   =====
   deep_copy = copy.deepcopy(original)
   =====
   deep_copy = copy.copy(original) #paired
   =====
   deep_copy = original[:] #paired
   =====
   original[0].append(99)
   =====
   print(deep_copy[0])  # Should not include 99

.. parsonsprob:: nested_assess_pp5
   :numbered: left
   :adaptive:

   Arrange the code blocks to count how many items are in all sublists combined.
   -----
   nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
   total_count = 0
   =====
   for sublist in nested_list:
   =====
       for item in sublist:
   =====
       for item in nested_list: #paired
   =====
           total_count += 1
   =====
           total_count = total_count + item #paired
   =====
   print(total_count)

.. parsonsprob:: nested_assess_pp6
   :numbered: left
   :adaptive:

   Arrange the code blocks to extract all email addresses from a nested structure and save them to a list.
   -----
   users = [
       {'name': 'Alice', 'contacts': {'email': 'alice@example.com'}},
       {'name': 'Bob', 'contacts': {'email': 'bob@example.com'}}
   ]
   emails = []
   =====
   for user in users:
   =====
       contact_info = user['contacts']
   =====
       contacts_info = users['contacts'] #paired
   =====
       emails.append(contact_info['email'])
   =====
       emails.append(user['email']) #paired

Active Code Problems
--------------------

.. activecode:: ac17_6_1
   :language: python
   :autograde: unittest
   :practice: T
   :topics: NestedData/ListswithComplexItems

   The variable ``nested`` contains a nested list. Assign 'snake' to the variable ``output`` using indexing.

   ~~~~
   nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(output, "snake", "Testing that output is assigned to correct value")

   myTests().main()

.. activecode:: ac17_6_2
   :language: python
   :autograde: unittest
   :practice: T
   :topics: NestedData/ListswithComplexItems

   Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.

   ~~~~
   lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

   #Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``


   #Test to see if 4 is in the second list of lst. Save to variable ``four``


   #Test to see if 'orange' is in the first element of lst. Save to variable ``orange``

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testTwo(self):
         self.assertEqual(yellow, True, "Testing that yellow is assigned to correct value")
      def testTwoB(self):
         self.assertEqual(four, False, "Testing that four is assigned to correct value")
      def testTwoC(self):
         self.assertEqual(orange, True, "Testing that orange is assigned to correct value")

   myTests().main()

.. activecode:: ac17_6_3
   :language: python
   :autograde: unittest
   :practice: T
   :topics: NestedData/ListswithComplexItems

   Below, we've provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.

   ~~~~
   L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

   # Test if 'hola' is in the list L. Save to variable name test1

   # Test if [5, 8, 7] is in the list L. Save to variable name test2

   # Test if 6.6 is in the third element of list L. Save to variable name test3

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testA(self):
         self.assertEqual(test1, False, "Testing that test1 has the correct value.")
      def testB(self):
         self.assertEqual(test2, True, "Testing that test2 has the correct value.")
      def testC(self):
         self.assertEqual(test3, True, "Testing that test3 has the correct value.")

   myTests().main()


.. activecode:: ac17_6_4
   :language: python
   :autograde: unittest
   :practice: T
   :topics: NestedData/NestedDictionaries

   Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.

   ~~~~
   nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

   # Check to see if the string 'data' is a key in nested, if it is, assign True to the variable data, otherwise assign False.

   # Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.

   # Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.

   # Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(data, True, "Testing that data has the correct value.")
      def testTwo(self):
         self.assertEqual(twentyfour, False, "Testing that twentyfour has the correct value.")
      def testThree(self):
         self.assertEqual(whole, False, "Testing that whole has the correct value.")
      def testFour(self):
         self.assertEqual(physics, False, "Testing that physics has the correct value.")

   myTests().main()


.. activecode:: ac17_6_5
   :language: python
   :autograde: unittest
   :practice: T
   :topics: NestedData/NestedDictionaries

   The variable ``nested_d`` contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics. Assign the value of Great Britain's gold medal count from the London Olympics to the variable ``london_gold``. Use indexing. Do not hardcode.

   ~~~~
   nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(london_gold, 29, "Testing that london_gold is assigned to correct value")

   myTests().main()


.. activecode:: ac17_6_6
   :language: python
   :autograde: unittest
   :practice: T
   :topics: NestedData/NestedDictionaries

   Below, we have provided a nested dictionary. Index into the dictionary to create variables that we have listed in the ActiveCode window.

   ~~~~
   sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

   # Assign the string 'backstroke' to the variable name v1

   # Assign the string 'platform' to the variable name v2

   # Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the variable name v3

   # Assign the string 'rings' to the variable name v4

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testA(self):
         self.assertEqual(v1, 'backstroke', "Testing that v1 was created correctly.")
         self.assertNotIn("v1 = 'backstroke'", self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
         self.assertNotIn('v1 = "backstroke"', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
      def testB(self):
         self.assertEqual(v2, 'platform', "Testing that v2 was created correctly.")
         self.assertNotIn('v2 = "platform"', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
         self.assertNotIn("v2 = 'platform'", self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
      def testC(self):
         self.assertEqual(v3, ['vault', 'floor', 'uneven bars', 'balance beam'], "Testing that v3 was created correctly.")
         self.assertNotIn("v3 = ['vault', 'floor', 'uneven bars', 'balance beam']", self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
      def testD(self):
         self.assertEqual(v4, 'rings', "Testing that v4 was created correctly.")
         self.assertNotIn("v4 = 'rings'", self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
         self.assertNotIn('v4 = "rings"', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()


.. activecode:: ac17_6_7
   :language: python
   :autograde: unittest
   :practice: T
   :topics: NestedData/NestedIteration

   Given the dictionary, ``nested_d``, save the medal count for the USA from all three Olympics in the dictionary to the list ``US_count``.

   ~~~~
   nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

   US_count = []


   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFour(self):
         self.assertEqual(sorted(US_count), [35, 36, 46], "Testing that US_count is assigned to correct values.")

   myTests().main()


.. activecode:: ac17_6_8
   :language: python
   :autograde: unittest
   :practice: T
   :topics: NestedData/NestedIteration

   Iterate through the contents of ``l_of_l`` and assign the third element of sublist to a new list called ``third``.

   ~~~~
   l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(third, ['blue', 'blood orange', 'lavender', 'mac n cheese'], "Testing that third has the correct list assigned to it.")

   myTests().main()


.. activecode:: ac17_6_9
   :language: python
   :autograde: unittest
   :practice: T
   :topics: NestedData/NestedIteration

   Given below is a list of lists of athletes. Create a list, ``t``, that saves only the athlete's name if it contains the letter "t". If it does not contain the letter "t", save the athlete name into list ``other``.

   ~~~~
   athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(t, ['Lochte', 'Bolt', 'Eaton', 'Dalton'], "Testing that t is assigned to correct values.")
      def testFiveA(self):
         self.assertEqual(other, ['Phelps', 'Schooling', 'Ledecky', 'Franklin', 'Felix', 'Gardner', 'Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak'], "Testing that other is assigned to correct values.")

   myTests().main()