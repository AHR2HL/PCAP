..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Section 4: Practice and Mastery
================================

.. index:: PCAP practice, final assessment, mastery

Introduction
------------

**🎉 YOU'VE MADE IT TO THE FINAL PRACTICE SECTION!**

You've completed all instructional content for PCAP certification preparation. Now it's time to demonstrate your mastery of the final power topics:

- ✅ Advanced Exception Handling
- ✅ Advanced File I/O
- ✅ String Methods Mastery

This comprehensive assessment section includes:

- **Vocabulary Review** — test terminology knowledge
- **Conceptual Understanding** — verify deep understanding
- **Parsons Problems** — arrange code blocks correctly
- **Coding Challenges** — build complete solutions (10 challenges)
- **Debugging Challenges** — find and fix bugs (5 challenges)
- **Self-Assessment Checklist** — comprehensive skills inventory
- **Quick Reference Guide** — syntax at a glance

**This is it! Let's finish strong!** 🚀

---

Part 1: Vocabulary Review
--------------------------

.. index:: PCAP vocabulary, terminology

Test your understanding of key terminology:

.. mchoice:: pcap_vocab_assert
   :answer_a: A statement that always raises an error
   :answer_b: A debugging statement that checks a condition
   :answer_c: A way to catch exceptions
   :answer_d: A type of loop
   :correct: b
   :feedback_a: assert only raises an error if the condition is False.
   :feedback_b: Correct! assert checks conditions during development and can be disabled with -O.
   :feedback_c: That's try/except, not assert.
   :feedback_d: assert is not a loop construct.

   What is an ``assert`` statement?

.. mchoice:: pcap_vocab_bytearray
   :answer_a: An immutable sequence of bytes
   :answer_b: A mutable sequence of bytes
   :answer_c: A type of string
   :answer_d: A list of integers
   :correct: b
   :feedback_a: That's bytes, not bytearray. bytearray is mutable!
   :feedback_b: Correct! bytearray is like bytes but mutable—you can modify individual bytes.
   :feedback_c: bytearray is for binary data, not text.
   :feedback_d: While it holds byte values (0-255), it's specifically a bytearray type.

   What is a ``bytearray``?

.. mchoice:: pcap_vocab_errno
   :answer_a: A module for handling errors
   :answer_b: A module providing error code constants
   :answer_c: A type of exception
   :answer_d: A debugging tool
   :correct: b
   :feedback_a: It provides error codes, not general error handling.
   :feedback_b: Correct! errno provides standard POSIX error code constants like ENOENT, EACCES.
   :feedback_c: errno is a module, not an exception type.
   :feedback_d: It's for error codes, not debugging.

   What is the ``errno`` module?

.. mchoice:: pcap_vocab_stderr
   :answer_a: Standard input stream
   :answer_b: Standard output stream
   :answer_c: Standard error stream
   :answer_d: A type of exception
   :correct: c
   :feedback_a: That's stdin.
   :feedback_b: That's stdout.
   :feedback_c: Correct! stderr is the standard error stream for error messages and logging.
   :feedback_d: It's a stream, not an exception.

   What is ``sys.stderr``?

.. mchoice:: pcap_vocab_strip
   :answer_a: Removes characters from the middle
   :answer_b: Removes characters from both ends
   :answer_c: Removes all whitespace
   :answer_d: Converts to lowercase
   :correct: b
   :feedback_a: strip() only works on the ends, not the middle.
   :feedback_b: Correct! strip() removes specified characters from the beginning and end.
   :feedback_c: It removes from the ends only, not the entire string.
   :feedback_d: strip() doesn't change case.

   What does the ``strip()`` method do?

.. mchoice:: pcap_vocab_partition
   :answer_a: Splits string into list of parts
   :answer_b: Splits string at first occurrence into 3-tuple
   :answer_c: Divides string in half
   :answer_d: Removes a separator
   :correct: b
   :feedback_a: That's split(), not partition().
   :feedback_b: Correct! partition() returns (before, separator, after) as a 3-tuple.
   :feedback_c: It splits at the separator, not necessarily in half.
   :feedback_d: It splits at the separator, doesn't remove it.

   What does the ``partition()`` method return?

.. mchoice:: pcap_vocab_finally
   :answer_a: Runs only if an exception occurs
   :answer_b: Runs only if no exception occurs
   :answer_c: Always runs, regardless of exceptions
   :answer_d: Never runs
   :correct: c
   :feedback_a: That's the except clause.
   :feedback_b: That's the else clause.
   :feedback_c: Correct! finally ALWAYS runs—perfect for cleanup code.
   :feedback_d: finally always runs!

   When does the ``finally`` clause execute?

.. mchoice:: pcap_vocab_exception_chaining
   :answer_a: Catching multiple exceptions
   :answer_b: Raising a new exception while preserving the original
   :answer_c: A chain of try/except blocks
   :answer_d: Multiple except clauses
   :correct: b
   :feedback_a: That's multiple except clauses, not chaining.
   :feedback_b: Correct! Use "raise NewError() from original" to preserve the original exception.
   :feedback_c: That's nesting, not chaining.
   :feedback_d: That's multiple exception handling, not chaining.

   What is exception chaining?

---

Part 2: Conceptual Understanding
---------------------------------

.. index:: PCAP concepts, deep understanding

Test your conceptual understanding:

.. mchoice:: pcap_concept_assert_production
   :answer_a: Always use assert in production
   :answer_b: Never use assert in production
   :answer_c: assert is fine for production validation
   :answer_d: assert is required for error handling
   :correct: b
   :feedback_a: assert can be disabled with -O flag!
   :feedback_b: Correct! Don't use assert in production—it can be disabled and raises AssertionError.
   :feedback_c: Use proper exceptions for validation, not assert.
   :feedback_d: Use try/except for error handling, not assert.

   Should you use ``assert`` for production input validation?

