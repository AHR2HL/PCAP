..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Section 2: Creating Closures
=============================

.. index:: creating closures, nonlocal keyword, modifying closure variables

Introduction
------------

In Section 1, you learned **what** closures are and saw them in action. But there was a problem with our counter example — it could only **read** variables from the enclosing scope, not **modify** them.

In this section, you'll learn how to create powerful closures that can:

- Modify variables from the enclosing scope
- Capture multiple variables at once
- Maintain state across multiple calls
- Avoid common closure pitfalls

By the end, you'll be able to build practical closures like counters, accumulators, and state managers.

---

The Problem: Read-Only Variables
---------------------------------

.. index:: closure read-only, UnboundLocalError

Let's revisit the counter from Section 1 and try to make it work:

.. activecode:: closure_counter_broken
   :language: python
   :caption: Why This Doesn't Work

   def make_counter():
       count = 0

       def increment():
           count = count + 1  # ❌ This causes an error!
           return count

       return increment

   counter = make_counter()
   try:
       print(counter())
   except UnboundLocalError as e:
       print(f"Error: {e}")

**Output:**

::

   Error: local variable 'count' referenced before assignment

**What went wrong?**

When Python sees ``count = count + 1``, it thinks you're creating a **new local variable** called ``count`` inside ``increment()``. But then it tries to read ``count`` on the right side before it's been assigned, causing the error.

.. important::
   **Key Insight: The Assignment Problem**

   - **Reading** an enclosing variable: ✅ Works automatically
   - **Assigning** to an enclosing variable: ❌ Creates a new local variable instead

   Python assumes any variable you assign to is **local** unless you say otherwise.

---

Solution: The nonlocal Keyword
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``nonlocal`` keyword tells Python: "This variable isn't local — it belongs to the enclosing scope."

**Here's the fix:**

.. code-block:: python

   def make_counter():
       count = 0

       def increment():
           nonlocal count  # ✅ Tell Python to use enclosing 'count'
           count = count + 1
           return count

       return increment

   # Create and test the counter
   counter = make_counter()
   print(counter())  # 1
   print(counter())  # 2
   print(counter())  # 3

   # Create a second independent counter
   counter2 = make_counter()
   print(counter2())  # 1
   print(counter2())  # 2

**Output:**

::

   1
   2
   3
   1
   2

**What's happening:**

1. ``nonlocal count`` tells Python: "Don't create a new local ``count`` — use the one from the enclosing function"
2. Now ``count = count + 1`` modifies the outer function's variable
3. Each counter maintains its own separate ``count`` (closure)
4. State persists between calls

**Visual representation:**

