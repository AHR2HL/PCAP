..  Copyright (C)  Alpha Schools

.. qnum::
   :prefix: AdvStrings-Assess-
   :start: 1

Chapter Assessment: Advanced String Operations
===============================================

Part 1: Multiple Choice Questions
----------------------------------

.. mchoice:: advstrings_assess_mc1
   :answer_a: "HELLO"
   :answer_b: "Hello"
   :answer_c: "hello"
   :answer_d: "HeLLo"
   :correct: b
   :feedback_a: capitalize() only capitalizes the first letter, not all letters
   :feedback_b: Correct! capitalize() makes the first letter uppercase and the rest lowercase
   :feedback_c: No, capitalize() makes the first letter uppercase
   :feedback_d: No, capitalize() makes all letters except the first lowercase

   What is the output of: ``"hELLO".capitalize()``


.. mchoice:: advstrings_assess_mc2
   :answer_a: "banana123"
   :answer_b: "123banana"
   :answer_c: "    banana123"
   :answer_d: "banana123    "
   :correct: d
   :feedback_a: ljust() adds padding, it doesn't remove characters
   :feedback_b: ljust() adds padding to the right (end), not the left
   :feedback_c: ljust() adds padding to the right (end), not the left
   :feedback_d: Correct! ljust(14) pads the string on the right to make it 14 characters total

   What is the output of: ``"banana123".ljust(14)``


.. mchoice:: advstrings_assess_mc3
   :answer_a: isalnum()
   :answer_b: isalpha()
   :answer_c: isdigit()
   :answer_d: isidentifier()
   :correct: d
   :feedback_a: isalnum() allows numbers anywhere, not just after the first character
   :feedback_b: isalpha() doesn't allow numbers or underscores at all
   :feedback_c: isdigit() only checks if all characters are digits
   :feedback_d: Correct! isidentifier() checks if a string is a valid Python identifier (variable name)

   Which method would you use to check if a string is a valid Python variable name?


.. mchoice:: advstrings_assess_mc4
   :answer_a: 2
   :answer_b: 6
   :answer_c: 7
   :answer_d: -1
   :correct: c
   :feedback_a: find() and index() search from the left; rfind() and rindex() search from the right
   :feedback_b: This would be the first occurrence from the left
   :feedback_c: Correct! rindex() finds the rightmost (last) occurrence, which is at position 7
   :feedback_d: rindex() raises an exception if not found; rfind() returns -1

   What is the output of: ``"banana".rindex("a")``


.. mchoice:: advstrings_assess_mc5
   :answer_a: ("hello", "world", "python")
   :answer_b: ("hello world", " ", "python")
   :answer_c: ("hello", " ", "world python")
   :answer_d: ("hello world python", "", "")
   :correct: c
   :feedback_a: partition() returns 3 elements including the separator
   :feedback_b: partition() only splits on the FIRST occurrence
   :feedback_c: Correct! partition() splits on the first occurrence and returns (before, separator, after)
   :feedback_d: partition() splits the string, it doesn't return it whole

   What is the output of: ``"hello world python".partition(" ")``


Part 2: Active Code Problems
-----------------------------

.. activecode:: advstrings_assess_ac1
   :nocolab:

   **Problem 1:** Write a function ``mask_credit_card(card_number)`` that takes a credit card number as a string and returns it with all but the last 4 digits replaced by asterisks (*).

   Example: ``mask_credit_card("1234567812345678")`` → ``"************5678"``

   ~~~~
   def mask_credit_card(card_number):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(mask_credit_card("1234567812345678"), "************5678", "Test 1")
           self.assertEqual(mask_credit_card("9876543210123456"), "************3456", "Test 2")
           self.assertEqual(mask_credit_card("1111222233334444"), "************4444", "Test 3")

   myTests().main()


