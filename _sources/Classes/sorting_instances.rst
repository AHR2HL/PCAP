..  Copyright (C)  Paul Resnick and Steve Oney.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  shortname:: Sorting Instances
..  description:: Invoking sort and sorted on lists of instances.

.. qnum::
   :prefix: sort-instances-
   :start: 1
   
.. _sort_instances_chap:

Sorting Lists of Instances
==========================

You previously learned :ref:`how to sort lists <sort_chap>`. Sorting lists of instances of a class is fundamentally the same as sorting lists of objects of any other type. There are two main ways to sort lists of instances: (1) by providing a ``key`` function as a parameter to ``sorted()`` (or ``.sort()``) or by (2) defining a "comparison operator" that determines how two instances should be compared (specifically, given two instances, which one should come first). We will describe both ways here.

Approach 1: Sorting Lists of Instances with ``key``
---------------------------------------------------

Previously, you have seen how to provide such a function as input when sorting lists of other kinds of objects. For example, given a list of strings, you can sort them in ascending order of their lengths by passing ``len`` as the key parameter. Note that if you refer to a function by name, you give the name of the function without parentheses after it, because you want the function object itself. The sorted function will take care of calling the function, passing the current item in the list. Thus, in the example below, we write ``key=len`` and not ``key=len()``.

.. activecode:: sort_instances_1

   L = ["Cherry", "Apple", "Blueberry"]
   
   print(sorted(L))
   print(sorted(L, key=len))
   #alternative form using lambda, if you find that easier to understand
   print(sorted(L, key= lambda x: len(x)))   

When each of the items in a list is an instance of a class, the function you pass for the key parameter takes one instance as an input and returns a number. The instances will be sorted by their returned numbers.

.. activecode:: sort_instances_2

   class Fruit():
       def __init__(self, name, price):
           self.name = name
           self.price = price
                      
   L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
   for f in sorted(L, key=lambda x: x.price):
       print(f.name)

Sometimes you will find it convenient to define a method for the class that does some computation on the data in an instance. In this case, our class is too simple to really illustrate that. But to simulate it, I've defined a method ``sort_priority`` that just returns the price that's stored in the instance. Now, that method, sort_priority takes one instance as input and returns a number. So it is exactly the kind of function we need to provide as the key parameter for sorted. Here it can get a little confusing: to refer to that method, without actually invoking it, you can refer to ``Fruit.sort_priority``. This is analogous to the code above that referred to ``len`` rather than invoking ``len()``.

.. activecode:: sort_instances_3

   class Fruit():
       def __init__(self, name, price):
           self.name = name
           self.price = price
           
       def sort_priority(self):
           return self.price
           
   L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]
   print("-----sorted by price, referencing a class method-----")
   for f in sorted(L, key=Fruit.sort_priority):
       print(f.name)
       
   print("---- one more way to do the same thing-----")
   for f in sorted(L, key=lambda x: x.sort_priority()):
       print(f.name)


Approach 2: Defining Sort Orders with Comparison Operators
----------------------------------------------------------

Another approach to sorting lists of instances is to specify a "comparison operator" for the class---a method that takes two instances as arguments and "decides" which should come first. One advantage of this approach is that you can call ``sorted`` on a list of instances **without** specifying a value for ``key`` and it will sort in the order you defined.

To do this, we can define a method named ``__lt__`` which stands for "less than". Note that this method starts and ends with two underscores. This signifies that it is a special method, just like ``__init__`` and ``__str__``. Our method, ``__lt__``, takes two instances as arguments: ``self`` and an argument for another instance. It returns ``True`` if the ``self`` instance should come before the other instance, and ``False`` otherwise. Normally, ``__lt__`` is called when we try to use the less than operator (``<``) on class instances; Python translates the expression ``a < b`` into ``a.__lt__(b)``. However, we can also use ``__lt__`` to decide which of two instances should come first in a sorted list. For example, if we wanted to sort instances of ``Fruit`` by prices by default, we could define ``__lt__`` as follows:

