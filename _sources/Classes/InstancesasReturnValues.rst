..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Instances as Return Values
--------------------------

Functions and methods can return objects.  This is actually nothing new since everything in Python is an object and we have
been returning values for quite some time. (You can also have lists or tuples of object instances, etc.)  The difference here is that we want to have the method create an object using
the constructor and then return it as the value of the method.

    
Suppose you have a point object
and wish to find the midpoint halfway between it and some other target point.  We would like to write a method, let's call
it ``halfway``, which takes another ``Point`` as a parameter and returns the ``Point`` that is halfway between the point and
the target point it accepts as input.

.. activecode:: chp13_classesmid1

    class Point:

        def __init__(self, initX, initY):

            self.x = initX
            self.y = initY

        def getX(self):
            return self.x

        def getY(self):
            return self.y

        def distanceFromOrigin(self):
            return ((self.x ** 2) + (self.y ** 2)) ** 0.5
          
        def __str__(self):
            return "x = {}, y = {}".format(self.x, self.y)

        def halfway(self, target): 
            mx = (self.x + target.x)/2
            my = (self.y + target.y)/2
            return Point(mx, my)

    p = Point(3,4)
    q = Point(5,12)
    mid = p.halfway(q)
    # note that you would have exactly the same result if you instead wrote
    # mid = q.halfway(p)
    # because they are both Point objects, and the middle is the same no matter what

    print(mid)
    print(mid.getX())
    print(mid.getY())
       

The resulting Point, ``mid``, has an x value of 4 and a y value of 8.  We can also use any other methods on ``mid`` since it is a
``Point`` object.

    
**More Examples of Returning Instances**

.. activecode:: chp13_return_instances_2

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"Point({self.x}, {self.y})"

        def halfway(self, target):
            """Return midpoint between self and target"""
            mx = (self.x + target.x) / 2
            my = (self.y + target.y) / 2
            return Point(mx, my)

        def translate(self, dx, dy):
            """Return new point shifted by dx, dy"""
            return Point(self.x + dx, self.y + dy)

        def reflect_x(self):
            """Return new point reflected across x-axis"""
            return Point(self.x, -self.y)

        def reflect_y(self):
            """Return new point reflected across y-axis"""
            return Point(-self.x, self.y)

    p = Point(3, 4)
    print(f"Original: {p}")

    # Various transformations
    shifted = p.translate(2, 3)
    print(f"Shifted by (2,3): {shifted}")

    reflected_x = p.reflect_x()
    print(f"Reflected across x-axis: {reflected_x}")

    reflected_y = p.reflect_y()
    print(f"Reflected across y-axis: {reflected_y}")

**Output:**
::

   Original: Point(3, 4)
   Shifted by (2,3): Point(5, 7)
   Reflected across x-axis: Point(3, -4)
   Reflected across y-axis: Point(-3, 4)

**Method Chaining with Returned Instances**

Since methods return new instances, you can chain operations:

.. activecode:: chp13_return_instances_3

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"({self.x}, {self.y})"

        def translate(self, dx, dy):
            return Point(self.x + dx, self.y + dy)

        def scale(self, factor):
            return Point(self.x * factor, self.y * factor)

    p = Point(2, 3)

    # Chain transformations
    result = p.translate(1, 1).scale(2).translate(0, 5)

    print(f"Start: {p}")
    print(f"After .translate(1,1).scale(2).translate(0,5): {result}")

    # Step by step (same result):
    step1 = p.translate(1, 1)      # (3, 4)
    step2 = step1.scale(2)         # (6, 8)
    step3 = step2.translate(0, 5)  # (6, 13)
    print(f"Step by step: {step3}")

**Output:**
::

   Start: (2, 3)
   After .translate(1,1).scale(2).translate(0,5): (6, 13)
   Step by step: (6, 13)

**Check Your Understanding**

1. Using the Point class, create a method ``double()`` that returns a new Point with coordinates doubled.
   Create ``p = Point(3, 4)`` and ``doubled = p.double()``. Save doubled's x to ``result``.

.. activecode:: ac_instances_return_01
   :tags: Classes/InstancesasReturnValues.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(result, 6, "Testing doubled point x coordinate")
           self.assertEqual(doubled.y, 8, "Testing doubled point y coordinate")

   myTests().main()

2. Create a class ``Circle`` with ``radius``. Add method ``scaled(self, factor)`` that returns a new Circle with radius multiplied by factor.
   Create ``c1 = Circle(5)`` and ``c2 = c1.scaled(3)``. Save ``c2.radius`` to ``new_radius``.

.. activecode:: ac_instances_return_02
   :tags: Classes/InstancesasReturnValues.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(c1.radius, 5, "Original circle unchanged")
           self.assertEqual(new_radius, 15, "New circle has scaled radius")

   myTests().main()

.. mchoice:: instances_return_mc1
   :answer_a: Numbers only
   :answer_b: Strings only
   :answer_c: Any type, including custom objects
   :answer_d: Only built-in types
   :correct: c
   :feedback_a: Methods can return any type!
   :feedback_b: Methods can return any type!
   :feedback_c: Correct! Methods can return objects of any type, including instances of custom classes
   :feedback_d: Custom objects work too!

   What types of values can methods return?

.. mchoice:: instances_return_mc2
   :answer_a: return Point(mx, my)
   :answer_b: return new Point(mx, my)
   :answer_c: return Point.new(mx, my)
   :answer_d: return self.Point(mx, my)
   :correct: a
   :feedback_a: Correct! Just call the class name like a function to create a new instance
   :feedback_b: No 'new' keyword needed in Python (unlike Java/C++)
   :feedback_c: Point is the constructor, not Point.new
   :feedback_d: self is an instance, not the class

   How do you create and return a new Point instance in a method?