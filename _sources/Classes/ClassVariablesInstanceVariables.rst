..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _class_and_instance_vars:

Class Variables and Instance Variables
---------------------------------------

This is a **critical PCAP topic** (Section 4 - 34% of exam).

Understanding the difference between class and instance variables is essential for professional Python programming and is explicitly tested on the PCAP certification exam.

You have already seen that each instance of a class has its own namespace with its own instance variables. Two instances of the Point class each have their own instance variable x. Setting x in one instance doesn't affect the other instance.

A class can also have class variables. A class variable is set as part of the class definition.

For example, consider the following version of the Point class. Here we have added a graph method that generates a string representing a little text-based graph with the Point plotted on the graph. It's not a very pretty graph, in part because the y-axis is stretched like a rubber band, but you can get the idea from this.

Note that there is an assignment to the variable printed_rep on line 4. It is not inside any method. That makes it a class variable. It is accessed in the same way as instance variables. For example, on line 16, there is a reference to self.printed_rep. If you change line 4, you have it print a different character at the x,y coordinates of the Point in the graph.

.. activecode:: classvars_1

    class Point:
        """ Point class for representing and manipulating x,y coordinates. """

        printed_rep = "*"

        def __init__(self, initX, initY):

            self.x = initX
            self.y = initY

        def graph(self):
            rows = []
            size = max(int(self.x), int(self.y)) + 2
            for j in range(size-1) :
                if (j+1) == int(self.y):
                    special_row = str((j+1) % 10) + (" "*(int(self.x) -1)) + self.printed_rep
                    rows.append(special_row)
                else:
                    rows.append(str((j+1) % 10))
            rows.reverse()  # put higher values of y first
            x_axis = ""
            for i in range(size):
                x_axis += str(i % 10)
            rows.append(x_axis)

            return "\n".join(rows)


    p1 = Point(2, 3)
    p2 = Point(3, 12)
    print(p1.graph())
    print()
    print(p2.graph())

To be able to reason about class variables and instance variables, it is helpful to know the rules that the python interpreter uses. That way, you can mentally simulate what the interpreter does.

When the interpreter sees an expression of the form <obj>.<varname>, it:
    1. Checks if the object has an instance variable set. If so, it uses that value.
    2. If it doesn't find an instance variable, it checks whether the class has a class variable. If so it uses that value.
    3. If it doesn't find an instance or a class variable, it creates a runtime error (actually, it does one other check first, which you will learn about in the next chapter).

When the interpreter sees an assignment statement of the form <obj>.<varname> = <expr>, it:
    1. Evaluates the expression on the right-hand side to yield some python object;
    2. Sets the instance variable <varname> of <obj> to be bound to that python object. Note that an assignment statement of this form never sets the class variable; it only sets the instance variable.

In order to set the class variable, you use an assignment statement of the form <varname> = <expr> at the top-level in a class definition, like on line 4 in the code above to set the class variable printed_rep.

In case you are curious, method definitions also create class variables. Thus, in the code above, graph becomes a class variable that is bound to a function/method object. p1.graph() is evaluated by:
    * looking up p1 and finding that it's an instance of Point
    * looking for an instance variable called graph in p1, but not finding one
    * looking for a class variable called graph in p1's class, the Point class; it finds a function/method object
    * Because of the () after the word graph, it invokes the function/method object, with the parameter self bound to the object p1 points to.

Try running it in codelens and see if you can follow how it all works.

**Class Variables are Shared Across All Instances**

Class variables are useful when all instances should share the same value:

.. activecode:: classvars_shared

    class Dog:
        """Dog class with species (class var) and name (instance var)."""

        species = "Canis familiaris"  # Class variable - all dogs share

        def __init__(self, name, age):
            self.name = name  # Instance variable - unique per dog
            self.age = age    # Instance variable - unique per dog

        def description(self):
            return f"{self.name} is {self.age} years old"

        def species_info(self):
            return f"{self.name} is a {self.species}"

    buddy = Dog("Buddy", 9)
    miles = Dog("Miles", 4)

    print(buddy.description())
    print(miles.description())
    print()
    print(buddy.species_info())
    print(miles.species_info())
    print()
    print(f"Both share species: {buddy.species == miles.species}")

