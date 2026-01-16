..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Objects as Arguments and Parameters
-----------------------------------

You can pass an object as an argument to a function, in the usual way.

Here is a simple function called ``distance`` involving our new ``Point`` objects.  The job of this function is to figure out the 
distance between two points.
 
.. activecode:: chp13_classes6aa

    import math
    
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

    def distance(point1, point2):
        xdiff = point2.getX()-point1.getX()
        ydiff = point2.getY()-point1.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist
    
    p = Point(4,3)
    q = Point(0,0)
    print(distance(p,q))


``distance`` takes two points and returns the distance between them.  Note that ``distance`` is **not** a method of the Point class.  You can see this by looking at the indentation pattern.  It is not inside the class definition.  The other way we
can know that ``distance`` is not a method of Point is that ``self`` is not included as a formal parameter.  In addition, we do not invoke ``distance`` using the dot notation.

We *could have* made distance be a method of the Point class. Then, we would have called the first parameter self, and would have invoked it using the dot notation, as in the following code. Which way to implement it is a matter of coding style. Both work correctly. Most programmers choose whether to make functions be stand-alone or methods of a class based on whether the function semantically seems to be an operation that is performed on instances of the class. In this case, because distance is really a property of a pair of points and is symmetric (the distance from a to b is the same as that from b to a) it makes more sense to have it be a standalone function and not a method. Many heated discussions have occurred between programmers about such style decisions.

.. activecode:: chp13_classes6b

    import math
    
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

        def distance(self, point2):
            xdiff = point2.getX()-self.getX()
            ydiff = point2.getY()-self.getY()

            dist = math.sqrt(xdiff**2 + ydiff**2)
            return dist
    
    p = Point(4,3)
    q = Point(0,0)
    print(p.distance(q))

**Functions Can Take Multiple Object Parameters**

.. activecode:: chp13_multiple_objects

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height

    def point_in_rectangle(point, rect):
        """Check if point is inside rectangle (assuming rect at origin)"""
        return 0 <= point.x <= rect.width and 0 <= point.y <= rect.height

    p1 = Point(3, 4)
    p2 = Point(15, 20)
    rect = Rectangle(10, 10)

    print(f"Is ({p1.x}, {p1.y}) in rectangle? {point_in_rectangle(p1, rect)}")
    print(f"Is ({p2.x}, {p2.y}) in rectangle? {point_in_rectangle(p2, rect)}")

**Output:**
::

   Is (3, 4) in rectangle? True
   Is (15, 20) in rectangle? False

**Check Your Understanding**

1. Create a class ``Rectangle`` with ``__init__(self, width, height)`` and instance variables ``width`` and ``height``.

   Create a standalone function ``area(rect)`` that takes a Rectangle object and returns its area (width × height).

   Create ``r1 = Rectangle(5, 10)`` and calculate ``area1 = area(r1)``.

.. activecode:: ac_objects_as_params_01
   :tags: Classes/ObjectsasArgumentsandParameters.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(r1.width, 5, "Testing r1 width")
           self.assertEqual(r1.height, 10, "Testing r1 height")
           self.assertEqual(area1, 50, "Testing area calculation")

   myTests().main()

2. Create a standalone function ``are_equal(p1, p2)`` that takes two Point objects and returns True if they have the same x and y coordinates.

   Create ``p1 = Point(3, 4)`` and ``p2 = Point(3, 4)`` and save ``are_equal(p1, p2)`` to ``result``.

.. activecode:: ac_objects_as_params_02
   :tags: Classes/ObjectsasArgumentsandParameters.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertTrue(result, "Points with same coordinates should be equal")

   myTests().main()

.. mchoice:: objects_params_mc1
   :answer_a: Functions cannot accept objects as parameters
   :answer_b: Objects can be passed like any other value
   :answer_c: Objects must be converted to strings first
   :answer_d: Only built-in objects can be passed
   :correct: b
   :feedback_a: Objects can definitely be passed as parameters!
   :feedback_b: Correct! Objects are passed to functions just like any other value
   :feedback_c: No conversion is needed
   :feedback_d: Custom objects work too!

   How are objects passed as function parameters?

.. mchoice:: objects_params_mc2
   :answer_a: It's indented inside the class
   :answer_b: It has self as first parameter
   :answer_c: It's called with dot notation
   :answer_d: All of the above
   :correct: d
   :feedback_a: True, but there are other indicators too!
   :feedback_b: True, but there are other indicators too!
   :feedback_c: True, but there are other indicators too!
   :feedback_d: Correct! All three are signs it's a method, not a standalone function

   How can you tell if a function is a method of a class?

.. mchoice:: objects_params_mc3
   :answer_a: If it operates on a single instance
   :answer_b: If it's symmetric (like distance between two points)
   :answer_c: If it's used in multiple unrelated classes
   :answer_d: All are valid reasons
   :correct: d
   :feedback_a: Correct reason for standalone function!
   :feedback_b: Correct reason for standalone function!
   :feedback_c: Correct reason for standalone function!
   :feedback_d: Correct! All are good reasons to make it standalone

   When should you make a function standalone instead of a method?