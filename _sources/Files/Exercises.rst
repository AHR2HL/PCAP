..  Copyright (C)  Alpha Schools

:skipreading:`True`

.. qnum::
   :prefix: files-9-
   :start: 1

Exercises
=========

Multiple Choice Questions
-------------------------

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


.. mchoice:: files_ex_mc4
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


.. mchoice:: files_ex_mc5
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


.. mchoice:: files_ex_mc6
   :answer_a: errno.ENOENT
   :answer_b: errno.EACCES
   :answer_c: errno.EISDIR
   :answer_d: errno.ENOTDIR
   :correct: a
   :feedback_a: Correct! ENOENT (Error NO ENTry) means "No such file or directory"
   :feedback_b: EACCES means "Permission denied"
   :feedback_c: EISDIR means "Is a directory"
   :feedback_d: ENOTDIR means "Not a directory"

   Which errno constant indicates "file not found"?


Parson's Problems
-----------------

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


.. parsonsprob:: files_ex_parsons2
   :language: python
   :adaptive:
   :numbered: left

   Arrange blocks to handle file opening with errno error checking.
   -----
   import errno
   =====
   def safe_open(filename):
   =====
       try:
   =====
           with open(filename, 'r') as f:
   =====
           with open(filename, 'rb') as f: #distractor
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


Active Code Problems
--------------------

.. activecode:: pcap_code_binary_checker
   :language: python
   :autograde: unittest

   **Problem 1:** Create a function ``is_png_data(data)`` that:

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

.. activecode:: files_ex_ac2
   :language: python
   :autograde: unittest

   **Problem 2:** Create a function ``modify_string(text, position, new_char)`` that:

   - Takes a string and converts it to a list (since strings are immutable)
   - Modifies the character at the given position
   - Returns the modified string

   Remember: strings are immutable in Python, so you need to convert to a list, modify, then convert back!

   Example::

       result = modify_string('Hello', 0, 'J')
       print(result)  # 'Jello'

   ~~~~
   def modify_string(text, position, new_char):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def test_basic_modification(self):
           result = modify_string('Hello', 0, 'J')
           self.assertEqual(result, 'Jello', "Testing modification at start")
           self.assertEqual(type(result), str, "Result should be a string")

       def test_middle_modification(self):
           result = modify_string('Python', 2, 'X')
           self.assertEqual(result, 'PyXhon', "Testing modification in middle")

       def test_last_modification(self):
           result = modify_string('Test', 3, '!')
           self.assertEqual(result, 'Tes!', "Testing modification at end")

       def test_uses_list(self):
           # Check that they converted to list
           code = self.getEditorText()
           self.assertTrue('list(' in code or '[' in code, "Make sure you convert the string to a list for modification")

   myTests().main()


.. activecode:: files_ex_ac3
   :language: python
   :autograde: unittest

   **Problem 3:** Create a function ``categorize_error(error_code)`` that takes an error code number and returns a category string:

   - Error code 2 → "File Not Found"
   - Error code 13 → "Permission Denied"
   - Error code 21 → "Is Directory"
   - Error code 17 → "File Exists"
   - Any other → "Unknown Error"

   These error codes simulate common file system errors you might encounter when working with files.

   ~~~~
   def categorize_error(error_code):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def test_file_not_found(self):
           self.assertEqual(categorize_error(2), "File Not Found", "Testing error code 2")

       def test_permission_denied(self):
           self.assertEqual(categorize_error(13), "Permission Denied", "Testing error code 13")

       def test_is_directory(self):
           self.assertEqual(categorize_error(21), "Is Directory", "Testing error code 21")

       def test_file_exists(self):
           self.assertEqual(categorize_error(17), "File Exists", "Testing error code 17")

       def test_unknown(self):
           self.assertEqual(categorize_error(999), "Unknown Error", "Testing unknown error code")

       def test_another_unknown(self):
           self.assertEqual(categorize_error(42), "Unknown Error", "Testing another unknown code")

   myTests().main()


