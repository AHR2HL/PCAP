..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Section 7: Practice and Mastery
================================

.. index:: OOP practice, OOP assessment, mastery

Introduction
------------

**Congratulations!** You've completed all instructional sections on Advanced OOP. Now it's time to **test your mastery** and solidify your understanding.

This comprehensive assessment section includes:

- **Vocabulary Review** — test your understanding of OOP terminology
- **Conceptual Understanding** — verify you understand how OOP works
- **Parsons Problems** — arrange code blocks to create working OOP solutions
- **Coding Challenges** — build OOP systems from scratch (10 challenges)
- **Debugging Challenges** — find and fix broken OOP code (5 challenges)
- **Self-Assessment Checklist** — comprehensive skills inventory
- **Quick Reference Guide** — syntax and patterns at a glance

Take your time, work through each section, and use this as a learning opportunity. **Good luck!** 🚀

---

Part 1: Vocabulary Review
--------------------------

.. index:: OOP vocabulary, OOP terminology

Test your understanding of OOP terminology:

.. mchoice:: oop_practice_vocab_introspection
   :answer_a: Examining objects at runtime to discover their properties
   :answer_b: Writing comments in your code
   :answer_c: Debugging with a debugger
   :answer_d: Looking at the source code
   :correct: a
   :feedback_a: Correct! Introspection is the ability to examine objects, attributes, and types at runtime.
   :feedback_b: Comments are documentation, not introspection.
   :feedback_c: Debugging tools use introspection, but that's not the definition.
   :feedback_d: Introspection happens at runtime, not by reading source code.

   What is **introspection** in Python?

.. mchoice:: oop_practice_vocab_mro
   :answer_a: Multiple Return Objects
   :answer_b: Method Resolution Order
   :answer_c: Memory Reference Optimization
   :answer_d: Module Runtime Organization
   :correct: b
   :feedback_a: That's not what MRO stands for.
   :feedback_b: Correct! MRO is Method Resolution Order—the order Python searches for methods in inheritance.
   :feedback_c: MRO isn't about memory optimization.
   :feedback_d: MRO is about method resolution, not modules.

   What does **MRO** stand for?

.. mchoice:: oop_practice_vocab_diamond_problem
   :answer_a: A problem with diamond-shaped objects
   :answer_b: When two parent classes share a common ancestor
   :answer_c: A memory allocation issue
   :answer_d: When a class has four parent classes
   :correct: b
   :feedback_a: The "diamond" refers to the inheritance structure, not object shapes.
   :feedback_b: Correct! The diamond problem occurs when a class inherits from two classes that share a common ancestor.
   :feedback_c: It's about inheritance ambiguity, not memory.
   :feedback_d: It's about shared ancestors, not the number of parents.

   What is the **diamond problem**?

.. mchoice:: oop_practice_vocab_mixin
   :answer_a: A class that combines multiple inheritance
   :answer_b: A small class that adds specific functionality through inheritance
   :answer_c: A function that mixes data types
   :answer_d: A method that calls multiple other methods
   :correct: b
   :feedback_a: That's any class with multiple inheritance, not specifically a mixin.
   :feedback_b: Correct! A mixin is a class designed to add specific capabilities without being standalone.
   :feedback_c: Mixins are classes, not functions.
   :feedback_d: That's just a regular method, not a mixin.

   What is a **mixin** class?

.. mchoice:: oop_practice_vocab_polymorphism
   :answer_a: Having multiple forms or implementations
   :answer_b: A class with many methods
   :answer_c: Inheritance from multiple parents
   :answer_d: A function that returns different types
   :correct: a
   :feedback_a: Correct! Polymorphism means "many forms"—treating different types uniformly through a common interface.
   :feedback_b: Having many methods is unrelated to polymorphism.
   :feedback_c: That's multiple inheritance, not polymorphism.
   :feedback_d: Polymorphism is about objects/methods, not return types specifically.

   What is **polymorphism**?

.. mchoice:: oop_practice_vocab_duck_typing
   :answer_a: Type checking based on class names
   :answer_b: Using objects based on their behavior, not type
   :answer_c: A typing system for databases
   :answer_d: Static type checking
   :correct: b
   :feedback_a: Duck typing doesn't care about class names!
   :feedback_b: Correct! "If it walks like a duck and quacks like a duck, it's a duck"—behavior over type.
   :feedback_c: Duck typing is unrelated to databases.
   :feedback_d: Duck typing is dynamic, not static.

   What is **duck typing**?

.. mchoice:: oop_practice_vocab_abc
   :answer_a: Always Be Coding
   :answer_b: Abstract Base Class
   :answer_c: Automatic Base Constructor
   :answer_d: Advanced Boolean Check
   :correct: b
   :feedback_a: That's motivational, not technical!
   :feedback_b: Correct! ABC stands for Abstract Base Class—a class with abstract methods that subclasses must implement.
   :feedback_c: That's not a Python concept.
   :feedback_d: That's not what ABC means.

   What does **ABC** stand for in Python OOP?

.. mchoice:: oop_practice_vocab_protocol
   :answer_a: A network communication standard
   :answer_b: A type hint that defines expected methods without inheritance
   :answer_c: A class initialization protocol
   :answer_d: A method calling convention
   :correct: b
   :feedback_a: That's network protocols, not Python Protocols.
   :feedback_b: Correct! Protocols enable structural subtyping—defining expected behavior without inheritance.
   :feedback_c: That's not what Protocol means in Python.
   :feedback_d: Protocols are about type structure, not calling conventions.

   What is a **Protocol** in Python 3.8+?

.. mchoice:: advfunc_assess_mc_kwargs
   :answer_a: To capture all positional arguments
   :answer_b: To capture all keyword arguments as a dictionary
   :answer_c: To create a double pointer
   :answer_d: To multiply arguments
   :correct: b
   :feedback_a: That's *args
   :feedback_b: Correct! **kwargs collects extra keyword arguments into a dict
   :feedback_c: Python doesn't have pointers
   :feedback_d: ** in function definition is for keyword arguments

   What does ``**kwargs`` do in a function definition?

.. mchoice:: advfunc_assess_mc_nonlocal
   :answer_a: To modify global variables
   :answer_b: To modify variables in the enclosing scope
   :answer_c: To create new variables
   :answer_d: To delete variables
   :correct: b
   :feedback_a: That's global keyword
   :feedback_b: Correct! nonlocal allows modifying variables from outer (not global) scope
   :feedback_c: You don't need nonlocal to create variables
   :feedback_d: Use del to delete variables

   What is the ``nonlocal`` keyword used for?