.. activecode:: sort_instances_4

    class Fruit():
        def __init__(self, name, price):
            self.name = name
            self.price = price
           
        def __lt__(self, other): # other is another instance of Fruit
            return self.price < other.price
           
    apple = Fruit("Apple", 10)
    cherry = Fruit("Cherry", 5)
    blueberry = Fruit("Blueberry", 20)
    L = [cherry, apple, blueberry]

    print("-----sorted using comparison operator (without key)-----")
    for f in sorted(L):
        print(f.name)

    print(f'apple < cherry: {apple < cherry}') # Equivalent to apple.__lt__(cherry) ; False

When we call ``sorted(L)`` without specifying a value for the ``key`` parameter, it will sort the items in the list using the ``__lt__`` method defined for the class of items. ``sorted()`` will automatically call the ``__lt__`` method, passing in two instances from the list. Calling ``__lt__`` when ``self`` is ``Fruit("Apple", 10)`` and ``other`` is ``Fruit("Cherry", 5)`` returns ``False`` (because the ``price`` of the apple is not less than the price of the cherry) so this means ``Cherry`` should come before ``Apple`` in the sorted list.

If we wanted to sort by names, we could define ``__lt__`` differently. *Note that when we call ``<`` on strings, it does an alphabetical comparison; ``"Apple" < "Cherry"`` is ``True``. We can take advantage of this in our ``__lt__`` method*:

.. activecode:: sort_instances_5

    class Fruit():
        def __init__(self, name, price):
            self.name = name
            self.price = price
           
        def __lt__(self, other): # other is another instance of Fruit
            return self.name < other.name # note we are comparing names
           
    apple = Fruit("Apple", 10)
    cherry = Fruit("Cherry", 5)
    blueberry = Fruit("Blueberry", 20)
    L = [cherry, apple, blueberry]

    print("-----sorted using comparison operator (without key)-----")
    for f in sorted(L):
        print(f.name)

    print(f'apple < cherry: {apple < cherry}') # Equivalent to apple.__lt__(cherry) ; False


Finally, note that if we pass in a function for the ``key`` parameter when we call ``sorted()`` (approach 1), it will use that key function instead of calling the ``__lt__`` method. You can try putting a print statement inside the ``__lt__`` method to see this for yourself: __lt__ will not be called when you provide a key function but it will be called when you don't provide a key function.

**Other Comparison Operators**

Besides ``__lt__`` (less than), you can define other comparison operators:

.. list-table:: Comparison Operator Methods
   :widths: 30 30 40
   :header-rows: 1

   * - Operator
     - Method
     - Example
   * - ``<`` (less than)
     - ``__lt__(self, other)``
     - ``a < b`` → ``a.__lt__(b)``
   * - ``<=`` (less or equal)
     - ``__le__(self, other)``
     - ``a <= b`` → ``a.__le__(b)``
   * - ``>`` (greater than)
     - ``__gt__(self, other)``
     - ``a > b`` → ``a.__gt__(b)``
   * - ``>=`` (greater or equal)
     - ``__ge__(self, other)``
     - ``a >= b`` → ``a.__ge__(b)``
   * - ``==`` (equal)
     - ``__eq__(self, other)``
     - ``a == b`` → ``a.__eq__(b)``
   * - ``!=`` (not equal)
     - ``__ne__(self, other)``
     - ``a != b`` → ``a.__ne__(b)``

.. activecode:: sort_instances_6

    class Fruit:
        def __init__(self, name, price):
            self.name = name
            self.price = price

        def __lt__(self, other):
            return self.price < other.price

        def __eq__(self, other):
            return self.price == other.price

        def __str__(self):
            return f"{self.name}(${self.price})"

    apple = Fruit("Apple", 5)
    cherry = Fruit("Cherry", 5)
    blueberry = Fruit("Blueberry", 10)

    print(f"apple < blueberry: {apple < blueberry}")  # True
    print(f"apple == cherry: {apple == cherry}")      # True
    print(f"blueberry > apple: {blueberry > apple}")  # Error! No __gt__ defined

