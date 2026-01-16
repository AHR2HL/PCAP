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
   :prefix: func-14-
   :start: 1

Exercises
=========
.. actex:: ac11_14_1
    :autograde: unittest

    Write a function named ``num_test`` that takes a number as input. If the number is greater than 10, the function should return "Greater than 10." If the number is less than 10, the function should return "Less than 10." If the number is equal to 10, the function should return "Equal to 10."
    ~~~~


    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

    def testOne(self):
        self.assertEqual(num_test(5), "Less than 10.", "Testing the num_test function on input 5.")
        self.assertEqual(num_test(0), "Less than 10.", "Testing the num_test function on input 0.")
        self.assertEqual(num_test(12.99), "Greater than 10.", "Testing the num_test function on input 12.99.")
        self.assertEqual(num_test(10.00), "Equal to 10.", "Testing the num_test function on input 10.00.")



    myTests().main()

.. actex:: ac11_14_2
    :autograde: unittest

    Write a function that will return the number of digits in an integer.
    ~~~~
    def numDigits(n):
      # your code here

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

    def testOne(self):
        self.assertEqual(numDigits(2),1,"Tested numDigits on input of 2")
        self.assertEqual(numDigits(55),2,"Tested numDigits on input of 55")
        self.assertEqual(numDigits(1352),4,"Tested numDigits on input of 1352")
        self.assertEqual(numDigits(444),3,"Tested numDigits on input of 444")



    myTests().main()


.. actex:: ac11_14_3
    :autograde: unittest

    Write a function that reverses its string argument.
    ~~~~
    def reverse(astring):
      # your code here

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def testOne(self):
          self.assertEqual(reverse("happy"),"yppah","Tested reverse on input of 'happy'")
          self.assertEqual(reverse("Python"),"nohtyP","Tested reverse on input of 'Python'")
          self.assertEqual(reverse(""),"","Tested reverse on input of ''")




    myTests().main()


.. actex:: ac11_14_4
    :nocodelens:
    :autograde: unittest

    Write a function that mirrors its string argument,
    generating a string containing the original string and the string backwards.
    ~~~~
    def mirror(mystr):
      # your code here

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def testOne(self):
          self.assertEqual(mirror("good"),"gooddoog","Tested mirror on input of 'good'")
          self.assertEqual(mirror("Python"),"PythonnohtyP","Tested mirror on input of 'Python'")
          self.assertEqual(mirror(""),"","Tested mirror on input of ''")
          self.assertEqual(mirror("a"),"aa","Tested mirror on input of 'a'")


    myTests().main()


.. actex:: ac11_14_5
    :nocodelens:
    :autograde: unittest

    Write a function that removes all occurrences of a given letter from a string.
    ~~~~
    def remove_letter(theLetter, theString):
      # your code here

    ====


    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def testOne(self):
          self.assertEqual(remove_letter("a","apple"),"pple","Tested remove_letter on inputs of 'a' and 'apple'")
          self.assertEqual(remove_letter("a","banana"),"bnn","Tested remove_letter on inputs of 'a' and 'banana'")
          self.assertEqual(remove_letter("z","banana"),"banana","Tested remove_letter on inputs of 'z' and 'banana'")



    myTests().main()


