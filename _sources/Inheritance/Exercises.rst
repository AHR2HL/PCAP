..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

:skipreading:`True`

Exercises
=========

For exercises, you can expand the Tamagotchi game even further. Try these out.

Here's *all* the code we just saw for our new and improved game, with a few additions. You can run this and play the game again.

#.

    .. tabbed:: q1

        .. tab:: Question

           .. actex:: tamagotchi_exercises
              :nocanvas:

              #. Change the above code to allow you to adopt a Tiger pet (that you're about to create). HINT: look at the ``whichtype`` function, and think about what's happening in the code for that function.

              #. Now, modify the code to define a new class, ``Tiger``. The ``Tiger`` class should inherit from the ``Cat`` class, but its default meow count should be ``5``, not ``3``, and it should have an extra instance method, ``roar``, that prints out the string ``ROOOOOAR!``. 

              #. Next, modify the code so that when the ``hi`` method is called for the ``Tiger`` class, the ``roar`` method is called. HINT: You'll have to call one instance method inside another, and you'll have to redefine a method for the ``Tiger`` class. See the **overriding methods** section. 

              #. Now, modify the code to define another new class, ``Retriever``. This class should inherit from ``Lab``. It should be exactly like ``Lab``, except instead of printing just ``I found the tennis ball!`` when the ``fetch`` method is called, it should say ``I found the tennis ball! I can fetch anything!``.

              #. Add your own new pets and modifications as you like -- remember, to use them in the game, you'll also have to alter the ``whichtype`` function so they can be used in game play. Otherwise, you'll have different classes that may work just fine, but you won't see the effects in the game, since the code that actually makes the game play is found in the second half of the provided code (look for the ``while`` loop!).
              ~~~~
              from random import randrange

              class Pet():
                  boredom_decrement = 4
                  hunger_decrement = 6
                  boredom_threshold = 5
                  hunger_threshold = 10
                  sounds = ['Mrrp']

                  def __init__(self, name = "Kitty"):
                      self.name = name
                      self.hunger = randrange(self.hunger_threshold)
                      self.boredom = randrange(self.boredom_threshold)
                      self.sounds = self.sounds[:]  # copy the class attribute, so that when we make changes to it, we won't affect the other Pets in the class

                  def clock_tick(self):
                      self.boredom += 1
                      self.hunger += 1

                  def mood(self):
                      if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
                          return "happy"
                      elif self.hunger > self.hunger_threshold:
                          return "hungry"
                      else:
                          return "bored"

                  def __str__(self):
                      state = "     I'm " + self.name + ". "
                      state += " I feel " + self.mood() + ". "
                      # state += "Hunger %d Boredom %d Words %s" % (self.hunger, self.boredom, self.sounds)
                      return state

                  def hi(self):
                      print(self.sounds[randrange(len(self.sounds))])
                      self.reduce_boredom()

                  def teach(self, word):
                      self.sounds.append(word)
                      self.reduce_boredom()

                  def feed(self):
                      self.reduce_hunger()

                  def reduce_hunger(self):
                      self.hunger = max(0, self.hunger - self.hunger_decrement)

                  def reduce_boredom(self):
                      self.boredom = max(0, self.boredom - self.boredom_decrement)

              class Dog(Pet):
                  # in the Dog class, Dog pets should express their hunger and boredom differently than generic Pets
                  def mood(self):
                      if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
                          return "happy, arf! Happy"
                      elif self.hunger > self.hunger_threshold:
                          return "hungry already, arrrf"
                      else:
                          return "bored, so you should play with me"

              class Cat(Pet):
                  # in the Cat class, cats express their hunger and boredom a little differently, too. They also have an extra instance, variable meow_count.
                  def __init__(self, name="Fluffy", meow_count=3):
                      Pet.__init__(self, name)
                      self.meow_count = meow_count

                  def hi(self):
                      for i in range(self.meow_count):
                          print(self.sounds[randrange(len(self.sounds))])
                      self.reduce_boredom()

                  def mood(self):
                      if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
                          return "happy, I suppose"
                      elif self.hunger > self.hunger_threshold:
                          return "mmmm...hungry"
                      else:
                          return "a bit bored"

              class Lab(Dog):
                  def fetch(self):
                      return "I found the tennis ball!"

                  def hi(self):
                      print(self.sounds[randrange(len(self.sounds))] + self.fetch())

              class Poodle(Dog):
                  def dance(self):
                      return "Dancin' in circles like poodles do."

                  def hi(self):
                      print(self.dance())
                      Dog.hi(self)

              class Bird(Pet):
                  sounds = ["chirp"]
                  def __init__(self, name="Kitty", chirp_number=2):
                      Pet.__init__(self, name) # call the parent class's constructor
                      # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
                      self.chirp_number = chirp_number # now, also assign the new instance variable

                  def hi(self):
                      for i in range(self.chirp_number):
                          print(self.sounds[randrange(len(self.sounds))])
                      self.reduce_boredom()


              def whichone(petlist, name):
                  for pet in petlist:
                      if pet.name == name:
                          return pet
                  return None # no pet matched

              pet_types = {'dog': Dog, 'lab': Lab, 'poodle': Poodle, 'cat': Cat, 'bird': Bird}
              def whichtype(adopt_type="general pet"):
                  return pet_types.get(adopt_type.lower(), Pet)

              def play():
                  animals = []

                  option = ""
                  base_prompt = """
                      Quit
                      Adopt <petname_with_no_spaces> <adopt_type - choose dog, cat, lab, poodle, or another unknown pet type>
                      Greet <petname>
                      Teach <petname> <word>
                      Feed <petname>

                      Choice: """
                  feedback = ""
                  while True:
                      action = input(feedback + "\n" + base_prompt)
                      feedback = ""
                      words = action.split()
                      if len(words) > 0:
                          command = words[0]
                      else:
                          command = None
                      if command == "Quit":
                          print("Exiting...")
                          return
                      elif command == "Adopt" and len(words) > 1:
                          if whichone(animals, words[1]):
                              feedback += "You already have a pet with that name\n"
                          else:
                              # figure out which class it should be
                              if len(words) > 2:
                                  Cl = whichtype(words[2])
                              else:
                                  Cl = Pet
                              # Make an instance of that class and append it
                              animals.append(Cl(words[1]))
                      elif command == "Greet" and len(words) > 1:
                          pet = whichone(animals, words[1])
                          if not pet:
                              feedback += "I didn't recognize that pet name. Please try again.\n"
                              print()
                          else:
                              pet.hi()
                      elif command == "Teach" and len(words) > 2:
                          pet = whichone(animals, words[1])
                          if not pet:
                              feedback += "I didn't recognize that pet name. Please try again."
                          else:
                              pet.teach(words[2])
                      elif command == "Feed" and len(words) > 1:
                          pet = whichone(animals, words[1])
                          if not pet:
                              feedback += "I didn't recognize that pet name. Please try again."
                          else:
                              pet.feed()
                      else:
                          feedback+= "I didn't understand that. Please try again."

                      for pet in animals:
                          pet.clock_tick()
                          feedback += "\n" + pet.__str__()

              import sys
              sys.setExecutionLimit(60000)
              play()