.. activecode:: advstrings_assess_ac2
   :nocolab:

   **Problem 2:** Write a function ``has_balanced_case(password)`` that returns ``True`` if a password contains at least one uppercase letter AND at least one lowercase letter, ``False`` otherwise.

   Use the ``.isupper()`` and ``.islower()`` methods!

   ~~~~
   def has_balanced_case(password):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(has_balanced_case("HelloWorld"), True, "Test 1")
           self.assertEqual(has_balanced_case("alllowercase"), False, "Test 2")
           self.assertEqual(has_balanced_case("ALLUPPERCASE"), False, "Test 3")
           self.assertEqual(has_balanced_case("Mix3dCase!"), True, "Test 4")
           self.assertEqual(has_balanced_case("12345"), False, "Test 5")

   myTests().main()


.. activecode:: advstrings_assess_ac3
   :nocolab:

   **Problem 3:** Write a function ``create_username(full_name)`` that creates a username from a full name by:

   * Converting to lowercase
   * Replacing spaces with underscores
   * Removing any non-alphanumeric characters except underscores

   Example: ``create_username("John O'Brien")`` → ``"john_obrien"``

   ~~~~
   def create_username(full_name):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(create_username("John Doe"), "john_doe", "Test 1")
           self.assertEqual(create_username("Mary-Jane Smith"), "maryjane_smith", "Test 2")
           self.assertEqual(create_username("John O'Brien"), "john_obrien", "Test 3")
           self.assertEqual(create_username("Alice B. Cooper"), "alice_b_cooper", "Test 4")

   myTests().main()


.. activecode:: advstrings_assess_ac4
   :nocolab:

   **Problem 4:** Write a function ``extract_initials(full_name)`` that extracts the initials from a full name and returns them in uppercase with periods.

   Example: ``extract_initials("john fitzgerald kennedy")`` → ``"J.F.K."``

   ~~~~
   def extract_initials(full_name):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(extract_initials("john fitzgerald kennedy"), "J.F.K.", "Test 1")
           self.assertEqual(extract_initials("martin luther king"), "M.L.K.", "Test 2")
           self.assertEqual(extract_initials("ada lovelace"), "A.L.", "Test 3")
           self.assertEqual(extract_initials("alan turing"), "A.T.", "Test 4")

   myTests().main()


.. activecode:: advstrings_assess_ac5
   :nocolab:

   **Problem 5 (Challenge):** Write a function ``format_currency(amount)`` that takes a number (as a string) and formats it as a currency with:

   * Comma separators for thousands
   * Exactly 2 decimal places
   * A dollar sign at the beginning
   * Right-aligned in a field of 15 characters

   Example: ``format_currency("1234567.89")`` → ``"   $1,234,567.89"``

   Hint: You'll need to work with the number string carefully. Consider using ``rjust()`` for alignment.

   ~~~~
   def format_currency(amount):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(format_currency("1234567.89"), "   $1,234,567.89", "Test 1")
           self.assertEqual(format_currency("1234.50"), "       $1,234.50", "Test 2")
           self.assertEqual(format_currency("99.99"), "          $99.99", "Test 3")

   myTests().main()


Part 3: Debugging Exercises
----------------------------

.. activecode:: advstrings_assess_debug1
   :nocolab:

   **Debug Exercise 1:** This function should check if a string contains only alphabetic characters and spaces (no numbers or special characters). Find and fix the bug.

   ~~~~
   def is_alpha_with_spaces(text):
       for char in text:
           if not char.isalpha():
               return False
       return True

   # Should return True
   print(is_alpha_with_spaces("Hello World"))

   # Should return False
   print(is_alpha_with_spaces("Hello123"))
   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(is_alpha_with_spaces("Hello World"), True, "Test 1: spaces allowed")
           self.assertEqual(is_alpha_with_spaces("HelloWorld"), True, "Test 2: no spaces")
           self.assertEqual(is_alpha_with_spaces("Hello123"), False, "Test 3: has numbers")
           self.assertEqual(is_alpha_with_spaces("Hello!"), False, "Test 4: has special char")

   myTests().main()


