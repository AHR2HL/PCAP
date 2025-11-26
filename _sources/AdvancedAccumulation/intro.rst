..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


.. qnum::
   :prefix: AdAccum-1-
   :start: 1

.. _list_comp_chap:

Introduction: Advanced Accumulation with map, filter, and zip
==============================================================

As a PCEP-certified programmer, you already know how to use **basic list comprehensions** to transform and filter sequences:

.. code-block:: python

   # Transform
   squares = [x**2 for x in numbers]

   # Filter
   evens = [x for x in numbers if x % 2 == 0]

   # Both
   even_squares = [x**2 for x in numbers if x % 2 == 0]

This chapter introduces three powerful built-in functions that provide alternative ways to accomplish these tasks, plus additional capabilities for working with multiple sequences.

What You'll Learn (PCAP Section 5 - 22%)
---

**1. The map() Function**

Transform every element in a sequence:

.. code-block:: python

   numbers = [1, 2, 3, 4, 5]
   squares = list(map(lambda x: x**2, numbers))
   # [1, 4, 9, 16, 25]

**2. The filter() Function**

Keep only elements that meet a condition:

.. code-block:: python

   numbers = [1, 2, 3, 4, 5, 6]
   evens = list(filter(lambda x: x % 2 == 0, numbers))
   # [2, 4, 6]

**3. The zip() Function**

Combine multiple sequences element-by-element:

.. code-block:: python

   names = ['Alice', 'Bob', 'Charlie']
   ages = [25, 30, 35]
   combined = list(zip(names, ages))
   # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

**4. Advanced List Comprehensions**

We'll also explore advanced comprehension techniques including:

* Nested list comprehensions
* Dictionary comprehensions
* Set comprehensions
* Generator expressions

When to Use Each Technique
---

**List comprehensions** are often more Pythonic and readable for simple transformations:

.. code-block:: python

   # Clear and readable
   squares = [x**2 for x in numbers]

**map() and filter()** are useful when:

* You have an existing function to apply
* You're working with multiple sequences
* You want to emphasize functional programming style

.. code-block:: python

   # Using existing function
   strings = ['1', '2', '3']
   numbers = list(map(int, strings))

**zip()** is essential when:

* Combining data from parallel lists
* Creating dictionaries from keys and values
* Iterating over multiple sequences simultaneously

Professional Python developers use all of these techniques. Understanding when to use each is part of writing idiomatic Python code.

Prerequisites
---

This chapter assumes you're comfortable with:

* Basic list comprehensions (from PCEP)
* Lambda expressions (from Advanced Functions chapter)
* Basic iteration with for loops

Let's begin!