.. mchoice:: advfunc_assess_mc9
   :answer_a: Functions can be passed as arguments
   :answer_b: Functions can be returned from other functions
   :answer_c: Functions can be assigned to variables
   :answer_d: All of the above
   :correct: d
   :feedback_a: True, but there's more!
   :feedback_b: True, but there's more!
   :feedback_c: True, but there's more!
   :feedback_d: Correct! First-class functions can be passed, returned, and assigned like any other value

   What does "first-class functions" mean in Python?

.. mchoice:: advfunc_assess_mc10
   :answer_a: from functools import reduce
   :answer_b: from itertools import reduce
   :answer_c: from operators import reduce
   :answer_d: reduce is built-in
   :correct: a
   :feedback_a: Correct! reduce was moved to functools in Python 3
   :feedback_b: reduce is in functools, not itertools
   :feedback_c: There's no operators module with reduce
   :feedback_d: reduce was built-in in Python 2, but moved to functools in Python 3

   How do you import ``reduce()`` in Python 3?

.. mchoice:: advfunc_assess_mc11
   :answer_a: A decorator that takes parameters
   :answer_b: A decorator inside another decorator
   :answer_c: Multiple decorators on one function
   :answer_d: A class-based decorator
   :correct: a
   :feedback_a: Correct! Decorator factories create decorators with custom parameters
   :feedback_b: That's nested decorators
   :feedback_c: That's decorator stacking
   :feedback_d: That's a different concept

   What is a decorator factory?

---

Part 2: Conceptual Understanding
---------------------------------

.. index:: OOP concepts, OOP behavior

Test your understanding of how OOP works:

.. mchoice:: oop_practice_concept_hasattr
   :answer_a: True
   :answer_b: False
   :answer_c: None
   :answer_d: AttributeError
   :correct: a
   :feedback_a: Correct! hasattr returns True if the object has the attribute (including inherited ones).
   :feedback_b: Inherited attributes are found by hasattr.
   :feedback_c: hasattr returns True or False, never None.
   :feedback_d: hasattr doesn't raise errors; it returns False instead.

   If a class inherits a method from its parent, what does ``hasattr(instance, 'method')`` return?

.. mchoice:: oop_practice_concept_isinstance_inherit
   :answer_a: True
   :answer_b: False
   :answer_c: TypeError
   :answer_d: Depends on the MRO
   :correct: a
   :feedback_a: Correct! isinstance returns True for the entire inheritance chain.
   :feedback_b: isinstance respects inheritance!
   :feedback_c: No error is raised.
   :feedback_d: isinstance always returns True for any class in the inheritance chain.

   If ``Dog`` inherits from ``Animal``, what does ``isinstance(dog_instance, Animal)`` return?

.. mchoice:: oop_practice_concept_is_vs_eq
   :answer_a: They are identical
   :answer_b: is checks identity, == checks equality
   :answer_c: is is faster, but they check the same thing
   :answer_d: == can't be used with objects
   :correct: b
   :feedback_a: They check fundamentally different things!
   :feedback_b: Correct! 'is' checks if objects are the same in memory, '==' checks if values are equal.
   :feedback_c: They check different things, not just speed difference.
   :feedback_d: == works with objects (can be customized with __eq__).

   What's the difference between ``is`` and ``==``?

.. mchoice:: oop_practice_concept_super_mi
   :answer_a: Calls the direct parent class
   :answer_b: Calls all parent classes
   :answer_c: Calls the next class in the MRO
   :answer_d: Calls the base class (object)
   :correct: c
   :feedback_a: In multiple inheritance, it doesn't always call the direct parent!
   :feedback_b: It calls one class, which then calls the next via its own super().
   :feedback_c: Correct! super() calls the next class in the MRO, enabling cooperative inheritance.
   :feedback_d: It calls the next in MRO, not necessarily the ultimate base.

   In multiple inheritance, what does ``super()`` call?

.. mchoice:: oop_practice_concept_class_vs_instance_dict
   :answer_a: They contain the same attributes
   :answer_b: Class __dict__ has methods, instance __dict__ has instance attributes
   :answer_c: Instance __dict__ has methods, class __dict__ has class attributes
   :answer_d: They are always identical
   :correct: b
   :feedback_a: They contain different things!
   :feedback_b: Correct! Class __dict__ has class attributes and methods; instance __dict__ has only instance attributes.
   :feedback_c: You have it backwards!
   :feedback_d: They contain very different things.

   What's in a class's ``__dict__`` vs an instance's ``__dict__``?

.. mchoice:: oop_practice_concept_mro_order
   :answer_a: Random order
   :answer_b: Alphabetical by class name
   :answer_c: Left-to-right, depth-first, no duplicates
   :answer_d: Right-to-left, breadth-first
   :correct: c
   :feedback_a: MRO is deterministic!
   :feedback_b: Class names don't affect MRO.
   :feedback_c: Correct! C3 linearization ensures left-to-right, depth-first with each class appearing once.
   :feedback_d: It's left-to-right, not right-to-left.

   What order does Python's MRO follow?

.. mchoice:: oop_practice_concept_abc_instantiate
   :answer_a: Yes, like any class
   :answer_b: No, it raises TypeError
   :answer_c: Yes, but only if it has no abstract methods
   :answer_d: Only if you use a special syntax
   :correct: b
   :feedback_a: Abstract classes can't be instantiated!
   :feedback_b: Correct! You can't instantiate an ABC with abstract methods—it raises TypeError.
   :feedback_c: If it has no abstract methods, it's not truly abstract anymore.
   :feedback_d: There's no special syntax to instantiate ABCs.

   Can you instantiate an Abstract Base Class?

.. mchoice:: oop_practice_concept_none_check
   :answer_a: if x == None:
   :answer_b: if x is None:
   :answer_c: if not x:
   :answer_d: All are equally valid
   :correct: b
   :feedback_a: While this works, 'is None' is the Pythonic way.
   :feedback_b: Correct! Always use 'is None' for checking None—it's faster and can't be overridden.
   :feedback_c: This checks truthiness, not specifically None (0, [], "" are also falsy).
   :feedback_d: They're not equivalent—each checks different things.

   What's the correct way to check if a variable is None?

---

Part 3: Parsons Problems
-------------------------

.. index:: parsons problems, code arrangement

Arrange the code blocks in the correct order to create working OOP solutions:

**Problem 1: Basic Introspection**

.. parsonsprob:: oop_practice_parsons_introspection
   :language: python
   :adaptive:
   :numbered: left

   Arrange the blocks to create a function that safely gets an attribute with a default value.
   -----
   def safe_get_attr(obj, attr_name, default=None):
   =====
       if hasattr(obj, attr_name):
   =====
       if obj.hasattr(attr_name): #distractor
   =====
           return getattr(obj, attr_name)
   =====
           return obj.attr_name #distractor
   =====
       return default
   =====
       return None #distractor

