..  Copyright (C)  Jaclyn Cohen, Lauren Murphy, Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Chapter Assessment
==================

Part 1: Multiple Choice Questions
----------------------------------

.. mchoice:: ch13_assess_mc1
   :answer_a: Instance variable
   :answer_b: Class variable
   :answer_c: Local variable
   :answer_d: Global variable
   :correct: b
   :feedback_a: Instance variables are defined in __init__ with self.varname
   :feedback_b: Correct! Variables defined at class level (outside methods) are class variables
   :feedback_c: Local variables are defined inside methods without self
   :feedback_d: Global variables are defined outside any class

   What type of variable is ``count`` in this code?

   .. code-block:: python

      class Example:
          count = 0

          def __init__(self):
              self.value = 5

.. mchoice:: ch13_assess_mc2
   :answer_a: __private
   :answer_b: _private
   :answer_c: private_
   :answer_d: _private_
   :correct: a
   :feedback_a: Correct! Double underscore prefix triggers name mangling
   :feedback_b: Single underscore is just a convention, no mangling
   :feedback_c: Trailing underscore has no special meaning
   :feedback_d: Surrounding underscores have no special meaning

   Which naming convention triggers Python's name mangling for private variables?

.. mchoice:: ch13_assess_mc3
   :answer_a: __sort__
   :answer_b: __cmp__
   :answer_c: __lt__
   :answer_d: __compare__
   :correct: c
   :feedback_a: There's no __sort__ method
   :feedback_b: __cmp__ was used in Python 2
   :feedback_c: Correct! __lt__ (less than) is used for sorting in Python 3
   :feedback_d: There's no __compare__ method

   Which special method should you define to enable sorting of class instances?

.. mchoice:: ch13_assess_mc4
   :answer_a: To print the object
   :answer_b: To convert the object to a string representation
   :answer_c: To initialize the object
   :answer_d: To delete the object
   :correct: b
   :feedback_a: __str__ doesn't print, it returns a string that can be printed
   :feedback_b: Correct! __str__ returns a string representation of the object
   :feedback_c: That's __init__
   :feedback_d: That's __del__

   What is the purpose of the __str__ method?

.. mchoice:: ch13_assess_mc5
   :answer_a: _ClassName__varname
   :answer_b: __varname__
   :answer_c: varname__
   :answer_d: __ClassName_varname
   :correct: a
   :feedback_a: Correct! __var becomes _ClassName__var
   :feedback_b: This format is for special methods, not mangled variables
   :feedback_c: Trailing underscores don't cause mangling
   :feedback_d: Wrong format - it's _ClassName__varname

   If a class named ``Person`` has a variable ``__age``, what does Python mangle it to?

.. mchoice:: ch13_assess_mc6
   :answer_a: All instances share the same value
   :answer_b: Each instance has its own value
   :answer_c: The variable cannot be modified
   :answer_d: The variable is private
   :correct: a
   :feedback_a: Correct! Class variables are shared across all instances
   :feedback_b: That's instance variables
   :feedback_c: Class variables can be modified
   :feedback_d: Class variables aren't necessarily private

   What is true about class variables?

.. activecode:: ac_ch13_01
   :practice: T
   :topics: Classes/ImprovingourConstructor.rst
   :tags: Classes/ImprovingourConstructor.rst
   :autograde: unittest

   Define a class called ``Bike`` that accepts a string and a float as input, and assigns those inputs respectively to two instance variables, ``color`` and ``price``. Assign to the variable ``testOne`` an instance of ``Bike`` whose color is **blue** and whose price is **89.99**. Assign to the variable ``testTwo`` an instance of Bike whose color is **purple** and whose price is **25.0**.
   ~~~~


   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(testOne.color, "blue", "Testing that testOne has the correct color assigned.")
         self.assertEqual(testOne.price, 89.99, "Testing that testOne has the correct price assigned.")

      def testTwo(self):
         self.assertEqual(testTwo.color, "purple", "Testing that testTwo has the correct color assigned.")
         self.assertEqual(testTwo.price, 25.0, "Testing that testTwo has the correct color assigned.")

   myTests().main()