.. mchoice:: pcap_concept_binary_mode
   :answer_a: Returns str objects
   :answer_b: Returns bytes objects
   :answer_c: Only for images
   :answer_d: Same as text mode
   :correct: b
   :feedback_a: Text mode returns str, binary mode returns bytes.
   :feedback_b: Correct! Binary mode ('rb', 'wb') returns bytes objects.
   :feedback_c: Binary mode is for ANY binary data, not just images.
   :feedback_d: They're very different!

   What does binary file mode return?

.. mchoice:: pcap_concept_context_manager
   :answer_a: Makes code faster
   :answer_b: Automatically closes files even on errors
   :answer_c: Only works with text files
   :answer_d: Prevents all errors
   :correct: b
   :feedback_a: Performance is the same; the benefit is automatic cleanup.
   :feedback_b: Correct! Context managers (with statement) guarantee cleanup even if exceptions occur.
   :feedback_c: Works with both text and binary files.
   :feedback_d: It ensures cleanup, not error prevention.

   What's the main benefit of using context managers (``with`` statement)?

.. mchoice:: pcap_concept_string_immutable
   :answer_a: String methods modify the original string
   :answer_b: String methods return new strings
   :answer_c: Strings can be changed in place
   :answer_d: String methods don't return anything
   :correct: b
   :feedback_a: Strings are immutable—they can't be modified!
   :feedback_b: Correct! String methods always return NEW strings; the original is unchanged.
   :feedback_c: Strings are immutable and cannot be changed in place.
   :feedback_d: String methods return new strings.

   How do string methods work with immutable strings?

.. mchoice:: pcap_concept_else_clause
   :answer_a: Runs if an exception occurs
   :answer_b: Runs if NO exception occurs
   :answer_c: Always runs
   :answer_d: Never runs
   :correct: b
   :feedback_a: That's the except clause.
   :feedback_b: Correct! The else clause runs only if the try block completed without exceptions.
   :feedback_c: That's finally.
   :feedback_d: else runs when no exception occurs.

   When does the ``else`` clause in try/except execute?

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

.. mchoice:: pcap_concept_find_vs_index
   :answer_a: They are identical
   :answer_b: find() returns -1, index() raises ValueError
   :answer_c: index() returns -1, find() raises ValueError
   :answer_d: find() is always better
   :correct: b
   :feedback_a: They handle "not found" differently!
   :feedback_b: Correct! find() returns -1 when not found; index() raises ValueError.
   :feedback_c: You have it backwards!
   :feedback_d: Each has appropriate use cases.

   What happens when a substring is not found in ``find()`` vs ``index()``?

.. mchoice:: pcap_concept_casefold
   :answer_a: Same as lower() for all strings
   :answer_b: More aggressive than lower() for Unicode
   :answer_c: Only works with ASCII
   :answer_d: Slower than lower()
   :correct: b
   :feedback_a: They differ for Unicode characters like German ß.
   :feedback_b: Correct! casefold() is more aggressive and better for case-insensitive comparisons.
   :feedback_c: casefold() is specifically better for Unicode!
   :feedback_d: Performance is similar; the difference is Unicode handling.

   How does ``casefold()`` differ from ``lower()``?

---

Part 3: Parsons Problems
-------------------------

.. index:: parsons problems, code arrangement

Arrange the code blocks in the correct order:

**Problem 1: Exception with Finally**

.. parsonsprob:: pcap_parsons_finally
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to create proper exception handling with finally clause.
   -----
   def process_file(filename):
   =====
       f = None
   =====
       try:
   =====
           f = open(filename, 'r')
   =====
           content = f.read()
   =====
           return content
   =====
       except FileNotFoundError:
   =====
           print("File not found")
   =====
           return None
   =====
       finally:
   =====
           if f is not None:
   =====
               f.close()

**Problem 2: Custom Exception**

.. parsonsprob:: pcap_parsons_custom_exception
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to create a custom exception class.
   -----
   class ValidationError(Exception):
   =====
   class ValidationError: #distractor
   =====
       def __init__(self, field, message):
   =====
           self.field = field
   =====
           self.message = message
   =====
           super().__init__(f"{field}: {message}")
   =====
           Exception.__init__(f"{field}: {message}") #distractor

**Problem 3: Binary File Reading**

.. parsonsprob:: pcap_parsons_binary_file
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to read and process a binary file.
   -----
   def read_binary_file(filename):
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

**Problem 4: String Processing Pipeline**

.. parsonsprob:: pcap_parsons_string_pipeline
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to clean and validate input string.
   -----
   def clean_input(text):
   =====
       cleaned = text.strip()
   =====
       cleaned = text.strip #distractor
   =====
       cleaned = cleaned.lower()
   =====
       if not cleaned.isalnum():
   =====
       if not cleaned.isalpha(): #distractor
   =====
           raise ValueError("Invalid input")
   =====
       return cleaned

**Problem 5: CSV Parsing**

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

---

Part 4: Coding Challenges
--------------------------

.. index:: coding challenges, PCAP practice

Build complete solutions from scratch!

**Challenge 1: Safe File Reader**

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

**Challenge 2: Exception Logger**