**Problem 2: Identity Check**

.. parsonsprob:: oop_practice_parsons_identity
   :language: python
   :adaptive:
   :numbered: left

   Arrange the blocks to create a function that checks if two objects are the same object (not just equal).
   -----
   def are_same_object(obj1, obj2):
   =====
       return obj1 is obj2
   =====
       return obj1 == obj2 #distractor
   =====
       return type(obj1) == type(obj2) #distractor

**Problem 3: Simple ABC**

.. parsonsprob:: oop_practice_parsons_abc
   :language: python
   :adaptive:
   :numbered: left

   Arrange the blocks to create an abstract base class with one abstract method.
   -----
   from abc import ABC, abstractmethod
   =====
   import abc #distractor
   =====
   class Shape(ABC):
   =====
   class Shape: #distractor
   =====
       @abstractmethod
   =====
       @abstract #distractor
   =====
       def area(self):
   =====
           pass
   =====
           raise NotImplementedError #distractor

**Problem 4: Multiple Inheritance with super()**

.. parsonsprob:: oop_practice_parsons_super
   :language: python
   :adaptive:
   :numbered: left

   Arrange the blocks to create a class with multiple inheritance using super() correctly.
   -----
   class A:
       def __init__(self):
           print("A")
           super().__init__()
   =====
   class B:
       def __init__(self):
           print("B")
           super().__init__()
   =====
   class C(A, B):
   =====
   class C(A, B): #distractor
       def __init__(self):
           A.__init__(self)
           B.__init__(self)
   =====
       def __init__(self):
           print("C")
           super().__init__()

**Problem 5: Polymorphic Function**

.. parsonsprob:: oop_practice_parsons_polymorphic
   :language: python
   :adaptive:
   :numbered: left

   Arrange the blocks to create a polymorphic function that works with any object having a draw() method.
   -----
   def render_all(shapes):
   =====
       results = []
   =====
       for shape in shapes:
   =====
           if hasattr(shape, 'draw'):
   =====
           if isinstance(shape, Shape): #distractor
   =====
               results.append(shape.draw())
   =====
       return results

---

Part 4: Coding Challenges
--------------------------

.. index:: OOP coding challenges

Build these OOP systems from scratch! Each challenge tests different aspects of OOP mastery.

**Challenge 1: Class Inspector**

.. activecode:: oop_practice_code_inspector
   :language: python
   :autograde: unittest

   Create a function ``inspect_hierarchy(cls)`` that returns a dictionary with:
   - 'name': class name
   - 'bases': list of parent class names
   - 'mro': list of all classes in MRO (as names)
   - 'methods': list of public method names (no underscores)

   Example::

       class Animal:
           def speak(self): pass

       class Dog(Animal):
           def bark(self): pass

       result = inspect_hierarchy(Dog)
       # result['name'] == 'Dog'
       # result['bases'] == ['Animal']
       # 'Animal' in result['mro']
       # 'bark' in result['methods']

   ~~~~
   def inspect_hierarchy(cls):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_name(self):
           class TestClass:
               pass
           result = inspect_hierarchy(TestClass)
           self.assertEqual(result['name'], 'TestClass')

       def test_bases(self):
           class Parent:
               pass
           class Child(Parent):
               pass
           result = inspect_hierarchy(Child)
           self.assertEqual(result['bases'], ['Parent'])

       def test_mro_includes_object(self):
           class TestClass:
               pass
           result = inspect_hierarchy(TestClass)
           self.assertIn('object', result['mro'])

       def test_methods(self):
           class TestClass:
               def public_method(self):
                   pass
               def _private_method(self):
                   pass
           result = inspect_hierarchy(TestClass)
           self.assertIn('public_method', result['methods'])
           self.assertNotIn('_private_method', result['methods'])

   myTests().main()


---

**Challenge 2: Safe Attribute Manager**

.. activecode:: oop_practice_code_attr_manager
   :language: python
   :autograde: unittest

   Create a class ``SafeAttributeManager`` that:
   - Stores attributes safely
   - Has ``set(name, value)`` method to set attributes
   - Has ``get(name, default=None)`` method to get attributes
   - Has ``has(name)`` method to check if attribute exists
   - Has ``delete(name)`` method to delete attributes

   Example::

       manager = SafeAttributeManager()
       manager.set('name', 'Alice')
       manager.get('name')  # 'Alice'
       manager.has('name')  # True
       manager.get('age', 25)  # 25 (default)
       manager.delete('name')
       manager.has('name')  # False

   ~~~~
   class SafeAttributeManager:
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_set_and_get(self):
           manager = SafeAttributeManager()
           manager.set('test', 'value')
           self.assertEqual(manager.get('test'), 'value')

       def test_get_with_default(self):
           manager = SafeAttributeManager()
           self.assertEqual(manager.get('missing', 'default'), 'default')

       def test_has(self):
           manager = SafeAttributeManager()
           manager.set('exists', True)
           self.assertTrue(manager.has('exists'))
           self.assertFalse(manager.has('missing'))

       def test_delete(self):
           manager = SafeAttributeManager()
           manager.set('temp', 'value')
           manager.delete('temp')
           self.assertFalse(manager.has('temp'))

   myTests().main()


---

**Challenge 3: Mixin Composition**

.. activecode:: oop_practice_code_mixins
   :language: python
   :autograde: unittest

   Create two mixins:
   - ``ReprMixin``: provides __repr__ that shows class name and attributes
   - ``EqualityMixin``: provides __eq__ that compares __dict__

   Then create a ``Point`` class that uses both mixins.

   Example::

       p1 = Point(3, 4)
       p2 = Point(3, 4)
       repr(p1)  # "Point(x=3, y=4)"
       p1 == p2  # True

   ~~~~
   class ReprMixin:
       # Your code here
       pass

   class EqualityMixin:
       # Your code here
       pass

   class Point(ReprMixin, EqualityMixin):
       def __init__(self, x, y):
           self.x = x
           self.y = y

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_repr(self):
           p = Point(3, 4)
           self.assertIn('Point', repr(p))
           self.assertIn('3', repr(p))
           self.assertIn('4', repr(p))

       def test_equality_true(self):
           p1 = Point(3, 4)
           p2 = Point(3, 4)
           self.assertEqual(p1, p2)

       def test_equality_false(self):
           p1 = Point(3, 4)
           p2 = Point(5, 6)
           self.assertNotEqual(p1, p2)

   myTests().main()


---

**Challenge 4: MRO Analyzer**

