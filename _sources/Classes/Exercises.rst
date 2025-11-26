..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

:skipreading:`True`

Exercises
---------

.. question:: classes_ex_1

    .. tabbed:: q1

        .. tab:: Question


           .. actex:: ch_cl_01

              Add a method ``reflect_x`` to Point which returns a new Point, one which is the reflection of the point about the x-axis. For example, ``Point(3, 5).reflect_x()`` is (3, -5)

              ~~~~
              class Point:
                  """ Point class for representing and manipulating x,y coordinates. """

                  def __init__(self, initX, initY):

                      self.x = initX
                      self.y = initY

                  def getX(self):
                      return self.x

                  def getY(self):
                      return self.y

                  def distanceFromOrigin(self):
                      return ((self.x ** 2) + (self.y ** 2)) ** 0.5
                    
                  def move(self, dx, dy):
                      self.x = self.x + dx
                      self.y = self.y + dy
                        
                  def __str__(self):
                      return str(self.x)+","+str(self.y)


.. question:: classes_ex_2

    .. tabbed:: q2

        .. tab:: Question

           .. actex:: ch_cl_02

                Add a method called ``move`` that will take two parameters, call them ``dx`` and ``dy``.  The method will cause the point to move in the x and y direction the number of units given. (Hint: you will change the values of the state of the point)

                ~~~~
                class Point:
                    """ Point class for representing and manipulating x,y coordinates. """

                    def __init__(self, initX, initY):

                        self.x = initX
                        self.y = initY

                    def getX(self):
                        return self.x

                    def getY(self):
                        return self.y

                    def distanceFromOrigin(self):
                        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
                        
                    # Put your new method here

                    def __str__(self):
                        return str(self.x)+","+str(self.y)

                ====
                from unittest.gui import TestCaseGui
                import re
                class myTests(TestCaseGui):
                    def testOne(self):
                        class _Point:
            
                            def __init__(self, initX, initY):
                
                                self.x = initX
                                self.y = initY
                
                            def getX(self):
                                return self.x
            
                            def getY(self):
                                return self.y
            
                            def distanceFromOrigin(self):
                                return ((self.x ** 2) + (self.y ** 2)) ** 0.5
            
                            def move(self, dx, dy):
                                self.x += dx
                                self.y += dy
                    
                            def __str__(self):
                                return str(self.x)+","+str(self.y)
            
            
                            def test_point(pt, dx, dy):
                                point = Point(pt[0], pt[1])
                                _point= _Point(pt[0], pt[1])
                                point.move(dx, dy)
                                _point.move(dx, dy)
                                self.assertAlmostEqual(point.x, _point.x, 7,
                                    'Checking x for Point({}, {}).move({}, {})'.format(pt[0], pt[1], dx, dy))
                                self.assertAlmostEqual(point.y, _point.y, 7,
                                    'Checking y for Point({}, {}).move({}, {})'.format(pt[0], pt[1], dx, dy))
                            test_point([0.29, 0.87], 0.8, 0.2)
                            test_point([0.13, 0.95], 0.89, 0.32)
                myTests().main()
           

        .. tab:: Answer
            
            .. activecode:: ch_cl_02_answer
            
                class Point:
                    """ Point class for representing and manipulating x,y coordinates. """

                    def __init__(self, initX, initY):

                        self.x = initX
                        self.y = initY

                    def getX(self):
                        return self.x

                    def getY(self):
                        return self.y

                    def distanceFromOrigin(self):
                        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
                    
                    def move(self, dx, dy):
                        self.x = self.x + dx
                        self.y = self.y + dy
                        
                    def __str__(self):
                        return str(self.x)+","+str(self.y)


                p = Point(7,6)
                print(p)
                p.move(5,10)
                print(p)

.. question:: classes_ex_3

   .. activecode:: ch_cl_03

      Create a class ``Employee`` with:
      - Class variable ``company_name = "TechCorp"``
      - Instance variables: ``name``, ``salary``
      - Method ``get_info()`` that returns: "{name} works at {company_name} and earns ${salary}"

      Create two employees and verify they share the same company_name.

      ~~~~
      # Your code here

      ====
      from unittest.gui import TestCaseGui

      class myTests(TestCaseGui):
          def testOne(self):
              e1 = Employee("Alice", 50000)
              e2 = Employee("Bob", 60000)
              self.assertEqual(e1.company_name, "TechCorp")
              self.assertEqual(e2.company_name, "TechCorp")
              self.assertEqual(e1.salary, 50000)
              self.assertEqual(e2.salary, 60000)

      myTests().main()
rst
.. question:: classes_ex_4

   .. activecode:: ch_cl_04

      Create a class ``Counter`` with:
      - Class variable ``total_count = 0``
      - Instance variable ``count`` (starts at 0)
      - In ``__init__``, increment the class variable ``total_count``
      - Method ``increment()`` that increases the instance ``count`` by 1

      This tracks both per-instance counts and total instances created.

      ~~~~
      # Your code here

      ====
      from unittest.gui import TestCaseGui

      class myTests(TestCaseGui):
          def testOne(self):
              c1 = Counter()
              c2 = Counter()
              c3 = Counter()
              self.assertEqual(Counter.total_count, 3)
              c1.increment()
              c1.increment()
              self.assertEqual(c1.count, 2)
              self.assertEqual(c2.count, 0)

      myTests().main()

