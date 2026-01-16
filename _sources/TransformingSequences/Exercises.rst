..  Copyright (C)  Alpha Schools

.. qnum::
   :prefix: AdvStrings-Ex-
   :start: 1

Exercises: Advanced String Operations
======================================

.. activecode:: advstrings_ex_01
   :autograde: unittest
   :practice: T

   **Exercise** Write a function ``title_case(text)`` that converts text to title case, but ensures that small words like "a", "an", "the", "in", "on", "at" remain lowercase unless they're the first word.

   Example:

   * ``title_case("the lord of the rings")`` → ``"The Lord of the Rings"``
   * ``title_case("a tale of two cities")`` → ``"A Tale of Two Cities"``

   ~~~~
   def title_case(text):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(title_case("the lord of the rings"), "The Lord of the Rings", "Test 1")
           self.assertEqual(title_case("a tale of two cities"), "A Tale of Two Cities", "Test 2")
           self.assertEqual(title_case("gone with the wind"), "Gone with the Wind", "Test 3")
           self.assertEqual(title_case("the catcher in the rye"), "The Catcher in the Rye", "Test 4")

   myTests().main()


.. activecode:: advstrings_ex_02
   :autograde: unittest
   :practice: T

   **Exercise** Write a function ``is_valid_variable_name(name)`` that returns ``True`` if the string is a valid Python variable name, ``False`` otherwise.

   Remember: A valid variable name:

   * Starts with a letter or underscore
   * Contains only letters, numbers, and underscores
   * Is not a Python keyword

   Use the ``.isidentifier()`` method to help!

   ~~~~
   import keyword

   def is_valid_variable_name(name):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(is_valid_variable_name("my_var"), True, "Test 1")
           self.assertEqual(is_valid_variable_name("_private"), True, "Test 2")
           self.assertEqual(is_valid_variable_name("var123"), True, "Test 3")
           self.assertEqual(is_valid_variable_name("123var"), False, "Test 4")
           self.assertEqual(is_valid_variable_name("my-var"), False, "Test 5")
           self.assertEqual(is_valid_variable_name("class"), False, "Test 6: keyword")
           self.assertEqual(is_valid_variable_name("for"), False, "Test 7: keyword")

   myTests().main()


.. activecode:: advstrings_ex_03
   :autograde: unittest
   :practice: T

   **Exercise** Write a function ``clean_whitespace(text)`` that:

   * Removes leading and trailing whitespace
   * Replaces multiple consecutive spaces with a single space
   * Returns the cleaned string

   Example: ``clean_whitespace("  Hello    world  ")`` → ``"Hello world"``

   ~~~~
   def clean_whitespace(text):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(clean_whitespace("  Hello    world  "), "Hello world", "Test 1")
           self.assertEqual(clean_whitespace("Python   is    awesome"), "Python is awesome", "Test 2")
           self.assertEqual(clean_whitespace("   spaces   everywhere   "), "spaces everywhere", "Test 3")
           self.assertEqual(clean_whitespace("NoExtraSpaces"), "NoExtraSpaces", "Test 4")

   myTests().main()


.. activecode:: advstrings_ex_04
   :autograde: unittest
   :practice: T

   **Exercise** Write a function ``format_table_row(items, width=15)`` that takes a list of strings and formats them into a table row where each item is centered in a field of the given width, separated by " | " (space-pipe-space).

   Example:

   * ``format_table_row(["Name", "Age", "City"], 15)`` should produce something like:

     ``"     Name      |      Age      |     City      "``

   Use the ``.center()`` method to center each item!

   ~~~~
   def format_table_row(items, width=15):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):

       def testOne(self):
           result1 = format_table_row(["Name", "Age", "City"], 15)
           # Split by pipe and check each field
           fields = result1.split('|')
           self.assertEqual(len(fields), 3, "Should have 3 fields separated by |")
           self.assertEqual(fields[0].strip(), "Name", "First field should contain 'Name'")
           self.assertEqual(fields[1].strip(), "Age", "Second field should contain 'Age'")
           self.assertEqual(fields[2].strip(), "City", "Third field should contain 'City'")
           # Check that fields have correct width (accounting for spaces)
           self.assertEqual(len(fields[0]), 15, "First field should be 15 characters wide")
           self.assertEqual(len(fields[1]), 15, "Second field should be 15 characters wide (including surrounding spaces)")

       def testTwo(self):
           result2 = format_table_row(["ID", "Product"], 10)
           fields = result2.split('|')
           self.assertEqual(len(fields), 2, "Should have 2 fields")
           self.assertEqual(fields[0].strip(), "ID", "First field should contain 'ID'")
           self.assertEqual(fields[1].strip(), "Product", "Second field should contain 'Product'")
           self.assertEqual(len(fields[0]), 10, "Fields should be 10 characters wide")

       def testThree(self):
           result3 = format_table_row(["A", "B", "C"], 5)
           fields = result3.split('|')
           self.assertEqual(len(fields), 3, "Should have 3 fields")
           self.assertEqual(fields[0].strip(), "A", "Fields should contain A, B, C")
           self.assertEqual(fields[1].strip(), "B", "Fields should contain A, B, C")
           self.assertEqual(fields[2].strip(), "C", "Fields should contain A, B, C")

       def testFour(self):
           # Check that .center() method is used
           self.assertIn('.center(', self.getEditorText(), "Make sure you use the .center() method")

   myTests().main()


