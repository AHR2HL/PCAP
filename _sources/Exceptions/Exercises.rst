..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

:skipreading:`True`

Exercises
=========

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

**Custom Exception**

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



---
Build complete solutions from scratch!

**Exception Logger**

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

---

.. actex:: assess_ac23_5_1
    :practice: T
    :autograde: unittest
    :topics: Exceptions/intro-exceptions

    Below, we have provided buggy code. Add a try/except clause so the code runs without errors. If a blog post didn't get any likes, a 'Likes' key should be added to that dictionary with a value of 0.

    ~~~~
    blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]

    total_likes = 0

    for post in blog_posts:
       total_likes = total_likes + post['Likes']

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

       def testA(self):
           self.assertEqual(total_likes, 86, "Testing that total_likes has the correct value.")
       def testB(self):
            accum = 0
            for d in blog_posts:
                if 'Likes' in d:
                    accum +=1
            self.assertEqual(accum, 6, "Testing that blog_post dictionaries all have a 'Likes' key.")

    myTests().main()

.. actex:: assess_ac23_5_2
    :practice: T
    :autograde: unittest
    :topics: Exceptions/intro-exceptions

    The code below assigns the 5th letter of each word in ``food`` to the new list ``fifth``. However, the code currently produces errors. Insert a try/except clause that will allow the code to run and produce of list of the 5th letter in each word. If the word is not long enough, it should not print anything out. Note: The ``pass`` statement is a null operation; nothing will happen when it executes.
    ~~~~
    food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
    fifth = []

    for x in food:
       fifth.append(x[4])

    ====

    from unittest.gui import TestCaseGui

    class myTests(TestCaseGui):

       def testOneA(self):
           self.assertEqual(fifth, ['o', 'k', 'w', 't', 'n'], "Testing that fifth is assigned to correct values.")

    myTests().main()


Contributed Exercises
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

    {% for q in questions: %}
        <div class='oneq full-width'>
            {{ q['htmlsrc']|safe }}
        </div>
    {% endfor %}