.. activecode:: pcap_code_exception_logger
   :language: python
   :autograde: unittest

   Create a function ``safe_divide(a, b)`` that:
   - Divides a by b
   - Returns result on success
   - Returns None and logs to stderr on error
   - Uses sys.stderr for error messages

   Example::

       result = safe_divide(10, 2)   # 5.0
       result = safe_divide(10, 0)   # None (logs error to stderr)

   ~~~~
   import sys

   def safe_divide(a, b):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_successful_division(self):
           result = safe_divide(10, 2)
           self.assertEqual(result, 5.0)

       def test_zero_division(self):
           result = safe_divide(10, 0)
           self.assertIsNone(result)

       def test_type_error(self):
           result = safe_divide("10", 2)
           self.assertIsNone(result)

   myTests().main()

.. reveal:: pcap_code_exception_logger_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      import sys

      def safe_divide(a, b):
          try:
              return a / b
          except ZeroDivisionError:
              sys.stderr.write("Error: Division by zero\n")
              return None
          except TypeError:
              sys.stderr.write("Error: Invalid types\n")
              return None

---

**Challenge 3: Binary Data Checker**

.. activecode:: pcap_code_binary_checker
   :language: python
   :autograde: unittest

   Create a function ``is_png_data(data)`` that:
   - Takes binary data (bytes)
   - Returns True if it's a PNG file signature
   - PNG signature: b'\\x89PNG\\r\\n\\x1a\\n'

   Example::

       png_sig = b'\x89PNG\r\n\x1a\n'
       is_png_data(png_sig)  # True
       is_png_data(b'JPEG')  # False

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

       def test_png_with_extra_data(self):
           png_sig = b'\x89PNG\r\n\x1a\nEXTRA DATA'
           self.assertTrue(is_png_data(png_sig))

       def test_not_png(self):
           self.assertFalse(is_png_data(b'JPEG'))

       def test_too_short(self):
           self.assertFalse(is_png_data(b'PNG'))

   myTests().main()

.. reveal:: pcap_code_binary_checker_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def is_png_data(data):
          png_signature = b'\x89PNG\r\n\x1a\n'
          if len(data) < len(png_signature):
              return False
          return data[:len(png_signature)] == png_signature

---

**Challenge 4: String Normalizer**

.. activecode:: pcap_code_string_normalizer
   :language: python
   :autograde: unittest

   Create a function ``normalize_string(text)`` that:
   - Strips whitespace
   - Converts to lowercase
   - Removes non-alphanumeric characters (keep spaces)
   - Normalizes multiple spaces to single space

   Example::

       normalize_string("  Hello,  World!  ")  # "hello world"
       normalize_string("Test@123")            # "test123"

   ~~~~
   def normalize_string(text):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_strips_whitespace(self):
           result = normalize_string("  hello  ")
           self.assertEqual(result, "hello")

       def test_lowercase(self):
           result = normalize_string("HELLO")
           self.assertEqual(result, "hello")

       def test_removes_special_chars(self):
           result = normalize_string("Hello, World!")
           self.assertEqual(result, "hello world")

       def test_normalizes_spaces(self):
           result = normalize_string("hello   world")
           self.assertEqual(result, "hello world")

   myTests().main()

.. reveal:: pcap_code_string_normalizer_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def normalize_string(text):
          # Strip and lowercase
          text = text.strip().lower()

          # Keep only alphanumeric and spaces
          cleaned = ''.join(c if c.isalnum() or c == ' ' else '' for c in text)

          # Normalize spaces
          return ' '.join(cleaned.split())

---

**Challenge 5: Email Validator**

.. activecode:: pcap_code_email_validator
   :language: python
   :autograde: unittest

   Create a function ``is_valid_email(email)`` that validates:
   - Contains exactly one '@'
   - Has content before and after '@'
   - Domain has at least one '.'
   - No spaces in email

   Example::

       is_valid_email("user@example.com")  # True
       is_valid_email("invalid")           # False
       is_valid_email("no@domain")         # False

   ~~~~
   def is_valid_email(email):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_valid_email(self):
           self.assertTrue(is_valid_email("user@example.com"))

       def test_no_at_sign(self):
           self.assertFalse(is_valid_email("invalid"))

       def test_multiple_at_signs(self):
           self.assertFalse(is_valid_email("user@@example.com"))

       def test_no_domain_dot(self):
           self.assertFalse(is_valid_email("user@domain"))

       def test_with_spaces(self):
           self.assertFalse(is_valid_email("user @example.com"))

   myTests().main()

.. reveal:: pcap_code_email_validator_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def is_valid_email(email):
          # Check for spaces
          if ' ' in email:
              return False

          # Check for exactly one @
          if email.count('@') != 1:
              return False

          # Split into parts
          local, domain = email.split('@')

          # Check for content
          if not local or not domain:
              return False

          # Check for dot in domain
          if '.' not in domain:
              return False

          return True

---

**Challenge 6: CSV Parser**

.. activecode:: pcap_code_csv_parser
   :language: python
   :autograde: unittest

   Create a function ``parse_csv(text)`` that:
   - Splits by newlines
   - Splits each line by commas
   - Strips whitespace from each field
   - Returns list of lists

   Example::

       csv = "name, age\nAlice, 30\nBob, 25"
       parse_csv(csv)
       # [['name', 'age'], ['Alice', '30'], ['Bob', '25']]

   ~~~~
   def parse_csv(text):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_basic_parsing(self):
           csv = "a,b\nc,d"
           result = parse_csv(csv)
           self.assertEqual(result, [['a', 'b'], ['c', 'd']])

       def test_strips_whitespace(self):
           csv = " a , b \n c , d "
           result = parse_csv(csv)
           self.assertEqual(result, [['a', 'b'], ['c', 'd']])

       def test_empty_string(self):
           result = parse_csv("")
           self.assertEqual(result, [])

   myTests().main()

