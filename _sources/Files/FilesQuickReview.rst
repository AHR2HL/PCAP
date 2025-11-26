..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Optional: PCEP Quick Review
============================

.. admonition:: Skip This Section

   This is a brief refresher for PCEP graduates. If you're confident with basic file operations, **skip to Advanced File I/O**.

**Basic File Reading:**

.. code-block:: python

   # Read entire file
   with open('data.txt', 'r') as f:
       content = f.read()

   # Read line by line
   with open('data.txt', 'r') as f:
       for line in f:
           print(line.strip())

   # Read all lines as list
   with open('data.txt', 'r') as f:
       lines = f.readlines()

**Basic File Writing:**

.. code-block:: python

   # Write text
   with open('output.txt', 'w') as f:
       f.write('Hello, World!\n')

   # Write multiple lines
   with open('output.txt', 'w') as f:
       for item in data:
           f.write(f"{item}\n")

**CSV Files:**

.. code-block:: python

   import csv

   # Read CSV
   with open('data.csv', 'r') as f:
       reader = csv.reader(f)
       for row in reader:
           print(row)

   # Write CSV
   with open('output.csv', 'w') as f:
       writer = csv.writer(f)
       writer.writerow(['Name', 'Age'])
       writer.writerow(['Alice', 25])

That's the PCEP review! Now continue to advanced topics.