.. activecode:: inheritance_ex_basic_1
   :autograde: unittest

   Create a class ``Vehicle`` with:
   - Instance variable ``wheels`` (set in __init__)
   - Method ``describe()`` that returns "A vehicle with {wheels} wheels"

   Create a class ``Car`` that inherits from ``Vehicle``.
   - Constructor should call parent's __init__ with wheels=4
   - Add method ``honk()`` that returns "Beep beep!"

   Create ``my_car = Car()``
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(my_car.wheels, 4)
           self.assertIn("4 wheels", my_car.describe())
           self.assertEqual(my_car.honk(), "Beep beep!")

   myTests().main()

.. activecode:: inheritance_ex_basic_2
   :autograde: unittest

   Create a class ``Animal`` with method ``speak()`` that returns "Some sound".

   Create a class ``Dog`` that inherits from ``Animal`` and overrides ``speak()`` to return "Woof!".

   Create a class ``Cat`` that inherits from ``Animal`` and overrides ``speak()`` to return "Meow!".

   Create ``dog = Dog()`` and ``cat = Cat()``.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(dog.speak(), "Woof!")
           self.assertEqual(cat.speak(), "Meow!")

   myTests().main()

.. activecode:: inheritance_ex_super_1
   :autograde: unittest

   Create a class ``Rectangle`` with:
   - __init__(width, height) that sets self.width and self.height
   - method area() that returns width * height

   Create a class ``Square`` that inherits from ``Rectangle``:
   - __init__(side) that uses super().__init__(side, side)

   Create ``sq = Square(5)``. It should have width=5, height=5, area()=25.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(sq.width, 5)
           self.assertEqual(sq.height, 5)
           self.assertEqual(sq.area(), 25)

   myTests().main()