.. activecode:: advstrings_assess_debug2
   :nocolab:

   **Debug Exercise 2:** This function should capitalize the first letter of each word in a sentence, but it's not working correctly. Find and fix the bug.

   ~~~~
   def capitalize_words(sentence):
       words = sentence.split()
       result = []
       for word in words:
           result.append(word.upper())
       return " ".join(result)

   # Should return "Hello World Python"
   print(capitalize_words("hello world python"))
   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(capitalize_words("hello world python"), "Hello World Python", "Test 1")
           self.assertEqual(capitalize_words("the quick brown fox"), "The Quick Brown Fox", "Test 2")
           self.assertEqual(capitalize_words("python programming"), "Python Programming", "Test 3")

   myTests().main()


.. activecode:: advstrings_assess_debug3
   :nocolab:

   **Debug Exercise 3:** This function should remove all vowels from a string, but it's not working correctly. Find and fix the bug.

   ~~~~
   def remove_vowels(text):
       vowels = "aeiouAEIOU"
       result = ""
       for char in text:
           if char in vowels:
               result += char
       return result

   # Should return "Hll Wrld"
   print(remove_vowels("Hello World"))
   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(remove_vowels("Hello World"), "Hll Wrld", "Test 1")
           self.assertEqual(remove_vowels("Python"), "Pythn", "Test 2")
           self.assertEqual(remove_vowels("aeiou"), "", "Test 3: all vowels")
           self.assertEqual(remove_vowels("bcdfg"), "bcdfg", "Test 4: no vowels")

   myTests().main()


Part 4: Parson's Problems
--------------------------

.. parsonsprob:: advstrings_assess_parsons1
   :numbered: left
   :adaptive:

   Arrange the code blocks to create a function that checks if a string is a palindrome (reads the same forwards and backwards), ignoring case and spaces.

   Example: ``is_palindrome("A man a plan a canal Panama")`` should return ``True``
   -----
   def is_palindrome(text):
   =====
       cleaned = text.lower().replace(" ", "")
   =====
       cleaned = text.upper().replace(" ", "") #paired
   =====
       return cleaned == cleaned[::-1]
   =====
       return cleaned == cleaned[:1] #paired


.. parsonsprob:: advstrings_assess_parsons2
   :numbered: left
   :adaptive:

   Arrange the code blocks to create a function that counts how many words in a sentence start with a capital letter.

   Example: ``count_capital_words("The Quick Brown Fox")`` should return ``4``
   -----
   def count_capital_words(sentence):
   =====
       words = sentence.split()
   =====
       words = sentence.partition() #paired
   =====
       count = 0
   =====
       for word in words:
   =====
           if word[0].isupper():
   =====
           if word.isupper(): #paired
   =====
               count += 1
   =====
       return count


.. parsonsprob:: advstrings_assess_parsons3
   :numbered: left
   :adaptive:

   Arrange the code blocks to create a function that finds the longest word in a sentence.

   Example: ``longest_word("The quick brown fox")`` should return ``"quick"``
   -----
   def longest_word(sentence):
   =====
       words = sentence.split()
   =====
       longest = ""
   =====
       longest = 0 #paired
   =====
       for word in words:
   =====
           if len(word) > len(longest):
   =====
           if len(word) > longest: #paired
   =====
               longest = word
   =====
       return longest


Summary & Self-Check
---------------------

After completing this assessment, you should be able to:

✅ Use advanced case manipulation methods (capitalize, title, swapcase, casefold)

✅ Apply alignment methods (center, ljust, rjust, zfill)

✅ Use character validation methods (isalnum, isalpha, isdigit, isidentifier, etc.)

✅ Apply advanced search methods (rfind, rindex, partition, rpartition)

✅ Combine multiple string methods to solve complex problems

✅ Debug common string manipulation errors

✅ Choose the most appropriate string method for a given task

**Struggling with any of these?** Review the Complete String Methods Reference section before continuing to the next chapter.