.. reveal:: pcap_code_csv_parser_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def parse_csv(text):
          lines = text.split('\n')
          result = []
          for line in lines:
              fields = [field.strip() for field in line.split(',')]
              result.append(fields)
          return result

---

**Challenge 7: File Extension Validator**

.. activecode:: pcap_code_extension_validator
   :language: python
   :autograde: unittest

   Create a function ``has_valid_extension(filename, extensions)`` that:
   - Checks if filename ends with any of the given extensions
   - Case-insensitive comparison
   - extensions is a tuple of valid extensions

   Example::

       has_valid_extension("photo.jpg", ('.jpg', '.png'))  # True
       has_valid_extension("doc.PDF", ('.pdf', '.doc'))    # True
       has_valid_extension("file.txt", ('.jpg', '.png'))   # False

   ~~~~
   def has_valid_extension(filename, extensions):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_valid_extension(self):
           result = has_valid_extension("file.txt", ('.txt', '.pdf'))
           self.assertTrue(result)

       def test_case_insensitive(self):
           result = has_valid_extension("FILE.TXT", ('.txt', '.pdf'))
           self.assertTrue(result)

       def test_invalid_extension(self):
           result = has_valid_extension("file.jpg", ('.txt', '.pdf'))
           self.assertFalse(result)

   myTests().main()

.. reveal:: pcap_code_extension_validator_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def has_valid_extension(filename, extensions):
          filename_lower = filename.lower()
          extensions_lower = tuple(ext.lower() for ext in extensions)
          return filename_lower.endswith(extensions_lower)

---

**Challenge 8: Word Counter**

.. activecode:: pcap_code_word_counter
   :language: python
   :autograde: unittest

   Create a function ``count_words(text)`` that:
   - Counts occurrences of each word (case-insensitive)
   - Returns dictionary {word: count}
   - Ignores punctuation (keep only alphanumeric)

   Example::

       text = "Hello world! Hello Python."
       count_words(text)
       # {'hello': 2, 'world': 1, 'python': 1}

   ~~~~
   def count_words(text):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_basic_count(self):
           result = count_words("hello world hello")
           self.assertEqual(result, {'hello': 2, 'world': 1})

       def test_case_insensitive(self):
           result = count_words("Hello HELLO hello")
           self.assertEqual(result, {'hello': 3})

       def test_ignores_punctuation(self):
           result = count_words("hello, world!")
           self.assertEqual(result, {'hello': 1, 'world': 1})

   myTests().main()

.. reveal:: pcap_code_word_counter_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def count_words(text):
          # Remove non-alphanumeric except spaces
          cleaned = ''.join(c if c.isalnum() or c == ' ' else '' for c in text)

          # Split and lowercase
          words = cleaned.lower().split()

          # Count
          counts = {}
          for word in words:
              counts[word] = counts.get(word, 0) + 1

          return counts

---

**Challenge 9: Data Sanitizer**

.. activecode:: pcap_code_sanitizer
   :language: python
   :autograde: unittest

   Create a function ``sanitize_input(text, max_length=100)`` that:
   - Strips whitespace
   - Removes control characters (char code < 32)
   - Truncates to max_length if needed
   - Returns sanitized string

   Example::

       sanitize_input("  hello\\n\\tworld  ", 5)  # "hello"
       sanitize_input("test", 100)                 # "test"

   ~~~~
   def sanitize_input(text, max_length=100):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_strips_whitespace(self):
           result = sanitize_input("  hello  ")
           self.assertEqual(result, "hello")

       def test_removes_control_chars(self):
           result = sanitize_input("hello\nworld\t")
           self.assertEqual(result, "helloworld")

       def test_truncates(self):
           result = sanitize_input("hello world", 5)
           self.assertEqual(result, "hello")

   myTests().main()

.. reveal:: pcap_code_sanitizer_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def sanitize_input(text, max_length=100):
          # Strip whitespace
          text = text.strip()

          # Remove control characters
          cleaned = ''.join(c for c in text if ord(c) >= 32)

          # Truncate
          return cleaned[:max_length]

---

**Challenge 10: Log Parser**

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

Part 5: Debugging Challenges
-----------------------------

.. index:: debugging, bug fixing

Find and fix the bugs!

**Debug 1: Broken Exception Handling**

.. activecode:: pcap_debug_exception
   :language: python
   :autograde: unittest

   This code doesn't handle exceptions properly. Fix it!
   ~~~~
   def divide_numbers(a, b):
       try:
           result = a / b
       except:
           print("Error occurred")

       return result

   print(divide_numbers(10, 2))
   print(divide_numbers(10, 0))

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_normal_division(self):
           """Should correctly divide two numbers"""
           result = divide_numbers(10, 2)
           self.assertEqual(result, 5.0, "10 / 2 should equal 5.0")

       def test_division_with_floats(self):
           """Should handle float division"""
           result = divide_numbers(7, 2)
           self.assertEqual(result, 3.5, "7 / 2 should equal 3.5")

       def test_zero_division_returns_value(self):
           """Should return a value (not crash) when dividing by zero"""
           result = divide_numbers(10, 0)
           self.assertIsNotNone(result, "Should return None instead of crashing")

       def test_zero_division_does_not_crash(self):
           """Should not raise exception when dividing by zero"""
           try:
               result = divide_numbers(10, 0)
               crashed = False
           except:
               crashed = True
           self.assertFalse(crashed, "Should handle division by zero without crashing")

       def test_catches_specific_exception(self):
           """Should catch ZeroDivisionError specifically"""
           source = self.getEditorText()
           func_code = source.split('def divide_numbers(')[1].split('\n\n')[0]
           self.assertIn('ZeroDivisionError', func_code,
                        "Should catch ZeroDivisionError specifically, not bare except")

       def test_no_bare_except(self):
           """Should not use bare except:"""
           source = self.getEditorText()
           func_code = source.split('def divide_numbers(')[1].split('\n\n')[0]

           # Check for bare except (except: with no exception type)
           lines = func_code.split('\n')
           for line in lines:
               if 'except' in line and ':' in line:
                   # Make sure there's something between 'except' and ':'
                   except_part = line.split('except')[1].split(':')[0].strip()
                   if except_part == '':
                       self.fail("Should not use bare 'except:' - specify exception type")

       def test_negative_numbers(self):
           """Should handle negative numbers"""
           result = divide_numbers(-10, 2)
           self.assertEqual(result, -5.0)

       def test_type_error_handled(self):
           """Should handle invalid types gracefully"""
           result = divide_numbers("10", 2)
           # Should return None or handle gracefully, not crash
           self.assertTrue(result is None or isinstance(result, (int, float)),
                         "Should handle type errors gracefully")

       def test_returns_none_on_error(self):
           """Should return None when error occurs"""
           result = divide_numbers(10, 0)
           self.assertIsNone(result, "Should return None when division by zero occurs")

   myTests().main()

