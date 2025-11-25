..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

The ``platform`` Module
=======================


Python's ``platform`` module gives you access to information about the system your code is running on. This includes details about the operating system, hardware, and Python implementation itself.

Why Use the ``platform`` Module?
---------------------------------

Understanding the runtime environment is crucial for:

* **Cross-platform compatibility** — Writing code that behaves correctly on Windows, macOS, and Linux
* **Debugging** — Gathering system information when troubleshooting issues
* **Feature detection** — Enabling or disabling features based on the OS
* **Logging and diagnostics** — Recording environment details for support

The ``platform`` module is part of Python's standard library, so it's always available without installation.

Importing the ``platform`` Module
----------------------------------

Like the ``math`` module, you must import ``platform`` before using it:

.. activecode:: platform_import_basic
   :nocodelens:

   import platform

   # Get basic system information
   print(f"System: {platform.system()}")
   print(f"Python version: {platform.python_version()}")

System Information Functions
-----------------------------

``platform()`` — Comprehensive Platform String
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``platform()`` function returns a single string with detailed information about your system. This is useful for logging or diagnostic reports.

.. note::

   **Browser Limitation:** The ``platform`` module is not available in the browser environment. The code below shows how it works in regular Python.

**How to use it:**

.. code-block:: python

   import platform

   # Get detailed platform information
   info = platform.platform()
   print(info)

**Example outputs (varies by system):**

::

   Windows: 'Windows-10-10.0.19041-SP0'
   macOS: 'macOS-11.2.3-x86_64-i386-64bit'
   Linux: 'Linux-5.4.0-42-generic-x86_64-with-glibc2.29'

**Try it yourself in real Python:**

.. activecode:: platform_function_demo
   :nocodelens:

   # The platform module is not available in the browser.
   # To see it work, copy this code and run it in your local Python:

   # import platform
   # info = platform.platform()
   # print(info)

   # Instead, here's what you'd typically see:
   print("Example output:")
   print("  Windows: 'Windows-10-10.0.19041-SP0'")
   print("  macOS: 'macOS-11.2.3-x86_64-i386-64bit'")
   print("  Linux: 'Linux-5.4.0-42-generic-x86_64-with-glibc2.29'")
   print()
   print("💡 To try this yourself:")
   print("   1. Open a Python file or terminal on your computer")
   print("   2. Run: import platform; print(platform.platform())")

``system()`` — Operating System Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``system()`` function returns the operating system name in a simplified form.

.. activecode:: platform_system_demo
   :nocodelens:

   import platform

   os_name = platform.system()
   print(f"Operating System: {os_name}")

   # Common return values:
   # 'Windows'
   # 'Darwin' (macOS)
   # 'Linux'
   # 'Java' (Jython)

   # Practical use: OS-specific behavior
   if os_name == 'Windows':
       print("Running on Windows - using backslashes for paths")
   elif os_name == 'Darwin':
       print("Running on macOS")
   elif os_name == 'Linux':
       print("Running on Linux")

``machine()`` — Machine Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``machine()`` function returns the machine type or processor architecture.

.. activecode:: platform_machine_demo
   :nocodelens:

   import platform

   machine_type = platform.machine()
   print(f"Machine type: {machine_type}")

   # Common return values:
   # 'AMD64' or 'x86_64' (64-bit Intel/AMD)
   # 'i386' or 'i686' (32-bit Intel)
   # 'arm64' or 'aarch64' (ARM 64-bit, like Apple M1/M2)
   # 'armv7l' (ARM 32-bit, like Raspberry Pi)

``processor()`` — Processor Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``processor()`` function returns the processor name, though the level of detail varies by platform.

.. activecode:: platform_processor_demo
   :nocodelens:

   import platform

   processor_name = platform.processor()
   print(f"Processor: {processor_name}")

   # Example outputs (varies significantly):
   # Windows: 'Intel64 Family 6 Model 142 Stepping 10, GenuineIntel'
   # macOS: 'i386' or 'arm'
   # Linux: 'x86_64' or actual processor name

   # Note: This function can return an empty string on some systems
   if processor_name:
       print(f"Detected processor: {processor_name}")
   else:
       print("Processor information not available")

``version()`` — System Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``version()`` function returns the system's release version.

