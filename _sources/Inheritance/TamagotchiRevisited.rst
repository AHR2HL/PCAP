..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Tamagotchi Revisited
====================

**Synthesis Project: Applying Inheritance**

This project demonstrates how inheritance simplifies the messy if/elif code from the chapter introduction. You'll see:

* ✅ Multiple pet types with shared behavior
* ✅ Method overriding for unique behaviors
* ✅ Using super() to extend parent methods
* ✅ Multi-level inheritance (Lab and Poodle from Dog)
* ✅ Polymorphism (treating all pets uniformly)

**Compare this elegant solution to the if/elif version from the introduction!**

Using what we know about class inheritance, we can make a new version of the Tamagotchi game, where you can adopt different types of pets that are slightly different from one another.

Understanding the Code Structure
---------------------------------

**Class Hierarchy:**
::

            Pet (base class)
           /  |  \
          /   |   \
       Cat  Dog  Bird
            / \
           /   \
        Lab   Poodle

**What Each Class Adds:**

* **Pet** - Base functionality (hunger, boredom, basic methods)
* **Cat** - Overrides mood() for cat personality
* **Dog** - Overrides mood() + extends feed() with "Arf! Thanks!"
* **Bird** - Overrides __init__ to add chirp_number, overrides hi()
* **Lab** - Adds fetch() method, overrides hi()
* **Poodle** - Adds dance() method, overrides hi()

**Key Design Patterns:**

1. **Factory pattern:** ``whichtype()`` creates instances based on string
2. **Polymorphism:** All pets in one list, same interface
3. **Extension:** Lab and Poodle extend Dog without modifying it

And now we can play the Tamagotchi game with some small changes, such that we can adopt different types of pets.

.. activecode:: tamagotchi_revisited
    :nocanvas:

    import sys
    sys.setExecutionLimit(60000)
    from random import randrange

    class Pet(object):
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
            self.update_boredom()

        def teach(self, word):
            self.sounds.append(word)
            self.update_boredom()

        def feed(self):
            self.update_hunger()

        def update_hunger(self):
            self.hunger = max(0, self.hunger - self.hunger_decrement)

        def update_boredom(self):
            self.boredom = max(0, self.boredom - self.boredom_decrement)

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

        def feed(self):
            super().feed()
            print("Arf! Thanks!")

    class Bird(Pet):
        sounds = ["chirp"]
        def __init__(self, name="Kitty", chirp_number=2):
            super().__init__(name) # call the parent class's constructor
            # basically, call the SUPER -- the parent version -- of the constructor, with all the parameters that it needs.
            self.chirp_number = chirp_number # now, also assign the new instance variable

        def hi(self):
            for i in range(self.chirp_number):
                print(self.sounds[randrange(len(self.sounds))])
            self.update_boredom()

    class Lab(Dog):
        def fetch(self):
            return "I found the tennis ball!"

        def hi(self):
            print(self.fetch())
            print(self.sounds[randrange(len(self.sounds))])

    class Poodle(Dog):
        def dance(self):
            return "Dancin' in circles like poodles do."

        def hi(self):
            print(self.dance())
            Dog.hi(self)

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
            Adopt <petname_with_no_spaces> <pet_type - choose dog, cat, lab, poodle, bird, or another unknown pet type>
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

    play()

Reflection Questions
--------------------

.. mchoice:: tamagotchi_revisited_mc1
   :answer_a: Less code duplication, clearer structure
   :answer_b: Faster execution
   :answer_c: Uses less memory
   :answer_d: Easier to debug
   :correct: a
   :feedback_a: Correct! Inheritance eliminates if/elif dispatching and puts unique behavior in subclasses
   :feedback_b: Performance is similar
   :feedback_c: Memory usage is similar
   :feedback_d: Debugging complexity is about the same

   What's the main advantage of using inheritance instead of if/elif dispatching (from the intro)?

.. mchoice:: tamagotchi_revisited_mc2
   :answer_a: So Cat can use it
   :answer_b: So all pets can use hi()
   :answer_c: To override Bird's hi()
   :answer_d: To prevent errors
   :correct: b
   :feedback_a: Cat doesn't override hi(), so it uses Pet's version
   :feedback_b: Correct! Pet.hi() is inherited by all subclasses that don't override it
   :feedback_c: Bird overrides hi(), so it doesn't use Pet's version
   :feedback_d: That's not the main purpose

   Why is ``hi()`` defined in the ``Pet`` class instead of in each subclass?

.. mchoice:: tamagotchi_revisited_mc3
   :answer_a: Lab.hi() only
   :answer_b: Dog.hi() only
   :answer_c: Both Lab.hi() and Dog.hi()
   :answer_d: Pet.hi()
   :correct: a
   :feedback_a: Correct! Python finds hi() in Lab first (MRO: Lab → Dog → Pet)
   :feedback_b: Lab overrides Dog's hi(), so Dog's version isn't used
   :feedback_c: Only one hi() is called (the first found in MRO)
   :feedback_d: Lab overrides it, so Pet's version isn't reached

   When you call ``lab_instance.hi()``, which method is invoked?