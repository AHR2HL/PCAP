..  Copyright (C)  Lauren Murphy, Jaclyn Cohen, Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
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

.. mchoice:: inheritance_assess_mc1
   :answer_a: Parent.__init__(self)
   :answer_b: super().__init__()
   :answer_c: Both A and B work
   :answer_d: Neither - constructors aren't inherited
   :correct: c
   :feedback_a: This works but is less flexible
   :feedback_b: This is the preferred way
   :feedback_c: Correct! Both work, but super() is preferred for flexibility
   :feedback_d: You can call parent constructors!

   What's the correct way to call a parent class constructor from a child class?

.. mchoice:: inheritance_assess_mc2
   :answer_a: True
   :answer_b: False
   :answer_c: Error
   :correct: a
   :feedback_a: Correct! isinstance checks the entire inheritance chain
   :feedback_b: Dog inherits from Animal, so it returns True
   :feedback_c: No error

   Given ``class Dog(Animal): pass`` and ``d = Dog()``, what does ``isinstance(d, Animal)`` return?

.. mchoice:: inheritance_assess_mc3
   :answer_a: Child's method only
   :answer_b: Parent's method only
   :answer_c: Both methods
   :answer_d: Error
   :correct: a
   :feedback_a: Correct! Child method overrides parent method
   :feedback_b: Parent method is overridden
   :feedback_c: Only one method is called (the child's)
   :feedback_d: No error - this is normal overriding

   If both parent and child classes define ``method()``, which is called on a child instance?

.. mchoice:: inheritance_assess_mc4
   :answer_a: To make code shorter
   :answer_b: To reuse code and model "is-a" relationships
   :answer_c: To make code run faster
   :answer_d: To hide methods
   :correct: b
   :feedback_a: That's a side effect, not the main purpose
   :feedback_b: Correct! Inheritance enables code reuse and models real-world relationships
   :feedback_c: Inheritance doesn't affect performance significantly
   :feedback_d: That's encapsulation, not inheritance

   What's the main purpose of inheritance?

.. mchoice:: inheritance_assess_mc5
   :answer_a: isinstance(obj, ClassName)
   :answer_b: issubclass(obj, ClassName)
   :answer_c: type(obj) == ClassName
   :answer_d: obj.__class__ == ClassName
   :correct: a
   :feedback_a: Correct! isinstance checks if obj is an instance of ClassName or its subclasses
   :feedback_b: issubclass checks class relationships, not object types
   :feedback_c: This doesn't check inheritance chain
   :feedback_d: This doesn't check inheritance chain

   How do you check if an object is an instance of a class or its subclasses?

.. mchoice:: inheritance_assess_mc6
   :answer_a: Inheritance
   :answer_b: Composition
   :answer_c: Either works equally well
   :correct: b
   :feedback_a: Car is not a type of Engine; use composition
   :feedback_b: Correct! A car HAS-A engine (composition), not IS-A engine
   :feedback_c: Composition is clearer here

   Should a ``Car`` class inherit from or contain an ``Engine`` instance?

Part 2: Active Code Questions
----------------------------------

.. activecode:: inheritance_assess_super_1
   :autograde: unittest

   Create a class ``Shape`` with __init__(color) that sets self.color.

   Create a class ``Circle`` that inherits from Shape:
   - __init__(color, radius) that uses super().__init__(color) and sets self.radius
   - method area() that returns 3.14159 * radius^2

   Create ``c = Circle("red", 5)``.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(c.color, "red")
           self.assertEqual(c.radius, 5)
           self.assertAlmostEqual(c.area(), 78.53975, 2)

   myTests().main()

.. activecode:: inheritance_assess_super_2
   :autograde: unittest

   Create a class ``Vehicle`` with:
   - __init__(make, model)
   - method describe() returns "{make} {model}"

   Create a class ``Car`` that inherits from Vehicle:
   - __init__(make, model, doors)
   - Uses super().__init__(make, model)
   - Overrides describe() to call super().describe() and add " with {doors} doors"

   Create ``car = Car("Toyota", "Camry", 4)``.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(car.make, "Toyota")
           self.assertEqual(car.doors, 4)
           desc = car.describe()
           self.assertIn("Toyota Camry", desc)
           self.assertIn("4 doors", desc)

   myTests().main()

.. activecode:: inheritance_assess_isinstance_1
   :autograde: unittest

   Given these classes:

   class Animal:
       pass

   class Mammal(Animal):
       pass

   class Dog(Mammal):
       pass

   Create variables using isinstance():
   - check1: True if Dog() is instance of Animal
   - check2: True if Dog() is instance of Mammal
   - check3: True if Animal() is instance of Dog
   ~~~~
   class Animal:
       pass

   class Mammal(Animal):
       pass

   class Dog(Mammal):
       pass

   # Your code here:

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertTrue(check1)
           self.assertTrue(check2)
           self.assertFalse(check3)

   myTests().main()

.. activecode:: inheritance_assess_issubclass_1
   :autograde: unittest

   Using the same Animal/Mammal/Dog hierarchy, create variables using issubclass():
   - sub1: True if Dog is subclass of Animal
   - sub2: True if Mammal is subclass of Dog
   - sub3: True if Dog is subclass of Dog (itself)
   ~~~~
   class Animal:
       pass

   class Mammal(Animal):
       pass

   class Dog(Mammal):
       pass

   # Your code here:

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertTrue(sub1)
           self.assertFalse(sub2)
           self.assertTrue(sub3)

   myTests().main()

.. activecode:: inheritance_assess_multilevel_1
   :autograde: unittest

   Create a 3-level hierarchy:

   class Employee:
       def __init__(self, name, salary):
           self.name = name
           self.salary = salary

   class Manager(Employee):
       def __init__(self, name, salary, team_size):
           super().__init__(name, salary)
           self.team_size = team_size

   class Director(Manager):
       def __init__(self, name, salary, team_size, budget):
           super().__init__(name, salary, team_size)
           self.budget = budget

       def info(self):
           return f"{self.name}: ${self.salary}, Team: {self.team_size}, Budget: ${self.budget}"

   Create ``dir = Director("Alice", 150000, 50, 1000000)``.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(dir.name, "Alice")
           self.assertEqual(dir.salary, 150000)
           self.assertEqual(dir.team_size, 50)
           self.assertEqual(dir.budget, 1000000)
           self.assertIn("Alice", dir.info())

   myTests().main()

.. activecode:: inheritance_assess_polymorphism_1
   :autograde: unittest

   Create a function ``speak_all(animals)`` that:
   - Takes a list of Animal objects
   - Calls speak() on each
   - Returns a list of all the sounds

   Test with Dog (returns "Woof") and Cat (returns "Meow").
   ~~~~
   class Animal:
       def speak(self):
           return "Some sound"

   class Dog(Animal):
       def speak(self):
           return "Woof"

   class Cat(Animal):
       def speak(self):
           return "Meow"

   def speak_all(animals):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           animals = [Dog(), Cat(), Dog()]
           result = speak_all(animals)
           self.assertEqual(result, ["Woof", "Meow", "Woof"])

   myTests().main()

.. activecode:: ee_inheritance_010
   :tags: Inheritance/inheritVarsAndMethods.rst
   :practice: T
   :autograde: unittest
   :topics: Inheritance/inheritVarsAndMethods

   The class, ``Pokemon``, is provided below and describes a Pokemon and its leveling and evolving characteristics. An instance of the class is one pokemon that you create.

   ``Grass_Pokemon`` is a subclass that inherits from ``Pokemon`` but changes some aspects, for instance, the boost values are different.

   For the subclass ``Grass_Pokemon``, add another method called ``action`` that returns the string ``"[name of pokemon] knows a lot of different moves!"``. Create an instance of this class with the ``name`` as ``"Belle"``. Assign this instance to the variable ``p1``.
   ~~~~
   class Pokemon(object):
       attack = 12
       defense = 10
       health = 15
       p_type = "Normal"

       def __init__(self, name, level = 5):
           self.name = name
           self.level = level

       def train(self):
           self.update()
           self.attack_up()
           self.defense_up()
           self.health_up()
           self.level = self.level + 1
           if self.level%self.evolve == 0:
               return self.level, "Evolved!"
           else:
               return self.level

       def attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack

       def defense_up(self):
           self.defense = self.defense + self.defense_boost
           return self.defense

       def health_up(self):
           self.health = self.health + self.health_boost
           return self.health

       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
           self.evolve = 10

       def __str__(self):
           self.update()
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

   class Grass_Pokemon(Pokemon):
       attack = 15
       defense = 14
       health = 12

       def update(self):
           self.health_boost = 6
           self.attack_boost = 2
           self.defense_boost = 3
           self.evolve = 12

       def moves(self):
           self.p_moves = ["razor leaf", "synthesis", "petal dance"]


   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOneA(self):
         self.assertEqual(p1.action(), "Belle knows a lot of different moves!", "Testing that action method is correct and p1 assigned to correct value")

   myTests().main()

.. activecode:: ee_inheritance_02
   :tags: Inheritance/inheritVarsAndMethods.rst, Inheritance/OverrideMethods.rst
   :practice: T
   :autograde: unittest
   :topics: Inheritance/OverrideMethods

   Modify the ``Grass_Pokemon`` subclass so that the attack strength for ``Grass_Pokemon`` instances does not change until they reach level 10. At level 10 and up, their attack strength should increase by the ``attack_boost`` amount when they are trained.

   To test, create an instance of the class with the name as ``"Bulby"``. Assign the instance to the variable ``p2``. Create another instance of the ``Grass_Pokemon`` class with the name set to ``"Pika"`` and assign that instance to the variable ``p3``. Then, use ``Grass_Pokemon`` methods to train the ``p3`` ``Grass_Pokemon`` instance until it reaches at least level 10.
   ~~~~
   class Pokemon(object):
       attack = 12
       defense = 10
       health = 15
       p_type = "Normal"

       def __init__(self, name, level = 5):
           self.name = name
           self.level = level

       def train(self):
           self.update()
           self.attack_up()
           self.defense_up()
           self.health_up()
           self.level = self.level + 1
           if self.level%self.evolve == 0:
               return self.level, "Evolved!"
           else:
               return self.level

       def attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack

       def defense_up(self):
           self.defense = self.defense + self.defense_boost
           return self.defense

       def health_up(self):
           self.health = self.health + self.health_boost
           return self.health

       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
           self.evolve = 10

       def __str__(self):
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

   class Grass_Pokemon(Pokemon):
       attack = 15
       defense = 14
       health = 12
       p_type = "Grass"

       def update(self):
           self.health_boost = 6
           self.attack_boost = 2
           self.defense_boost = 3
           self.evolve = 12

       def moves(self):
           self.p_moves = ["razor leaf", "synthesis", "petal dance"]


   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOneA(self):
         self.assertEqual(p2.__str__(), "Pokemon name: Bulby, Type: Grass, Level: 5", "Testing that p2 is assigned to correct value.")
      def testOneB(self):
         self.assertTrue(p3.attack_up() >= 17, "Testing that attack value is assigned to correct value at level 10.")

   myTests().main()

.. activecode:: ee_inheritance_05
   :tags: Inheritance/inheritVarsAndMethods.rst
   :autograde: unittest

   Along with the ``Pokemon`` parent class, we have also provided several subclasses. Write another method in the parent class that will be inherited by the subclasses. Call it ``opponent``. It should return which type of pokemon the current type is weak and strong against, as a tuple.

   - **Grass** is weak against *Fire* and strong against *Water*
   - **Ghost** is weak against *Dark* and strong against *Psychic*
   - **Fire** is weak against *Water* and strong against *Grass*
   - **Flying** is weak against *Electric* and strong against *Fighting*

   For example, if the ``p_type`` of the subclass is ``'Grass'``, ``.opponent()`` should return the tuple ``('Fire', 'Water')``
   ~~~~
   class Pokemon():
       attack = 12
       defense = 10
       health = 15
       p_type = "Normal"

       def __init__(self, name,level = 5):
           self.name = name
           self.level = level
           self.weak = "Normal"
           self.strong = "Normal"

       def train(self):
           self.update()
           self.attack_up()
           self.defense_up()
           self.health_up()
           self.level = self.level + 1
           if self.level%self.evolve == 0:
               return self.level, "Evolved!"
           else:
               return self.level

       def attack_up(self):
           self.attack = self.attack + self.attack_boost
           return self.attack

       def defense_up(self):
           self.defense = self.defense + self.defense_boost
           return self.defense

       def health_up(self):
           self.health = self.health + self.health_boost
           return self.health

       def update(self):
           self.health_boost = 5
           self.attack_boost = 3
           self.defense_boost = 2
           self.evolve = 10

       def __str__(self):
           self.update()
           return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)

   class Grass_Pokemon(Pokemon):
       attack = 15
       defense = 14
       health = 12
       p_type = "Grass"

       def update(self):
           self.health_boost = 6
           self.attack_boost = 2
           self.defense_boost = 3
           self.evolve = 12

   class Ghost_Pokemon(Pokemon):
       p_type = "Ghost"

       def update(self):
           self.health_boost = 3
           self.attack_boost = 4
           self.defense_boost = 3

   class Fire_Pokemon(Pokemon):
       p_type = "Fire"

   class Flying_Pokemon(Pokemon):
       p_type = "Flying"

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOneA(self):
         self.assertEqual(Grass_Pokemon("Buggy").opponent(), ("Fire", "Water"), "Testing that Grass weak and strong are assigned to correct values.")
      def testOneB(self):
         self.assertEqual(Fire_Pokemon("Buggy").opponent(), ("Water", "Grass"), "Testing that Fire weak and strong are assigned to correct values.")
      def testOneC(self):
         self.assertEqual(Ghost_Pokemon("Buggy").opponent(), ("Dark", "Psychic"), "Testing that Ghost weak and strong are assigned to correct values.")
      def testOneD(self):
         self.assertEqual(Flying_Pokemon("Buggy").opponent(), ("Electric", "Fighting"), "Testing that Flying weak and strong are assigned to correct values.")

   myTests().main()


