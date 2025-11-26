..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. qnum::
   :prefix: files-10-
   :start: 1

Chapter Assessment
==================

.. datafile:: travel_plans.txt
   :fromfile: travel_plans.txt
   :hide:

.. datafile:: school_prompt.txt
   :fromfile: school_prompt.txt
   :hide:

.. datafile:: emotion_words.txt
   :fromfile: emotion_words.txt
   :hide:

.. activecode:: ac9_10_1
   :language: python
   :autograde: unittest
   :practice: T
   :available_files: travel_plans.txt
   :nocodelens:

   The textfile, ``travel_plans.txt``, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable ``num``.
   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(num, 316, "Testing that num value is assigned to correct value.")

   myTests().main()

.. activecode:: ac9_10_2
   :language: python
   :autograde: unittest
   :practice: T
   :available_files: emotion_words.txt
   :nocodelens:

   We have provided a file called ``emotion_words.txt`` that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable ``num_words``.
   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(num_words, 48, "Testing that num_words was assigned to the correct value.")

   myTests().main()


.. activecode:: ac9_10_3
   :language: python
   :autograde: unittest
   :practice: T
   :available_files: school_prompt.txt
   :nocodelens:

   Assign to the variable ``num_lines`` the number of lines in the file ``school_prompt.txt``.
   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(num_lines, 10, "Testing that num_lines has the correct value.")

   myTests().main()


.. activecode:: ac9_10_4
   :language: python
   :autograde: unittest
   :practice: T
   :available_files: school_prompt.txt
   :nocodelens:

   Assign the first 30 characters of ``school_prompt.txt`` as a string to the variable ``beginning_chars``.
   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(len(beginning_chars), 30, "Testing that beginning_chars has the correct length.")
         self.assertEqual(beginning_chars, "Writing essays for school can ", "Testing that beginning_chars has the correct string.")

   myTests().main()


.. activecode:: ac9_10_5
   :language: python
   :autograde: unittest
   :practice: T
   :available_files: school_prompt.txt
   :nocodelens:

   **Challenge:** Using the file ``school_prompt.txt``, assign the third word of every line to a list called ``three``.
   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(three, ['for', 'find', 'to', 'many', 'they', 'solid', 'for', 'have', 'some', 'ups,'], "Testing that three has the correct value.")

   myTests().main()


.. activecode:: ac9_10_6
   :language: python
   :autograde: unittest
   :practice: T
   :available_files: emotion_words.txt
   :nocodelens:

   **Challenge:** Create a list called ``emotions`` that contains the first word of every line in ``emotion_words.txt``.
   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(emotions, ['Sad', 'Angry', 'Happy', 'Confused', 'Excited', 'Scared', 'Nervous'], "Testing that emotions was created correctly.")

   myTests().main()


.. activecode:: ac9_10_7
   :language: python
   :autograde: unittest
   :practice: T
   :available_files: travel_plans.txt
   :nocodelens:

   Assign the first 33 characters from the textfile, ``travel_plans.txt`` to the variable ``first_chars``.
   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testFive(self):
         self.assertEqual(first_chars, "This summer I will be travelling.", "Testing that first_chars is assigned to correct value.")

   myTests().main()


.. activecode:: ac9_10_8
   :language: python
   :autograde: unittest
   :practice: T
   :available_files: school_prompt.txt
   :nocodelens:

   **Challenge:** Using the file ``school_prompt.txt``, if the character 'p' is in a word, then add the word to a list called ``p_words``.
   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertEqual(p_words, ['topic', 'point', 'papers,', 'ups,', 'scripts.'], "Testing that p_words has the correct list.")

   myTests().main()

.. activecode:: ac_9_10_9
   :language: python
   :autograde: unittest
   :practice: T
   :available_files: SP500.txt
   :topics: Files/ReadingCSVFiles

   Read in the contents of the file ``SP500.txt`` which has monthly data for 2016 and 2017 about the S&P 500 closing prices as well as some other financial indicators, including the "Long Term Interest Rate", which is interest rate paid on 10-year U.S. government bonds.

   Write a program that computes the average closing price (the second column, labeled SP500) and the highest long-term interest rate. Both should be computed only for the period from June 2016 through May 2017. Save the results in the variables ``mean_SP`` and ``max_interest``.

   ~~~~

   ====

   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

      def testOne(self):
         self.assertLess(abs(mean_SP - 2237), 0.5, "Testing that mean_SP is within 0.5 of the correct value. Make sure to use only the correct 12 month period.")
         self.assertEqual(max_interest, 2.49, "Testing the max_interest is correct. Make sure to use only the correct 12 month period.")

   myTests().main()