.. reveal:: pcap_debug_exception_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Problems:**

   1. Bare ``except:`` catches everything (bad practice)
   2. ``result`` not defined if exception occurs (UnboundLocalError)
   3. ``return`` is outside try/except block

   **Fix:**

   .. code-block:: python

      def divide_numbers(a, b):
          try:
              result = a / b
              return result
          except ZeroDivisionError:
              print("Error: Division by zero")
              return None
          except TypeError:
              print("Error: Invalid types")
              return None

   **Key insights:**

   - Never use bare ``except:`` - always specify exception types
   - Return inside the try block OR ensure variable is always defined
   - Handle specific exceptions (ZeroDivisionError, TypeError, etc.)

---

**Debug 2: File Not Closing**

.. activecode:: pcap_debug_file_closing
   :language: python
   :autograde: unittest

   This code doesn't properly close files. Fix it!
   ~~~~
   def read_and_process(filename):
       f = open(filename, 'r')
       data = f.read()

       if len(data) == 0:
           return None

       result = data.upper()
       f.close()
       return result

   print("Testing file handling...")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_uses_context_manager(self):
           """Should use 'with' statement for file handling"""
           source = self.getEditorText()
           func_code = source.split('def read_and_process(')[1].split('\n\n')[0]
           self.assertIn('with open(', func_code,
                        "Should use 'with open()' context manager")

       def test_no_manual_close(self):
           """Should not manually call f.close() when using context manager"""
           source = self.getEditorText()
           func_code = source.split('def read_and_process(')[1].split('\n\n')[0]

           # If using 'with', should not have manual close
           if 'with open(' in func_code:
               self.assertNotIn('.close()', func_code,
                              "Don't need manual .close() when using 'with' statement")

       def test_no_bare_open(self):
           """Should not use open() without context manager"""
           source = self.getEditorText()
           func_code = source.split('def read_and_process(')[1].split('\n\n')[0]

           # Check if open is used without 'with'
           lines = func_code.split('\n')
           for line in lines:
               if 'open(' in line and 'with' not in line:
                   self.fail("Should use 'with open()' not bare 'open()' assignment")

       def test_simulated_normal_file(self):
           """Test logic with simulated file content"""
           # Create a mock file-like object
           class MockFile:
               def __init__(self, content):
                   self.content = content
                   self.closed = False

               def read(self):
                   return self.content

               def close(self):
                   self.closed = True

               def __enter__(self):
                   return self

               def __exit__(self, *args):
                   self.closed = True

           # Test that logic would work correctly
           # We can't actually test the function directly in Skulpt,
           # but we verify the structure is correct
           source = self.getEditorText()
           self.assertIn('data.upper()', source,
                        "Should still convert data to uppercase")

       def test_handles_empty_file_case(self):
           """Should handle empty file by returning None"""
           source = self.getEditorText()
           func_code = source.split('def read_and_process(')[1].split('\n\n')[0]
           self.assertIn('return None', func_code,
                        "Should return None for empty data")
           self.assertIn('len(data) == 0', func_code,
                        "Should check if data is empty")

       def test_returns_uppercase(self):
           """Should return uppercase version of data"""
           source = self.getEditorText()
           func_code = source.split('def read_and_process(')[1].split('\n\n')[0]
           self.assertIn('.upper()', func_code,
                        "Should convert data to uppercase")

       def test_proper_indentation_with_context_manager(self):
           """Code inside 'with' block should be properly indented"""
           source = self.getEditorText()
           func_code = source.split('def read_and_process(')[1].split('\n\n')[0]

           if 'with open(' in func_code:
               # Find the with statement and check following lines are indented
               lines = func_code.split('\n')
               with_line_idx = None
               for i, line in enumerate(lines):
                   if 'with open(' in line:
                       with_line_idx = i
                       break

               if with_line_idx is not None and with_line_idx + 1 < len(lines):
                   # Next line should be more indented
                   with_indent = len(lines[with_line_idx]) - len(lines[with_line_idx].lstrip())
                   next_indent = len(lines[with_line_idx + 1]) - len(lines[with_line_idx + 1].lstrip())
                   self.assertGreater(next_indent, with_indent,
                                    "Code inside 'with' block should be indented")

       def test_returns_result_not_variable(self):
           """Should return data.upper() directly or store then return"""
           source = self.getEditorText()
           func_code = source.split('def read_and_process(')[1].split('\n\n')[0]
           # Should have return statement with upper()
           has_return = 'return' in func_code and '.upper()' in func_code
           self.assertTrue(has_return, "Should return the uppercase result")

       def test_as_variable_used_with_context_manager(self):
           """Should use 'as' to assign file handle in context manager"""
           source = self.getEditorText()
           func_code = source.split('def read_and_process(')[1].split('\n\n')[0]

           if 'with open(' in func_code:
               self.assertIn(' as ', func_code,
                           "Should use 'as' to assign file handle: 'with open(...) as f:'")

   myTests().main()

