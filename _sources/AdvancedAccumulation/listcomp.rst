..  Copyright (C)  Alpha Schools. Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. qnum::
   :prefix: AdAccum-4-
   :start: 1

List Comprehensions: Review and Advanced Techniques
====================================================

Quick Review
------------

As a PCEP graduate, you already know basic list comprehensions:

.. code-block:: python

   # Basic transformation
   squares = [x**2 for x in range(10)]

   # With filtering
   even_squares = [x**2 for x in range(10) if x % 2 == 0]

   # With string operations
   names = ['alice', 'bob', 'charlie']
   upper_names = [name.upper() for name in names]

If you need a detailed refresher, refer to your PCEP course materials.

This section covers advanced comprehension techniques required for PCAP certification.

Nested List Comprehensions
---------------------------

.. index:: nested list comprehension

A **nested list comprehension** contains another comprehension inside it. This is useful for working with 2D data structures like matrices.

Creating a Multiplication Table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The outer comprehension creates rows, the inner comprehension creates columns:

.. activecode:: listcomp_nested_1

   # Create a 3x3 multiplication table
   matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]

   # Print it nicely
   for row in matrix:
       print(row)
   # Output:
   # [1, 2, 3]   (1*1, 1*2, 1*3)
   # [2, 4, 6]   (2*1, 2*2, 2*3)
   # [3, 6, 9]   (3*1, 3*2, 3*3)

**How to read nested comprehensions:** Start from the outside and work inward.

.. code-block:: python

   [[i * j for j in range(1, 4)] for i in range(1, 4)]
   # ^^^^^^^^^^^^^^^^^^^^^^^^      ^^^^^^^^^^^^^^^^^^^^^^^
   #   Inner: creates one row       Outer: repeats for each row

Equivalent nested loops:

.. code-block:: python

   matrix = []
   for i in range(1, 4):           # Outer comprehension
       row = []
       for j in range(1, 4):       # Inner comprehension
           row.append(i * j)
       matrix.append(row)

Flattening a 2D List
~~~~~~~~~~~~~~~~~~~~~

You can also use nested comprehensions to flatten nested structures:

.. activecode:: listcomp_nested_2

   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

   # Flatten to a single list
   flattened = [num for row in matrix for num in row]
   print(flattened)
   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

**Reading order:** Read left to right (unlike nested creation):

.. code-block:: python

   [num for row in matrix for num in row]
   #     ^^^^^^^^^^^^^^^^  ^^^^^^^^^^^^^^
   #     First: iterate rows  Then: iterate items in each row

Equivalent nested loops:

.. code-block:: python

   flattened = []
   for row in matrix:          # First for
       for num in row:         # Second for
           flattened.append(num)

Filtering in Nested Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can add conditions to nested comprehensions:

.. activecode:: listcomp_nested_3

   # Create a matrix, but only include even products
   matrix = [[i * j for j in range(1, 6) if (i * j) % 2 == 0]
             for i in range(1, 6)]

   for row in matrix:
       print(row)
   # [2, 4]           (row 1: only 1*2 and 1*4 are even)
   # [2, 4, 6, 8]     (row 2: all products are even)
   # [6]              (row 3: only 3*2, 3*4 are even)
   # ...

**Check your understanding**

