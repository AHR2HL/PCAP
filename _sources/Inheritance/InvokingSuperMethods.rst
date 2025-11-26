..  Copyright (C)  Paul Resnick and Steve Oney.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".



Invoking the Parent Class's Method
===================================

**Critical PCAP Topic** (Section 4 - 34% of exam)

Sometimes you want to **extend** parent behavior, not **replace** it. You want the parent's code PLUS some extra code.

**Without super() - Code Duplication:**

.. code-block:: python

   class Pet:
       def __init__(self, name):
           self.name = name
           self.hunger = 5
           self.boredom = 3

   class Dog(Pet):
       def __init__(self, name, breed):
           # Must duplicate Pet's initialization! ❌
           self.name = name
           self.hunger = 5
           self.boredom = 3
           self.breed = breed  # Plus new stuff

**With super() - No Duplication:**

.. code-block:: python

   class Dog(Pet):
       def __init__(self, name, breed):
           super().__init__(name)  # Call parent! ✅
           self.breed = breed      # Then add new stuff

Much cleaner!

This technique is very often used with the ``__init__`` method for a subclass. Suppose that some extra instance variables are defined for the subclass. When you invoke the constructor, you pass all the regular parameters for the parent class, plus the extra ones for the subclass. The subclass' ``__init__`` method then stores the extra parameters in instance variables and calls the parent class'   ``__init__`` method to store the common parameters in instance variables and do any other initialization that it normally does.

Let's say we want to create a subclass of ``Pet``, called ``Bird``, and we want it to take an extra parameter, ``chirp_number``, with a default value of ``2``, and have an extra instance variable, ``self.chirp_number``. Then, we'll use this in the ``hi`` method to make more than one sound.

.. activecode:: super_methods_1
    :nocanvas:
    :include: inheritance_pet_class_copy

    class Bird(Pet):
        sounds = ["chirp"]
        def __init__(self, name="Kitty", chirp_number=2):
            super().__init__(name) # call the parent class's constructor
            self.chirp_number = chirp_number # now, also assign the new instance variable

        def hi(self):
            for i in range(self.chirp_number):
                print(self.sounds[randrange(len(self.sounds))])
            self.reduce_boredom()

    b1 = Bird('tweety', 5)
    b1.teach("Polly wanna cracker")
    b1.hi()

Common Patterns with super()
-----------------------------

**Pattern 1: Extend Method (Add Before)**

.. code-block:: python

   class Pet:
       def feed(self):
           self.hunger -= 5

   class Dog(Pet):
       def feed(self):
           print("Getting excited!")  # Before
           super().feed()              # Then parent code

**Pattern 2: Extend Method (Add After)**

.. code-block:: python

   class Dog(Pet):
       def feed(self):
           super().feed()              # Parent code first
           print("Arf! Thanks!")       # Then extra code

**Pattern 3: Extend and Modify**

.. code-block:: python

   class Dog(Pet):
       def feed(self):
           super().feed()              # Do parent behavior
           self.happiness += 2         # Plus extra state change

**Pattern 4: Extend __init__ (Most Common!)**

.. code-block:: python

   class Dog(Pet):
       def __init__(self, name, breed):
           super().__init__(name)      # Initialize parent
           self.breed = breed          # Add child attributes

Why super() Matters: A Cautionary Tale
---------------------------------------

**Without super() - Must duplicate everything:**

.. activecode:: inheritance_without_super

    from random import randrange

    class Pet:
        def __init__(self, name):
            self.name = name
            self.hunger = randrange(10)
            self.boredom = randrange(5)
            print(f"Pet initialized: {self.name}")

    class BadDog(Pet):
        """Dog that doesn't use super() - BAD!"""
        def __init__(self, name, breed):
            # Must duplicate all Pet initialization ❌
            self.name = name
            self.hunger = randrange(10)
            self.boredom = randrange(5)
            print(f"Pet initialized: {self.name}")  # Duplicated!

            self.breed = breed
            print(f"Dog initialized: {self.breed}")

    class GoodDog(Pet):
        """Dog that uses super() - GOOD!"""
        def __init__(self, name, breed):
            super().__init__(name)  # No duplication! ✅
            self.breed = breed
            print(f"Dog initialized: {self.breed}")

    print("=== Bad Dog (duplicated code) ===")
    bad = BadDog("Fido", "Poodle")

    print("\n=== Good Dog (using super) ===")
    good = GoodDog("Rover", "Labrador")