**Output:**
::

   Buddy is 9 years old
   Miles is 4 years old

   Buddy is a Canis familiaris
   Miles is a Canis familiaris

   Both share species: True

**Common Pattern: Tracking Total Instances**

Class variables are perfect for tracking how many instances have been created:

.. activecode:: classvars_counter

    class Player:
        """Player class that tracks total players."""

        total_players = 0  # Class variable - shared counter

        def __init__(self, name):
            self.name = name           # Instance variable
            Player.total_players += 1  # Increment class variable

        @classmethod
        def get_player_count(cls):
            """Return total number of players."""
            return cls.total_players

    print(f"Players at start: {Player.total_players}")

    p1 = Player("Alice")
    print(f"After creating Alice: {Player.total_players}")

    p2 = Player("Bob")
    p3 = Player("Charlie")
    print(f"After creating Bob and Charlie: {Player.total_players}")

    print(f"Using class method: {Player.get_player_count()}")

**Output:**
::

   Players at start: 0
   After creating Alice: 1
   After creating Bob and Charlie: 3
   Using class method: 3

**Important: Instance Assignment Creates Instance Variable**

Be careful! Assigning to ``self.class_var`` creates an **instance** variable, not a class variable:

.. activecode:: classvars_warning

    class Example:
        shared = "I'm shared"  # Class variable

        def __init__(self):
            pass

    # Both instances share the class variable
    e1 = Example()
    e2 = Example()

    print(f"e1.shared: {e1.shared}")
    print(f"e2.shared: {e2.shared}")
    print(f"Example.shared: {Example.shared}")
    print()

    # Modify via instance - creates instance variable!
    e1.shared = "I'm NOT shared anymore"

    print("After e1.shared = 'I'm NOT shared anymore':")
    print(f"e1.shared: {e1.shared}")  # Instance variable
    print(f"e2.shared: {e2.shared}")  # Still class variable
    print(f"Example.shared: {Example.shared}")  # Class variable unchanged
    print()

    # Modify via class - affects all instances (that don't have instance var)
    Example.shared = "New shared value"

    print("After Example.shared = 'New shared value':")
    print(f"e1.shared: {e1.shared}")  # Still instance variable (not affected)
    print(f"e2.shared: {e2.shared}")  # Class variable (updated!)
    print(f"Example.shared: {Example.shared}")  # Class variable (updated!)

**Output:**
::

   e1.shared: I'm shared
   e2.shared: I'm shared
   Example.shared: I'm shared

   After e1.shared = 'I'm NOT shared anymore':
   e1.shared: I'm NOT shared anymore
   e2.shared: I'm shared
   Example.shared: I'm shared

   After Example.shared = 'New shared value':
   e1.shared: I'm NOT shared anymore
   e2.shared: New shared value
   Example.shared: New shared value

**Check Your Understanding**

1. Create a class called ``NumberSet`` that accepts 2 integers as input, and defines two instance variables: ``num1`` and ``num2``, which hold each of the input integers. Then, create an instance of ``NumberSet`` where its num1 is 6 and its num2 is 10. Save this instance to a variable ``t``.

[Keep existing problem]

2. **NEW:** Create a class called ``BankAccount`` with:
   - Class variable ``bank_name = "Python Bank"``
   - Instance variables ``owner`` and ``balance``
   - Create two accounts: ``acc1`` (owner="Alice", balance=1000) and ``acc2`` (owner="Bob", balance=500)

.. activecode:: ee_ch13_classvars_2
   :tags:Classes/ClassVariablesInstanceVariables.rst

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(BankAccount.bank_name, "Python Bank", "Testing class variable")
       def testTwo(self):
           self.assertEqual(acc1.owner, "Alice", "Testing acc1 owner")
           self.assertEqual(acc1.balance, 1000, "Testing acc1 balance")
       def testThree(self):
           self.assertEqual(acc2.owner, "Bob", "Testing acc2 owner")
           self.assertEqual(acc2.balance, 500, "Testing acc2 balance")
       def testFour(self):
           self.assertEqual(acc1.bank_name, acc2.bank_name, "Both should share class variable")

   myTests().main()