.. mchoice:: question_listcomp_nested_1
   :practice: T
   :answer_a: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
   :answer_b: [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
   :answer_c: [0, 1, 2, 0, 1, 2, 0, 1, 2]
   :answer_d: [0, 0, 0, 1, 1, 1, 2, 2, 2]
   :correct: a
   :feedback_a: Correct! The outer loop creates 3 rows, each containing [0, 1, 2]
   :feedback_b: This would be [[j, j, j] for j in range(3)]
   :feedback_c: This would be [i for _ in range(3) for i in range(3)]
   :feedback_d: This would be [j for j in range(3) for _ in range(3)]

   What does this nested list comprehension produce?

   .. code-block:: python

      result = [[i for i in range(3)] for j in range(3)]

Dictionary Comprehensions
-------------------------

.. index:: dictionary comprehension

A **dictionary comprehension** creates a dictionary using similar syntax to list comprehensions, but with key-value pairs.

Basic Dictionary Comprehension Syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   {key_expression: value_expression for item in iterable}

The key difference from list comprehensions:
- Use ``{}`` instead of ``[]``
- Use ``:`` between key and value expressions

Creating Dictionaries from Lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Combine two lists into a dictionary:

.. activecode:: dictcomp_1

   names = ['Alice', 'Bob', 'Charlie']
   ages = [25, 30, 35]

   # Create dictionary mapping names to ages
   people = {name: age for name, age in zip(names, ages)}
   print(people)
   # {'Alice': 25, 'Bob': 30, 'Charlie': 35}

This is much cleaner than:

.. code-block:: python

   people = {}
   for name, age in zip(names, ages):
       people[name] = age

Transforming Dictionary Keys or Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. activecode:: dictcomp_2

   prices = {'apple': 0.50, 'banana': 0.30, 'orange': 0.75}

   # Convert to cents
   prices_cents = {fruit: int(price * 100) for fruit, price in prices.items()}
   print(prices_cents)
   # {'apple': 50, 'banana': 30, 'orange': 75}

Filtering Dictionaries
~~~~~~~~~~~~~~~~~~~~~~~

Only include entries that meet a condition:

.. activecode:: dictcomp_3

   scores = {'Alice': 85, 'Bob': 72, 'Charlie': 90, 'David': 65}

   # Keep only passing scores (70 or higher)
   passing = {name: score for name, score in scores.items() if score >= 70}
   print(passing)
   # {'Alice': 85, 'Bob': 72, 'Charlie': 90}

Inverting a Dictionary
~~~~~~~~~~~~~~~~~~~~~~~

Swap keys and values:

.. activecode:: dictcomp_4

   country_capital = {'USA': 'Washington', 'France': 'Paris', 'Japan': 'Tokyo'}

   # Invert: capital -> country
   capital_country = {capital: country for country, capital in country_capital.items()}
   print(capital_country)
   # {'Washington': 'USA', 'Paris': 'France', 'Tokyo': 'Japan'}

**Warning:** Only works if all values are unique. Duplicate values will overwrite earlier keys.

Creating Dictionaries from a Single List
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. activecode:: dictcomp_5

   words = ['apple', 'banana', 'cherry']

   # Map words to their lengths
   word_lengths = {word: len(word) for word in words}
   print(word_lengths)
   # {'apple': 5, 'banana': 6, 'cherry': 6}

**Check your understanding**

.. mchoice:: question_dictcomp_1
   :practice: T
   :answer_a: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
   :answer_b: {1: 1, 4: 2, 9: 3, 16: 4, 25: 5}
   :answer_c: [1, 4, 9, 16, 25]
   :answer_d: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
   :correct: a
   :feedback_a: Correct! Keys are 1-5, values are their squares
   :feedback_b: This would be {x**2: x for x in range(1, 6)}
   :feedback_c: This would be [x**2 for x in range(1, 6)] (a list)
   :feedback_d: This would use range(5) which starts at 0

   What does this dictionary comprehension produce?

   .. code-block:: python

      result = {x: x**2 for x in range(1, 6)}

Set Comprehensions
------------------

.. index:: set comprehension

A **set comprehension** creates a set, automatically removing duplicates. Sets are useful when you only care about unique values.

Basic Set Comprehension Syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   {expression for item in iterable}

Looks identical to dict comprehensions, but without the ``:`` for key-value pairs.

Extracting Unique Values
~~~~~~~~~~~~~~~~~~~~~~~~~

.. activecode:: setcomp_1

   numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

   # Get unique squares
   unique_squares = {x**2 for x in numbers}
   print(unique_squares)
   # {16, 1, 4, 9}  (order may vary - sets are unordered)

Without set comprehension:

.. code-block:: python

   unique_squares = set()
   for x in numbers:
       unique_squares.add(x**2)

Finding Unique Characters
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. activecode:: setcomp_2

   sentence = "the quick brown fox jumps over the lazy dog"

   # Get all unique letters (no spaces)
   unique_letters = {char.lower() for char in sentence if char.isalpha()}
   print(sorted(unique_letters))  # Sort for display
   # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
   #  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

Set Operations with Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. activecode:: setcomp_3

   # Multiples of 2 and 3 under 20
   multiples_of_2 = {x for x in range(20) if x % 2 == 0}
   multiples_of_3 = {x for x in range(20) if x % 3 == 0}

   print("Multiples of 2:", multiples_of_2)
   print("Multiples of 3:", multiples_of_3)
   print("Common multiples:", multiples_of_2 & multiples_of_3)  # Intersection

When to Use Set Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use set comprehensions when:

* You need unique values
* Order doesn't matter
* You want to use set operations (union, intersection, difference)
* You want to remove duplicates efficiently

**Check your understanding**

.. mchoice:: question_setcomp_1
   :practice: T
   :answer_a: [1, 2, 2, 3, 3, 3]
   :answer_b: {1, 2, 3}
   :answer_c: {1, 4, 9}
   :answer_d: [1, 4, 9]
   :correct: b
   :feedback_a: This is a list with duplicates
   :feedback_b: Correct! Sets automatically remove duplicates
   :feedback_c: This would be {x**2 for x in [1, 2, 2, 3, 3, 3]}
   :feedback_d: This is a list

   What does this set comprehension produce?

   .. code-block:: python

      result = {x for x in [1, 2, 2, 3, 3, 3]}

Generator Expressions
---------------------

.. index:: generator expression, memory efficiency

A **generator expression** looks like a list comprehension, but uses ``()`` instead of ``[]``. It creates an iterator that generates values on-demand, rather than creating a full list in memory.

Syntax and Memory Efficiency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # List comprehension - creates entire list immediately
   squares_list = [x**2 for x in range(1000000)]  # Uses ~8 MB of memory

   # Generator expression - creates iterator
   squares_gen = (x**2 for x in range(1000000))   # Uses ~100 bytes

The generator produces values one at a time as you iterate, not all at once.

Basic Generator Expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. activecode:: genexp_1

   # Generator expression with parentheses
   squares_gen = (x**2 for x in range(10))

   print(type(squares_gen))  # <class 'generator'>

   # Iterate through it
   for square in squares_gen:
       print(square, end=' ')
   # Output: 0 1 4 9 16 25 36 49 64 81

Once you iterate through a generator, it's exhausted:

.. activecode:: genexp_2

   squares_gen = (x**2 for x in range(5))

   # First iteration
   print(list(squares_gen))  # [0, 1, 4, 9, 16]

   # Second iteration - generator is exhausted!
   print(list(squares_gen))  # []

Using Generators with Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many built-in functions accept iterators, so you can pass generators directly:

.. activecode:: genexp_3

   # sum() accepts an iterator
   total = sum(x**2 for x in range(100))  # No need for extra []
   print(total)  # 328350

   # max() accepts an iterator
   longest = max(len(word) for word in ['cat', 'elephant', 'dog'])
   print(longest)  # 8

Notice: When a generator expression is the only argument to a function, you can omit the outer parentheses.

When to Use Generator Expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use generator expressions when:

* Working with large datasets (saves memory)
* You only need to iterate once
* Passing to functions like ``sum()``, ``max()``, ``min()``, ``any()``, ``all()``

Use list comprehensions when:

* You need to iterate multiple times
* You need to use list methods (``append``, ``sort``, etc.)
* The dataset is small
* You need to inspect the contents immediately

.. activecode:: genexp_4

   # Compare memory usage (conceptually)

   # BAD for large data - creates huge list
   def sum_squares_list(n):
       return sum([x**2 for x in range(n)])

   # GOOD for large data - uses generator
   def sum_squares_gen(n):
       return sum(x**2 for x in range(n))

   print(sum_squares_list(1000))
   print(sum_squares_gen(1000))
   # Both give same result, but gen uses far less memory

**Check your understanding**

.. mchoice:: question_genexp_1
   :practice: T
   :answer_a: A list
   :answer_b: A generator object
   :answer_c: A tuple
   :answer_d: A set
   :correct: b
   :feedback_a: Lists use [], not ()
   :feedback_b: Correct! Parentheses with comprehension syntax create a generator
   :feedback_c: Tuples would be created with tuple(), and don't use comprehension syntax like this
   :feedback_d: Sets use {} braces

   What type of object does this expression create?

   .. code-block:: python

      result = (x**2 for x in range(10))

Comparing Comprehension Types
------------------------------

.. index:: comprehension comparison

Here's a quick comparison of all comprehension types:

+---+---+---+---+
| Type          | Syntax          | Result     | Use Case                    |
+===============+=================+============+=============================+
| **List**      | ``[x for ...]`` | list       | Ordered collection, need    |
|               |                 |            | multiple iterations         |
+---+---+---+---+
| **Dict**      | ``{k: v for     | dict       | Key-value pairs, lookups    |
|               | ...}``          |            |                             |
+---+---+---+---+
| **Set**       | ``{x for ...}`` | set        | Unique values, membership   |
|               |                 |            | testing                     |
+---+---+---+---+
| **Generator** | ``(x for ...)`` | generator  | Large datasets, single      |
|               |                 |            | iteration, memory           |
|               |                 |            | efficiency                  |
+---+---+---+---+

Example: Same Data, Different Comprehensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. activecode:: comprehension_comparison

   numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

   # List comprehension - all squares (with duplicates)
   list_result = [x**2 for x in numbers]
   print("List:", list_result)
   # [1, 4, 4, 9, 9, 9, 16, 16, 16, 16]

   # Set comprehension - unique squares
   set_result = {x**2 for x in numbers}
   print("Set:", set_result)
   # {16, 1, 4, 9}

   # Dict comprehension - number to its square
   dict_result = {x: x**2 for x in numbers}  # Later duplicates overwrite
   print("Dict:", dict_result)
   # {1: 1, 2: 4, 3: 9, 4: 16}

   # Generator - memory-efficient iteration
   gen_result = (x**2 for x in numbers)
   print("Generator:", list(gen_result))  # Convert to list to display
   # [1, 4, 4, 9, 9, 9, 16, 16, 16, 16]

Practice Problems
-----------------

.. activecode:: ac20_4_2
   :language: python
   :practice: T

   Write a function that uses a list comprehension to keep only even numbers.
   ~~~~
   def keep_evens(nums):
       new_list = [num for num in nums if num % 2 == 0]
       return new_list

   print(keep_evens([3, 4, 6, 7, 0, 1]))
   # Should print: [4, 6, 0]


.. activecode:: ac20_4_3
   :language: python
   :practice: T

   Compare using map/filter vs list comprehension for the same task.
   ~~~~
   things = [3, 4, 6, 7, 0, 1]

   # Using map and filter (functional style)
   result1 = list(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))
   print("map/filter:", result1)

   # Equivalent using list comprehension (more Pythonic)
   result2 = [x*2 for x in things if x % 2 == 0]
   print("list comp:", result2)

   # Both produce: [8, 12, 0]