.. question:: classes_ex_5

   .. activecode:: ch_cl_05

      Create a class ``BankAccount`` with:
      - Private instance variable ``__balance`` (starts at 0)
      - Method ``deposit(amount)`` - adds to balance
      - Method ``withdraw(amount)`` - subtracts if sufficient funds, returns True/False
      - Method ``get_balance()`` - returns current balance

      The balance should NOT be directly accessible outside the class.

      ~~~~
      class BankAccount:
          # Your code here
          pass

      ====
      from unittest.gui import TestCaseGui

      class myTests(TestCaseGui):
          def testOne(self):
              acc = BankAccount()
              acc.deposit(100)
              self.assertEqual(acc.get_balance(), 100)
              result = acc.withdraw(30)
              self.assertTrue(result)
              self.assertEqual(acc.get_balance(), 70)

          def testTwo(self):
              acc = BankAccount()
              acc.deposit(50)
              result = acc.withdraw(100)
              self.assertFalse(result)
              self.assertEqual(acc.get_balance(), 50)

      myTests().main()

.. question:: classes_ex_6

   .. activecode:: ch_cl_06

      Create a class ``Book`` with instance variables ``title``, ``author``, ``pages``.
      Define ``__str__`` to return: "'{title}' by {author} ({pages} pages)"

      ~~~~
      class Book:
          # Your code here
          pass

      ====
      from unittest.gui import TestCaseGui

      class myTests(TestCaseGui):
          def testOne(self):
              b = Book("1984", "George Orwell", 328)
              self.assertEqual(str(b), "'1984' by George Orwell (328 pages)")

      myTests().main()

.. question:: classes_ex_7

   .. activecode:: ch_cl_07

      Create a class ``Student`` with ``name`` and ``grade``.
      Define ``__lt__`` to sort by grade (descending - higher grades first).

      Create a list of 3 students and sort them.

      ~~~~
      class Student:
          # Your code here
          pass

      # Create students and test sorting
      students = [
          Student("Alice", 85),
          Student("Bob", 95),
          Student("Charlie", 78)
      ]

      sorted_students = sorted(students)
      # Bob should be first (95), then Alice (85), then Charlie (78)

      ====
      from unittest.gui import TestCaseGui

      class myTests(TestCaseGui):
          def testOne(self):
              self.assertEqual(sorted_students[0].name, "Bob")
              self.assertEqual(sorted_students[1].name, "Alice")
              self.assertEqual(sorted_students[2].name, "Charlie")

      myTests().main()

.. question:: classes_ex_8

   .. activecode:: ch_cl_08

      Create a class ``Rectangle`` with ``width`` and ``height``.

      Create a standalone function ``fits_inside(rect1, rect2)`` that returns True if rect1 fits inside rect2.

      ~~~~
      class Rectangle:
          # Your code here
          pass

      def fits_inside(rect1, rect2):
          # Your code here
          pass

      ====
      from unittest.gui import TestCaseGui

      class myTests(TestCaseGui):
          def testOne(self):
              small = Rectangle(3, 4)
              large = Rectangle(10, 10)
              self.assertTrue(fits_inside(small, large))
              self.assertFalse(fits_inside(large, small))

      myTests().main()

.. question:: classes_ex_9

   .. activecode:: ch_cl_09

      Add a method ``scaled(self, factor)`` to the Point class that returns a NEW Point with coordinates multiplied by factor.

      The original point should NOT be modified.

      ~~~~
      class Point:
          def __init__(self, x, y):
              self.x = x
              self.y = y

          # Add scaled method here

      ====
      from unittest.gui import TestCaseGui

      class myTests(TestCaseGui):
          def testOne(self):
              p1 = Point(3, 4)
              p2 = p1.scaled(2)
              self.assertEqual(p1.x, 3)  # Original unchanged
              self.assertEqual(p1.y, 4)
              self.assertEqual(p2.x, 6)  # New point scaled
              self.assertEqual(p2.y, 8)

      myTests().main()

.. question:: classes_ex_10

   .. activecode:: ch_cl_10

      Design and implement a class ``Car`` with:
      - Instance variables: ``make``, ``model``, ``year``, ``mileage``
      - Method ``drive(miles)`` - increases mileage
      - Method ``age(current_year)`` - returns car's age
      - ``__str__`` method showing: "{year} {make} {model} with {mileage} miles"

      ~~~~
      # Your code here

      ====
      from unittest.gui import TestCaseGui

      class myTests(TestCaseGui):
          def testOne(self):
              c = Car("Toyota", "Camry", 2015, 50000)
              c.drive(100)
              self.assertEqual(c.mileage, 50100)
              self.assertEqual(c.age(2024), 9)
              self.assertIn("2015", str(c))

      myTests().main()

Contributed Exercises
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    {% for q in questions: %}
        <div class='oneq full-width'>
            {{ q['htmlsrc']|safe }}
        </div>
    {% endfor %}