.. activecode:: files_ex_ac4
   :language: python
   :autograde: unittest

   **Problem 4:** Create a function ``write_to_stream(message, is_error=False)`` that:

   - Writes to sys.stdout if is_error is False
   - Writes to sys.stderr if is_error is True
   - Adds a newline to the message
   - Returns the stream it wrote to

   ~~~~
   import sys

   def write_to_stream(message, is_error=False):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_normal_output(self):
           result = write_to_stream("Hello")
           self.assertEqual(result, sys.stdout)

       def test_error_output(self):
           result = write_to_stream("Error", is_error=True)
           self.assertEqual(result, sys.stderr)

   myTests().main()


.. activecode:: files_ex_ac5
   :language: python
   :autograde: unittest

   **Problem 5:** Create a function ``choose_mode(need_read, need_write, is_binary)`` that returns the appropriate file mode string:

   - read only + text → 'r'
   - read only + binary → 'rb'
   - write only + text → 'w'
   - write only + binary → 'wb'
   - read and write + text → 'r+'
   - read and write + binary → 'rb+'

   ~~~~
   def choose_mode(need_read, need_write, is_binary):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_read_text(self):
           self.assertEqual(choose_mode(True, False, False), 'r')

       def test_read_binary(self):
           self.assertEqual(choose_mode(True, False, True), 'rb')

       def test_write_text(self):
           self.assertEqual(choose_mode(False, True, False), 'w')

       def test_write_binary(self):
           self.assertEqual(choose_mode(False, True, True), 'wb')

       def test_readwrite_text(self):
           self.assertEqual(choose_mode(True, True, False), 'r+')

       def test_readwrite_binary(self):
           self.assertEqual(choose_mode(True, True, True), 'rb+')

   myTests().main()


.. activecode:: files_ex_ac6
   :language: python
   :autograde: unittest

   **Problem 6:** Create a function ``xor_encrypt(text, key)`` that implements simple XOR encryption:

   - Takes a string and a key (integer 0-255)
   - XORs each character's ASCII value with the key
   - Returns the encrypted string

   **How XOR encryption works:**

   - Convert each character to its ASCII value using ``ord()``
   - XOR it with the key: ``ord(char) ^ key``
   - Convert back to a character using ``chr()``

   **Fun fact:** XOR encryption is reversible - encrypting twice with the same key returns the original!

   Example::

       encrypted = xor_encrypt('ABC', 42)
       decrypted = xor_encrypt(encrypted, 42)  # Back to 'ABC'!

   ~~~~
   def xor_encrypt(text, key):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def test_basic_encryption(self):
           original = 'ABC'
           encrypted = xor_encrypt(original, 42)
           # XOR twice returns original
           decrypted = xor_encrypt(encrypted, 42)
           self.assertEqual(decrypted, original, "XOR encryption should be reversible")

       def test_returns_string(self):
           result = xor_encrypt('Test', 10)
           self.assertEqual(type(result), str, "Should return a string")

       def test_different_key(self):
           data = 'Hello'
           result1 = xor_encrypt(data, 5)
           result2 = xor_encrypt(data, 10)
           self.assertNotEqual(result1, result2, "Different keys should produce different results")

       def test_reversible(self):
           original = 'Python123'
           key = 77
           encrypted = xor_encrypt(original, key)
           decrypted = xor_encrypt(encrypted, key)
           self.assertEqual(decrypted, original, "Double encryption should return original")

       def test_empty_string(self):
           result = xor_encrypt('', 42)
           self.assertEqual(result, '', "Empty string should return empty string")

   myTests().main()


Debugging Exercises
-------------------

.. activecode:: pcap_debug_file_closing
   :language: python
   :autograde: unittest

   **Debug Exercise 1:** This code doesn't properly close files. Fix it to use context managers!
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
           source = self.getEditorText()
           self.assertIn('with open(', source, "Should use 'with open()' context manager")

       def test_no_manual_close(self):
           source = self.getEditorText()
           if 'with open(' in source:
               self.assertNotIn('.close()', source, "Don't need manual .close() with 'with' statement")

   myTests().main()


.. activecode:: files_ex_debug2
   :language: python
   :autograde: unittest

   **Debug Exercise 2:** This code tries to read a binary file as text. Fix the file mode!
   ~~~~
   def read_image_header(filename):
       # Should read first 8 bytes of binary file
       with open(filename, 'r') as f:
           header = f.read(8)
       return header

   # Test with simulated PNG signature
   print("Testing with binary data...")

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_uses_binary_mode(self):
           source = self.getEditorText()
           self.assertIn("'rb'", source, "Should use 'rb' mode for binary files")

   myTests().main()