**Output:**
::

   apple < blueberry: True
   apple == cherry: True
   blueberry > apple: Error! No __gt__ defined

.. note::
   **Use @functools.total_ordering**

   Python provides a decorator that auto-generates missing comparison methods if you define ``__eq__`` and one other (like ``__lt__``):

   .. code-block:: python

      from functools import total_ordering

      @total_ordering
      class Fruit:
          def __init__(self, name, price):
              self.name = name
              self.price = price

          def __eq__(self, other):
              return self.price == other.price

          def __lt__(self, other):
              return self.price < other.price

          # __le__, __gt__, __ge__, __ne__ auto-generated!

**Sorting by Multiple Criteria**

Sometimes you need to sort by multiple attributes:

.. activecode:: sort_instances_7

    class Student:
        def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age

        def __str__(self):
            return f"{self.name} (Grade: {self.grade}, Age: {self.age})"

    students = [
        Student("Alice", 90, 20),
        Student("Bob", 85, 19),
        Student("Charlie", 90, 19),
        Student("Diana", 85, 20)
    ]

    # Sort by grade (descending), then by age (ascending)
    sorted_students = sorted(students, key=lambda s: (-s.grade, s.age))

    print("Sorted by grade (desc), then age (asc):")
    for s in sorted_students:
        print(f"  {s}")

**Output:**
::

   Sorted by grade (desc), then age (asc):
     Charlie (Grade: 90, Age: 19)
     Alice (Grade: 90, Age: 20)
     Bob (Grade: 85, Age: 19)
     Diana (Grade: 85, Age: 20)

**Explanation:** The lambda returns a tuple ``(-grade, age)``. Python compares tuples element by element, so it sorts by grade first (negated for descending), then by age.

**Check Your Understanding**

1. Create a class ``Book`` with ``title`` and ``pages``. Create a list of 3 books and sort them by number of pages (ascending). Save the title of the book with fewest pages to ``shortest_title``.

.. activecode:: ac_sort_instances_01
   :tags: Classes/sorting_instances.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           # Should sort by pages ascending
           self.assertIn("shortest", shortest_title.lower(), "Test hint: shortest book should have fewest pages")

   myTests().main()

2. Create a class ``Person`` with ``name`` and ``age``. Define ``__lt__`` to sort by age. Create a list of 3 people with different ages and sort them. The youngest person should be first.

.. activecode:: ac_sort_instances_02
   :tags: Classes/sorting_instances.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           # Should be sorted by age
           ages = [p.age for p in sorted_people]
           self.assertEqual(ages, sorted(ages), "Should be sorted by age ascending")

   myTests().main()

.. mchoice:: sort_instances_mc1
   :answer_a: key=len
   :answer_b: key=len()
   :answer_c: key=lambda x: len
   :answer_d: key=lambda: len(x)
   :correct: a
   :feedback_a: Correct! Pass the function itself, not a call to it
   :feedback_b: This would call len() with no arguments and pass the result
   :feedback_c: This lambda returns the len function, not the length
   :feedback_d: lambda needs a parameter

   How do you pass the len function as the key parameter?

.. mchoice:: sort_instances_mc2
   :answer_a: __sort__
   :answer_b: __cmp__
   :answer_c: __lt__
   :answer_d: __compare__
   :correct: c
   :feedback_a: There's no __sort__ special method
   :feedback_b: __cmp__ was used in Python 2, but Python 3 uses __lt__
   :feedback_c: Correct! __lt__ stands for "less than"
   :feedback_d: There's no __compare__ special method

   Which special method defines the default sort order for a class?

.. mchoice:: sort_instances_mc3
   :answer_a: key parameter is ignored
   :answer_b: __lt__ is ignored
   :answer_c: Both are used together
   :answer_d: An error occurs
   :correct: b
   :feedback_a: The key parameter is used!
   :feedback_b: Correct! If you provide a key parameter, __lt__ is not called
   :feedback_c: Only one is used - the key parameter takes precedence
   :feedback_d: No error - key parameter just takes precedence

   What happens if a class has __lt__ defined AND you provide a key parameter to sorted()?