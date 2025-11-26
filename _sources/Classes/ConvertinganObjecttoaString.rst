..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Converting an Object to a String
---------------------------------

**Critical PCAP Topic** (Section 4 - 34% of exam)

The ``__str__`` special method is explicitly tested on the PCAP certification exam. Understanding special methods (also called "magic methods" or "dunder methods") is essential for professional Python programming.


.. activecode:: chp13_classesstr1

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
    print(p)

The ``print`` function shown above produces a string representation of the Point ``p``.  The default functionality provided by
Python tells you that ``p`` is an object of type ``Point``.  However, it does not tell you anything about the specific
state of the point.

We can improve on this representation if we include a special method call ``__str__``.  Notice that this method uses the same naming convention as the constructor, that is two underscores before and after the name.  It is common that Python
uses this naming technique for special methods.

The ``__str__`` method is responsible for returning a string representation as defined by the class creator.  In other words, you as the programmer, get to choose what a ``Point`` should look like when it gets printed.  In this case, we
have decided that the string representation will include the values of x and y as well as some identifying text.  It
is required that the ``__str__`` method create and *return* a string.

Whatever string the ``__str__`` method for a class returns, that is the string that will print when you put any instance of that class in a print statement. For that reason, the string that a class's ``__str__`` method returns should usually include values of instance variables. If a point has ``x`` value 3 and ``y`` value 4, but another point has ``x`` value 5 and ``y`` value 9, those two Point objects should probably look different when you print them, right?

Take a look at the code below.

.. activecode:: chp13_classesstr2

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

        def __str__(self):
            return "x = {}, y = {}".format(self.x, self.y)

    p = Point(7,6)
    print(p)


When we run the program above you can see that the ``print`` function now shows the string that we chose.

Now, you ask, don't we already have a ``str`` type converter that can
turn our object into a string?  Yes we do!

And doesn't ``print``
automatically use this when printing things?  Yes again!

However, as we saw earlier, these automatic mechanisms do not do exactly what we want.  Python provides many default implementations for
methods that we as programmers will probably want to change.  When a programmer changes the meaning of a method we
say that we **override** the method.  Note also that the ``str`` type converter function uses whatever ``__str__`` method we
provide.

**Advanced: __str__ vs __repr__**

Python actually has TWO special methods for string representation:

- ``__str__`` - "informal" string for end users (via ``print()`` and ``str()``)
- ``__repr__`` - "official" string for developers (via ``repr()``)

.. activecode:: chp13_classesstr3

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            """User-friendly representation"""
            return f"Point at ({self.x}, {self.y})"

        def __repr__(self):
            """Developer-friendly representation (recreatable)"""
            return f"Point({self.x}, {self.y})"

    p = Point(3, 4)

    print("Using print() calls __str__:")
    print(p)

    print("\nUsing str() calls __str__:")
    print(str(p))

    print("\nUsing repr() calls __repr__:")
    print(repr(p))

    print("\nIn interactive mode or lists, __repr__ is used:")
    points = [p]
    print(points)

**Output:**
::

   Using print() calls __str__:
   Point at (3, 4)

   Using str() calls __str__:
   Point at (3, 4)

   Using repr() calls __repr__:
   Point(3, 4)

   In interactive mode or lists, __repr__ is used:
   [Point(3, 4)]

.. important::
   **When to use which:**

   - ``__str__``: Human-readable, for end users
   - ``__repr__``: Unambiguous, ideally recreatable (``eval(repr(obj)) == obj``)

   **If you only define one**, define ``__repr__`` - Python will use it as fallback for ``__str__``.

**When is __str__ Called?**

The ``__str__`` method is automatically called in several situations:

.. activecode:: chp13_classesstr4

    class Temperature:
        def __init__(self, celsius):
            self.celsius = celsius

        def __str__(self):
            return f"{self.celsius}°C"

    temp = Temperature(25)

    # 1. print() calls __str__
    print("Using print():", temp)

    # 2. str() calls __str__
    result = str(temp)
    print("Using str():", result)

    # 3. String formatting calls __str__
    message = f"The temperature is {temp}"
    print("In f-string:", message)

    # 4. String concatenation calls __str__
    combined = "Current: " + str(temp)
    print("Concatenation:", combined)

**Output:**
::

   Using print(): 25°C
   Using str(): 25°C
   In f-string: The temperature is 25°C
   Concatenation: Current: 25°C

**Common Patterns for __str__**

**1. Simple attribute listing:**

.. code-block:: python

   def __str__(self):
       return f"Person(name={self.name}, age={self.age})"