.. activecode:: advstrings_ex_05
   :autograde: unittest
   :practice: T

   **Exercise** Write a function ``parse_name_email(text)`` that extracts a name and email from a string formatted as "Name <email@domain.com>".

   Use ``.rindex()`` or ``.partition()`` to help split the string!

   Return a tuple: ``(name, email)``

   Example:

   * ``parse_name_email("John Doe <john@example.com>")`` → ``("John Doe", "john@example.com")``

   ~~~~
   def parse_name_email(text):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(parse_name_email("John Doe <john@example.com>"), ("John Doe", "john@example.com"), "Test 1")
           self.assertEqual(parse_name_email("Alice Smith <alice@test.org>"), ("Alice Smith", "alice@test.org"), "Test 2")
           self.assertEqual(parse_name_email("Bob <bob@site.net>"), ("Bob", "bob@site.net"), "Test 3")

   myTests().main()


.. activecode:: advstrings_ex_06
   :autograde: unittest
   :practice: T

   **Exercise** Write a function ``is_strong_password(password)`` that returns ``True`` if a password meets these criteria:

   * At least 8 characters long
   * Contains at least one uppercase letter
   * Contains at least one lowercase letter
   * Contains at least one digit
   * Contains at least one special character (not alphanumeric)

   Use multiple ``.isXXX()`` methods and combine them!

   ~~~~
   def is_strong_password(password):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(is_strong_password("Abc123!@"), True, "Test 1: valid password")
           self.assertEqual(is_strong_password("weak"), False, "Test 2: too short")
           self.assertEqual(is_strong_password("alllowercase123!"), False, "Test 3: no uppercase")
           self.assertEqual(is_strong_password("ALLUPPERCASE123!"), False, "Test 4: no lowercase")
           self.assertEqual(is_strong_password("NoDigits!@#"), False, "Test 5: no digits")
           self.assertEqual(is_strong_password("NoSpecial123Abc"), False, "Test 6: no special chars")
           self.assertEqual(is_strong_password("Perfect1!Pass"), True, "Test 7: valid password")

   myTests().main()


.. activecode:: advstrings_ex_07
   :autograde: unittest
   :practice: T

   **Exercise** Write a function ``extract_domain(url)`` that extracts the domain name from a URL.

   Examples:

   * ``extract_domain("https://www.example.com/path")`` → ``"example.com"``
   * ``extract_domain("http://subdomain.site.org/page.html")`` → ``"site.org"``

   Hints:

   * Remove the protocol (http:// or https://) first
   * Use ``.partition()`` to split on "/" to get just the domain part
   * Get the last two parts of the domain (handle subdomains)

   ~~~~
   def extract_domain(url):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(extract_domain("https://www.example.com/path"), "example.com", "Test 1")
           self.assertEqual(extract_domain("http://subdomain.site.org/page.html"), "site.org", "Test 2")
           self.assertEqual(extract_domain("https://github.com/user/repo"), "github.com", "Test 3")
           self.assertEqual(extract_domain("http://docs.python.org/3/"), "python.org", "Test 4")

   myTests().main()


.. activecode:: advstrings_ex_08
   :autograde: unittest
   :practice: T

   **Exercise** Write a function ``normalize_phone(phone)`` that takes a phone number in various formats and returns it in the standard format: ``(XXX) XXX-XXXX``

   Your function should:

   * Remove all non-digit characters
   * Handle 10-digit and 11-digit numbers (if 11 digits, remove leading 1)
   * Return ``None`` if the number is invalid (not 10 or 11 digits)
   * Format the valid 10-digit number as ``(XXX) XXX-XXXX``

   Examples:

   * ``normalize_phone("555-123-4567")`` → ``"(555) 123-4567"``
   * ``normalize_phone("(555) 123-4567")`` → ``"(555) 123-4567"``
   * ``normalize_phone("1-555-123-4567")`` → ``"(555) 123-4567"``
   * ``normalize_phone("5551234567")`` → ``"(555) 123-4567"``
   * ``normalize_phone("123")`` → ``None``

   ~~~~
   def normalize_phone(phone):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(normalize_phone("555-123-4567"), "(555) 123-4567", "Test 1")
           self.assertEqual(normalize_phone("(555) 123-4567"), "(555) 123-4567", "Test 2")
           self.assertEqual(normalize_phone("1-555-123-4567"), "(555) 123-4567", "Test 3")
           self.assertEqual(normalize_phone("5551234567"), "(555) 123-4567", "Test 4")
           self.assertEqual(normalize_phone("1 (555) 123-4567"), "(555) 123-4567", "Test 5")
           self.assertEqual(normalize_phone("123"), None, "Test 6: too short")
           self.assertEqual(normalize_phone("12345678901234"), None, "Test 7: too long")

   myTests().main()