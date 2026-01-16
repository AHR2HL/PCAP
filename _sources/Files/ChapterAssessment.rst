..  Copyright (C)  Alpha Schools

.. qnum::
   :prefix: files-10-
   :start: 1

Chapter Assessment
==================

Part 1: Multiple Choice Questions
----------------------------------

.. mchoice:: files_assess_mc1
   :answer_a: Both return str
   :answer_b: Both return bytes
   :answer_c: Text returns str, binary returns bytes
   :answer_d: They return the same type
   :correct: c
   :feedback_a: Binary mode returns bytes, not str.
   :feedback_b: Text mode returns str, not bytes.
   :feedback_c: Correct! Text mode ('r') returns str, binary mode ('rb') returns bytes.
   :feedback_d: They return different types!

   What's the difference between text and binary mode return types?


.. mchoice:: files_assess_mc2
   :answer_a: bytes is mutable, bytearray is immutable
   :answer_b: Both are mutable
   :answer_c: Both are immutable
   :answer_d: bytes is immutable, bytearray is mutable
   :correct: d
   :feedback_a: You have it backwards!
   :feedback_b: bytes is immutable.
   :feedback_c: bytearray is mutable!
   :feedback_d: Correct! bytes is immutable (like str), bytearray is mutable (like list).

   What's the difference between ``bytes`` and ``bytearray``?


.. mchoice:: files_assess_mc3
   :answer_a: errno.ENOENT
   :answer_b: errno.EACCES
   :answer_c: errno.EISDIR
   :answer_d: errno.EEXIST
   :correct: a
   :feedback_a: Correct! ENOENT (Error NO ENTry) means "No such file or directory"
   :feedback_b: EACCES means "Permission denied"
   :feedback_c: EISDIR means "Is a directory"
   :feedback_d: EEXIST means "File exists"

   Which errno constant indicates "file not found"?


.. mchoice:: files_assess_mc4
   :answer_a: sys.stdin
   :answer_b: sys.stdout
   :answer_c: sys.stderr
   :answer_d: sys.output
   :correct: c
   :feedback_a: stdin is for input, not error messages
   :feedback_b: stdout is for normal output, not errors
   :feedback_c: Correct! stderr is specifically for error messages and logging
   :feedback_d: There is no sys.output

   Which standard stream should be used for error messages?


.. mchoice:: files_assess_mc5
   :answer_a: 'rb+'
   :answer_b: 'r+'
   :answer_c: 'wb'
   :answer_d: 'rb'
   :correct: a
   :feedback_a: Correct! 'rb+' opens binary file for both reading and writing
   :feedback_b: This is text mode (read and write), not binary
   :feedback_c: This only allows writing, not reading
   :feedback_d: This only allows reading, not writing

   Which file mode allows both reading and writing a binary file?


.. mchoice:: files_assess_mc6
   :answer_a: read() - load entire file
   :answer_b: readlines() - load all lines
   :answer_c: Iterate line by line
   :answer_d: All methods are equal
   :correct: c
   :feedback_a: This loads everything into memory—bad for large files!
   :feedback_b: This also loads everything into memory.
   :feedback_c: Correct! Iterate with "for line in file:" to process large files without loading all into memory.
   :feedback_d: They have very different memory characteristics!

   What's the best way to process a very large file?


Part 2: Active Code Problems
-----------------------------

.. activecode:: files_assess_ac1
   :language: python
   :autograde: unittest
   :practice: T

   Create a function ``is_png_data(data)`` that checks if binary data starts with PNG signature.

   PNG signature: b'\\x89PNG\\r\\n\\x1a\\n'

   Returns True if data starts with PNG signature, False otherwise.
   ~~~~
   def is_png_data(data):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_valid_png(self):
           png_sig = b'\x89PNG\r\n\x1a\n'
           self.assertTrue(is_png_data(png_sig))

       def test_png_with_extra(self):
           png_sig = b'\x89PNG\r\n\x1a\nEXTRA'
           self.assertTrue(is_png_data(png_sig))

       def test_not_png(self):
           self.assertFalse(is_png_data(b'JPEG'))

       def test_too_short(self):
           self.assertFalse(is_png_data(b'PNG'))

   myTests().main()


.. activecode:: files_assess_ac2
   :language: python
   :autograde: unittest
   :practice: T

   Create a function ``modify_char(text, index, new_char)`` that:

   - Converts string to list (since strings are immutable)
   - Modifies character at given index
   - Converts back to string and returns it

   This demonstrates converting immutable data to mutable for modification!
   ~~~~
   def modify_char(text, index, new_char):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def test_basic(self):
           result = modify_char('Hello', 0, 'J')
           self.assertEqual(result, 'Jello', "Testing modification at start")

       def test_middle(self):
           result = modify_char('Python', 2, 'X')
           self.assertEqual(result, 'PyXhon', "Testing modification in middle")

       def test_returns_string(self):
           result = modify_char('Test', 0, 'B')
           self.assertEqual(type(result), str, "Should return a string")

       def test_last_char(self):
           result = modify_char('Code', 3, '!')
           self.assertEqual(result, 'Cod!', "Testing modification at end")

   myTests().main()