.. activecode:: ac11_14_6
   :autograde: unittest

   Although Python provides us with many list methods, it is good practice and very instructive to think about how they are implemented. Implement Python functions that work like the following list methods. Do not use the built-in methods in your implementations.

   a. ``my_count(lst, item)`` - Returns the number of times item appears in lst
   b. ``my_in(lst, item)`` - Returns True if item is in lst, False otherwise
   c. ``my_reverse(lst)`` - Returns a new list with elements in reverse order
   d. ``my_index(lst, item)`` - Returns the index of the first occurrence of item (raise ValueError if not found)
   e. ``my_insert(lst, index, item)`` - Returns a new list with item inserted at the given index

   ~~~~
   def my_count(lst, item):
       """Count how many times item appears in lst."""
       # Your code here
       pass

   def my_in(lst, item):
       """Return True if item is in lst, False otherwise."""
       # Your code here
       pass

   def my_reverse(lst):
       """Return a new list with elements in reverse order."""
       # Your code here
       pass

   def my_index(lst, item):
       """Return the index of first occurrence of item. Raise ValueError if not found."""
       # Your code here
       pass

   def my_insert(lst, index, item):
       """Return a new list with item inserted at index."""
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       # Tests for my_count
       def testCount1(self):
           self.assertEqual(my_count([1, 2, 3, 2, 2], 2), 3, "Testing my_count with item appearing 3 times")

       def testCount2(self):
           self.assertEqual(my_count([1, 2, 3], 5), 0, "Testing my_count with item not in list")

       def testCount3(self):
           self.assertEqual(my_count([], 1), 0, "Testing my_count with empty list")

       def testCount4(self):
           self.assertEqual(my_count(['a', 'b', 'a', 'a'], 'a'), 3, "Testing my_count with strings")

       # Tests for my_in
       def testIn1(self):
           self.assertEqual(my_in([1, 2, 3], 2), True, "Testing my_in with item present")

       def testIn2(self):
           self.assertEqual(my_in([1, 2, 3], 5), False, "Testing my_in with item not present")

       def testIn3(self):
           self.assertEqual(my_in([], 1), False, "Testing my_in with empty list")

       def testIn4(self):
           self.assertEqual(my_in(['hello', 'world'], 'hello'), True, "Testing my_in with strings")

       # Tests for my_reverse
       def testReverse1(self):
           self.assertEqual(my_reverse([1, 2, 3, 4]), [4, 3, 2, 1], "Testing my_reverse with normal list")

       def testReverse2(self):
           self.assertEqual(my_reverse([1]), [1], "Testing my_reverse with single item")

       def testReverse3(self):
           self.assertEqual(my_reverse([]), [], "Testing my_reverse with empty list")

       def testReverse4(self):
           self.assertEqual(my_reverse(['a', 'b', 'c']), ['c', 'b', 'a'], "Testing my_reverse with strings")

       def testReverse5(self):
           original = [1, 2, 3]
           result = my_reverse(original)
           self.assertEqual(original, [1, 2, 3], "Testing my_reverse doesn't modify original list")

       # Tests for my_index
       def testIndex1(self):
           self.assertEqual(my_index([1, 2, 3, 4], 3), 2, "Testing my_index with item in middle")

       def testIndex2(self):
           self.assertEqual(my_index([1, 2, 3, 4], 1), 0, "Testing my_index with item at start")

       def testIndex3(self):
           self.assertEqual(my_index([1, 2, 3, 4], 4), 3, "Testing my_index with item at end")

       def testIndex4(self):
           self.assertEqual(my_index([1, 2, 3, 2], 2), 1, "Testing my_index returns first occurrence")

       def testIndex5(self):
           with self.assertRaises(ValueError):
               my_index([1, 2, 3], 5)

       # Tests for my_insert
       def testInsert1(self):
           self.assertEqual(my_insert([1, 2, 3], 1, 99), [1, 99, 2, 3], "Testing my_insert in middle")

       def testInsert2(self):
           self.assertEqual(my_insert([1, 2, 3], 0, 99), [99, 1, 2, 3], "Testing my_insert at start")

       def testInsert3(self):
           self.assertEqual(my_insert([1, 2, 3], 3, 99), [1, 2, 3, 99], "Testing my_insert at end")

       def testInsert4(self):
           self.assertEqual(my_insert([], 0, 1), [1], "Testing my_insert into empty list")

       def testInsert5(self):
           original = [1, 2, 3]
           result = my_insert(original, 1, 99)
           self.assertEqual(original, [1, 2, 3], "Testing my_insert doesn't modify original list")

   myTests().main()