.. activecode:: ac_ch13_021
   :practice: T
   :topics: Classes/AddingOtherMethodstoourClass.rst
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rst
   :autograde: unittest

   Create a class called ``AppleBasket`` whose constructor accepts two inputs: a string representing a color, and a number representing a quantity of apples. The constructor should initialize two instance variables: ``apple_color`` and ``apple_quantity``.  Write a class method called ``increase`` that increases the quantity by ``1`` each time it is invoked. You should also write a ``__str__`` method for this class that returns a string of the format: ``"A basket of [quantity goes here] [color goes here] apples."`` e.g. ``"A basket of 4 red apples."`` or ``"A basket of 50 blue apples."`` (Writing some test code that creates instances and assigns values to variables may help you solve this problem!)
   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         tester = AppleBasket("red",4)
         self.assertEqual(tester.apple_quantity, 4, "Testing the initialization of the apple_quantity inst var.")
      def testTwo(self):
         tester = AppleBasket("red",4)
         tester.increase()
         self.assertEqual(tester.apple_quantity, 5, "Testing the increase method")
      def testThree(self):
         tester = AppleBasket("green",17)
         self.assertEqual(tester.__str__(),"A basket of 17 green apples.")


   myTests().main()


.. activecode:: ac_ch13_03
   :practice: T
   :topics: Classes/AddingOtherMethodstoourClass.rst
   :tags: Classes/AddingOtherMethodstoourClass.rst, Classes/ImprovingourConstructor.rst, Classes/ConvertinganObjecttoaString.rst
   :autograde: unittest

   Define a class called ``BankAccount`` that accepts the name you want associated with your bank account in a string, and an integer that represents the amount of money in the account. The constructor should initialize two instance variables from those inputs: ``name`` and ``amt``. Add a string method so that when you print an instance of ``BankAccount``, you see ``"Your account, [name goes here], has [start_amt goes here] dollars."`` Create an instance of this class with ``"Bob"`` as the name and ``100`` as the amount. Save this to the variable ``t1``.
   ~~~~



   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(t1.__str__(), "Your account, Bob, has 100 dollars.", "Testing that t1 is assigned to correct value")

   myTests().main()

.. activecode:: ac_ch13_04
   :practice: T
   :autograde: unittest

   Create a class ``Player`` with:
   - Class variable ``game_name = "Chess"`` (shared by all players)
   - Instance variables: ``player_name`` and ``score`` (unique per player)
   - Constructor that accepts name and score

   Create two players: ``p1`` ("Alice", 100) and ``p2`` ("Bob", 150).
   Both should share the same game_name.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(Player.game_name, "Chess", "Testing class variable")
           self.assertEqual(p1.game_name, "Chess", "p1 should access class variable")
           self.assertEqual(p2.game_name, "Chess", "p2 should access class variable")
           self.assertEqual(p1.player_name, "Alice", "Testing p1 name")
           self.assertEqual(p2.player_name, "Bob", "Testing p2 name")
           self.assertEqual(p1.score, 100, "Testing p1 score")
           self.assertEqual(p2.score, 150, "Testing p2 score")

   myTests().main()
rst
.. activecode:: ac_ch13_05
   :practice: T
   :autograde: unittest

   Create a class ``IDCard`` with:
   - Class variable ``next_id = 1000`` (tracks next available ID)
   - Instance variable ``card_id``
   - Constructor that assigns the current ``next_id`` to ``card_id``, then increments ``next_id``

   Create three cards: ``card1``, ``card2``, ``card3``.
   They should have IDs 1000, 1001, 1002.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(card1.card_id, 1000, "Testing card1 ID")
           self.assertEqual(card2.card_id, 1001, "Testing card2 ID")
           self.assertEqual(card3.card_id, 1002, "Testing card3 ID")
           self.assertEqual(IDCard.next_id, 1003, "Testing next_id incremented")

   myTests().main()

.. activecode:: ac_ch13_06
   :practice: T
   :autograde: unittest

   Create a class ``SecureBox`` with:
   - Private instance variable ``__contents`` (starts as empty string)
   - Method ``store(item)`` - sets __contents to item
   - Method ``retrieve()`` - returns __contents

   The __contents should NOT be directly accessible as ``box.__contents``.
   Create a box, store "secret" in it, and save the retrieved value to ``result``.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           box = SecureBox()
           box.store("secret")
           self.assertEqual(box.retrieve(), "secret", "Testing retrieve")

       def testTwo(self):
           box = SecureBox()
           # Should not be able to access __contents directly
           try:
               x = box.__contents
               self.fail("__contents should not be directly accessible")
           except AttributeError:
               pass  # Expected

   myTests().main()