::

   make_counter() called
   ├── Creates count = 0
   ├── Creates increment() function
   │   └── increment() remembers count from outer scope
   └── Returns increment

   counter() called → increment() runs
   ├── nonlocal count (use outer scope's count)
   ├── count = 0 + 1 → count = 1
   └── return 1

   counter() called again → increment() runs
   ├── nonlocal count (use outer scope's count)
   ├── count = 1 + 1 → count = 2
   └── return 2

**Practice: Understanding nonlocal**

.. mchoice:: nonlocal_understanding_q1
   :answer_a: It creates a new variable in the local scope
   :answer_b: It tells Python to use a variable from the enclosing function's scope
   :answer_c: It makes a variable global
   :answer_d: It prevents a variable from being modified
   :correct: b
   :feedback_a: No, that's what happens WITHOUT nonlocal. nonlocal does the opposite.
   :feedback_b: Correct! nonlocal tells Python: "This variable belongs to an enclosing scope, not local or global."
   :feedback_c: No, that's what 'global' does. nonlocal refers to enclosing function scope, not global scope.
   :feedback_d: No, nonlocal actually enables modification. Without it, you'd get an error trying to reassign.

   What does the ``nonlocal`` keyword do?

.. mchoice:: nonlocal_understanding_q2
   :answer_a: The inner function can read count but not modify it
   :answer_b: Python creates a new local variable count in the inner function
   :answer_c: UnboundLocalError: count referenced before assignment
   :answer_d: It works fine without nonlocal
   :correct: c
   :feedback_a: Close! Reading works, but the assignment causes an error.
   :feedback_b: Python tries to, but sees count on the right side of = first, causing confusion.
   :feedback_c: Correct! Python sees "count = ..." and assumes count is local, but then sees "count + 1" trying to read it first → error!
   :feedback_d: No, you'll get an UnboundLocalError. That's exactly why nonlocal is needed.

   What happens if you remove ``nonlocal count`` from the increment function?

   .. code-block:: python

      def make_counter():
          count = 0
          def increment():
              # nonlocal count removed!
              count = count + 1  # Error on this line
              return count
          return increment

.. mchoice:: nonlocal_vs_global_q1
   :answer_a: Code A
   :answer_b: Code B
   :answer_c: Code C
   :answer_d: They all do the same thing
   :correct: a
   :feedback_a: Correct! nonlocal refers to the enclosing function's scope (make_counter's count).
   :feedback_b: No, global refers to module-level variables, not enclosing function scope.
   :feedback_c: No, without a keyword, Python treats count = count + 1 as creating a local variable, causing an error.
   :feedback_d: No, they behave very differently. Only A works correctly for closures.

   Which code correctly implements a closure that modifies the enclosing scope?

   **Code A:**

   .. code-block:: python

      def make_counter():
          count = 0
          def increment():
              nonlocal count
              count += 1
              return count
          return increment

   **Code B:**

   .. code-block:: python

      def make_counter():
          count = 0
          def increment():
              global count
              count += 1
              return count
          return increment

   **Code C:**

   .. code-block:: python

      def make_counter():
          count = 0
          def increment():
              count += 1
              return count
          return increment

**Practice: Build a closure with nonlocal**

.. parsonsprob:: nonlocal_parsons_counter
   :language: python
   :adaptive:
   :numbered: left

   Arrange the code to create a working counter using nonlocal.
   -----
   def make_counter():
   =====
       count = 0
   =====
       def increment():
   =====
           nonlocal count
   =====
           count = count + 1
   =====
           count == 0 #distractor
   =====
           return count
   =====
       return increment
   =====
       return increment() #distractor

.. parsonsprob:: nonlocal_parsons_account
   :language: python
   :adaptive:
   :numbered: left

   Create a bank account with deposit and get_balance functions using closures.
   -----
   def create_account(initial_balance):
   =====
       balance = initial_balance
   =====
       def deposit(amount):
   =====
           nonlocal balance
   =====
           balance = balance + amount
   =====
           balance = amount #distractor
   =====
       def get_balance():
   =====
           return balance
   =====
           nonlocal deposit #distractor
   =====
       return deposit, get_balance
   =====
       return balance, deposit #distractor

**When to use nonlocal:**

.. list-table::
   :widths: 40 30 30
   :header-rows: 1

   * - Situation
     - Need nonlocal?
     - Example
   * - Reading outer variable
     - ❌ No
     - .. code-block:: python

          def outer():
              x = 10
              def inner():
                  print(x)  # Just reading
   * - Modifying mutable object
     - ❌ No
     - .. code-block:: python

          def outer():
              data = []
              def inner():
                  data.append(1)  # Modifying contents
   * - Reassigning outer variable
     - ✅ Yes!
     - .. code-block:: python

          def outer():
              x = 10
              def inner():
                  nonlocal x
                  x = 20  # Reassigning

**Try it yourself:**

To test this code on your own computer, save it as ``counter.py``:

.. code-block:: python

   def make_counter():
       count = 0

       def increment():
           nonlocal count
           count += 1
           return count

       return increment

   # Test it
   counter = make_counter()
   print(counter())  # 1
   print(counter())  # 2
   print(counter())  # 3

Run: ``python counter.py``

**Key Takeaways:**

.. important::

   1. **nonlocal** allows inner functions to modify variables in enclosing (non-global) scopes
   2. Without nonlocal, assignment creates a new local variable
   3. Reading outer variables doesn't need nonlocal
   4. Modifying mutable objects (lists, dicts) doesn't need nonlocal
   5. Reassigning outer variables DOES need nonlocal

---

What's Next?
------------

You now know how to create closures that can read **and** modify enclosing variables. But closures become truly powerful when you use them for **encapsulation** — hiding implementation details and protecting data.

**In Section 3: State and Encapsulation**, you'll learn:

- How closures provide data privacy and encapsulation
- Creating "private" variables that can't be accessed directly
- Building lightweight objects using closures
- Closures vs. classes for state management
- When encapsulation matters in real-world code

Ready to see how closures can replace classes? Let's go! 🚀

---

.. note::
   **✅ Section 2 Complete!**

   You've learned:
   - [✓] How to modify enclosing variables with ``nonlocal``
   - [✓] Capturing multiple variables in a single closure
   - [✓] Returning multiple functions that share state
   - [✓] Common pitfalls and how to avoid them
   - [✓] Practical closure patterns

   **Ready to master encapsulation?** → Continue to Section 3!