.. activecode:: oop_practice_code_mro_analyzer
   :language: python
   :autograde: unittest

   Create a function ``find_method_source(cls, method_name)`` that returns the class name where a method is defined in the MRO.

   Example::

       class A:
           def method(self): pass

       class B(A):
           pass

       class C(B):
           def method(self): pass

       find_method_source(B, 'method')  # 'A'
       find_method_source(C, 'method')  # 'C'
       find_method_source(A, 'missing')  # None

   ~~~~
   def find_method_source(cls, method_name):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_direct_method(self):
           class TestClass:
               def test_method(self):
                   pass
           result = find_method_source(TestClass, 'test_method')
           self.assertEqual(result, 'TestClass')

       def test_inherited_method(self):
           class Parent:
               def parent_method(self):
                   pass
           class Child(Parent):
               pass
           result = find_method_source(Child, 'parent_method')
           self.assertEqual(result, 'Parent')

       def test_overridden_method(self):
           class Parent:
               def method(self):
                   pass
           class Child(Parent):
               def method(self):
                   pass
           result = find_method_source(Child, 'method')
           self.assertEqual(result, 'Child')

       def test_missing_method(self):
           class TestClass:
               pass
           result = find_method_source(TestClass, 'missing')
           self.assertIsNone(result)

   myTests().main()


---

**Challenge 5: Identity vs Equality Checker**

.. activecode:: oop_practice_code_identity_equality
   :language: python
   :autograde: unittest

   Create a function ``compare_objects(obj1, obj2)`` that returns a dictionary:
   - 'identical': True if same object (is)
   - 'equal': True if equal values (==)
   - 'same_type': True if same type
   - 'same_id': True if same id

   Example::

       a = [1, 2, 3]
       b = [1, 2, 3]
       c = a

       compare_objects(a, b)
       # {'identical': False, 'equal': True, 'same_type': True, 'same_id': False}

       compare_objects(a, c)
       # {'identical': True, 'equal': True, 'same_type': True, 'same_id': True}

   ~~~~
   def compare_objects(obj1, obj2):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_identical_objects(self):
           a = [1, 2, 3]
           b = a
           result = compare_objects(a, b)
           self.assertTrue(result['identical'])
           self.assertTrue(result['equal'])
           self.assertTrue(result['same_type'])
           self.assertTrue(result['same_id'])

       def test_equal_not_identical(self):
           a = [1, 2, 3]
           b = [1, 2, 3]
           result = compare_objects(a, b)
           self.assertFalse(result['identical'])
           self.assertTrue(result['equal'])
           self.assertTrue(result['same_type'])
           self.assertFalse(result['same_id'])

       def test_different_objects(self):
           a = [1, 2, 3]
           b = "hello"
           result = compare_objects(a, b)
           self.assertFalse(result['identical'])
           self.assertFalse(result['equal'])
           self.assertFalse(result['same_type'])

   myTests().main()


---

**Challenge 6: Multiple Inheritance Diamond**

.. activecode:: oop_practice_code_diamond
   :language: python
   :autograde: unittest

   Create a diamond inheritance structure with cooperative __init__ methods.
   All classes should use super() and print their names when initialized.

   Structure::

          Base
          /  \
         A    B
          \  /
           C

   Example::

       c = C()
       # Prints: Base, A, B, C (in MRO order)

   ~~~~
   class Base:
       # Your code here
       pass

   class A(Base):
       # Your code here
       pass

   class B(Base):
       # Your code here
       pass

   class C(A, B):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_mro_order(self):
           mro_names = [cls.__name__ for cls in C.__mro__]
           self.assertEqual(mro_names[:4], ['C', 'A', 'B', 'Base'])

       def test_can_instantiate(self):
           c = C()
           self.assertIsInstance(c, C)
           self.assertIsInstance(c, A)
           self.assertIsInstance(c, B)
           self.assertIsInstance(c, Base)

   myTests().main()


---

**Challenge 7: Duck Typing Function**

.. activecode:: oop_practice_code_duck_typing
   :language: python
   :autograde: unittest

   Create a function ``process_drawable(obj)`` that:
   - If obj has a draw() method, call it and return the result
   - Otherwise, return "Object cannot be drawn"

   Don't use isinstance or type checking—use duck typing!

   Example::

       class Circle:
           def draw(self):
               return "Drawing circle"

       class Square:
           def draw(self):
               return "Drawing square"

       class Point:
           pass

       process_drawable(Circle())  # "Drawing circle"
       process_drawable(Point())   # "Object cannot be drawn"

   ~~~~
   def process_drawable(obj):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_with_draw_method(self):
           class Drawable:
               def draw(self):
                   return "Drawing"
           result = process_drawable(Drawable())
           self.assertEqual(result, "Drawing")

       def test_without_draw_method(self):
           class NotDrawable:
               pass
           result = process_drawable(NotDrawable())
           self.assertEqual(result, "Object cannot be drawn")

       def test_with_different_draw(self):
           class CustomDrawable:
               def draw(self):
                   return "Custom drawing"
           result = process_drawable(CustomDrawable())
           self.assertEqual(result, "Custom drawing")

   myTests().main()


---

**Challenge 8: Class Decorator**

.. activecode:: oop_practice_code_class_decorator
   :language: python
   :autograde: unittest

   Create a class decorator ``@countable`` that adds:
   - A class variable ``instance_count`` (starts at 0)
   - Increments ``instance_count`` in __init__
   - A class method ``get_count()`` that returns the count

   Example::

       @countable
       class MyClass:
           pass

       obj1 = MyClass()
       obj2 = MyClass()
       MyClass.get_count()  # 2

   ~~~~
   def countable(cls):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_count_increments(self):
           @countable
           class TestClass:
               pass

           obj1 = TestClass()
           self.assertEqual(TestClass.get_count(), 1)
           obj2 = TestClass()
           self.assertEqual(TestClass.get_count(), 2)

       def test_independent_counts(self):
           @countable
           class Class1:
               pass

           @countable
           class Class2:
               pass

           Class1()
           Class2()
           Class2()

           self.assertEqual(Class1.get_count(), 1)
           self.assertEqual(Class2.get_count(), 2)

   myTests().main()


---

**Challenge 9: Polymorphic Container**