.. actex:: ac11_14_7
    :autograde: unittest

    Write a function ``replace(s, old, new)`` that replaces all occurences of
    ``old`` with ``new`` in a string ``s``::

     test(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')

     s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
     test(replace(s, 'om', 'am'),
            'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')

     test(replace(s, 'o', 'a'),
            'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')

    *Hint*: use the ``split`` and ``join`` methods.
    ~~~~
    def replace(s, old, new):
      # your code here

    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def testOne(self):
          self.assertEqual(replace('Mississippi','i','I'),'MIssIssIppI',"Tested replace on input 'Mississippi','i','I'")
          self.assertEqual(replace('Bookkeeper','e','A'),'BookkAApAr',"Tested failed on input 'Bookkeeper','e','A'")
          self.assertEqual(replace('Deeded','e','q'),'Dqqdqd',"Tested failed on input 'Deeded','e','q'")

    myTests().main()

.. actex:: ac11_14_8
    :autograde: unittest

    Write a Python function that will take a the list of 100 random integers between 0 and 1000 and return the maximum value.  (Note: there is a builtin function named ``max`` but pretend you cannot use it.)
    ~~~~
    import random as r
    lst = []

    for i in range(100):
        num = r.randint(1, 1000)
        lst.append(num)

    def largest(lst):
        #your code here

    ====
    from unittest.gui import TestCaseGui
    import re
    class myTests(TestCaseGui):
        def testOne(self):
            output = self.getOutput().split('\n')
            editor = self.getEditorText().split('\n')
            float_re = r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'

            self.assertEqual(largest(lst), max(lst), 'Checking for the list'+ str(lst))

            # hardcode check
            self.assertFalse(re.search(r'max', self.getEditorText()), 'Checking for max')
    myTests().main()


.. actex:: ac11_14_9
  :autograde: unittest

  Write a function ``sum_of_squares(xs)`` that computes the sum
  of the squares of the numbers in the list ``xs``.  For example,
  ``sum_of_squares([2, 3, 4])`` should return 4+9+16 which is 29:
  ~~~~
  def sum_of_squares(xs):
      # your code here

  ====
  from unittest.gui import TestCaseGui

  class myTests(TestCaseGui):

      def testOne(self):
          self.assertEqual(sum_of_squares([2,3,4]),29,"Tested sum_of_squares on input [2,3,4]")
          self.assertEqual(sum_of_squares([0,1,-1]),2,"Tested sum_of_squares on input [0,1,-1]")
          self.assertEqual(sum_of_squares([5,12,14]),365,"Tested sum_of_squares on input [5,12,14]")

  myTests().main()

.. actex:: ac11_14_10
    :autograde: unittest

    Write a function to count how many odd numbers are in a list.
    ~~~~
    def countOdd(lst):
      # your code here

    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

      def testOne(self):
          self.assertEqual(countOdd([1,3,5,7,9]),5,"Tested countOdd on input [1,3,5,7,9]")
          self.assertEqual(countOdd([1,2,3,4,5]),3,"Tested countOdd on input [-1,-2,-3,-4,-5]")
          self.assertEqual(countOdd([2,4,6,8,10]),0,"Tested countOdd on input [2,4,6,8,10]")
          self.assertEqual(countOdd([0,-1,12,-33]),2,"Tested countOdd on input [0,-1,12,-33]")

    myTests().main()

.. actex:: ac11_14_11
    :autograde: unittest

    Sum up all the even numbers in a list.
    ~~~~
    def sumEven(lst):
      # your code here

    ====
    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

    def testOne(self):
        self.assertEqual(sumEven([1,3,5,7,9]),0,"Tested sumEven on input [1,3,5,7,9]")
        self.assertEqual(sumEven([-1,-2,-3,-4,-5]),-6,"Tested sumEven on input [-1,-2,-3,-4,-5]")
        self.assertEqual(sumEven([2,4,6,7,9]),12,"Tested sumEven on input [2,4,6,7,9]")
        self.assertEqual(sumEven([0,1,12,33]),12,"Tested sumEven on input [0,1,12,33]")

    myTests().main()

.. actex:: ac11_14_12
  :autograde: unittest

  Sum up all the negative numbers in a list.
  ~~~~
  def sumNegatives(lst):
      # your code here

  ====
  from unittest.gui import TestCaseGui

  class myTests(TestCaseGui):

      def testOne(self):
          self.assertEqual(sumNegatives([-1,-2,-3,-4,-5]),-15,"Tested sumNegatives on input [-1,-2,-3,-4,-5]")
          self.assertEqual(sumNegatives([1,-3,5,-7,9]),-10,"Tested sumNegatives on input [1,-3,5,-7,9]")
          self.assertEqual(sumNegatives([-2,-4,6,-7,9]),-13,"Tested sumNegatives on input [-2,-4,6,-7,9]")
          self.assertEqual(sumNegatives([0,1,2,3,4]),0,"Tested sumNegatives on input [0,1,2,3,4]")

  myTests().main()

.. actex:: ac11_14_13
    :nocodelens:
    :autograde: unittest

    Write a function ``findHypot``.  The function will be given the length of two sides of a right-angled triangle and it should return the length of the hypotenuse. (Hint:  ``x ** 0.5`` will return the square root, or use ``sqrt`` from the math module)
    ~~~~
    def findHypot(a,b):
        # your code here

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual(findHypot(12.0,5.0),13.0,"Tested findHypot on inputs of 12.0 and 5.0")
            self.assertEqual(findHypot(14.0,48.0),50.0,"Tested findHypot on inputs of 14.0 and 48.0")
            self.assertEqual(findHypot(21.0,72.0),75.0,"Tested findHypot on inputs of 21.0 and 72.0")
            self.assertAlmostEqual(findHypot(1,1.73205),1.999999,2,"Tested findHypot on inputs of 1 and 1.73205")

    myTests().main()

.. actex:: ac11_14_14
   :nocodelens:
   :autograde: unittest

   Write a function called ``is_even(n)`` that takes an integer as an argument and returns ``True`` if the argument is an **even number** and ``False`` if it is **odd**.
   ~~~~
   def is_even(n):
       #your code here

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
        def testOne(self):
            self.assertEqual(is_even(10),True,"Tested is_even on input of 10")
            self.assertEqual(is_even(5),False,"Tested is_even on input of 5")
            self.assertEqual(is_even(1),False,"Tested is_even on input of 1")
            self.assertEqual(is_even(0),True,"Tested is_even on input of 0")

   myTests().main()


.. actex:: ac11_14_15
   :nocodelens:
   :autograde: unittest

   Now write the function ``is_odd(n)`` that returns ``True`` when ``n`` is odd and ``False`` otherwise.
   ~~~~
   def is_odd(n):
       # your code here


   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(is_odd(10),False,"Tested is_odd on input of 10")
           self.assertEqual(is_odd(5),True,"Tested is_odd on input of 5")
           self.assertEqual(is_odd(1),True,"Tested is_odd on input of 1")
           self.assertEqual(is_odd(0),False,"Tested is_odd on input of 0")

   myTests().main()

.. actex:: ac11_14_16
   :autograde: unittest

   Write a function ``is_rightangled`` which, given the length of three sides of a triangle, will determine whether the triangle is right-angled. Assume that the third argument to the function is always the longest side. It will return ``True`` if the triangle is right-angled, or ``False`` otherwise.

   Hint: floating point arithmetic is not always exactly accurate,
   so it is not safe to test floating point numbers for equality.
   If a good programmer wants to know whether
   ``x`` is equal or close enough to ``y``, they would probably code it up as

   .. sourcecode:: python

       if  abs(x - y) < 0.001:      # if x is approximately equal to y
           ...

   ~~~~
   def is_rightangled(a, b, c):
       # your code here


   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(is_rightangled(1.5,2.0,2.5),True,"Tested is_rightangled on inputs of 1.5, 2.0 and 2.5")
           self.assertEqual(is_rightangled(4.0,8.0,16.0),False,"Tested is_rightangled on inputs of 4.0, 8.0 and 16.0")
           self.assertEqual(is_rightangled(4.1,8.2,9.1678787077),True,"Tested is_rightangled on inputs of 4.1, 8.2 and 9.1678787077")
           self.assertEqual(is_rightangled(4.1,8.2,9.16787),True,"Tested is_rightangled on inputs of 4.1, 8.2, and 9.16787")
           self.assertEqual(is_rightangled(4.1,8.2,9.168),False,"Tested is_rightangled on inputs of 4.1, 8.2 and 9.168")
           self.assertEqual(is_rightangled(0.5,0.4,0.64031),True,"Tested is_rightangled on inputs of 0.5, 0.4 and 0.64031")

   myTests().main()

Contributed Exercises
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    {% for q in questions: %}
        <div class='oneq full-width'>
            {{ q['htmlsrc']|safe }}
        </div>
    {% endfor %}