.. activecode:: files_ex_debug3
   :language: python
   :autograde: unittest

   **Debug Exercise 3:** This error handler checks the wrong errno constant. Fix it!
   ~~~~
   import errno

   def safe_read(filename):
       try:
           with open(filename, 'r') as f:
               return f.read()
       except OSError as e:
           if e.errno == errno.EACCES:  # Wrong constant!
               print("File not found")
               return None
           else:
               raise

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_uses_enoent(self):
           source = self.getEditorText()
           self.assertIn('errno.ENOENT', source, "Should use errno.ENOENT for file not found")
           self.assertNotIn('errno.EACCES', source.split('if e.errno ==')[1].split('\n')[0],
                          "EACCES is permission denied, not file not found")

   myTests().main()


Active Code Problems
--------------------

.. activecode:: files_ex_ac1
   :language: python
   :autograde: unittest

   **Problem 7:** Write a function ``string_to_list_upper(text)`` that demonstrates working with mutable data:

   - Takes a string
   - Converts to a list of characters (since strings are immutable)
   - Converts all alphabetic characters to uppercase
   - Returns as a string

   This demonstrates the concept of converting immutable data (strings) to mutable data (lists) for modification!

   ~~~~
   def string_to_list_upper(text):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def test_basic(self):
           result = string_to_list_upper('hello')
           self.assertEqual(result, 'HELLO', "Should convert 'hello' to 'HELLO'")

       def test_mixed_case(self):
           result = string_to_list_upper('HeLLo WoRLd')
           self.assertEqual(result, 'HELLO WORLD', "Should handle mixed case")

       def test_returns_string(self):
           result = string_to_list_upper('test')
           self.assertEqual(type(result), str, "Should return a string")

       def test_with_numbers(self):
           result = string_to_list_upper('test123')
           self.assertEqual(result, 'TEST123', "Should keep numbers unchanged")

       def test_with_punctuation(self):
           result = string_to_list_upper('hello, world!')
           self.assertEqual(result, 'HELLO, WORLD!', "Should keep punctuation unchanged")

   myTests().main()


.. activecode:: files_ex_ac8
   :language: python
   :autograde: unittest

   **Problem 8 (Challenge):** Create a function ``create_binary_header(file_type, version, size)`` that:

   - Takes file_type (string, max 4 chars), version (int 0-255), size (int 0-65535)
   - Returns bytes object with:
     - First 4 bytes: file_type (padded with spaces if needed)
     - Byte 5: version number
     - Bytes 6-7: size as 2-byte big-endian integer

   Example::

       header = create_binary_header('PNG', 1, 1024)
       # b'PNG \\x01\\x04\\x00'
       #   ^^^^ = 'PNG '
       #       ^^ = version 1
       #         ^^^^ = 1024 as 2 bytes

   ~~~~
   def create_binary_header(file_type, version, size):
       # Your code here
       # Hint: Use .ljust(4) for padding
       # Hint: size.to_bytes(2, 'big') converts int to 2 bytes
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_basic_header(self):
           result = create_binary_header('PNG', 1, 1024)
           self.assertEqual(len(result), 7)
           self.assertEqual(result[:4], b'PNG ')
           self.assertEqual(result[4], 1)

       def test_short_type(self):
           result = create_binary_header('AB', 5, 256)
           self.assertEqual(result[:4], b'AB  ')

       def test_returns_bytes(self):
           result = create_binary_header('TEST', 0, 0)
           self.assertEqual(type(result), bytes)

   myTests().main()


Debugging Exercises
-------------------

[Debug exercises from above already included]


Summary
-------

After completing these exercises, you should be able to:

✅ Understand the difference between bytes and bytearray

✅ Work with binary file modes ('rb', 'wb', 'rb+')

✅ Use bytearray for mutable binary data

✅ Handle file errors with errno constants

✅ Use standard streams appropriately (stdin, stdout, stderr)

✅ Choose the correct file mode for different scenarios

✅ Use context managers for file handling

✅ Debug common file handling mistakes

**Struggling with any of these?** Review the Advanced File I/O section before continuing to the chapter assessment.