.. activecode:: oop_practice_code_polymorphic_container
   :language: python
   :autograde: unittest

   Create a ``ProcessorContainer`` class that:
   - Stores a list of objects
   - Has ``add(obj)`` method to add objects
   - Has ``process_all()`` method that calls process() on each object and returns results
   - Uses duck typing (no type checking!)

   Example::

       class DataProcessor:
           def process(self):
               return "Processing data"

       class ImageProcessor:
           def process(self):
               return "Processing image"

       container = ProcessorContainer()
       container.add(DataProcessor())
       container.add(ImageProcessor())
       results = container.process_all()  # ["Processing data", "Processing image"]

   ~~~~
   class ProcessorContainer:
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_add_and_process(self):
           class TestProcessor:
               def process(self):
                   return "test"

           container = ProcessorContainer()
           container.add(TestProcessor())
           results = container.process_all()

           self.assertEqual(results, ["test"])

       def test_multiple_processors(self):
           class Proc1:
               def process(self):
                   return "one"

           class Proc2:
               def process(self):
                   return "two"

           container = ProcessorContainer()
           container.add(Proc1())
           container.add(Proc2())
           results = container.process_all()

           self.assertEqual(results, ["one", "two"])

       def test_empty_container(self):
           container = ProcessorContainer()
           results = container.process_all()
           self.assertEqual(results, [])

   myTests().main()


---

Part 5: Debugging Challenges
-----------------------------

.. index:: debugging OOP, OOP errors

Find and fix the bugs in these broken OOP systems!

**Debug 1: Broken Introspection**

.. activecode:: oop_practice_debug_introspection
   :language: python
   :autograde: unittest

   This code tries to safely access attributes but has bugs. Fix it!
   ~~~~
   def get_all_attributes(obj):
       """Get all public attributes of an object."""
       attributes = {}

       for attr in dir(obj):
           if not attr.startswith('_'):
               attributes[attr] = getattr(obj, attr)

       return attributes

   class Person:
       def __init__(self, name):
           self.name = name

       def greet(self):
           return f"Hello, {self.name}"

   person = Person("Alice")
   attrs = get_all_attributes(person)

   print(f"Attributes: {attrs}")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_returns_name_attribute(self):
           """Should return the name attribute"""
           person = Person("Alice")
           attrs = get_all_attributes(person)
           self.assertIn('name', attrs, "Should include 'name' attribute")
           self.assertEqual(attrs['name'], "Alice")

       def test_excludes_methods(self):
           """Should NOT include methods"""
           person = Person("Bob")
           attrs = get_all_attributes(person)
           self.assertNotIn('greet', attrs,
                          "Should NOT include 'greet' method")

       def test_only_returns_data_attributes(self):
           """Should only return non-callable attributes"""
           class Car:
               def __init__(self):
                   self.brand = "Toyota"
                   self.year = 2020

               def drive(self):
                   return "Driving"

               def stop(self):
                   return "Stopping"

           car = Car()
           attrs = get_all_attributes(car)

           self.assertIn('brand', attrs)
           self.assertIn('year', attrs)
           self.assertNotIn('drive', attrs)
           self.assertNotIn('stop', attrs)

       def test_excludes_private_attributes(self):
           """Should exclude attributes starting with underscore"""
           class Secret:
               def __init__(self):
                   self.public = "visible"
                   self._private = "hidden"
                   self.__very_private = "very hidden"

           obj = Secret()
           attrs = get_all_attributes(obj)

           self.assertIn('public', attrs)
           self.assertNotIn('_private', attrs)

       def test_returns_dict(self):
           """Should return a dictionary"""
           person = Person("Charlie")
           attrs = get_all_attributes(person)
           self.assertIsInstance(attrs, dict, "Should return a dictionary")

       def test_multiple_attributes(self):
           """Should handle multiple data attributes"""
           class Book:
               def __init__(self):
                   self.title = "Python 101"
                   self.author = "Alice"
                   self.pages = 300

               def read(self):
                   pass

           book = Book()
           attrs = get_all_attributes(book)

           self.assertEqual(len(attrs), 3,
                          "Should have exactly 3 attributes")
           self.assertEqual(attrs['title'], "Python 101")
           self.assertEqual(attrs['author'], "Alice")
           self.assertEqual(attrs['pages'], 300)

       def test_empty_object(self):
           """Should return empty dict for object with no public attributes"""
           class Empty:
               def method(self):
                   pass

           obj = Empty()
           attrs = get_all_attributes(obj)
           self.assertEqual(attrs, {},
                          "Should return empty dict for object with no attributes")

   myTests().main()


---

**Debug 2: Identity Confusion**

.. activecode:: oop_practice_debug_identity_2
   :language: python
   :autograde: unittest

   This code has identity vs equality confusion. Fix it!
   ~~~~
   def find_matching_user(users, target_name):
       """Find user with matching name."""
       for user in users:
           if user['name'] is target_name:
               return user
       return None

   users = [
       {'name': 'Alice', 'age': 30},
       {'name': 'Bob', 'age': 25},
       {'name': 'Charlie', 'age': 35}
   ]

   target = ''.join(['B', 'o', 'b'])

   result = find_matching_user(users, target)
   print(f"Found: {result}")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_finds_alice(self):
           """Test finding Alice"""
           users = [
               {'name': 'Alice', 'age': 30},
               {'name': 'Bob', 'age': 25}
           ]
           result = find_matching_user(users, 'Alice')
           self.assertIsNotNone(result, "Should find Alice")
           self.assertEqual(result['name'], 'Alice')

       def test_finds_bob_constructed_string(self):
           """Test finding Bob with constructed string (the bug!)"""
           users = [
               {'name': 'Alice', 'age': 30},
               {'name': 'Bob', 'age': 25}
           ]
           target = ''.join(['B', 'o', 'b'])
           result = find_matching_user(users, target)
           self.assertIsNotNone(result, "Should find Bob even with constructed string")
           self.assertEqual(result['name'], 'Bob')

       def test_finds_charlie_with_concatenation(self):
           """Test with another constructed string"""
           users = [
               {'name': 'Charlie', 'age': 35}
           ]
           target = 'Char' + 'lie'
           result = find_matching_user(users, target)
           self.assertIsNotNone(result, "Should find Charlie with concatenated string")
           self.assertEqual(result['name'], 'Charlie')

       def test_returns_none_when_not_found(self):
           """Test returns None when user not found"""
           users = [
               {'name': 'Alice', 'age': 30}
           ]
           result = find_matching_user(users, 'David')
           self.assertIsNone(result, "Should return None when user not found")

       def test_returns_first_match(self):
           """Test returns first matching user"""
           users = [
               {'name': 'Alice', 'age': 30},
               {'name': 'Alice', 'age': 25}
           ]
           result = find_matching_user(users, 'Alice')
           self.assertEqual(result['age'], 30,
                          "Should return first matching user")

       def test_with_empty_list(self):
           """Test with empty user list"""
           users = []
           result = find_matching_user(users, 'Anyone')
           self.assertIsNone(result, "Should return None for empty list")

       def test_case_sensitive(self):
           """Test that matching is case-sensitive"""
           users = [
               {'name': 'Bob', 'age': 25}
           ]
           result = find_matching_user(users, 'bob')
           self.assertIsNone(result,
                          "Should not find 'bob' when name is 'Bob' (case-sensitive)")

   myTests().main()


