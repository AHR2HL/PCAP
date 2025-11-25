..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Creating Packages
=================

.. index:: packages, __init__.py, __pycache__, modules vs packages

In Chapter 4, you learned how to create and import modules—single Python files that contain related code. Now you'll learn how to organize multiple related modules into **packages**, which are the building blocks of professional Python projects.

What's the Difference? Modules vs. Packages
--------------------------------------------

Let's clarify the terminology:

.. list-table:: Modules vs. Packages
   :header-rows: 0
   :widths: 20 40 40

   * - **Type**
     - **What It Is**
     - **Example**
   * - **Module**
     - A single ``.py`` file
     - ``math.py``, ``myutils.py``
   * - **Package**
     - A directory containing modules (and an ``__init__.py`` file)
     - ``mypackage/`` (directory with modules inside)

**Think of it this way:**
- A **module** is like a single document
- A **package** is like a folder that organizes multiple documents

.. activecode:: modules_vs_packages_demo_2
   :nocodelens:

   # ✅ Modules that work in browser Python:
   import math        # math is a single module
   import random      # random is a single module

   print("Single Modules:")
   print(f"  math.pi = {math.pi}")
   print(f"  random.randint(1, 10) = {random.randint(1, 10)}")
   print()

   # Note: Some packages aren't available in browser Python
   # Here's what package imports WOULD look like:

   print("Package Structure Examples:")
   print("  (These work in regular Python, not browser)")
   print()

   print("📦 os (package)")
   print("  import os.path  # os is package, path is module inside")
   print("  Example: os.path.join('folder', 'file.txt')")
   print()

   print("📦 email (package)")
   print("  import email.mime.text  # nested package structure")
   print("  Example: email.mime.text.MIMEText('Hello')")
   print()

   print("📦 xml (package)")
   print("  import xml.etree.ElementTree  # deeply nested")
   print("  Example: xml.etree.ElementTree.parse('data.xml')")
   print()

   print("="*50)
   print("Key Difference:")
   print("  Module: Single file (math.py)")
   print("  Package: Folder with __init__.py + multiple modules")

**Visual Example:**

::

   Python Installation
   ├── math.py              ← Single module (import math)
   ├── random.py            ← Single module (import random)
   └── os/                  ← Package (import os.path)
       ├── __init__.py
       ├── path.py          ← Module inside package
       └── environ.py

Why Use Packages?
-----------------

As projects grow, organizing code into packages becomes essential:

* **Organization** — Group related modules together logically
* **Namespace management** — Avoid naming conflicts between modules
* **Reusability** — Share organized code across projects
* **Professional structure** — Industry-standard project layout

.. note::

   **Real-world example:**

   Django, one of Python's most popular web frameworks, is organized into packages:

   - ``django.db`` — Database functionality
   - ``django.http`` — HTTP request/response handling
   - ``django.utils`` — Utility functions

   Each package contains multiple related modules.

Package Structure Basics
-------------------------

A package is simply a directory that contains:

1. **An ``__init__.py`` file** (can be empty)
2. **One or more Python modules** (``.py`` files)

Here's a simple package structure:

.. code-block:: text

   myproject/
   ├── main.py
   └── mypackage/
       ├── __init__.py
       ├── module1.py
       └── module2.py

