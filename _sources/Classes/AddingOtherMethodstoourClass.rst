..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Adding Other Methods to a Class
-------------------------------

The key advantage of using a class like ``Point`` rather than something like a simple
tuple ``(7, 6)`` now becomes apparent.  We can add methods to
the ``Point`` class that are sensible operations for points.  Had we chosen to use a
tuple to represent the point, we would not have this capability.
Creating a class like ``Point`` brings an exceptional
amount of "organizational power" to our programs, and to our thinking.
We can group together the sensible operations, and the kinds of data
they apply to, and each instance of the class can have its own state.

A **method** behaves like a function but it is invoked on a specific
instance.  For example, with a list bound to variable L, ``L.append(7)`` calls the function append, with the list itself as the first parameter and 7 as the second parameter.   Methods are accessed using dot notation. This is why ``L.append(7)`` has 2 parameters even though you may think it only has one: the list stored in the variable ``L`` is the first parameter value and 7 is the second.

Let's add two simple methods to allow a point to give us information about its state.  The ``getX`` method, when invoked, will return the value of the x coordinate.

The implementation of this method is straight forward since we already know how
to write functions that return values.  One thing to notice is that even though the ``getX`` method does not need any other parameter information to do its work, there is still one formal parameter, ``self``.  As we stated earlier, all methods defined in a class that operate on objects of that class will have ``self`` as their first parameter.  Again, this serves as a reference to the object itself which in turn gives access to the state data inside the object.

.. activecode:: chp13_classes4

    class Point:
        """ Point class for representing and manipulating x,y coordinates. """

        def __init__(self, initX, initY):

            self.x = initX
            self.y = initY

        def getX(self):
            return self.x

        def getY(self):
            return self.y


    p = Point(7,6)
    print(p.getX())
    print(p.getY())

Note that the ``getX`` method simply returns the value of the instance variable x from the object self.  In other words, the implementation of the method is to go to the state of the object itself and get the value of ``x``.  Likewise, the ``getY`` method looks almost the same.

Let's add another method, ``distanceFromOrigin``, to see better how methods
work.  This method will again not need any additional information to do its work, beyond the data stored in the instance variables.
It will perform a more complex task.

.. activecode:: chp13_classes5

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


    p = Point(7,6)
    print(p.distanceFromOrigin())


Notice that the call of ``distanceFromOrigin`` does not *explicitly*
supply an argument to match the ``self`` parameter.  This is true of all method calls. The definition will always seem to
have one additional parameter as compared to the invocation.

**Methods Can Modify State**

Not all methods just return values - many methods modify the object's state:

.. activecode:: chp13_classes6

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
            """Move the point by dx and dy"""
            self.x += dx
            self.y += dy

        def reset(self):
            """Move point back to origin"""
            self.x = 0
            self.y = 0

    p = Point(7, 6)
    print(f"Initial: ({p.getX()}, {p.getY()})")

    p.move(3, 4)
    print(f"After move(3, 4): ({p.getX()}, {p.getY()})")

    p.reset()
    print(f"After reset: ({p.getX()}, {p.getY()})")

**Output:**
::

   Initial: (7, 6)
   After move(3, 4): (10, 10)
   After reset: (0, 0)

**Methods Can Call Other Methods**

Methods can use ``self`` to call other methods on the same object:

.. activecode:: chp13_classes7

    class Point:
        def __init__(self, initX, initY):
            self.x = initX
            self.y = initY

        def distanceFromOrigin(self):
            return ((self.x ** 2) + (self.y ** 2)) ** 0.5

        def distanceFromPoint(self, other):
            """Calculate distance to another point"""
            dx = other.x - self.x
            dy = other.y - self.y
            return (dx ** 2 + dy ** 2) ** 0.5

        def isNearOrigin(self, threshold=10):
            """Check if point is within threshold of origin"""
            # Calls distanceFromOrigin method!
            return self.distanceFromOrigin() < threshold

    p1 = Point(3, 4)
    p2 = Point(100, 100)

    print(f"p1 distance from origin: {p1.distanceFromOrigin():.2f}")
    print(f"p1 near origin? {p1.isNearOrigin()}")

    print(f"p2 distance from origin: {p2.distanceFromOrigin():.2f}")
    print(f"p2 near origin? {p2.isNearOrigin()}")

    print(f"Distance between p1 and p2: {p1.distanceFromPoint(p2):.2f}")

**Output:**
::

   p1 distance from origin: 5.00
   p1 near origin? True
   p2 distance from origin: 141.42
   p2 near origin? False
   Distance between p1 and p2: 136.42

**Check Your Understanding**

1. Create a class called ``Animal`` that accepts two numbers as inputs and assigns them respectively to two instance variables: ``arms`` and ``legs``. Create an instance method called ``limbs`` that, when called, returns the total number of limbs the animal has. To the variable name ``spider``, assign an instance of ``Animal`` that has 4 arms and 4 legs. Call the limbs method on the ``spider`` instance and save the result to the variable name ``spidlimbs``.

.. activecode:: ac_chp13_classes_01
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rs


   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(spider.arms, 4, "Testing that spider was assigned the correct number of arms.")
         self.assertEqual(spider.legs, 4, "Testing that spider was assigned the correct number of legs.")
         self.assertEqual(spidlimbs, 8, "Testing that spidlimbs was assigned correctly.")

   myTests().main()


2. Create a class ``Rectangle`` with instance variables ``width`` and ``height``.
   Add a method ``area()`` that returns width × height.
   Create ``rect`` = Rectangle(5, 10) and save ``rect.area()`` to ``rect_area``.

.. activecode:: ac_chp13_classes_02
   :tags: Classes/AddingOtherMethodstoourClass.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(rect.width, 5, "Testing rect width")
           self.assertEqual(rect.height, 10, "Testing rect height")
           self.assertEqual(rect_area, 50, "Testing area calculation")

   myTests().main()

3. Create a class ``Counter`` with instance variable ``count`` (starts at 0).
   Add methods: ``increment()`` (adds 1 to count), ``reset()`` (sets count to 0).
   Create ``c``, call increment 3 times, save ``c.count`` to ``result``.

.. activecode:: ac_chp13_classes_03
   :tags: Classes/AddingOtherMethodstoourClass.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(result, 3, "Testing that count incremented correctly")

   myTests().main()