.. activecode:: platform_version_demo
   :nocodelens:

   import platform

   sys_version = platform.version()
   print(f"System version: {sys_version}")

   # Example outputs (varies by system):
   # Windows: '10.0.19041'
   # macOS: 'Darwin Kernel Version 20.3.0...'
   # Linux: '#46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020'

.. mchoice:: platform_system_understanding
   :answer_a: 'Darwin'
   :answer_b: 'macOS'
   :answer_c: 'Apple'
   :answer_d: 'OSX'
   :correct: a
   :feedback_a: Correct! platform.system() returns 'Darwin' for macOS systems.
   :feedback_b: This is the marketing name, but platform.system() returns 'Darwin'.
   :feedback_c: This is the company name, not what platform.system() returns.
   :feedback_d: This was an old name, but platform.system() returns 'Darwin'.

   What does ``platform.system()`` return on a macOS computer?

Python Information Functions
-----------------------------

``python_version()`` — Python Version String
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``python_version()`` function returns the Python version as a string.

.. activecode:: platform_python_version_demo
   :nocodelens:

   import platform

   py_version = platform.python_version()
   print(f"Python version: {py_version}")

   # Example output: '3.10.4'

``python_version_tuple()`` — Python Version Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``python_version_tuple()`` function returns the Python version as a tuple of strings, making it easy to compare versions.

.. activecode:: platform_python_version_tuple_demo
   :nocodelens:

   import sys

   # In browser Python, we can check the version like this:
   print("Browser Python version:", sys.version)
   print()

   # Let's simulate platform.python_version_tuple() behavior
   def explain_version_tuple():
       """Show how version tuples work"""

       print("=== Understanding Version Tuples ===")
       print()

       # Example versions
       versions = [
           ('3', '8', '10'),
           ('3', '10', '4'),
           ('3', '11', '2')
       ]

       for version_tuple in versions:
           major, minor, micro = version_tuple
           print(f"Version: {'.'.join(version_tuple)}")
           print(f"  Major: {major} (Python 3.x)")
           print(f"  Minor: {minor} (feature version)")
           print(f"  Micro: {micro} (bug fix version)")

           # Check features available
           if int(major) >= 3 and int(minor) >= 10:
               print(f"  ✅ Has match/case (Python 3.10+)")
           if int(major) >= 3 and int(minor) >= 9:
               print(f"  ✅ Has dict merge operator | (Python 3.9+)")

           print()

   explain_version_tuple()

   print("="*50)
   print("Practical Version Checking:")
   print("="*50)

   # Simulate checking for Python 3.8+
   current_version = ('3', '10', '4')  # Example
   major, minor, _ = current_version

   required_major, required_minor = 3, 8

   if (int(major), int(minor)) >= (required_major, required_minor):
       print(f"✅ Python {major}.{minor} meets requirement (>= 3.8)")
       print("   Modern features available!")
   else:
       print(f"⚠️  Python {major}.{minor} is too old")
       print("   Please upgrade to Python 3.8 or newer")

.. tip::

   **To check YOUR Python version:**

   In a terminal or Python file:

   .. code-block:: python

      import platform
      version = platform.python_version_tuple()
      print(f"You're running Python {'.'.join(version)}")

``python_implementation()`` — Python Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``python_implementation()`` function tells you which Python implementation you're using.

.. activecode:: platform_python_implementation_demo
   :nocodelens:

   import platform

   implementation = platform.python_implementation()
   print(f"Python implementation: {implementation}")

   # Common return values:
   # 'CPython' - Standard Python (most common)
   # 'PyPy' - Alternative fast implementation
   # 'Jython' - Python for Java Virtual Machine
   # 'IronPython' - Python for .NET

   if implementation == 'CPython':
       print("Using standard Python implementation")
   elif implementation == 'PyPy':
       print("Using PyPy - optimized for speed")

.. mchoice:: platform_python_implementation_understanding
   :answer_a: CPython
   :answer_b: Python
   :answer_c: StandardPython
   :answer_d: Official
   :correct: a
   :feedback_a: Correct! CPython is the standard Python implementation written in C.
   :feedback_b: This is too generic; the function returns 'CPython' specifically.
   :feedback_c: This is not the name returned by the function.
   :feedback_d: The function returns implementation names like 'CPython', not 'Official'.

   What does ``platform.python_implementation()`` return for the standard Python you download from python.org?

Practical Applications
-----------------------

Writing Cross-Platform Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here's a practical example of using ``platform`` to write OS-specific code:

.. activecode:: platform_cross_platform_example
   :nocodelens:

   import platform

   def get_config_path():
       """Return the appropriate config file path for the current OS."""
       os_name = platform.system()

       if os_name == 'Windows':
           return 'C:\\Users\\Public\\config.ini'
       elif os_name == 'Darwin':  # macOS
           return '/Users/Shared/config.ini'
       elif os_name == 'Linux':
           return '/etc/myapp/config.ini'
       else:
           return './config.ini'  # Fallback

   config_path = get_config_path()
   print(f"Config file location: {config_path}")

System Diagnostic Report
~~~~~~~~~~~~~~~~~~~~~~~~~

Combining multiple ``platform`` functions for a complete system report:

.. activecode:: platform_diagnostic_report
   :nocodelens:

   import sys

   def system_report():
       """Generate a comprehensive system information report."""
       print("=" * 50)
       print("SYSTEM DIAGNOSTIC REPORT")
       print("=" * 50)

       # What we CAN check in browser Python:
       print("\n📱 Browser Environment:")
       print(f"Python Version: {sys.version}")
       print(f"Platform: Browser (Skulpt)")

       print("\n" + "=" * 50)
       print("EXAMPLE: Real Python Output")
       print("=" * 50)

       # Show what it would look like on different systems
       examples = [
           {
               "name": "Windows 10 Laptop",
               "os": "Windows",
               "version": "10.0.19041",
               "platform": "Windows-10-10.0.19041-SP0",
               "machine": "AMD64",
               "processor": "Intel64 Family 6 Model 142 Stepping 12, GenuineIntel",
               "python_version": "3.11.2",
               "implementation": "CPython"
           },
           {
               "name": "macOS MacBook",
               "os": "Darwin",
               "version": "Darwin Kernel Version 21.3.0",
               "platform": "macOS-12.2-arm64-arm-64bit",
               "machine": "arm64",
               "processor": "arm",
               "python_version": "3.10.4",
               "implementation": "CPython"
           },
           {
               "name": "Ubuntu Linux Server",
               "os": "Linux",
               "version": "#46-Ubuntu SMP",
               "platform": "Linux-5.4.0-42-generic-x86_64-with-glibc2.29",
               "machine": "x86_64",
               "processor": "x86_64",
               "python_version": "3.9.7",
               "implementation": "CPython"
           }
       ]

       for example in examples:
           print(f"\n{'='*50}")
           print(f"Example: {example['name']}")
           print(f"{'='*50}")
           print(f"\nOperating System: {example['os']}")
           print(f"OS Version: {example['version']}")
           print(f"Platform: {example['platform']}")
           print(f"\nMachine Type: {example['machine']}")
           print(f"Processor: {example['processor']}")
           print(f"\nPython Version: {example['python_version']}")
           print(f"Python Implementation: {example['implementation']}")

       print("\n" + "=" * 50)
       print("\n💡 To get YOUR system info:")
       print("   Copy the code below and run it in local Python!")
       print("=" * 50)

   system_report()

.. note::

   **To run this on YOUR computer:**

   Copy and paste this code into a Python file or terminal:

   .. code-block:: python

      import platform

      def system_report():
          """Generate a comprehensive system information report."""
          print("=" * 50)
          print("SYSTEM DIAGNOSTIC REPORT")
          print("=" * 50)

          print(f"\nOperating System: {platform.system()}")
          print(f"OS Version: {platform.version()}")
          print(f"Platform: {platform.platform()}")

          print(f"\nMachine Type: {platform.machine()}")
          processor = platform.processor()
          if processor:
              print(f"Processor: {processor}")

          print(f"\nPython Version: {platform.python_version()}")
          print(f"Python Implementation: {platform.python_implementation()}")

          print("=" * 50)

      system_report()

   Save as ``my_system_report.py`` and run: ``python my_system_report.py``

.. mchoice:: platform_practical_understanding
   :answer_a: To display fancy graphics
   :answer_b: To adjust code behavior based on the operating system
   :answer_c: To make Python run faster
   :answer_d: To download files from the internet
   :correct: b
   :feedback_a: The platform module provides information, not graphics capabilities.
   :feedback_b: Correct! You can use platform information to write code that adapts to different operating systems.
   :feedback_c: The platform module provides information; it doesn't affect performance.
   :feedback_d: The platform module is for system information, not network operations.

   What is the primary reason for using ``platform.system()`` in cross-platform applications?