---

**Debug 3: Multiple Inheritance Gone Wrong**

.. activecode:: oop_practice_debug_mi
   :language: python
   :autograde: unittest

   This multiple inheritance doesn't work correctly. Fix it!
   ~~~~
   class A:
       def __init__(self):
           self.initialized_a = True
           print("A")

   class B:
       def __init__(self):
           self.initialized_b = True
           print("B")

   class C(A, B):
       def __init__(self):
           self.initialized_c = True
           print("C")
           A.__init__(self)
           B.__init__(self)

   c = C()
   print(f"MRO: {[cls.__name__ for cls in C.__mro__]}")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_all_classes_initialized(self):
           """All classes in hierarchy should be initialized"""
           c = C()
           self.assertTrue(hasattr(c, 'initialized_a'), "A should be initialized")
           self.assertTrue(hasattr(c, 'initialized_b'), "B should be initialized")
           self.assertTrue(hasattr(c, 'initialized_c'), "C should be initialized")

       def test_object_initialized(self):
           """object.__init__ should be called (via cooperative chain)"""
           # If super() is used correctly, no errors should occur
           try:
               c = C()
               success = True
           except:
               success = False
           self.assertTrue(success, "Should initialize without errors")

       def test_uses_super_in_a(self):
           """Class A should use super()"""
           source = self.getEditorText()
           a_class_code = source.split('class A:')[1].split('class B:')[0]
           self.assertIn('super()', a_class_code,
                        "Class A should call super().__init__()")

       def test_uses_super_in_b(self):
           """Class B should use super()"""
           source = self.getEditorText()
           b_class_code = source.split('class B:')[1].split('class C')[0]
           self.assertIn('super()', b_class_code,
                        "Class B should call super().__init__()")

       def test_uses_super_in_c(self):
           """Class C should use super()"""
           source = self.getEditorText()
           c_class_code = source.split('class C(A, B):')[1]
           self.assertIn('super()', c_class_code,
                        "Class C should call super().__init__()")

       def test_no_direct_parent_calls_in_c(self):
           """Class C should not call A.__init__ or B.__init__ directly"""
           source = self.getEditorText()
           c_class_code = source.split('class C(A, B):')[1]
           self.assertNotIn('A.__init__', c_class_code,
                          "Don't call A.__init__ directly, use super()")
           self.assertNotIn('B.__init__', c_class_code,
                          "Don't call B.__init__ directly, use super()")

       def test_mro_is_correct(self):
           """MRO should be C -> A -> B -> object"""
           mro_names = [cls.__name__ for cls in C.__mro__]
           self.assertEqual(mro_names[:4], ['C', 'A', 'B', 'object'],
                          "MRO should be C -> A -> B -> object")

       def test_multiple_instances(self):
           """Should work correctly for multiple instances"""
           c1 = C()
           c2 = C()

           self.assertTrue(hasattr(c1, 'initialized_a'))
           self.assertTrue(hasattr(c2, 'initialized_a'))
           self.assertTrue(c1 is not c2, "Should be different instances")

   myTests().main()


---

**Debug 4: Type Checking Bug**

.. activecode:: oop_practice_debug_type_checking
   :language: python
   :autograde: unittest

   This type checking code doesn't work with subclasses. Fix it!
   ~~~~
   class Animal:
       def __init__(self, name):
           self.name = name

   class Dog(Animal):
       def speak(self):
           return "Woof!"

   class Cat(Animal):
       def speak(self):
           return "Meow!"

   class Puppy(Dog):
       def speak(self):
           return "Yip!"

   def process_animal(animal):
       """Process animal based on type."""
       if type(animal) == Dog:
           return f"Dog {animal.name} says: {animal.speak()}"
       elif type(animal) == Cat:
           return f"Cat {animal.name} says: {animal.speak()}"
       else:
           return f"Unknown animal: {animal.name}"

   dog = Dog("Buddy")
   cat = Cat("Whiskers")
   puppy = Puppy("Max")

   print(process_animal(dog))
   print(process_animal(cat))
   print(process_animal(puppy))

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_processes_dog_correctly(self):
           """Should correctly identify and process Dog"""
           dog = Dog("Buddy")
           result = process_animal(dog)
           self.assertIn("Dog", result, "Should identify as Dog")
           self.assertIn("Woof!", result, "Should include dog's sound")

       def test_processes_cat_correctly(self):
           """Should correctly identify and process Cat"""
           cat = Cat("Whiskers")
           result = process_animal(cat)
           self.assertIn("Cat", result, "Should identify as Cat")
           self.assertIn("Meow!", result, "Should include cat's sound")

       def test_processes_puppy_as_dog(self):
           """Puppy (subclass of Dog) should be treated as Dog"""
           puppy = Puppy("Max")
           result = process_animal(puppy)
           self.assertIn("Dog", result, "Puppy should be identified as Dog (subclass)")
           self.assertNotIn("Unknown", result, "Should not be 'Unknown animal'")

       def test_uses_isinstance(self):
           """Code should use isinstance() not type()"""
           source = self.getEditorText()
           func_code = source.split('def process_animal(')[1].split('def ')[0]
           self.assertIn('isinstance', func_code,
                        "Should use isinstance() for type checking")

       def test_does_not_use_type_equality(self):
           """Should not use type() == comparison"""
           source = self.getEditorText()
           func_code = source.split('def process_animal(')[1].split('def ')[0]
           self.assertNotIn('type(', func_code,
                          "Should not use type() for type checking - use isinstance()")

       def test_kitten_subclass(self):
           """Should work with other subclasses too"""
           class Kitten(Cat):
               def speak(self):
                   return "Mew!"

           kitten = Kitten("Fluffy")
           result = process_animal(kitten)
           self.assertIn("Cat", result, "Kitten should be identified as Cat")
           self.assertNotIn("Unknown", result)

       def test_all_animals_have_names(self):
           """All processed animals should include their names"""
           dog = Dog("Rex")
           cat = Cat("Luna")
           puppy = Puppy("Spot")

           self.assertIn("Rex", process_animal(dog))
           self.assertIn("Luna", process_animal(cat))
           self.assertIn("Spot", process_animal(puppy))

       def test_inheritance_hierarchy(self):
           """Verify class hierarchy is correct"""
           puppy = Puppy("Test")
           self.assertIsInstance(puppy, Dog, "Puppy should be instance of Dog")
           self.assertIsInstance(puppy, Animal, "Puppy should be instance of Animal")

   myTests().main()


---

**Debug 5: Mixin Order Bug**

