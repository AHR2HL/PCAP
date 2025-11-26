Quick Review: Exception Handling Basics
========================================

.. admonition:: Skip This Section

   This is a quick refresher for PCEP graduates. If you're confident with basic exception handling, **skip to Advanced Exception Handling**.

As a PCEP-certified programmer, you already know:

**Basic Try-Except Syntax**

.. code-block:: python

   try:
       risky_operation()
   except ExceptionType:
       handle_error()

**Common Exception Types (PCEP)**

+-----------------------+------------------------------------------+
| Exception             | When It Occurs                           |
+=======================+==========================================+
| **IndexError**        | Invalid list/tuple index                 |
+-----------------------+------------------------------------------+
| **KeyError**          | Invalid dictionary key                   |
+-----------------------+------------------------------------------+
| **ValueError**        | Wrong value (e.g., int("abc"))           |
+-----------------------+------------------------------------------+
| **TypeError**         | Wrong type (e.g., "hello" + 5)           |
+-----------------------+------------------------------------------+
| **ZeroDivisionError** | Division by zero                         |
+-----------------------+------------------------------------------+
| **NameError**         | Undefined variable                       |
+-----------------------+------------------------------------------+

**Exception Hierarchy (PCEP)**

.. code-block:: text

   BaseException
   └── Exception
        ├── ArithmeticError
        │    └── ZeroDivisionError
        ├── LookupError
        │    ├── IndexError
        │    └── KeyError
        ├── ValueError
        ├── TypeError
        └── NameError

**Catching Multiple Exceptions**

.. code-block:: python

   try:
       risky_operation()
   except (ValueError, TypeError):
       print("Value or type error occurred")
   except KeyError:
       print("Key not found")

**The finally Clause**

.. code-block:: python

   try:
       file = open("data.txt")
       process(file)
   except FileNotFoundError:
       print("File not found")
   finally:
       file.close()  # Always runs

That's the PCEP review! Now let's learn the PCAP advanced topics.