Practice Problems
-----------------

.. mchoice:: platform_challenge_1
   :answer_a: ('3', '10', '4')
   :answer_b: (3, 10, 4)
   :answer_c: "3.10.4"
   :answer_d: [3, 10, 4]
   :correct: a
   :feedback_a: Correct! python_version_tuple() returns a tuple of STRINGS, not integers.
   :feedback_b: Close, but the values are strings ('3', '10', '4'), not integers (3, 10, 4).
   :feedback_c: No, it returns a tuple, not a single string.
   :feedback_d: No, it returns a tuple (immutable), not a list (mutable).

   What does ``platform.python_version_tuple()`` return for Python version 3.10.4?

.. mchoice:: platform_challenge_1b
   :answer_a: if python_version_tuple()[0] >= '3'
   :answer_b: if int(python_version_tuple()[0]) >= 3
   :answer_c: if python_version_tuple() >= (3, 8)
   :answer_d: if tuple(python_version_tuple()) >= ('3', '8', '0')
   :correct: b
   :feedback_a: String comparison doesn't work correctly for numbers. '3' >= '3' works, but what about '10' vs '9'?
   :feedback_b: Correct! Convert to int for proper numeric comparison.
   :feedback_c: This compares strings to integers, which will cause a TypeError.
   :feedback_d: python_version_tuple() already returns a tuple, no need to convert. Also mixing string and int comparison.

   How should you check if the current Python version is at least 3.8?

.. mchoice:: platform_challenge_1c
   :answer_a: '10' < '9' evaluates to True
   :answer_b: String comparison is lexicographic (dictionary order)
   :answer_c: '1' comes before '9' alphabetically
   :answer_d: All of the above
   :correct: d
   :feedback_a: Correct! '10' < '9' is True because '1' < '9' in string comparison.
   :feedback_b: Correct! Strings are compared character by character, not as numbers.
   :feedback_c: Correct! This is why '10' < '9' (compares '1' vs '9' first).
   :feedback_d: Correct! This is why you MUST convert version strings to integers before comparing.

   Why do we need to convert version tuple strings to integers before comparing?

.. activecode:: platform_challenge_2
   :nocodelens:

   Write a function ``system_summary()`` that returns a dictionary with the following keys and values:
   - 'os': Operating system name
   - 'machine': Machine type
   - 'python_version': Python version string
   - 'implementation': Python implementation
   ~~~~
   import platform

   def system_summary():
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class MyTests(TestCaseGui):
       def test_system_summary(self):
           result = system_summary()
           self.assertIn('os', result)
           self.assertIn('machine', result)
           self.assertIn('python_version', result)
           self.assertIn('implementation', result)

           # Check that values are non-empty strings
           self.assertIsInstance(result['os'], str)
           self.assertGreater(len(result['os']), 0)
           self.assertIsInstance(result['python_version'], str)
           self.assertGreater(len(result['python_version']), 0)

   MyTests().main()

Key Takeaways
-------------

.. admonition:: Summary

   * The ``platform`` module provides system and Python environment information
   * **System information functions:**

     * ``platform()`` — Comprehensive platform string
     * ``system()`` — OS name ('Windows', 'Darwin', 'Linux')
     * ``machine()`` — Processor architecture
     * ``processor()`` — Processor name (varies by system)
     * ``version()`` — System version details

   * **Python information functions:**

     * ``python_version()`` — Python version string
     * ``python_version_tuple()`` — Version as tuple for comparison
     * ``python_implementation()`` — Python type ('CPython', 'PyPy', etc.)

   * Use ``platform`` functions to write **cross-platform compatible code**

----

What's Next?
------------

You've mastered system information with the ``platform`` module!

In the next lesson, you'll learn:

- **Creating Python packages** from scratch
- Understanding ``__init__.py`` files
- The ``__pycache__`` directory and bytecode compilation
- Structuring multi-file projects

.. note::

   **✅ Lesson 2 Complete!**

   **You've learned the ``platform`` module:**

   - ✅ System information functions (``system()``, ``machine()``, ``version()``)
   - ✅ Python information functions (``python_version()``, ``python_implementation()``)
   - ✅ Cross-platform code patterns
   - ✅ Generating diagnostic reports
   - ✅ Version checking and OS detection

   **Next:** Learn how to create and organize Python packages!