**2. Formatted output:**

.. code-block:: python

   def __str__(self):
       return f"{self.name} is {self.age} years old"

**3. Multi-line representation:**

.. code-block:: python

   def __str__(self):
       return f"""
       Name: {self.name}
       Age: {self.age}
       Email: {self.email}
       """.strip()

**4. Conditional formatting:**

.. code-block:: python

   def __str__(self):
       status = "adult" if self.age >= 18 else "minor"
       return f"{self.name} ({status})"


**Check Your Understanding**

1. Create a class called Cereal that accepts three inputs: 2 strings and 1 integer, and assigns them to 3 instance variables in the constructor: ``name``, ``brand``, and ``fiber``. When an instance of ``Cereal`` is printed, the user should see the following: "[name] cereal is produced by [brand] and has [fiber integer] grams of fiber in every serving!" To the variable name ``c1``, assign an instance of ``Cereal`` whose name is ``"Corn Flakes"``, brand is ``"Kellogg's"``, and fiber is ``2``. To the variable name ``c2``, assign an instance of ``Cereal`` whose name is ``"Honey Nut Cheerios"``, brand is ``"General Mills"``, and fiber is ``3``. Practice printing both!

.. activecode:: ac_ch13_classstr_01
   :tags: Classes/ImprovingourConstructor.rst, Classes/AddingOtherMethodstoourClass.rst, Classes/ConvertinganObjecttoaString.rst


   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(c1.__str__(), "Corn Flakes cereal is produced by Kellogg's and has 2 grams of fiber in every serving!", "Testing that c1 prints correctly.")
      def testTwo(self):
         self.assertEqual(c2.__str__(), "Honey Nut Cheerios cereal is produced by General Mills and has 3 grams of fiber in every serving!", "Testing that c2 prints correctly.")

   myTests().main()

2. Create a class called ``Book`` with instance variables ``title``, ``author``, and ``pages``.
   When printed, it should show: "'{title}' by {author} ({pages} pages)"
   Create ``b1`` = Book("1984", "George Orwell", 328)

.. activecode:: ac_ch13_classstr_02
   :tags: Classes/ConvertinganObjecttoaString.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(str(b1), "'1984' by George Orwell (328 pages)", "Testing book string")

   myTests().main()

3. Create a class ``BankAccount`` with ``owner`` and ``balance``.
   When printed, show: "Account owner: {owner}, Balance: ${balance:.2f}"
   Create ``acc`` = BankAccount("Alice", 1234.56)

.. activecode:: ac_ch13_classstr_03
   :tags: Classes/ConvertinganObjecttoaString.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(str(acc), "Account owner: Alice, Balance: $1234.56", "Testing account string")

   myTests().main()

.. mchoice:: str_method_mc1
   :answer_a: __string__
   :answer_b: __str__
   :answer_c: toString
   :answer_d: __print__
   :correct: b
   :feedback_a: Close, but it's abbreviated to __str__
   :feedback_b: Correct! The method is called __str__ (short for string)
   :feedback_c: That's Java! Python uses __str__
   :feedback_d: There's no __print__ method in Python

   What is the name of the special method for string representation?

.. mchoice:: str_method_mc2
   :answer_a: It can return any type
   :answer_b: It must return a string
   :answer_c: It must return None
   :answer_d: It must return an integer
   :correct: b
   :feedback_a: No, it must specifically return a string
   :feedback_b: Correct! __str__ must return a string object
   :feedback_c: That would make print() useless!
   :feedback_d: It returns a string, not an integer

   What must the __str__ method return?

.. mchoice:: str_method_mc3
   :answer_a: print() only
   :answer_b: str() only
   :answer_c: Both print() and str()
   :answer_d: Neither - you must call it manually
   :correct: c
   :feedback_a: str() also calls __str__!
   :feedback_b: print() also calls __str__!
   :feedback_c: Correct! Both print() and str() automatically call __str__
   :feedback_d: Python calls it automatically in several situations

   When is __str__ automatically called?

.. mchoice:: str_method_mc4
   :answer_a: To make printing faster
   :answer_b: To encrypt object data
   :answer_c: To provide a readable string representation of an object
   :answer_d: To convert objects to JSON
   :correct: c
   :feedback_a: __str__ doesn't affect performance
   :feedback_b: __str__ doesn't encrypt data
   :feedback_c: Correct! __str__ provides a human-readable string representation
   :feedback_d: That's what json.dumps() does, not __str__

   What is the purpose of defining a __str__ method?