.. activecode:: oop_practice_debug_mixin_order
   :language: python
   :autograde: unittest

   The mixin order is wrong, causing method resolution issues. Fix it!
   ~~~~
   class Base:
       def process(self):
           return "Base"

   class LogMixin:
       def process(self):
           print("Logging...")
           return super().process()

   class CacheMixin:
       def process(self):
           print("Caching...")
           return super().process()

   class Processor(Base, LogMixin, CacheMixin):
       pass

   p = Processor()
   result = p.process()
   print(f"Result: {result}")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_result_is_base(self):
           """Process should eventually return 'Base'"""
           p = Processor()
           result = p.process()
           self.assertEqual(result, "Base", "Should return 'Base' from base class")

       def test_mro_has_mixins_before_base(self):
           """MRO should have mixins before Base class"""
           mro_names = [cls.__name__ for cls in Processor.__mro__]

           # Find positions
           processor_idx = mro_names.index('Processor')
           base_idx = mro_names.index('Base')

           # At least one mixin should be between Processor and Base
           mixins_before_base = any(
               'Mixin' in name and processor_idx < mro_names.index(name) < base_idx
               for name in mro_names
           )

           self.assertTrue(mixins_before_base,
                          "At least one mixin should appear before Base in MRO")

       def test_logmixin_before_base_in_mro(self):
           """LogMixin should come before Base in MRO"""
           mro_names = [cls.__name__ for cls in Processor.__mro__]
           log_idx = mro_names.index('LogMixin')
           base_idx = mro_names.index('Base')
           self.assertLess(log_idx, base_idx,
                          "LogMixin should come before Base in MRO")

       def test_cachemixin_before_base_in_mro(self):
           """CacheMixin should come before Base in MRO"""
           mro_names = [cls.__name__ for cls in Processor.__mro__]
           cache_idx = mro_names.index('CacheMixin')
           base_idx = mro_names.index('Base')
           self.assertLess(cache_idx, base_idx,
                          "CacheMixin should come before Base in MRO")

       def test_inheritance_order_in_code(self):
           """Processor class should list mixins before Base"""
           source = self.getEditorText()

           # Find the Processor class definition line
           for line in source.split('\n'):
               if 'class Processor(' in line and ')' in line:
                   # Extract the parents
                   parents_part = line.split('class Processor(')[1].split(')')[0]

                   # Check Base is not first
                   self.assertFalse(parents_part.strip().startswith('Base'),
                                  "Base should not be the first parent in Processor class")
                   break

       def test_all_classes_in_mro(self):
           """All classes should be present in MRO"""
           mro_names = [cls.__name__ for cls in Processor.__mro__]
           self.assertIn('Processor', mro_names)
           self.assertIn('Base', mro_names)
           self.assertIn('LogMixin', mro_names)
           self.assertIn('CacheMixin', mro_names)

       def test_processor_inherits_from_all(self):
           """Processor should inherit from all classes"""
           p = Processor()
           self.assertIsInstance(p, Base)
           self.assertIsInstance(p, LogMixin)
           self.assertIsInstance(p, CacheMixin)

       def test_cooperative_inheritance_works(self):
           """With call tracking, verify all methods are called"""
           # Create tracked versions
           call_order = []

           class TrackedBase:
               def process(self):
                   call_order.append('Base')
                   return "Base"

           class TrackedLogMixin:
               def process(self):
                   call_order.append('LogMixin')
                   return super().process()

           class TrackedCacheMixin:
               def process(self):
                   call_order.append('CacheMixin')
                   return super().process()

           # Correct order
           class GoodProcessor(TrackedLogMixin, TrackedCacheMixin, TrackedBase):
               pass

           # Bad order
           class BadProcessor(TrackedBase, TrackedLogMixin, TrackedCacheMixin):
               pass

           # Test good order
           call_order.clear()
           GoodProcessor().process()
           self.assertEqual(len(call_order), 3,
                          "With correct mixin order, all three methods should be called")

           # Test bad order
           call_order.clear()
           BadProcessor().process()
           self.assertEqual(len(call_order), 1,
                          "With wrong order (Base first), only Base is called")

   myTests().main()


---

.. parsonsprob:: advfunc_assess_parsons_pm_4
   :numbered: left
   :adaptive:

   Arrange the blocks to use reduce() to find the maximum value in a list.
   -----
   from functools import reduce
   =====
   from itertools import reduce #paired
   =====
   numbers = [3, 7, 2, 9, 1]
   =====
   max_val = reduce(lambda a, b: a if a > b else b, numbers)
   =====
   max_val = reduce(lambda a, b: max(a, b), numbers) #paired
   =====
   max_val = map(lambda a, b: a if a > b else b, numbers) #paired

.. parsonsprob:: advfunc_assess_parsons_pm_5
   :numbered: left
   :adaptive:

   Arrange the blocks to create a function that accepts any arguments with ``*args`` and ``**kwargs``.
   -----
   def flexible_func(*args, **kwargs):
   =====
   def flexible_func(args, kwargs): #paired
   =====
       print(f"Positional: {args}")
   =====
       print(f"Keyword: {kwargs}")
   =====
       return len(args) + len(kwargs)
   =====
       return args + kwargs #paired

---

Part 6: Self-Assessment Checklist
----------------------------------

.. index:: OOP skills checklist

Check off the skills you've mastered:

**Introspection**

.. code-block:: text

   □ I can use hasattr() to check for attributes
   □ I can use getattr() with default values
   □ I can use setattr() to dynamically set attributes
   □ I can use delattr() to remove attributes
   □ I can use dir() to list all attributes
   □ I understand the difference between __dict__ and vars()

**Type Checking**

.. code-block:: text

   □ I can use isinstance() for instance checking
   □ I can use issubclass() for class relationships
   □ I understand why isinstance() is better than type()
   □ I know when to use type checking vs duck typing
   □ I understand Python's EAFP philosophy

**Identity and Equality**

.. code-block:: text

   □ I understand the difference between is and ==
   □ I know when to use is (None checks, singletons)
   □ I know when to use == (value comparisons)
   □ I can use id() to check object identity
   □ I understand Python's object interning
   □ I can implement custom __eq__ methods

**Class Introspection**

.. code-block:: text

   □ I can examine __dict__ for class and instance attributes
   □ I can use __module__ to find where classes are defined
   □ I can use __bases__ to find direct parent classes
   □ I can use __mro__ to see method resolution order
   □ I understand the difference between class and instance attributes

**Multiple Inheritance**

.. code-block:: text

   □ I understand what multiple inheritance is
   □ I know about the diamond problem
   □ I understand how Python's MRO solves the diamond problem
   □ I can use super() correctly in multiple inheritance
   □ I know the C3 linearization algorithm rules
   □ I can create and use mixin classes
   □ I understand when to use multiple inheritance