.. activecode:: inheritance_ex_super_2
   :autograde: unittest

   Create a class ``Employee`` with:
   - __init__(name, salary)
   - method get_info() returns "{name} earns ${salary}"

   Create a class ``Manager`` that inherits from ``Employee``:
   - __init__(name, salary, department)
   - Uses super().__init__(name, salary)
   - Sets self.department
   - Overrides get_info() to call super().get_info() and add " in {department}"

   Create ``mgr = Manager("Alice", 80000, "Engineering")``.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(mgr.name, "Alice")
           self.assertEqual(mgr.salary, 80000)
           self.assertEqual(mgr.department, "Engineering")
           self.assertIn("Alice earns $80000", mgr.get_info())
           self.assertIn("Engineering", mgr.get_info())

   myTests().main()

.. activecode:: inheritance_ex_super_3
   :autograde: unittest

   Create a class ``BankAccount`` with:
   - __init__(balance=0)
   - method deposit(amount) that adds to balance

   Create a class ``SavingsAccount`` that inherits from ``BankAccount``:
   - __init__(balance=0, interest_rate=0.01)
   - Uses super().__init__(balance)
   - Adds method add_interest() that multiplies balance by (1 + interest_rate)

   Create ``savings = SavingsAccount(1000, 0.05)``, deposit 500, add interest.
   Balance should be 1575.0.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(savings.balance, 1000)
           savings.deposit(500)
           self.assertEqual(savings.balance, 1500)
           savings.add_interest()
           self.assertAlmostEqual(savings.balance, 1575.0, 2)

   myTests().main()

.. activecode:: inheritance_ex_isinstance_1
   :autograde: unittest

   Given:

   class Animal:
       pass

   class Dog(Animal):
       pass

   class Cat(Animal):
       pass

   dog = Dog()
   cat = Cat()

   Create variables:
   - is_dog_animal: True if dog is an instance of Animal
   - is_cat_dog: True if cat is an instance of Dog
   - is_dog_dog: True if dog is an instance of Dog

   Use isinstance().
   ~~~~
   class Animal:
       pass

   class Dog(Animal):
       pass

   class Cat(Animal):
       pass

   dog = Dog()
   cat = Cat()

   # Your code here:

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertTrue(is_dog_animal)
           self.assertFalse(is_cat_dog)
           self.assertTrue(is_dog_dog)

   myTests().main()

.. activecode:: inheritance_ex_issubclass_1
   :autograde: unittest

   Given the same Animal/Dog/Cat hierarchy, create variables:
   - dog_sub_animal: True if Dog is a subclass of Animal
   - cat_sub_dog: True if Cat is a subclass of Dog
   - animal_sub_animal: True if Animal is a subclass of itself

   Use issubclass().
   ~~~~
   class Animal:
       pass

   class Dog(Animal):
       pass

   class Cat(Animal):
       pass

   # Your code here:

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertTrue(dog_sub_animal)
           self.assertFalse(cat_sub_dog)
           self.assertTrue(animal_sub_animal)

   myTests().main()