.. activecode:: files_assess_ac3
   :language: python
   :autograde: unittest
   :practice: T

   Create a function ``get_error_message(error_code)`` that returns appropriate message:

   - 2 (ENOENT) → "File not found"
   - 13 (EACCES) → "Permission denied"
   - 21 (EISDIR) → "Is a directory"
   - Other → "Unknown error"
   ~~~~
   def get_error_message(error_code):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_enoent(self):
           self.assertEqual(get_error_message(2), "File not found")

       def test_eacces(self):
           self.assertEqual(get_error_message(13), "Permission denied")

       def test_eisdir(self):
           self.assertEqual(get_error_message(21), "Is a directory")

       def test_unknown(self):
           self.assertEqual(get_error_message(999), "Unknown error")

   myTests().main()


.. activecode:: files_assess_ac4
   :language: python
   :autograde: unittest
   :practice: T

   Create a function ``safe_get_data(data_dict, key, default=None)`` that safely retrieves data from a dictionary:

   - Returns the value for the given key if it exists
   - Returns default value if KeyError occurs (key not found)
   - Returns default value if TypeError occurs (invalid key type)

   This teaches the same error handling concepts as file operations!
   ~~~~
   def safe_get_data(data_dict, key, default=None):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def test_successful_lookup(self):
           data = {'name': 'Alice', 'age': 30}
           result = safe_get_data(data, 'name')
           self.assertEqual(result, 'Alice', "Should return value when key exists")

       def test_default_on_missing(self):
           data = {'name': 'Alice'}
           result = safe_get_data(data, 'city', default='Unknown')
           self.assertEqual(result, 'Unknown', "Should return default when key missing")

       def test_none_by_default(self):
           data = {'name': 'Alice'}
           result = safe_get_data(data, 'city')
           self.assertIsNone(result, "Should return None by default")

       def test_uses_try_except(self):
           code = self.getEditorText()
           self.assertIn('try', code, "Should use try/except for error handling")
           self.assertIn('except', code, "Should use try/except for error handling")

   myTests().main()


.. activecode:: files_assess_ac5
   :language: python
   :autograde: unittest
   :practice: T

   Create a function ``choose_file_mode(read, write, binary)`` that returns correct mode:

   - read=True, write=False, binary=False → 'r'
   - read=True, write=False, binary=True → 'rb'
   - read=False, write=True, binary=False → 'w'
   - read=False, write=True, binary=True → 'wb'
   - read=True, write=True, binary=False → 'r+'
   - read=True, write=True, binary=True → 'rb+'
   ~~~~
   def choose_file_mode(read, write, binary):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_read_text(self):
           self.assertEqual(choose_file_mode(True, False, False), 'r')

       def test_read_binary(self):
           self.assertEqual(choose_file_mode(True, False, True), 'rb')

       def test_write_text(self):
           self.assertEqual(choose_file_mode(False, True, False), 'w')

       def test_write_binary(self):
           self.assertEqual(choose_file_mode(False, True, True), 'wb')

       def test_readwrite_text(self):
           self.assertEqual(choose_file_mode(True, True, False), 'r+')

       def test_readwrite_binary(self):
           self.assertEqual(choose_file_mode(True, True, True), 'rb+')

   myTests().main()


.. datafile:: SP500.txt

    Date,SP500,Dividend,Earnings,Consumer Price Index,Long Interest Rate,Real Price,Real Dividend,Real Earnings,PE10
    1/1/2016,1918.6,43.55,86.5,236.92,2.09,2023.23,45.93,91.22,24.21
    2/1/2016,1904.42,43.72,86.47,237.11,1.78,2006.62,46.06,91.11,24
    3/1/2016,2021.95,43.88,86.44,238.13,1.89,2121.32,46.04,90.69,25.37
    4/1/2016,2075.54,44.07,86.6,239.26,1.81,2167.27,46.02,90.43,25.92
    5/1/2016,2065.55,44.27,86.76,240.23,1.81,2148.15,46.04,90.23,25.69
    6/1/2016,2083.89,44.46,86.92,241.02,1.64,2160.13,46.09,90.1,25.84
    7/1/2016,2148.9,44.65,87.64,240.63,1.5,2231.13,46.36,91,26.69
    8/1/2016,2170.95,44.84,88.37,240.85,1.56,2251.95,46.51,91.66,26.95
    9/1/2016,2157.69,45.03,89.09,241.43,1.63,2232.83,46.6,92.19,26.73
    10/1/2016,2143.02,45.25,90.91,241.73,1.76,2214.89,46.77,93.96,26.53
    11/1/2016,2164.99,45.48,92.73,241.35,2.14,2241.08,47.07,95.99,26.85
    12/1/2016,2246.63,45.7,94.55,241.43,2.49,2324.83,47.29,97.84,27.87
    1/1/2017,2275.12,45.93,96.46,242.84,2.43,2340.67,47.25,99.24,28.06
    2/1/2017,2329.91,46.15,98.38,243.6,2.42,2389.52,47.33,100.89,28.66
    3/1/2017,2366.82,46.38,100.29,243.8,2.48,2425.4,47.53,102.77,29.09
    4/1/2017,2359.31,46.66,101.53,244.52,2.3,2410.56,47.67,103.74,28.9
    5/1/2017,2395.35,46.94,102.78,244.73,2.3,2445.29,47.92,104.92,29.31
    6/1/2017,2433.99,47.22,104.02,244.96,2.19,2482.48,48.16,106.09,29.75
    7/1/2017,2454.1,47.54,105.04,244.79,2.32,2504.72,48.52,107.21,30
    8/1/2017,2456.22,47.85,106.06,245.52,2.21,2499.4,48.69,107.92,29.91
    9/1/2017,2492.84,48.17,107.08,246.82,2.2,2523.31,48.76,108.39,30.17
    10/1/2017,2557,48.42,108.01,246.66,2.36,2589.89,49.05,109.4,30.92
    11/1/2017,2593.61,48.68,108.95,246.67,2.35,2626.9,49.3,110.35,31.3
    12/1/2017,2664.34,48.93,109.88,246.52,2.4,2700.13,49.59,111.36,32.09