**Output:**
::

   === Bad Dog (duplicated code) ===
   Pet initialized: Fido
   Dog initialized: Poodle

   === Good Dog (using super) ===
   Pet initialized: Rover
   Dog initialized: Labrador

**Problems with BadDog:**
- ❌ Code duplication (violates DRY principle)
- ❌ If Pet.__init__ changes, BadDog breaks
- ❌ Must remember all parent initialization steps
- ❌ Error-prone and hard to maintain

**Benefits of GoodDog:**
- ✅ No duplication
- ✅ Automatic updates if parent changes
- ✅ Clear, maintainable code
- ✅ Professional Python style

**Check your understanding**

.. mchoice:: question_inheritance_4
   :answer_a: 7
   :answer_b: ["Mrrp"]
   :answer_c: ["chirp"]
   :answer_d: Error
   :feedback_a: This would print if the code was print(b2.chirp_number).
   :feedback_b: We set b2 to be Bird('Sunny', 7) above.  Bird is a subclass of Pet, which has ["Mrrp"] for sounds, but Bird has a different value for that class variable. The interpreter looks in the subclass first.
   :feedback_c: The interpeter finds the value in the class variable for the class Bird.
   :feedback_d: We ran set b2 to be Bird('Sunny', 7) above.  Bird has a value set for the attribute sounds.
   :correct: c

   What will the following code print (assuming we use the above definitions of ``Bird`` and ``Pet``)::

    b2 = Bird('Sunny', 7)
    print(b2.sounds)

.. mchoice:: question_inheritance_5
   :answer_a: Error when invoked
   :answer_b: The string "Arf! Thanks!" would not print out but d1 would still have its hunger reduced.
   :answer_c: The string "Arf! Thanks!" would still print out but d1 would not have its hunger reduced.
   :answer_d: Nothing would be different. It is the same as the current code.
   :feedback_a: Since we are no longer calling the parent method in the subclass method definition, the actions defined in the parent method feed will not happen, and only Arf! Thanks! will be printed.
   :feedback_b: Remember that the Python interpreter checks for the existence of feed in the Dog class and looks for feed in Pet only if it isn't found in Dog.
   :feedback_c: Since we are no longer calling the parent Pet class's method in the Dog subclass's method definition, the class definition will override the parent method.
   :feedback_d: Remember that the Python interpreter checks for the existence of feed in the Dog class and looks for feed in Pet only if it isn't found in Dog.
   :correct: c
   
   For the ``Dog`` class defined in the earlier activecode window, what would happen when ``d1.feed()`` is run if the ``super().feed()`` line was deleted?

.. mchoice:: question_inheritance_super_1
   :answer_a: To call the parent class's method
   :answer_b: To make the method run faster
   :answer_c: To make the code shorter
   :answer_d: To avoid using inheritance
   :correct: a
   :feedback_a: Correct! super() lets you call the parent class's version of a method
   :feedback_b: super() doesn't affect performance
   :feedback_c: While it may be shorter, that's not the main purpose
   :feedback_d: super() is used WITH inheritance, not to avoid it

   What is the purpose of super()?

.. mchoice:: question_inheritance_super_2
   :answer_a: super().__init__()
   :answer_b: super.__init__()
   :answer_c: super().__init__(self)
   :answer_d: super().init()
   :correct: a
   :feedback_a: Correct! super() is called with (), then you call the method
   :feedback_b: super itself needs to be called with ()
   :feedback_c: Don't pass self - super() handles that automatically
   :feedback_d: The method is __init__ with double underscores

   What's the correct syntax to call the parent's __init__ method using super()?

.. mchoice:: question_inheritance_super_3
   :answer_a: ParentClass.method(self)
   :answer_b: super().method()
   :answer_c: Both work, but super() is preferred
   :answer_d: Neither works
   :correct: c
   :feedback_a: This works but is less flexible
   :feedback_b: This is the preferred way
   :feedback_c: Correct! Both work, but super() is better for flexibility
   :feedback_d: Both actually work!

   Which is the best way to call a parent class method?

.. mchoice:: question_inheritance_super_4
   :answer_a: To replace parent behavior completely
   :answer_b: To extend parent behavior with additional code
   :answer_c: To prevent inheritance
   :answer_d: To make methods private
   :correct: b
   :feedback_a: If you want to replace completely, just override without calling super()
   :feedback_b: Correct! super() lets you keep parent behavior AND add to it
   :feedback_c: super() is used WITH inheritance
   :feedback_d: super() doesn't affect method visibility

   When should you use super() in a subclass method?