.. mchoice:: pcap_concept_read_large_file
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


**CSV Parsing**

.. parsonsprob:: pcap_parsons_csv
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to parse CSV data.
   -----
   def parse_csv(data):
   =====
       lines = data.strip().splitlines()
   =====
       lines = data.strip().split('\n') #distractor
   =====
       result = []
   =====
       for line in lines:
   =====
           fields = [f.strip() for f in line.split(',')]
   =====
           fields = line.split(',').strip() #distractor
   =====
           result.append(fields)
   =====
       return result

**Safe File Reader**

.. activecode:: pcap_code_safe_file_reader
   :language: python
   :autograde: unittest

   Create a function ``safe_read_file(filename, default=None)`` that:
   - Reads and returns file contents
   - Returns default value if file not found
   - Handles permission errors appropriately
   - Always closes the file

   Example::

       content = safe_read_file('data.txt', default='')
       # Returns file content or '' if not found

   ~~~~
   def safe_read_file(filename, default=None):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_returns_default_on_missing(self):
           result = safe_read_file('nonexistent.txt', default='DEFAULT')
           self.assertEqual(result, 'DEFAULT')

       def test_returns_none_by_default(self):
           result = safe_read_file('nonexistent.txt')
           self.assertIsNone(result)

   myTests().main()

.. reveal:: pcap_code_safe_file_reader_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def safe_read_file(filename, default=None):
          try:
              with open(filename, 'r') as f:
                  return f.read()
          except FileNotFoundError:
              return default
          except PermissionError:
              return default

---

**Log Parser**

.. activecode:: pcap_code_log_parser
   :language: python
   :autograde: unittest

   Create a function ``parse_log_line(line)`` that parses log format:
   "[LEVEL] message"

   Returns dictionary: {'level': 'LEVEL', 'message': 'message'}
   Returns None if format is invalid

   Example::

       parse_log_line("[ERROR] File not found")
       # {'level': 'ERROR', 'message': 'File not found'}

   ~~~~
   def parse_log_line(line):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_valid_log(self):
           result = parse_log_line("[ERROR] Test message")
           self.assertEqual(result, {'level': 'ERROR', 'message': 'Test message'})

       def test_strips_whitespace(self):
           result = parse_log_line("  [INFO]  Test  ")
           self.assertEqual(result, {'level': 'INFO', 'message': 'Test'})

       def test_invalid_format(self):
           result = parse_log_line("Invalid log")
           self.assertIsNone(result)

   myTests().main()

.. reveal:: pcap_code_log_parser_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def parse_log_line(line):
          line = line.strip()

          # Check format
          if not line.startswith('[') or ']' not in line:
              return None

          # Find closing bracket
          close_idx = line.find(']')

          # Extract level and message
          level = line[1:close_idx]
          message = line[close_idx + 1:].strip()

          return {'level': level, 'message': message}

---


**Debug: Binary Mode Mistake**