.. activecode:: files_assess_ac6
   :language: python
   :autograde: unittest
   :practice: T
   :datafile: SP500.txt

   **PCEP Review:** Read ``SP500.txt`` which has monthly S&P 500 data for 2016-2017.

   Compute the average closing price (column 2) and highest long-term interest rate (column 6) for June 2016 through May 2017 only.

   Save results in ``mean_SP`` and ``max_interest``.

   The ``open()`` command will work here with ``SP500.txt``.
   ~~~~

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
      def testOne(self):
         self.assertLess(abs(mean_SP - 2237), 0.5, "Testing mean_SP is correct for June 2016-May 2017.")
         self.assertEqual(max_interest, 2.49, "Testing max_interest is correct for June 2016-May 2017.")

   myTests().main()


Part 3: Debugging Exercises
----------------------------

.. activecode:: files_assess_debug1
   :language: python
   :autograde: unittest

   **Debug** This code tries to read binary file as text. Fix the mode!
   ~~~~
   def read_image_header(filename):
       with open(filename, 'r') as f:
           header = f.read(8)

       if header == b'\x89PNG\r\n\x1a\n':
           return "PNG file"
       return "Unknown"

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_uses_binary_mode(self):
           source = self.getEditorText()
           self.assertIn("'rb'", source, "Should use 'rb' mode for binary files")

   myTests().main()


.. activecode:: files_assess_debug2
   :language: python
   :autograde: unittest

   **Debug** File not closing on early return. Fix it!
   ~~~~
   def process_file(filename):
       f = open(filename, 'r')
       data = f.read()

       if not data:
           return None

       result = data.upper()
       f.close()
       return result

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_uses_context_manager(self):
           source = self.getEditorText()
           self.assertIn('with open(', source, "Should use context manager")
           self.assertNotIn('.close()', source, "Don't need manual close with 'with'")

   myTests().main()


.. activecode:: files_assess_debug3
   :language: python
   :autograde: unittest

   **Debug** Wrong errno constant for "file not found". Fix it!
   ~~~~
   import errno

   def safe_open(filename):
       try:
           with open(filename, 'r') as f:
               return f.read()
       except OSError as e:
           if e.errno == errno.EACCES:
               print("File not found")
               return None
           raise

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_uses_enoent(self):
           source = self.getEditorText()
           self.assertIn('errno.ENOENT', source, "Should use ENOENT for file not found")

   myTests().main()


Part 4: Parson's Problems
--------------------------

.. parsonsprob:: files_assess_parsons1
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to read a binary file.
   -----
   def read_binary(filename):
   =====
       with open(filename, 'rb') as f:
   =====
       with open(filename, 'r') as f: #distractor
   =====
           data = f.read()
   =====
       return data
   =====
       return bytes(data) #distractor


.. parsonsprob:: files_assess_parsons2
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to handle file errors with errno.
   -----
   import errno
   =====
   def safe_read(filename):
   =====
       try:
   =====
           with open(filename, 'r') as f:
   =====
               return f.read()
   =====
       except OSError as e:
   =====
       except FileNotFoundError as e: #distractor
   =====
           if e.errno == errno.ENOENT:
   =====
               return None


.. parsonsprob:: files_assess_parsons3
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to modify bytearray.
   -----
   def uppercase_bytes(data):
   =====
       buffer = bytearray(data)
   =====
       buffer = bytes(data) #distractor
   =====
       for i in range(len(buffer)):
   =====
           if 97 <= buffer[i] <= 122:
   =====
           if 'a' <= buffer[i] <= 'z': #distractor
   =====
               buffer[i] -= 32
   =====
       return buffer


Summary & Self-Check
---------------------

After completing this assessment, you should be able to:

✅ Distinguish between text and binary file modes

✅ Work with bytes and bytearray types

✅ Handle file errors using errno constants

✅ Use standard streams (stdin, stdout, stderr)

✅ Choose appropriate file modes for different scenarios

✅ Use context managers for file handling

✅ Process large files efficiently

✅ Work with binary data (file signatures, headers)

**Struggling with any of these?** Review the Advanced File I/O sections before continuing.