**Check your understanding**

.. mchoice:: question21_4_1
   :practice: T
   :answer_a: [4,2,8,6,5]
   :answer_b: [8,4,16,12,10]
   :answer_c: 10
   :answer_d: [10]
   :correct: d
   :feedback_a: Items from alist are doubled before being placed in blist.
   :feedback_b: Not all the items in alist are to be included in blist. Look at the if clause.
   :feedback_c: The result needs to be a list.
   :feedback_d: Yes, 5 is the only odd number in alist. It is doubled before being placed in blist.

   What is printed by the following statements?

   .. code-block:: python

     alist = [4,2,8,6,5]
     blist = [num*2 for num in alist if num%2==1]
     print(blist)


.. activecode:: ac21_4_4
   :language: python
   :autograde: unittest
   :chatcodes:
   :practice: T

   **2.** The for loop below produces a list of numbers greater than 10. Below the given code, use list comprehension to accomplish the same thing. Assign it the the variable ``lst2``. Only one line of code is needed.
   ~~~~
   L = [12, 34, 21, 4, 6, 9, 42]
   lst = []
   for x in L:
       if x > 10:
           lst.append(x)
   print(lst)

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFourA(self):
         self.assertEqual(lst2, [12, 34, 21, 42], "Testing that lst2 is assigned to correct values")
         self.assertNotIn('map(', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")
         self.assertNotIn('filter(', self.getEditorText(), "Testing your code (Don't worry about actual and expected values).")

   myTests().main()


.. activecode:: ac21_4_5
   :language: python
   :autograde: unittest
   :chatcodes:
   :practice: T

   **3.** Write code to assign to the variable ``compri`` all the values of the key ``name`` in any of the sub-dictionaries in the dictionary ``tester``. Do this using a list comprehension.
   ~~~~
   tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}


   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(sorted(compri), sorted(['Lauren', 'Ayo', 'Kathryn', 'Nick', 'Gladys', 'Adam']), "Testing that compri has the correct values.")

   myTests().main()


Summary
-------

You've now mastered all types of Python comprehensions:

✅ **Nested list comprehensions** - Creating and flattening 2D structures

✅ **Dictionary comprehensions** - Building dictionaries efficiently with ``{k: v for ...}``

✅ **Set comprehensions** - Getting unique values with ``{x for ...}``

✅ **Generator expressions** - Memory-efficient iteration with ``(x for ...)``

**Key Takeaways:**

* List comprehensions are the most common and most readable for simple transformations
* Dictionary comprehensions are perfect for creating mappings
* Set comprehensions automatically handle uniqueness
* Generator expressions save memory for large datasets
* All comprehensions can include filtering with ``if`` clauses
* Nested comprehensions work, but readability decreases quickly

In the next sections, you'll learn about ``map()``, ``filter()``, and ``zip()`` - functional programming alternatives to comprehensions.