.. activecode:: pcap_debug_binary_mode
   :language: python
   :autograde: unittest

   This code tries to read a binary file as text. Fix it!
   ~~~~
   def read_image_header(filename):
       with open(filename, 'r') as f:
           header = f.read(8)

       if header == b'\x89PNG\r\n\x1a\n':
           return "PNG file"
       return "Unknown"

   print("Testing binary file handling...")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_uses_binary_mode(self):
           """Should use 'rb' mode for binary files"""
           source = self.getEditorText()
           func_code = source.split('def read_image_header(')[1].split('\n\n')[0]
           self.assertIn("'rb'", func_code,
                        "Should use 'rb' mode for reading binary files")

       def test_not_using_text_mode(self):
           """Should not use text mode 'r' for binary data"""
           source = self.getEditorText()
           func_code = source.split('def read_image_header(')[1].split('\n\n')[0]

           # Check for 'r' mode (but allow 'rb')
           if "'r'" in func_code or '"r"' in func_code:
               self.assertTrue("'rb'" in func_code or '"rb"' in func_code,
                             "Should use 'rb' not 'r' for binary files")

       def test_compares_with_bytes(self):
           """Should compare header with bytes literal"""
           source = self.getEditorText()
           func_code = source.split('def read_image_header(')[1].split('\n\n')[0]
           self.assertIn("b'", func_code,
                        "Should compare with bytes literal (b'...')")

       def test_reads_correct_amount(self):
           """Should read 8 bytes for PNG header"""
           source = self.getEditorText()
           func_code = source.split('def read_image_header(')[1].split('\n\n')[0]
           self.assertIn('.read(8)', func_code,
                        "Should read 8 bytes for PNG header")

       def test_returns_png_file_on_match(self):
           """Should return 'PNG file' when header matches"""
           source = self.getEditorText()
           func_code = source.split('def read_image_header(')[1].split('\n\n')[0]
           self.assertIn('"PNG file"', func_code,
                        "Should return 'PNG file' when header matches")

       def test_returns_unknown_on_mismatch(self):
           """Should return 'Unknown' when header doesn't match"""
           source = self.getEditorText()
           func_code = source.split('def read_image_header(')[1].split('\n\n')[0]
           self.assertIn('"Unknown"', func_code,
                        "Should return 'Unknown' when header doesn't match")

       def test_uses_with_statement(self):
           """Should use context manager (with statement)"""
           source = self.getEditorText()
           func_code = source.split('def read_image_header(')[1].split('\n\n')[0]
           self.assertIn('with open(', func_code,
                        "Should use 'with open()' for file handling")

       def test_correct_png_signature(self):
           """Should check for correct PNG signature bytes"""
           source = self.getEditorText()
           func_code = source.split('def read_image_header(')[1].split('\n\n')[0]
           # PNG signature: \x89PNG\r\n\x1a\n
           self.assertIn('\\x89PNG', func_code,
                        "Should check for PNG signature starting with \\x89PNG")

       def test_binary_mode_format(self):
           """Binary mode should be properly formatted"""
           source = self.getEditorText()
           func_code = source.split('def read_image_header(')[1].split('\n\n')[0]

           # Should have 'rb' as a string
           has_rb = ("'rb'" in func_code or '"rb"' in func_code)
           self.assertTrue(has_rb,
                         "Should use 'rb' mode (as a string)")

       def test_no_mixed_type_comparison(self):
           """Code structure should avoid str/bytes comparison issues"""
           source = self.getEditorText()
           func_code = source.split('def read_image_header(')[1].split('\n\n')[0]

           # If using text mode 'r', can't properly compare to bytes
           has_text_mode = ("open(filename, 'r')" in func_code or
                           'open(filename, "r")' in func_code)
           has_bytes_compare = "b'" in func_code or 'b"' in func_code

           if has_text_mode and has_bytes_compare:
               self.fail("Can't compare text (from 'r' mode) with bytes literal - use 'rb' mode")

   myTests().main()

.. reveal:: pcap_debug_binary_mode_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Problems:**

   1. Opening binary file in text mode ('r') instead of binary mode ('rb')
   2. Text mode returns strings, but comparing with bytes literal

   **Fix:**

   .. code-block:: python

      def read_image_header(filename):
          with open(filename, 'rb') as f:  # Binary mode!
              header = f.read(8)

          # header is now bytes, comparison works
          if header == b'\x89PNG\r\n\x1a\n':
              return "PNG file"
          return "Unknown"

   **Key insights:**

   - **Text mode ('r')**: Returns strings, decodes bytes using encoding (usually UTF-8)
   - **Binary mode ('rb')**: Returns bytes objects, no decoding
   - **Use 'rb' for**: Images, audio, video, executables, any non-text files
   - **Use 'r' for**: Text files, CSV, JSON, source code
   - Can't compare ``str`` with ``bytes`` - types must match

---


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
