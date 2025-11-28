..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Checking Assumptions About Data Types
======================================

Unlike some other programming languages, the Python interpreter does not enforce restrictions about the data types of objects that can be bound to particular variables. For example, in Java, before assigning a value to a variable, the program would include a declaration of what type of value (integer, float, Boolean, etc.) that the variable is allowed to hold. The variable ``x`` in a Python program can be bound to an integer at one point and to a list at some other point in the program execution.

That flexibility makes it easier to get started with programming in Python. Sometimes, however, type checking could alert us that something has gone wrong in our program execution. If we are assuming at that ``x`` is a list, but it's actually an integer, then at some point later in the program execution, there will probably be an error. We can add ``assert`` statements that will cause an error to be flagged sooner rather than later, which might make it a lot easier to debug.

.. admonition:: 💡 Why Type Checking Matters

   **Dynamic typing is powerful but dangerous.** Python won't stop you from writing:

   ::

      total = 0
      # ... 100 lines later ...
      total = "Error: calculation failed"
      # ... 50 lines later ...
      result = total + 10  # 💥 TypeError!

   The error appears far from where the problem started. Type assertions catch these issues **immediately**, making debugging exponentially easier.

Testing Numeric Type Assumptions
---------------------------------

In the code below, we explicitly state some natural assumptions about how truncated division might work in Python. It turns out that the second assumption is wrong: ``9.0//5`` produces ``2.0``, a floating point value!

.. activecode:: ac19_1b_1

    assert type(9//5) == int
    assert type(9.0//5) == int

.. important:: Surprising Type Behavior

   **Python's type rules aren't always intuitive:**

   * ``9 // 5`` → ``1`` (int)
   * ``9.0 // 5`` → ``2.0`` (float) ← **Surprise!**
   * ``9 / 5`` → ``1.8`` (always float in Python 3)

   **The rule:** If *any* operand is a float, the result is a float—even for ``//`` (floor division).

   This is why type assertions are valuable: they catch assumptions that seem obvious but are actually wrong.

Testing Collection Type Uniformity
-----------------------------------

In the code below, ``lst`` is bound to a list object. In Python, not all the elements of a list have to be of the same type. We can check that they all have the same type and get an error if they are not. Notice that with ``lst2``, one of the assertions fails.

.. activecode:: ac19_1b_2

    lst = ['a', 'b', 'c']

    first_type = type(lst[0])
    for item in lst:
        assert type(item) == first_type

    lst2 = ['a', 'b', 'c', 17]
    first_type = type(lst2[0])
    for item in lst2:
        assert type(item) == first_type

.. note:: When to Check List Uniformity

   **Check element types when:**

   * Processing data from external sources (files, APIs, user input)
   * Performing mathematical operations on list elements
   * Before passing lists to functions that expect uniform types

   **Example:** If you're calculating an average, you need all numbers:

   ::

      def average(numbers):
          assert all(type(n) in [int, float] for n in numbers), "All elements must be numeric"
          return sum(numbers) / len(numbers)

Common Type Checking Patterns
------------------------------

.. admonition:: 🛠️ Practical Type Assertion Patterns

   **Pattern 1: Check function parameters**

   ::

      def calculate_discount(price, discount_rate):
          assert type(price) in [int, float], "Price must be numeric"
          assert type(discount_rate) == float, "Discount rate must be float"
          assert 0 <= discount_rate <= 1, "Discount rate must be between 0 and 1"
          return price * (1 - discount_rate)

   **Pattern 2: Validate data structure types**

   ::

      def process_records(records):
          assert type(records) == list, "Records must be a list"
          assert all(type(r) == dict for r in records), "Each record must be a dict"

   **Pattern 3: Check return values**

   ::

      result = some_function()
      assert type(result) == dict, "Expected function to return dictionary"

Type Checking vs. Type Hints
-----------------------------

.. important:: Modern Python: Type Hints

   Python 3.5+ introduced **type hints** as an alternative approach:

   ::

      def greet(name: str) -> str:
          return f"Hello, {name}"

   **Type hints vs. assertions:**

   =============================  ================================  =============================
   Feature                        Type Hints                        Assert Statements
   =============================  ================================  =============================
   Enforcement                    Not enforced by Python            Enforced at runtime
   Performance                    No runtime cost                   Small runtime cost
   Tools                          IDE autocomplete, mypy checker    Immediate error on failure
   When to use                    Development/documentation         Critical runtime checks
   =============================  ================================  =============================

   **Best practice:** Use type hints for documentation + mypy, use assertions for critical runtime validation.

When NOT to Use Type Assertions
--------------------------------

.. warning:: Avoid Assertion Overuse

   **Don't use assertions for:**

   1. **Validating user input** (use proper validation)

      ::

         # ❌ Bad
         age = int(input("Enter age: "))
         assert age > 0

         # ✅ Good
         age = int(input("Enter age: "))
         if age <= 0:
             raise ValueError("Age must be positive")

   2. **Program logic that should always run**

      Assertions can be disabled with ``python -O`` (optimize mode), so critical checks shouldn't rely on them.

   3. **Every single variable** (creates noise)

      Focus on **critical assumptions** and **external data**, not obvious cases.

**Check Your Understanding**

.. mchoice:: tc_types_1
   :answer_a: int
   :answer_b: float
   :answer_c: str
   :answer_d: It will cause an error
   :correct: b
   :feedback_a: Remember: if any operand is a float, the result is a float.
   :feedback_b: Correct! Even though both inputs are floats and the result is a whole number, Python returns a float.
   :feedback_c: Division never returns a string.
   :feedback_d: This operation is valid in Python.

   What type does ``10.0 // 3.0`` return?

.. mchoice:: tc_types_2
   :answer_a: To make the program run faster
   :answer_b: To catch type-related bugs early before they cause problems elsewhere
   :answer_c: To convert variables to the correct type
   :answer_d: To document what types are expected
   :correct: b
   :feedback_a: Type assertions add a small performance cost, not a benefit.
   :feedback_b: Correct! Assertions fail immediately when type assumptions are violated, making debugging easier.
   :feedback_c: Assertions check types but don't convert them.
   :feedback_d: While they do document expectations, this isn't their primary purpose. Type hints are better for documentation.

   What is the main purpose of using ``assert type(x) == int`` in your code?