.. reveal:: pcap_debug_file_closing_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Problem:** File isn't closed if function returns early (when data is empty). Manual ``f.close()`` is only reached if execution continues to that line.

   **Fix:**

   .. code-block:: python

      def read_and_process(filename):
          with open(filename, 'r') as f:
              data = f.read()

              if len(data) == 0:
                  return None

              return data.upper()
          # File automatically closed here, even with early return

   **Key insight:** Context managers (``with`` statement) **guarantee** cleanup happens, even with early returns or exceptions. The file is closed when exiting the ``with`` block, regardless of how you exit.

---

**Debug 3: String Modification Bug**

.. activecode:: pcap_debug_string_modification
   :language: python
   :autograde: unittest

   This code tries to modify a string but fails. Fix it!
   ~~~~
   def capitalize_words(text):
       words = text.split()

       for word in words:
           word.capitalize()

       return ' '.join(words)

   result = capitalize_words("hello world")
   print(f"Result: '{result}'")
   print("Expected: 'Hello World'")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_capitalizes_hello_world(self):
           """Should capitalize 'hello world' to 'Hello World'"""
           result = capitalize_words("hello world")
           self.assertEqual(result, "Hello World",
                          "Should capitalize each word")

       def test_capitalizes_single_word(self):
           """Should capitalize single word"""
           result = capitalize_words("python")
           self.assertEqual(result, "Python")

       def test_capitalizes_multiple_words(self):
           """Should capitalize multiple words"""
           result = capitalize_words("the quick brown fox")
           self.assertEqual(result, "The Quick Brown Fox")

       def test_handles_already_capitalized(self):
           """Should handle already capitalized words"""
           result = capitalize_words("Hello World")
           self.assertEqual(result, "Hello World")

       def test_handles_mixed_case(self):
           """Should handle mixed case input"""
           result = capitalize_words("hELLo WoRLd")
           self.assertEqual(result, "Hello World")

       def test_captures_capitalize_result(self):
           """Should capture the return value of capitalize()"""
           source = self.getEditorText()
           func_code = source.split('def capitalize_words(')[1].split('\n\n')[0]

           # Should either use list comprehension, assignment, or build new list
           has_capture = (
               '[' in func_code and 'for' in func_code and ']' in func_code  # List comp
               or 'append(' in func_code  # Building list
               or '=' in func_code and 'capitalize()' in func_code  # Assignment
               or '.title()' in func_code  # Using title() method
           )
           self.assertTrue(has_capture,
                         "Should capture the result of capitalize() or use .title()")

       def test_not_modifying_in_place(self):
           """Should not try to modify strings in place"""
           source = self.getEditorText()
           func_code = source.split('def capitalize_words(')[1].split('\n\n')[0]

           # Check if there's a standalone capitalize() call (not assigned)
           lines = func_code.split('\n')
           for line in lines:
               line_stripped = line.strip()
               # Look for capitalize() that's not being assigned or used
               if 'capitalize()' in line_stripped:
                   # Check if it's standalone (not assigned, not in list comp, not in return)
                   if '=' not in line_stripped and '[' not in line_stripped and 'return' not in line_stripped:
                       self.fail("Don't call capitalize() without capturing its return value")

       def test_handles_empty_string(self):
           """Should handle empty string"""
           result = capitalize_words("")
           self.assertEqual(result, "")

       def test_handles_single_letter_words(self):
           """Should handle single letter words"""
           result = capitalize_words("a b c")
           self.assertEqual(result, "A B C")

       def test_preserves_spacing(self):
           """Should preserve single space between words"""
           result = capitalize_words("hello world")
           self.assertEqual(result.count(' '), 1,
                          "Should have single space between words")

   myTests().main()

.. reveal:: pcap_debug_string_modification_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Problem:** ``capitalize()`` returns a new string but doesn't modify the original. The returned value is ignored, so ``words`` list remains unchanged.

   **Fix Option 1 (List Comprehension):**

   .. code-block:: python

      def capitalize_words(text):
          words = text.split()
          capitalized = [word.capitalize() for word in words]
          return ' '.join(capitalized)

   **Fix Option 2 (Append to New List):**

   .. code-block:: python

      def capitalize_words(text):
          words = text.split()
          capitalized = []
          for word in words:
              capitalized.append(word.capitalize())  # Capture result
          return ' '.join(capitalized)

   **Fix Option 3 (Built-in Method):**

   .. code-block:: python

      def capitalize_words(text):
          return text.title()  # Simpler!

   **Key insight:** Strings are **immutable** in Python. String methods like ``capitalize()``, ``upper()``, ``lower()`` return **new strings** and don't modify the original. Always capture the return value.

---

**Debug 4: Binary Mode Mistake**

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

**Debug 5: Strip Misunderstanding**

