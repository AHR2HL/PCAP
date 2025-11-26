..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Introduction: Advanced File I/O
================================

As a PCEP-certified programmer, you already know how to work with files:

* Opening and closing files
* Reading text files (``read()``, ``readline()``, ``readlines()``)
* Writing text files (``write()``)
* Using context managers (``with`` statement)
* Reading and writing CSV files
* Basic exception handling

If you need a refresher on any of these topics, refer to your PCEP course materials.

This chapter covers **advanced file I/O techniques required for PCAP certification (Section 5 - 22% of exam)**.

What You'll Learn
-----------------

**1. Binary File Operations**

Work with non-text files (images, audio, executables):

.. code-block:: python

   # Read binary file
   with open('image.png', 'rb') as f:
       data = f.read()
   
   # Write binary file
   with open('output.bin', 'wb') as f:
       f.write(bytes([0xFF, 0xD8, 0xFF]))

**2. The bytearray Type**

Mutable byte buffers for efficient binary operations:

.. code-block:: python

   buffer = bytearray(b"Hello")
   buffer[0] = ord('J')  # Modify in place
   print(buffer)  # bytearray(b'Jello')

**3. Error Handling with errno**

Professional error code checking:

.. code-block:: python

   import errno
   
   try:
       with open('file.txt', 'r') as f:
           data = f.read()
   except OSError as e:
       if e.errno == errno.ENOENT:
           print("File not found")
       elif e.errno == errno.EACCES:
           print("Permission denied")

**4. Standard Streams**

Standard input, output, and error:

.. code-block:: python

   import sys
   
   sys.stdout.write("Normal output\n")
   sys.stderr.write("Error message\n")
   user_input = sys.stdin.readline()

**5. File Modes Reference**

Complete guide to all file opening modes:

- Basic: 'r', 'w', 'a'
- Binary: 'rb', 'wb', 'ab'
- Read/write: 'r+', 'w+', 'a+'
- All combinations

**6. Reading Methods Comparison**

When to use each method:

- ``read()`` — Small files, need entire content
- ``readline()`` — Large files, line-by-line processing
- ``readlines()`` — All lines as list
- Direct iteration — Most Pythonic

**7. Best Practices**

Professional file handling patterns.

Why This Matters
-----------------

**For PCAP Certification:**
* Binary file operations and bytearray are explicitly tested
* errno and standard streams are required knowledge
* Understanding file modes is essential
* These topics comprise Section 5 (22% of exam)

**For Your Career:**
* Real applications work with binary data (images, databases, network protocols)
* Professional error handling is critical
* Standard streams are used in command-line tools
* Understanding internals makes you a better developer

Prerequisites
-------------

This chapter assumes you're comfortable with:

* Basic file operations (open, read, write, close)
* Context managers (``with`` statement)
* Text file processing
* CSV file handling
* Basic exception handling

If these feel unfamiliar, review your PCEP course first.

Let's begin!