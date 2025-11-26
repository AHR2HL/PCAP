..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

:skipreading:`True`

.. qnum::
   :prefix: files-9-
   :start: 1

Exercises
---------

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

**Binary File Reading**

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

**Binary Data Checker**

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

**CSV Parser**

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

**Debug: File Not Closing**

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

Below are the datafiles that you have been using so far, and will continue to use for the rest of the chapter.

The file below is ``travel_plans.txt``.

.. raw:: html

    <pre id="travel_plans.txt">
    This summer I will be travelling.
    I will go to...
    Italy: Rome
    Greece: Athens
    England: London, Manchester
    France: Paris, Nice, Lyon
    Spain: Madrid, Barcelona, Granada
    Austria: Vienna
    I will probably not even want to come back!
    However, I wonder how I will get by with all the different languages.
    I only know English!
    </pre>

The file below is ``school_prompt.txt``.

.. raw:: html

    <pre id="school_prompt.txt">
    Writing essays for school can be difficult but
    many students find that by researching their topic that they
    have more to say and are better informed. Here are the university
    we require many undergraduate students to take a first year writing requirement
    so that they can
    have a solid foundation for their writing skills. This comes
    in handy for many students.
    Different schools have different requirements, but everyone uses
    writing at some point in their academic career, be it essays, research papers,
    technical write ups, or scripts.
    </pre>

The file below is ``emotion_words.txt``.

.. raw:: html

    <pre id="emotion_words.txt">
    Sad upset blue down melancholy somber bitter troubled
    Angry mad enraged irate irritable wrathful outraged infuriated
    Happy cheerful content elated joyous delighted lively glad
    Confused disoriented puzzled perplexed dazed befuddled
    Excited eager thrilled delighted
    Scared afraid fearful panicked terrified petrified startled
    Nervous anxious jittery jumpy tense uneasy apprehensive
    </pre>


.. question:: files_ex_1
   :number: 1

    .. tabbed:: q1

        .. tab:: Question

            .. actex:: ac9_9_1
                :nocodelens:
                :available_files: studentdata.txt

                The following sample file called ``studentdata.txt`` contains one line for each student in an imaginary class.  The
                students name is the first thing on each line, followed by some exam scores.
                The number of scores might be different for each student.

                .. raw:: html

                    <pre id="studentdata.txt">
                    joe 10 15 20 30 40
                    bill 23 16 19 22
                    sue 8 22 17 14 32 17 24 21 2 9 11 17
                    grace 12 28 21 45 26 10
                    john 14 32 25 16 89
                    </pre>

                Using the text file ``studentdata.txt`` write a program that prints out the names of
                students that have more than six quiz scores.
                ~~~~
                # Hint: first see if you can write a program that just prints out the number of scores on each line
                # Then, make it print the number only if the number is at least six
                # Then, switch it to printing the name instead of the number

                ====
                from unittest.gui import TestCaseGui
                import re
                class myTests(TestCaseGui):
                    def testOne(self):
                        names = []
                        with open('studentdata.txt', 'r') as fh:
                            for line in fh:
                                values = line.split()
                                name = values[0]
                                scores = values[1:]
                                if len(scores) > 6:
                                    names.append(name)
                        self.assertEqual(self.getOutput().rstrip(), '\n'.join(names), 'Checking names')
                        for name in names:
                            self.assertFalse(re.search(name, self.getEditorText()), 'Checking for hardcoding')
                        if re.search(r'[^#]+= *open', self.getEditorText(), re.M):
                            self.assertTrue(re.search(r'[^#]+\.close\(', self.getEditorText(), re.M), 'Checking for matching open and close statements')
                        else:
                            self.assertTrue(re.search(r'with[ (] *open', self.getEditorText(), re.M), 'Checking open statement')
                myTests().main()


        .. tab:: Answer

            .. activecode:: ch_files_q1answer
                :nocodelens:

                f = open("studentdata.txt", "r")

                for aline in f:
                    items = aline.split()
                    if len(items[1:]) > 6:
                        print(items[0])

                f.close()

.. question:: files_ex_2
   :number: 2

    .. tabbed:: q2

        .. tab:: Question

            .. actex:: ac9_9_2
               :nocodelens:
               :available_files: travel_plans.txt

               Create a list called ``destination`` using the data stored in ``travel_plans.txt``. Each element of the list should contain a line from the file that lists a country and cities inside that country. Hint: each line that has this information also has a colon ``:`` in it.
               ~~~~

               ====

               from unittest.gui import TestCaseGui

               class myTests(TestCaseGui):

                  def testFour(self):
                     self.assertEqual(destination, ['Italy: Rome\n', 'Greece: Athens\n', 'England: London, Manchester\n', 'France: Paris, Nice, Lyon\n', 'Spain: Madrid, Barcelona, Granada\n', 'Austria: Vienna\n'], "Testing that destination is assigned to correct values.")

               myTests().main()

.. question:: files_ex_3
   :number: 3

    .. tabbed:: q3

        .. tab:: Question

            .. actex:: ac9_9_3
               :nocodelens:
               :available_files: emotion_words.txt

               Create a list called ``j_emotions`` that contains every word in ``emotion_words.txt`` that begins with the letter "j".
               ~~~~

               ====

               from unittest.gui import TestCaseGui

               class myTests(TestCaseGui):

                  def testOne(self):
                     self.assertEqual(j_emotions, ['joyous', 'jittery', 'jumpy'], "Testing that j_emotions was created correctly.")

               myTests().main()


Contributed Exercises
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    {% for q in questions: %}
        <div class='oneq full-width'>
            {{ q['htmlsrc']|safe }}
        </div>
    {% endfor %}