.. activecode:: ac_ch13_07
   :practice: T
   :autograde: unittest

   Create a class ``Movie`` with instance variables ``title`` and ``rating``.
   Define ``__lt__`` to sort movies by rating (descending - highest first).

   Create three movies:
   - ``m1``: "Inception", 8.8
   - ``m2``: "The Matrix", 8.7
   - ``m3``: "Interstellar", 8.6

   Save the sorted list to ``sorted_movies``.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(sorted_movies[0].title, "Inception", "Highest rating first")
           self.assertEqual(sorted_movies[1].title, "The Matrix")
           self.assertEqual(sorted_movies[2].title, "Interstellar")

   myTests().main()

.. activecode:: ac_ch13_08
   :practice: T
   :autograde: unittest

   Create a class ``Circle`` with instance variables ``radius``.

   Create a standalone function ``compare_circles(c1, c2)`` that returns:
   - "equal" if radii are the same
   - "first larger" if c1's radius > c2's radius
   - "second larger" if c2's radius > c1's radius

   Create ``circle1`` (radius=5) and ``circle2`` (radius=3).
   Save ``compare_circles(circle1, circle2)`` to ``result``.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(result, "first larger", "Testing comparison")
           c3 = Circle(5)
           c4 = Circle(5)
           self.assertEqual(compare_circles(c3, c4), "equal")

   myTests().main()

.. activecode:: ac_ch13_09
   :practice: T
   :autograde: unittest

   Add a method ``combined(self, other)`` to the Point class that returns a NEW Point
   whose coordinates are the sum of the two points' coordinates.

   Example: Point(1, 2).combined(Point(3, 4)) returns Point(4, 6)

   Create ``p1`` (1, 2), ``p2`` (3, 4), and ``p3 = p1.combined(p2)``.
   ~~~~
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y

       # Add combined method here

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(p3.x, 4, "Testing combined x")
           self.assertEqual(p3.y, 6, "Testing combined y")
           self.assertEqual(p1.x, 1, "Original p1 unchanged")
           self.assertEqual(p2.x, 3, "Original p2 unchanged")

   myTests().main()

Part 3: Debugging Exercises
----------------------------

.. activecode:: ac_ch13_debug1
   :practice: T
   :autograde: unittest

   **Debug:** This class is trying to use a class variable but it's not working correctly. Fix it!
   ~~~~
   class School:
       def __init__(self, name):
           self.school_name = name
           self.num_students = 0

       def enroll_student(self):
           num_students += 1  # BUG: Should access instance variable

   school = School("Lincoln High")
   school.enroll_student()
   print(school.num_students)  # Should be 1

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           s = School("Test")
           s.enroll_student()
           self.assertEqual(s.num_students, 1)

   myTests().main()
rst
.. activecode:: ac_ch13_debug2
   :practice: T
   :autograde: unittest

   **Debug:** The __str__ method isn't working. Fix it!
   ~~~~
   class Product:
       def __init__(self, name, price):
           self.name = name
           self.price = price

       def __str__(self):
           print(f"{self.name}: ${self.price}")  # BUG: Should return, not print

   p = Product("Widget", 9.99)
   print(p)  # Should show "Widget: $9.99"

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           p = Product("Test", 5.00)
           self.assertEqual(str(p), "Test: $5.0")

   myTests().main()

Part 4: Parson's Problems
--------------------------

.. parsonsprob:: ch13_parsons1
   :language: python
   :adaptive:
   :numbered: left

   Arrange the blocks to create a Point class with __init__ and distance_from_origin methods.
   -----
   class Point:
   =====
       def __init__(self, x, y):
   =====
       def __init__(x, y): #distractor
   =====
           self.x = x
           self.y = y
   =====
           x = self.x #distractor
           y = self.y #distractor
   =====
       def distance_from_origin(self):
   =====
           return (self.x**2 + self.y**2)**0.5
   =====
           return (x**2 + y**2)**0.5 #distractor

.. parsonsprob:: ch13_parsons2
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to create a class with a class variable and instance variable.
   -----
   class Counter:
   =====
       total = 0  # Class variable
   =====
       def __init__(self):
   =====
           self.count = 0  # Instance variable
   =====
           Counter.total += 1
   =====
           self.total += 1 #distractor