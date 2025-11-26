..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Best Practices
==============

.. index:: exception handling best practices

**✅ DO: Be Specific with Exceptions**

.. code-block:: python

   # ✅ GOOD: Catch specific exceptions
   try:
       data = int(input())
   except ValueError:
       print("Invalid number")

   # ❌ BAD: Catch all exceptions
   try:
       data = int(input())
   except:
       print("Something went wrong")

**✅ DO: Use else for Success Code**

.. code-block:: python

   # ✅ GOOD: Separate success code
   try:
       file = open("data.txt")
   except FileNotFoundError:
       print("File not found")
   else:
       process(file)
       file.close()

**✅ DO: Use finally for Cleanup**

.. code-block:: python

   # ✅ GOOD: Guaranteed cleanup
   resource = acquire_resource()
   try:
       use_resource(resource)
   finally:
       release_resource(resource)

**✅ DO: Create Custom Exception Hierarchies**

.. code-block:: python

   # ✅ GOOD: Organized hierarchy
   class AppError(Exception):
       pass

   class ValidationError(AppError):
       pass

   class DatabaseError(AppError):
       pass

---

**❌ DON'T: Catch and Ignore**

.. code-block:: python

   # ❌ BAD: Silently ignoring errors
   try:
       risky_operation()
   except Exception:
       pass  # What went wrong?

**❌ DON'T: Use Bare except**

.. code-block:: python

   # ❌ BAD: Catches EVERYTHING (even KeyboardInterrupt!)
   try:
       operation()
   except:
       handle_error()

**❌ DON'T: Use assert for Validation**

.. code-block:: python

   # ❌ BAD: Can be disabled
   def withdraw(amount):
       assert amount > 0

   # ✅ GOOD: Proper validation
   def withdraw(amount):
       if amount <= 0:
           raise ValueError("Amount must be positive")

---


Check Your Understanding
-------------------------

.. mchoice:: exceptions_bp_mc1
   :answer_a: try/except/else/finally
   :answer_b: try/except/finally/else
   :answer_c: try/finally/except/else
   :answer_d: try/else/except/finally
   :correct: a
   :feedback_a: Correct! The order is: try, except (one or more), else (optional), finally (optional)
   :feedback_b: The else clause must come before finally
   :feedback_c: except must come immediately after try, before finally
   :feedback_d: else can only appear if there's at least one except clause

   What is the correct order of exception handling clauses in Python?


.. mchoice:: exceptions_bp_mc2
   :answer_a: To catch all exceptions including KeyboardInterrupt
   :answer_b: To make code shorter and easier to read
   :answer_c: To handle any type of error that might occur
   :answer_d: You should never use bare except; always catch specific exceptions
   :correct: d
   :feedback_a: This is why bare except is BAD - it catches too much, including system exits
   :feedback_b: Shorter code isn't better if it hides errors and makes debugging harder
   :feedback_c: This seems reasonable but is bad practice - you can't handle different errors appropriately
   :feedback_d: Correct! Always catch specific exceptions so you know what went wrong and can handle it appropriately

   When should you use a bare ``except:`` clause (without specifying an exception type)?


.. mchoice:: exceptions_bp_mc3
   :answer_a: assert is for testing conditions that should never fail during development; raise exceptions for validation
   :answer_b: assert is faster than raising exceptions
   :answer_c: assert is for user input validation; exceptions are for programmer errors
   :answer_d: They are equivalent and interchangeable
   :correct: a
   :feedback_a: Correct! assert is for debugging (can be disabled with -O flag); exceptions are for runtime validation that should always run
   :feedback_b: Performance is not the reason to choose between them; it's about purpose and reliability
   :feedback_c: This is backwards! assert is for developer assumptions; exceptions are for runtime validation including user input
   :feedback_d: They are NOT equivalent - assert can be disabled, exceptions cannot

   What's the difference between using ``assert`` and raising an exception for validation?


.. mchoice:: exceptions_bp_mc4
   :answer_a: The else clause runs if an exception occurs; the finally clause runs if no exception occurs
   :answer_b: The else clause runs if no exception occurs; the finally clause always runs
   :answer_c: The else clause is required; the finally clause is optional
   :answer_d: They are the same thing - you can use either one
   :correct: b
   :feedback_a: This is backwards! else runs on success; finally always runs
   :feedback_b: Correct! Use else for code that should only run if no exception occurred; use finally for cleanup that must always happen
   :feedback_c: Both are optional; you don't need either one
   :feedback_d: They serve completely different purposes - else is conditional, finally is unconditional

   What is the difference between the ``else`` and ``finally`` clauses in exception handling?


.. mchoice:: exceptions_bp_mc5
   :answer_a: So you can catch all application errors with one except clause if needed
   :answer_b: To make the code longer and more complex
   :answer_c: Because Python requires all custom exceptions to inherit from a base class
   :answer_d: To avoid using the built-in Exception class
   :correct: a
   :feedback_a: Correct! A hierarchy lets you catch specific errors individually OR catch all related errors by catching the base class
   :feedback_b: The purpose is organization and flexibility, not complexity
   :feedback_c: Python doesn't require this - you can make unrelated exception classes
   :feedback_d: Your custom exceptions should still inherit from Exception (through your base class)

   Why should you create a custom exception hierarchy (like ``AppError`` as a base class for ``ValidationError`` and ``DatabaseError``)?

Key Takeaways
-------------

.. important::
   **Summary: Advanced Exception Handling**

   ✅ **assert Statement:**
      - Use for debugging and internal checks
      - Can be disabled with ``python -O``
      - Don't use for validation or production code
      - Raises ``AssertionError`` if condition is false

   ✅ **else Clause:**
      - Runs only if NO exception was raised in try
      - Separates success code from error handling
      - More Pythonic than using flags

   ✅ **finally Clause:**
      - ALWAYS executes, exception or not
      - Perfect for cleanup (files, connections, locks)
      - Runs even if return, break, or continue is used

   ✅ **Execution Order:**
      ``try`` → (``except`` OR ``else``) → ``finally``

   ✅ **Custom Exceptions:**
      - Inherit from ``Exception``
      - Create hierarchies for organization
      - Add custom attributes for context
      - Use descriptive names ending in "Error"

   ✅ **Exception Chaining:**
      - ``raise NewError() from original``
      - Preserves original exception as ``__cause__``
      - Better debugging and error tracing

   ✅ **Best Practices:**
      - Be specific with exception types
      - Don't catch and ignore errors
      - Avoid bare ``except:``
      - Use ``else`` and ``finally`` appropriately
      - Create custom exception hierarchies

---

What's Next?
------------

You now understand advanced exception handling! Next, you'll master **Advanced File I/O** — working with binary files, `bytearray`, `errno`, and standard streams.

**In Section 2: Advanced File I/O**, you'll learn:

- Binary vs text file modes
- The ``bytearray`` type for binary data
- Error codes with ``errno`` module
- Standard streams: ``stdin``, ``stdout``, ``stderr``
- ``readlines()`` vs ``readline()`` vs ``read()``
- Context managers and file handling
- Best practices for file operations

---