.. activecode:: inheritance_ex_isinstance_2
   :autograde: unittest

   Create a function ``count_animals(objects)`` that:
   - Takes a list of objects
   - Returns how many are instances of Animal (including subclasses)

   Test with: animals_count = count_animals([Dog(), Cat(), Dog(), "not an animal", Animal()])
   Should return 4.
   ~~~~
   class Animal:
       pass

   class Dog(Animal):
       pass

   class Cat(Animal):
       pass

   def count_animals(objects):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           result = count_animals([Dog(), Cat(), Dog(), "text", Animal()])
           self.assertEqual(result, 4)

   myTests().main()

.. activecode:: inheritance_ex_multilevel_1
   :autograde: unittest

   Create a 3-level hierarchy:

   class Shape:
       def __init__(self, color):
           self.color = color

   class Polygon(Shape):
       def __init__(self, color, sides):
           super().__init__(color)
           self.sides = sides

   class Triangle(Polygon):
       def __init__(self, color, base, height):
           super().__init__(color, 3)
           self.base = base
           self.height = height

       def area(self):
           return 0.5 * self.base * self.height

   Create ``tri = Triangle("red", 10, 5)``. Should have color="red", sides=3, area=25.0.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(tri.color, "red")
           self.assertEqual(tri.sides, 3)
           self.assertEqual(tri.area(), 25.0)

   myTests().main()

.. activecode:: inheritance_ex_polymorphism_1
   :autograde: unittest

   Create classes:

   class Shape:
       def area(self):
           return 0

   class Circle(Shape):
       def __init__(self, radius):
           self.radius = radius
       def area(self):
           return 3.14159 * self.radius ** 2

   class Square(Shape):
       def __init__(self, side):
           self.side = side
       def area(self):
           return self.side ** 2

   Create a function ``total_area(shapes)`` that:
   - Takes a list of Shape objects
   - Returns the sum of all their areas

   Test: shapes = [Circle(5), Square(4), Circle(3)]
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           shapes = [Circle(5), Square(4), Circle(3)]
           result = total_area(shapes)
           self.assertAlmostEqual(result, 3.14159*25 + 16 + 3.14159*9, 2)

   myTests().main()

.. mchoice:: inheritance_ex_design_1
   :answer_a: Inheritance
   :answer_b: Composition
   :answer_c: Either works equally well
   :answer_d: Neither - use a single class
   :correct: b
   :feedback_a: Car HAS-A engine, not IS-A engine. Use composition.
   :feedback_b: Correct! A car HAS an engine (composition), not IS an engine.
   :feedback_c: Composition is clearly better here.
   :feedback_d: You need both classes.

   A ``Car`` needs to have an ``Engine``. Should ``Car`` inherit from ``Engine`` or contain an Engine instance?

.. mchoice:: inheritance_ex_design_2
   :answer_a: Inheritance
   :answer_b: Composition
   :answer_c: Either works equally well
   :answer_d: Neither - use a single class
   :correct: a
   :feedback_a: Correct! A Dog IS-A Animal. This is a clear inheritance relationship.
   :feedback_b: Composition doesn't make sense here - a dog doesn't HAVE an animal.
   :feedback_c: Inheritance is clearly better for "is-a" relationships.
   :feedback_d: You need the Animal parent class for shared behavior.

   A ``Dog`` is a type of ``Animal``. Should ``Dog`` inherit from ``Animal`` or contain an Animal instance?

Contributed Exercises
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    {% for q in questions: %}
        <div class='oneq full-width'>
            {{ q['htmlsrc']|safe }}
        </div>
    {% endfor %}