**MRO and Polymorphism**

.. code-block:: text

   □ I understand C3 linearization properties
   □ I can predict MRO for complex hierarchies
   □ I understand different types of polymorphism
   □ I know the difference between duck typing and inheritance polymorphism
   □ I can create abstract base classes with @abstractmethod
   □ I understand Protocols for structural subtyping
   □ I can implement polymorphic design patterns

**Best Practices**

.. code-block:: text

   □ I use isinstance() instead of type()
   □ I use is None for None checks
   □ I use super() consistently in inheritance
   □ I name mixins with "Mixin" suffix
   □ I put mixins before base classes
   □ I avoid deep diamond hierarchies
   □ I prefer duck typing over excessive type checking

---

Part 7: Quick Reference Guide
------------------------------

.. index:: OOP reference, OOP cheat sheet

**Introspection Functions**

.. code-block:: python

   # Check if attribute exists
   hasattr(obj, 'attr')

   # Get attribute with default
   getattr(obj, 'attr', default)

   # Set attribute dynamically
   setattr(obj, 'attr', value)

   # Delete attribute
   delattr(obj, 'attr')

   # List all attributes
   dir(obj)

   # Get attribute dictionary
   vars(obj)  # Same as obj.__dict__

---

**Type Checking**

.. code-block:: python

   # Check instance type
   isinstance(obj, Class)
   isinstance(obj, (Class1, Class2))  # Multiple types

   # Check class relationship
   issubclass(SubClass, ParentClass)

   # Get object type
   type(obj)

   # Get object ID
   id(obj)

---

**Identity vs Equality**

.. code-block:: python

   # Identity (same object)
   obj1 is obj2
   obj1 is not obj2
   id(obj1) == id(obj2)

   # Equality (same value)
   obj1 == obj2
   obj1 != obj2

   # Always use 'is' for None
   if value is None:
       pass

   # Use == for value comparisons
   if value == expected:
       pass

---

**Class Introspection**

.. code-block:: python

   # Class attributes and methods
   MyClass.__dict__

   # Instance attributes only
   instance.__dict__

   # Module where class is defined
   MyClass.__module__

   # Direct parent classes
   MyClass.__bases__

   # Method Resolution Order
   MyClass.__mro__
   MyClass.mro()  # Same thing

---

**Multiple Inheritance**

.. code-block:: python

   # Basic multiple inheritance
   class Child(Parent1, Parent2):
       pass

   # Cooperative inheritance with super()
   class A:
       def __init__(self):
           super().__init__()

   class B(A):
       def __init__(self):
           super().__init__()

   class C(A):
       def __init__(self):
           super().__init__()

   class D(B, C):
       def __init__(self):
           super().__init__()

---

**Abstract Base Classes**

.. code-block:: python

   from abc import ABC, abstractmethod

   class Shape(ABC):
       @abstractmethod
       def area(self):
           pass

       @abstractmethod
       def perimeter(self):
           pass

   class Rectangle(Shape):
       def area(self):
           return self.width * self.height

       def perimeter(self):
           return 2 * (self.width + self.height)

---

**Protocols (Python 3.8+)**

.. code-block:: python

   from typing import Protocol

   class Drawable(Protocol):
       def draw(self) -> str:
           ...

   # No inheritance needed!
   class Circle:
       def draw(self) -> str:
           return "Drawing circle"

   def render(obj: Drawable):
       print(obj.draw())

---

**Mixin Pattern**

.. code-block:: python

   class LoggerMixin:
       def log(self, message):
           print(f"[LOG] {message}")

   class TimestampMixin:
       def get_timestamp(self):
           from datetime import datetime
           return datetime.now()

   # Mixins before base class
   class MyClass(LoggerMixin, TimestampMixin, BaseClass):
       pass

---

**Common Patterns**

.. code-block:: python

   # Safe attribute access
   value = getattr(obj, 'attr', default)

   # Check before access
   if hasattr(obj, 'method'):
       obj.method()

   # Duck typing (EAFP)
   try:
       obj.method()
   except AttributeError:
       handle_error()

   # Polymorphic function
   def process(obj):
       return obj.process()  # Works with any object having process()

---

**Decision Guides**

.. code-block:: text

   Use isinstance() over type():
   ✓ isinstance() respects inheritance
   ✓ isinstance() checks multiple types
   ✓ type() only checks exact type

   Use 'is' for:
   ✓ None checks (if x is None:)
   ✓ Singleton checks
   ✓ Identity verification

   Use '==' for:
   ✓ Value comparisons
   ✓ String comparisons
   ✓ Number comparisons
   ✓ Collection comparisons

   Use Duck Typing when:
   ✓ Working with flexible interfaces
   ✓ You don't control the types
   ✓ Maximum flexibility needed

   Use Type Checking when:
   ✓ Different behavior for different types
   ✓ Input validation required
   ✓ Clear contracts needed

---

Lesson Complete!
----------------

.. important::
   **🎉 Congratulations! You've completed Chapter 28: Advanced OOP Mastery!**

   You've mastered:
   - ✅ Object and class introspection (hasattr, getattr, dir, __dict__)
   - ✅ Type checking (isinstance, issubclass)
   - ✅ Identity vs equality (is vs ==, id())
   - ✅ Class structure inspection (__module__, __bases__, __mro__)
   - ✅ Multiple inheritance and the diamond problem
   - ✅ MRO and C3 linearization
   - ✅ Polymorphism (duck typing, inheritance, protocols)
   - ✅ Abstract base classes
   - ✅ Mixin pattern
   - ✅ Comprehensive self-assessment

   **You're now an Advanced OOP master!** 🚀

---

What's Next?
------------

With Chapter 28 complete, you're ready for the final chapter!

**Chapter 29: PCAP Power Topics**
- Part 1: Advanced Exception Handling
- Part 2: Advanced File I/O
- Part 3: String Methods Mastery

**Continue your PCAP journey!** These final topics will complete your PCAP preparation. 💪

---

.. note::
   **✅ Chapter 28: Advanced OOP Mastery - COMPLETE!**

   You've completed all 7 sections:
   1. Object Introspection
   2. Type Checking
   3. Identity vs Equality
   4. Class Introspection
   5. Multiple Inheritance and the Diamond Problem
   6. MRO and Advanced Polymorphism
   7. Practice and Mastery

   **Total Content:**
   - 60+ interactive examples
   - 5 Parsons problems
   - 10 coding challenges
   - 5 debugging challenges
   - 40+ MCQs
   - Comprehensive reference guide

   **PCAP OOP topics: COMPLETE!** 🎯