.. activecode:: pcap_debug_strip
   :language: python
   :autograde: unittest

   This code doesn't remove all intended characters. Fix it!
   ~~~~
   def clean_string(text):
       cleaned = text.strip('*')
       return cleaned

   test = "**hello*world**"
   result = clean_string(test)
   print(f"Result: '{result}'")
   print("Expected: 'helloworld'")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_removes_all_asterisks(self):
           """Should remove ALL asterisks, not just from ends"""
           result = clean_string("**hello*world**")
           self.assertEqual(result, "helloworld",
                          "Should remove asterisks from middle too, not just ends")

       def test_asterisks_in_middle_only(self):
           """Should remove asterisks from middle"""
           result = clean_string("hello*world")
           self.assertEqual(result, "helloworld",
                          "Should remove asterisks from the middle")

       def test_asterisks_at_ends_only(self):
           """Should remove asterisks from ends"""
           result = clean_string("**hello**")
           self.assertEqual(result, "hello")

       def test_multiple_asterisks_scattered(self):
           """Should remove all asterisks regardless of position"""
           result = clean_string("*a*b*c*")
           self.assertEqual(result, "abc")

       def test_no_asterisks(self):
           """Should handle strings without asterisks"""
           result = clean_string("hello")
           self.assertEqual(result, "hello")

       def test_only_asterisks(self):
           """Should return empty string for only asterisks"""
           result = clean_string("***")
           self.assertEqual(result, "")

       def test_uses_replace_or_alternative(self):
           """Should use replace() or another method to remove all occurrences"""
           source = self.getEditorText()
           func_code = source.split('def clean_string(')[1].split('\n\n')[0]

           # Should use replace, or translate, or list comprehension, etc.
           has_solution = (
               '.replace(' in func_code or
               '.translate(' in func_code or
               '[' in func_code and 'for' in func_code and 'if' in func_code or  # List comp with filter
               ''.join' in func_code
           )
           self.assertTrue(has_solution,
                         "Should use replace() or another method to remove ALL asterisks")

       def test_not_relying_only_on_strip(self):
           """Strip alone is not sufficient for this task"""
           result = clean_string("**hello*world**")
           # The key test: if there's an asterisk in the middle, strip() alone won't work
           self.assertNotIn('*', result,
                          "Result should not contain any asterisks (strip() alone won't work)")

       def test_consecutive_asterisks(self):
           """Should handle consecutive asterisks"""
           result = clean_string("hello***world")
           self.assertEqual(result, "helloworld")

       def test_empty_string(self):
           """Should handle empty string"""
           result = clean_string("")
           self.assertEqual(result, "")

       def test_mixed_content(self):
           """Should only remove asterisks, keep other characters"""
           result = clean_string("*hello!@#world*")
           self.assertEqual(result, "hello!@#world",
                          "Should keep other special characters")

       def test_spaces_preserved(self):
           """Should preserve spaces while removing asterisks"""
           result = clean_string("*hello * world*")
           self.assertEqual(result, "hello  world",
                          "Should preserve spaces")

   myTests().main()

.. reveal:: pcap_debug_strip_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Problem:** ``strip()`` only removes characters from the **beginning and end** of a string, not from the middle.

   **Fix:**

   .. code-block:: python

      def clean_string(text):
          return text.replace('*', '')  # Removes ALL occurrences

   **Alternative solutions:**

   .. code-block:: python

      # Using filter and join
      def clean_string(text):
          return ''.join(char for char in text if char != '*')

      # Using translate (for multiple characters)
      def clean_string(text):
          return text.translate(str.maketrans('', '', '*'))

   **Key insight:**

   - ``strip('*')`` → Removes '*' from **start and end only**
   - ``replace('*', '')`` → Removes '*' from **everywhere**
   - ``lstrip('*')`` → Removes from **start only**
   - ``rstrip('*')`` → Removes from **end only**

---

Part 6: Self-Assessment Checklist
----------------------------------

.. index:: skills checklist, self-assessment

Check off the skills you've mastered:

**Exception Handling**

.. code-block:: text

   □ I understand assert and when (not) to use it
   □ I can use the else clause in try/except
   □ I can use the finally clause for cleanup
   □ I know the execution order: try → except/else → finally
   □ I can create custom exception classes
   □ I can build exception hierarchies
   □ I can chain exceptions with 'from'
   □ I know best practices for exception handling

**File I/O**

.. code-block:: text

   □ I understand text vs binary file modes
   □ I can work with binary data using bytes
   □ I can use bytearray for mutable binary data
   □ I understand the errno module for error codes
   □ I can use stdin, stdout, stderr appropriately
   □ I know when to use read() vs readline() vs readlines()
   □ I always use context managers (with statement)
   □ I handle file errors appropriately

**String Methods**

.. code-block:: text

   □ I know strings are immutable
   □ I can use case methods (upper, lower, capitalize, title, casefold)
   □ I can search strings (find, rfind, index, count)
   □ I can validate strings (isalpha, isdigit, isalnum, etc.)
   □ I can modify strings (strip, replace)
   □ I can split and join strings
   □ I can align strings (center, ljust, rjust, zfill)
   □ I can test patterns (startswith, endswith)
   □ I use casefold() for case-insensitive comparisons
   □ I know the difference between find() and index()

**Best Practices**

.. code-block:: text

   □ I don't use assert for production validation
   □ I use specific exception types, not bare except
   □ I always use context managers for files
   □ I specify encoding when opening text files
   □ I use binary mode for binary data
   □ I process large files line by line
   □ I remember strings are immutable
   □ I use appropriate string methods for the task

---

Part 7: Quick Reference Guide
------------------------------

.. index:: quick reference, cheat sheet

**Exception Handling**

.. code-block:: python

   # Assert (debugging only!)
   assert condition, "message"

   # Complete exception structure
   try:
       risky_operation()
   except SpecificError as e:
       handle_error(e)
   else:
       success_code()  # Runs if NO exception
   finally:
       cleanup()  # ALWAYS runs

   # Custom exceptions
   class MyError(Exception):
       def __init__(self, message):
           super().__init__(message)

   # Exception chaining
   raise NewError("message") from original_exception

