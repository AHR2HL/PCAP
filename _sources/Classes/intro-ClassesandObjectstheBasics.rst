..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _classes_chap:

Introduction: Classes and Objects - the Basics
==============================================

As a PCEP-certified programmer, you already understand object-oriented programming from working with Python's Turtle module:

.. code-block:: python

   # You already know objects from PCEP
   import turtle

   alex = turtle.Turtle()  # Created an instance
   alex.color("red")       # Used attributes
   alex.forward(50)        # Called methods

You've been **using** objects. Now you'll learn to **define your own classes**.

What You Already Know
---------------------

From PCEP, you understand:

✅ **Objects** are instances of classes
✅ **Attributes** store object state (data)
✅ **Methods** define object behavior (functions)
✅ **Instances** are created from classes
✅ Different instances can have different attribute values

What You'll Learn (PCAP Section 4 - 34% of exam)
-------------------------------------------------

This chapter covers class definition required for PCAP certification:

**1. Class Definition Syntax**

.. code-block:: python

   class Point:
       """Represents a point in 2D space."""

       def __init__(self, x, y):
           self.x = x
           self.y = y

**2. The __init__ Constructor**

.. code-block:: python

   p = Point(3, 4)  # __init__ called automatically

**3. Instance vs Class Variables**

.. code-block:: python

   class Counter:
       total = 0  # Class variable (shared)

       def __init__(self):
           self.count = 0  # Instance variable (per object)

**4. Special Methods**

.. code-block:: python

   def __str__(self):
       return f"Point({self.x}, {self.y})"

**5. Class and Static Methods**

.. code-block:: python

   @classmethod
   def from_tuple(cls, coords):
       return cls(coords[0], coords[1])

   @staticmethod
   def distance(p1, p2):
       return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5

**6. Private Variables (Name Mangling)**

.. code-block:: python

   class BankAccount:
       def __init__(self):
           self.__balance = 0  # Private!

**7. The __dict__ Attribute**

.. code-block:: python

   print(p.__dict__)  # {'x': 3, 'y': 4}

Why This Matters
----------------

**For PCAP Certification:**
* Class definition is Section 4 (34% of exam)
* Instance vs class variables are explicitly tested
* Special methods (__init__, __str__) are required
* Decorators (@classmethod, @staticmethod) are required
* Private variables (name mangling) are tested

**For Your Career:**
* Classes are fundamental to professional Python
* Most real-world code uses custom classes
* Understanding OOP is essential for frameworks (Django, Flask, etc.)
* Classes organize complex programs effectively

Prerequisites
-------------

This chapter assumes you're comfortable with:

* Using objects and calling methods (from Turtle)
* Functions and parameters
* Lists and dictionaries
* Understanding of attributes and methods

Let's define your first class!