In this structure:
- ``mypackage`` is a **package** (it's a directory with ``__init__.py``)
- ``module1.py`` and ``module2.py`` are **modules** inside the package
- ``main.py`` can import from the package

The ``__init__.py`` File
------------------------

What Is ``__init__.py``?
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``__init__.py`` file is a special file that tells Python "this directory is a package."

**Key points:**

* It **must** be named exactly ``__init__.py`` (with double underscores)
* It **can be empty** (often is for simple packages)
* It runs automatically when the package is imported
* It can contain initialization code or control what gets imported

.. important::

   **Python 3.3+ Note:**

   Technically, Python 3.3+ doesn't *require* ``__init__.py`` for "namespace packages," but **best practice** and the PCAP exam expect you to use it. Always include ``__init__.py`` in your packages.

Why Does ``__init__.py`` Exist?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two main reasons:

1. **Mark directories as packages** — Distinguishes package directories from regular directories
2. **Package initialization** — Run setup code when the package is imported

.. activecode:: init_file_purpose_demo
   :nocodelens:

   # Imagine this is the content of mypackage/__init__.py:

   # __init__.py can be empty, or contain code like:
   print("mypackage is being imported!")

   # It can also define what's available from the package:
   __all__ = ['module1', 'module2']

   # For now, understand that __init__.py is the "entry point"
   # when someone imports your package

Creating Your First Package
----------------------------

Let's create a practical package step by step.

Step 1: Create the Directory Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create this folder structure on your computer:

.. code-block:: text

   calculator_project/
   ├── main.py
   └── mathtools/
       ├── __init__.py
       ├── basic.py
       └── advanced.py

Step 2: Write the Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~

**File: ``mathtools/basic.py``**

.. code-block:: python

   def add(a, b):
       """Add two numbers."""
       return a + b

   def subtract(a, b):
       """Subtract b from a."""
       return a - b

   def multiply(a, b):
       """Multiply two numbers."""
       return a * b

   def divide(a, b):
       """Divide a by b."""
       if b == 0:
           return "Cannot divide by zero"
       return a / b

**File: ``mathtools/advanced.py``**

.. code-block:: python

   def power(base, exponent):
       """Raise base to the power of exponent."""
       return base ** exponent

   def factorial(n):
       """Calculate factorial of n."""
       if n == 0 or n == 1:
           return 1
       return n * factorial(n - 1)

Step 3: Create ``__init__.py``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For now, create an empty ``__init__.py`` file:

**File: ``mathtools/__init__.py``**

.. code-block:: python

   # This file can be empty for basic packages
   # Just its presence makes this directory a package

Step 4: Use Your Package
~~~~~~~~~~~~~~~~~~~~~~~~~

**File: ``main.py``**

.. code-block:: python

   # Import from your package
   from mathtools.basic import add, multiply
   from mathtools.advanced import power, factorial

   # Use the imported functions
   print(f"5 + 3 = {add(5, 3)}")
   print(f"5 × 3 = {multiply(5, 3)}")
   print(f"2^8 = {power(2, 8)}")
   print(f"5! = {factorial(5)}")

.. note::

   **Running the code:**

   Save all files in the structure shown, then run ``main.py``:

   .. code-block:: bash

      $ python main.py
      5 + 3 = 8
      5 × 3 = 15
      2^8 = 256
      5! = 120

.. mchoice:: package_structure_understanding_1
   :answer_a: A single .py file
   :answer_b: A directory containing .py files and an __init__.py file
   :answer_c: Any directory with Python files
   :answer_d: A file named __init__.py
   :correct: b
   :feedback_a: That's a module, not a package.
   :feedback_b: Correct! A package is a directory with modules AND an __init__.py file.
   :feedback_c: The __init__.py file is what makes it a package, not just any directory.
   :feedback_d: The __init__.py is part of a package, but not the package itself.

   What is a Python package?

The ``__pycache__`` Directory
------------------------------

What Is ``__pycache__``?
~~~~~~~~~~~~~~~~~~~~~~~~~

When you run Python code that imports modules, you'll notice a new folder appears:

.. code-block:: text

   calculator_project/
   ├── main.py
   └── mathtools/
       ├── __init__.py
       ├── basic.py
       ├── advanced.py
       └── __pycache__/          ← This appears automatically!
           ├── __init__.cpython-310.pyc
           ├── basic.cpython-310.pyc
           └── advanced.cpython-310.pyc

The ``__pycache__`` directory contains **bytecode-compiled** versions of your Python files.

Why Does Python Create ``__pycache__``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Performance optimization!**

When Python imports a module for the first time:

1. Python reads your ``.py`` source code
2. Python **compiles** it to bytecode (``.pyc`` files)
3. Python saves the bytecode in ``__pycache__``
4. **Next time** you import, Python uses the faster bytecode version

.. activecode:: pycache_explanation_demo
   :nocodelens:

   # When you run this:
   import math

   # Python checks:
   # 1. Is there a math.pyc in __pycache__?
   # 2. Is it up-to-date with math.py?
   #
   # If YES: Use the compiled .pyc (fast!)
   # If NO: Compile math.py and save to __pycache__

**Key points about ``__pycache__``:**

* It's created **automatically** by Python
* It's **safe to delete** (Python will recreate it)
* You typically **don't commit it to version control** (add to ``.gitignore``)
* The ``.cpython-310`` part indicates Python version (3.10 in this case)

.. mchoice:: pycache_understanding
   :answer_a: To store backup copies of your code
   :answer_b: To store compiled bytecode for faster imports
   :answer_c: To cache downloaded packages
   :answer_d: To store error logs
   :correct: b
   :feedback_a: __pycache__ is not for backups; it's for performance.
   :feedback_b: Correct! Python stores compiled bytecode to speed up future imports.
   :feedback_c: Downloaded packages go elsewhere (like site-packages), not __pycache__.
   :feedback_d: Error logs are not stored in __pycache__.

   What is the purpose of the ``__pycache__`` directory?

Different Ways to Import from Packages
---------------------------------------

Once you have a package, there are several ways to import from it:

Method 1: Import Specific Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from mathtools.basic import add, subtract

   result = add(5, 3)  # Use directly
   print(result)

Method 2: Import Entire Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from mathtools import basic

   result = basic.add(5, 3)  # Use with module prefix
   print(result)

Method 3: Import with Alias
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from mathtools.basic import multiply as mult

   result = mult(5, 3)  # Use the alias
   print(result)

Method 4: Import Entire Package Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import mathtools.basic

   result = mathtools.basic.add(5, 3)  # Full path
   print(result)

.. activecode:: import_methods_comparison
   :nocodelens:

   # Let's simulate different import styles
   # (Imagine mathtools exists as shown earlier)

   # Style 1: Direct import
   # from mathtools.basic import add
   # print(add(5, 3))  # Clean!

   # Style 2: Module import
   # from mathtools import basic
   # print(basic.add(5, 3))  # Clear where it comes from

   # Style 3: Full path
   # import mathtools.basic
   # print(mathtools.basic.add(5, 3))  # Very explicit

   # For this demo, let's create simple functions
   def add(a, b):
       return a + b

   print(f"5 + 3 = {add(5, 3)}")
   print("\nAll three import styles work—choose based on clarity!")

.. mchoice:: import_methods_understanding
   :answer_a: from mypackage.mymodule import myfunction
   :answer_b: import mypackage.mymodule.myfunction
   :answer_c: from mypackage import mymodule.myfunction
   :answer_d: import myfunction from mypackage.mymodule
   :correct: a
   :feedback_a: Correct! This imports a specific function from a module in a package.
   :feedback_b: This syntax doesn't work; you can't import a function with 'import' alone.
   :feedback_c: This syntax is incorrect; the dot notation doesn't work after 'import'.
   :feedback_d: This is backwards; Python doesn't use 'from' after 'import'.

   Which syntax correctly imports a specific function from a module inside a package?

Practical Example: Building a Utilities Package
------------------------------------------------

Let's create a more realistic package:

.. code-block:: text

   myproject/
   ├── app.py
   └── utils/
       ├── __init__.py
       ├── strings.py
       ├── numbers.py
       └── files.py

**File: ``utils/strings.py``**

.. code-block:: python

   def reverse(text):
       """Reverse a string."""
       return text[::-1]

   def capitalize_words(text):
       """Capitalize each word."""
       return text.title()

   def count_words(text):
       """Count words in text."""
       return len(text.split())

**File: ``utils/numbers.py``**

.. code-block:: python

   def is_even(n):
       """Check if number is even."""
       return n % 2 == 0

   def sum_list(numbers):
       """Sum all numbers in a list."""
       return sum(numbers)

**File: ``utils/__init__.py``**

.. code-block:: python

   # Empty for now—just marks this as a package

**File: ``app.py``**

.. code-block:: python

   from utils.strings import reverse, count_words
   from utils.numbers import is_even, sum_list

   # Use string utilities
   text = "Hello Python World"
   print(f"Reversed: {reverse(text)}")
   print(f"Word count: {count_words(text)}")

   # Use number utilities
   print(f"Is 42 even? {is_even(42)}")
   print(f"Sum: {sum_list([1, 2, 3, 4, 5])}")

.. mchoice:: practical_package_understanding
   :answer_a: To make the code run faster
   :answer_b: To organize related functions into logical groups
   :answer_c: To reduce file size
   :answer_d: To make imports shorter
   :correct: b
   :feedback_a: Packages organize code; they don't inherently improve performance.
   :feedback_b: Correct! Packages help organize related modules for better project structure.
   :feedback_c: Packages don't reduce file size; they organize code.
   :feedback_d: While imports might be cleaner, the main purpose is organization.

   Why would you organize ``strings.py`` and ``numbers.py`` into a ``utils`` package?

Practice Problems
-----------------

.. parsonsprob:: package_structure_parsons
   :numbered: left
   :adaptive:

   Arrange the following to create a proper package structure for a "game" package with two modules: "player.py" and "enemy.py". Put the items in the correct order from top to bottom as they would appear in a file system.
   -----
   game_project/
   =====
   ├── main.py
   =====
   └── game/
   =====
       ├── __init__.py
   =====
       ├── player.py
   =====
       └── enemy.py

.. mchoice:: modules_vs_packages_q1
   :answer_a: A module is a single .py file; a package is a folder containing multiple modules
   :answer_b: A module is for functions; a package is for classes
   :answer_c: A module is built-in; a package is third-party
   :answer_d: A module is old Python; a package is Python 3 only
   :correct: a
   :feedback_a: Correct! A module is a single Python file, while a package is a directory containing multiple modules (and must have __init__.py).
   :feedback_b: No. Both modules and packages can contain functions, classes, and any Python code. The difference is structure, not content.
   :feedback_c: No. Both modules and packages can be built-in or third-party. For example, 'math' is a built-in module, and 'os' is a built-in package.
   :feedback_d: No. Both modules and packages have existed since early Python versions. This has nothing to do with Python version.

   What is the key difference between a **module** and a **package**?

.. mchoice:: modules_vs_packages_q2
   :answer_a: os/__init__.py and os/path.py
   :answer_b: os.py and os_path.py
   :answer_c: os/package.py and os/path.py
   :answer_d: Just os/path.py is enough
   :correct: a
   :feedback_a: Correct! A package needs __init__.py to mark the folder as a package, plus the module files (like path.py) inside it.
   :feedback_b: No. This would create two separate modules (os and os_path), not a package structure. You need a folder with __init__.py.
   :feedback_c: Close! You need __init__.py (not package.py) to make the folder a proper Python package.
   :feedback_d: No. Without __init__.py, Python won't recognize the 'os' folder as a package, so 'import os.path' won't work.

   To create a package structure that allows ``import os.path``, what files are minimally required?

   **File structure:**

   ::

      python_lib/
      └── os/
          ├── ???
          └── ???


.. mchoice:: modules_vs_packages_q4
   :answer_a: It contains the code that runs when you import the package
   :answer_b: It marks the directory as a Python package
   :answer_c: It can define what's available when using 'from package import *'
   :answer_d: All of the above
   :correct: d
   :feedback_a: Yes, any code in __init__.py runs when you first import the package. But is it the only answer?
   :feedback_b: Correct! __init__.py tells Python "this folder is a package, not just a regular directory."
   :feedback_c: Correct! __init__.py can define __all__ to control what gets imported with 'from package import *'.
   :feedback_d: Correct! __init__.py serves all these purposes. It's required to make a package and can customize how the package behaves.

   What is the purpose of ``__init__.py`` in a package folder?

   **Example structure:**

   ::

      mypackage/
      ├── __init__.py      ← This file!
      ├── module1.py
      └── module2.py

Key Takeaways
-------------

.. admonition:: Summary

   * **Module** = Single ``.py`` file
   * **Package** = Directory with ``__init__.py`` + modules
   * ``__init__.py`` marks a directory as a package (can be empty)
   * ``__pycache__`` stores compiled bytecode for performance
   * Package structure:

     .. code-block:: text

        mypackage/
        ├── __init__.py
        ├── module1.py
        └── module2.py

   * Import styles: ``from package.module import function``
   * Packages organize related modules logically

----

What's Next?
------------

You've learned how to create basic packages!

In the next lesson, you'll learn:

- **How Python finds modules** when you import them
- The ``sys.path`` variable and module search order
- Adding directories to Python's search path
- Using ``dir()`` to explore modules
- Debugging import errors

.. note::

   **✅ Lesson 3 Complete!**

   **You've learned about packages:**

   - ✅ Module vs. Package distinction
   - ✅ Creating package directory structures
   - ✅ The purpose of ``__init__.py``
   - ✅ Understanding ``__pycache__`` and bytecode
   - ✅ Different import methods for packages
   - ✅ Building organized, professional project structures

   **Next:** Master how Python searches for and imports modules!