---

**File I/O**

.. code-block:: python

   # Text file
   with open('file.txt', 'r', encoding='utf-8') as f:
       content = f.read()

   # Binary file
   with open('file.bin', 'rb') as f:
       data = f.read()

   # Read methods
   f.read()        # Entire file
   f.read(size)    # Up to size bytes/chars
   f.readline()    # One line
   f.readlines()   # All lines as list

   # Iterate (best for large files)
   for line in f:
       process(line)

   # bytearray (mutable bytes)
   data = bytearray(b"hello")
   data[0] = ord('H')  # Modify

   # Standard streams
   import sys
   sys.stdin.read()
   sys.stdout.write("output\n")
   sys.stderr.write("error\n")

---

**String Methods**

.. code-block:: python

   # Case
   s.upper()       # UPPERCASE
   s.lower()       # lowercase
   s.capitalize()  # First char upper
   s.title()       # Title Case
   s.casefold()    # Aggressive lowercase (use for comparisons)

   # Search
   s.find(sub)     # Index or -1
   s.index(sub)    # Index or ValueError
   s.count(sub)    # Number of occurrences

   # Validation
   s.isalpha()     # All letters?
   s.isdigit()     # All digits?
   s.isalnum()     # Letters or digits?
   s.isspace()     # All whitespace?
   s.isupper()     # All uppercase?
   s.islower()     # All lowercase?

   # Modification
   s.strip()       # Remove from both ends
   s.lstrip()      # Remove from left
   s.rstrip()      # Remove from right
   s.replace(old, new)  # Replace substring

   # Split/Join
   s.split(sep)    # Split into list
   sep.join(list)  # Join list with separator
   s.partition(sep)  # Split at first sep (3-tuple)
   s.splitlines()  # Split on line breaks

   # Alignment
   s.center(width)   # Center
   s.ljust(width)    # Left justify
   s.rjust(width)    # Right justify
   s.zfill(width)    # Pad with zeros

   # Testing
   s.startswith(prefix)  # Starts with?
   s.endswith(suffix)    # Ends with?
   sub in s              # Contains?

---

**Decision Guides**

.. code-block:: text

   Use assert when:
   ✓ Debugging during development
   ✓ Checking internal invariants
   ✗ NOT for input validation
   ✗ NOT in production code

   Use finally when:
   ✓ Need guaranteed cleanup
   ✓ Releasing resources
   ✓ Closing connections

   Use else when:
   ✓ Success code separate from error handling
   ✓ Code shouldn't catch its own exceptions

   Use binary mode when:
   ✓ Images, videos, executables
   ✓ Any non-text data
   ✗ NOT for text files

   Use context managers when:
   ✓ Opening files (ALWAYS!)
   ✓ Any resource that needs cleanup

   Use casefold() when:
   ✓ Case-insensitive comparisons
   ✓ Working with Unicode

   Use find() when:
   ✓ -1 is acceptable return value
   ✓ You'll check the result

   Use index() when:
   ✓ You want exceptions on not found
   ✓ Substring must exist

---

🎉 CONGRATULATIONS! 🎉
-----------------------

.. important::
   **YOU DID IT! YOU'VE COMPLETED THE ENTIRE PCAP PREPARATION COURSE!**

   **🏆 ACHIEVEMENT UNLOCKED: PCAP Master 🏆**

   You've completed:

   ✅ **Chapter 26: Advanced Modules and Packages**
      - math module, platform module
      - Package creation and imports
      - pip and virtual environments

   ✅ **Chapter 27: Closures and Advanced Functions**
      - Closures and LEGB scope
      - Decorators and patterns
      - State management and encapsulation

   ✅ **Chapter 28: Advanced OOP Mastery**
      - Introspection (hasattr, getattr, dir, __dict__)
      - Type checking (isinstance, issubclass)
      - Identity vs equality (is vs ==)
      - Multiple inheritance and MRO
      - Polymorphism and ABCs

   ✅ **Chapter 29: PCAP Power Topics**
      - Advanced exception handling
      - Advanced file I/O
      - String methods mastery

   **📊 Your Achievement Stats:**

   - 📚 4 Complete Chapters
   - 📖 29 Comprehensive Sections
   - 💻 200+ Interactive Examples
   - ✅ 150+ MCQs
   - 🧩 20+ Parsons Problems
   - 🔧 40+ Coding Challenges
   - 🐛 20+ Debugging Challenges
   - 📝 Complete Reference Guides

   **You are now ready for PCAP certification!**

   **Next Steps:**

   1. 📖 Review the quick reference guides
   2. ✅ Complete any remaining challenges
   3. 🔄 Revisit sections where you need more practice
   4. 📝 Take practice PCAP exams
   5. 🎯 Schedule your PCAP certification exam

   **Remember:**

   - You've learned advanced Python concepts
   - You've practiced with real-world examples
   - You've solved complex problems
   - You're ready to succeed!

   **Good luck on your PCAP certification! You've got this! 🚀**

---

.. note::
   **✅ Chapter 29: PCAP Power Topics - COMPLETE!**

   **✅ ENTIRE COURSE - COMPLETE!**

   You've learned:
   - [✓] Advanced exception handling
   - [✓] Advanced file I/O
   - [✓] String methods mastery
   - [✓] 40+ coding challenges across all chapters
   - [✓] Complete PCAP exam preparation

   **🎊 CONGRATULATIONS ON COMPLETING THE COURSE! 🎊**