Part 3: Debugging Exercises
----------------------------

.. activecode:: inheritance_assess_debug1
   :autograde: unittest

   **Debug this code!** The child class should call the parent constructor.
   ~~~~
   class Parent:
       def __init__(self, value):
           self.value = value

   class Child(Parent):
       def __init__(self, value, extra):
           # BUG: Not calling parent constructor!
           self.extra = extra

   c = Child(10, 20)
   print(c.value)  # Should work but causes error

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           c = Child(10, 20)
           self.assertEqual(c.value, 10)
           self.assertEqual(c.extra, 20)

   myTests().main()

.. activecode:: inheritance_assess_debug2
   :autograde: unittest

   **Debug!** The method should call the parent method, not replace it.
   ~~~~
   class Logger:
       def log(self, msg):
           print(f"[LOG] {msg}")

   class FileLogger(Logger):
       def log(self, msg):
           # BUG: Should call parent's log() first!
           print(f"[Saving to file...]")

   fl = FileLogger()
   fl.log("Test")  # Should print both messages

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           # Implementation check
           import inspect
           source = inspect.getsource(FileLogger.log)
           self.assertIn("super()", source, "Should call super().log()")

   myTests().main()

Part 4: Parson's Problems
--------------------------

.. parsonsprob:: inheritance_assess_parsons1
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to create a Vehicle class and Car subclass using super().
   -----
   class Vehicle:
   =====
       def __init__(self, make):
   =====
       def __init__(make): #distractor
   =====
           self.make = make
   =====
   class Car(Vehicle):
   =====
   class Car: #distractor
   =====
       def __init__(self, make, doors):
   =====
           super().__init__(make)
   =====
           Vehicle.__init__(self, make) #distractor
   =====
           self.doors = doors

.. parsonsprob:: inheritance_assess_parsons2
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to override a method while calling the parent version.
   -----
   class Animal:
   =====
       def speak(self):
   =====
           return "Some sound"
   =====
   class Dog(Animal):
   =====
       def speak(self):
   =====
           parent_sound = super().speak()
   =====
           parent_sound = Animal.speak() #distractor
   =====
           return parent_sound + " and Woof!"
   =====
           return "Woof!" #distractor