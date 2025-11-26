..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Overriding Methods
==================

If a method is defined for a class, and also defined for its parent class, the subclass' method is called and not the parent's. This follows from the rules for looking up attributes that you saw in the previous section.

We can use the same idea to understand overriding methods.

Let's return to our idea of making Cats, Dogs, and other pets generate a string for their "mood" differently.

Here's the original Pet class again.

.. activecode:: inheritance_pet_class
    :nocanvas:

    from random import randrange

    # Here's the original Pet class
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

Now let's make two subclasses, Dog and Cat. Dogs are always happy unless they are bored *and* hungry. Cats, on the other hand, are happy only if they are fed and if their boredom level is in a narrow range and, even then, only with probability 1/2.

.. activecode:: inheritance_override
    :nocanvas:
    :include: inheritance_pet_class

    class Cat(Pet):
        sounds = ['Meow']

        def mood(self):
            if self.hunger > self.hunger_threshold:
                return "hungry"
            if self.boredom <2:
                return "grumpy; leave me alone"
            elif self.boredom > self.boredom_threshold:
                return "bored"
            elif randrange(2) == 0:
                return "randomly annoyed"
            else:
                return "happy"

    class Dog(Pet):
        sounds = ['Woof', 'Ruff']

        def mood(self):
            if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
                return "bored and hungry"
            else:
                return "happy"

    c1 = Cat("Fluffy")
    d1 = Dog("Astro")

    c1.boredom = 1
    print(c1.mood())
    c1.boredom = 3
    for i in range(10):
        print(c1.mood())
    print(d1.mood())

Overriding the Constructor (__init__)
--------------------------------------

A common pattern is overriding ``__init__`` to customize initialization:

.. activecode:: inheritance_override_init

    from random import randrange

    class Pet:
        def __init__(self, name="Pet"):
            self.name = name
            self.hunger = 5

        def __str__(self):
            return f"{self.name} (hunger: {self.hunger})"

    class Dog(Pet):
        def __init__(self, name="Dog", breed="Mixed"):
            self.name = name
            self.hunger = 5
            self.breed = breed  # New attribute!

        def __str__(self):
            return f"{self.name} the {self.breed} (hunger: {self.hunger})"

    # Create instances
    generic_pet = Pet("Fluffy")
    print(generic_pet)

    dog = Dog("Fido", "Labrador")
    print(dog)

**Output:**
::

   Fluffy (hunger: 5)
   Fido the Labrador (hunger: 5)

**Notice:** Dog's ``__init__`` overrides Pet's ``__init__``, adding the breed attribute.

**Problem:** We had to duplicate the initialization code! (More on this in the next section with ``super()``.)

Common Patterns for Method Overriding
--------------------------------------

**Pattern 1: Specialized Behavior**

.. code-block:: python

   class Animal:
       def speak(self):
           return "Some sound"

   class Dog(Animal):
       def speak(self):  # Override with dog-specific sound
           return "Woof!"

**Pattern 2: Additional Validation**

.. code-block:: python

   class BankAccount:
       def withdraw(self, amount):
           self.balance -= amount

   class SavingsAccount(BankAccount):
       def withdraw(self, amount):  # Override with restriction
           if self.balance - amount < self.minimum_balance:
               return False
           self.balance -= amount
           return True

**Pattern 3: Extended Functionality**

.. code-block:: python

   class Employee:
       def calculate_pay(self):
           return self.hours * self.rate

   class Manager(Employee):
       def calculate_pay(self):  # Override to add bonus
           base_pay = self.hours * self.rate
           return base_pay + self.bonus

.. mchoice:: question_inheritance_override_1
   :answer_a: The parent class method is called
   :answer_b: The child class method is called
   :answer_c: Both methods are called
   :answer_d: An error occurs
   :correct: b
   :feedback_a: The child method overrides the parent method
   :feedback_b: Correct! When a method is defined in both parent and child, the child's version is used
   :feedback_c: Only the child method is called (unless you use super())
   :feedback_d: No error - overriding is normal and expected

   If both a parent class and child class define a method with the same name, which one is called on an instance of the child class?

.. mchoice:: question_inheritance_override_2
   :answer_a: mood()
   :answer_b: __init__()
   :answer_c: __str__()
   :answer_d: All of the above can be overridden
   :correct: d
   :feedback_a: Yes, but others can be too!
   :feedback_b: Yes, but others can be too!
   :feedback_c: Yes, but others can be too!
   :feedback_d: Correct! Any method can be overridden, including special methods

   Which methods can be overridden in a subclass?

.. mchoice:: question_inheritance_override_3
   :answer_a: To change the parent class
   :answer_b: To customize behavior in subclasses
   :answer_c: To make the code run faster
   :answer_d: To avoid using inheritance
   :correct: b
   :feedback_a: Overriding doesn't change the parent, it customizes the child
   :feedback_b: Correct! Overriding lets subclasses customize inherited behavior
   :feedback_c: Overriding doesn't affect performance
   :feedback_d: Overriding is used WITH inheritance, not to avoid it

   What is the main purpose of method overriding?