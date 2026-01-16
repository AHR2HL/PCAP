..  Copyright (C)  Alpha Schools

Exercises
=========

Multiple Choice Questions
--------------------------

.. mchoice:: buildprog_mc1
   :answer_a: Copy code from the textbook and make small edits
   :answer_b: Start writing code immediately
   :answer_c: Sketch an outline in plain language
   :answer_d: Write all the code at once and test at the end
   :correct: c
   :feedback_a: Copying code should come LATER, after you understand the problem.
   :feedback_b: Planning first saves time and reduces confusion.
   :feedback_c: Correct! Always outline your approach before coding.
   :feedback_d: Code incrementally, testing each section as you go.

   What should be the FIRST step when starting a new programming problem?

.. mchoice:: buildprog_mc2
   :answer_a: Outline, Code One Section at a Time, Clean Up
   :answer_b: Code, Test, Debug
   :answer_c: Copy, Edit, Test
   :answer_d: Plan, Write, Submit
   :correct: a
   :feedback_a: Correct! This is the three-step strategy from the chapter.
   :feedback_b: This is too general and misses the outlining step.
   :feedback_c: Copying is not the first step in the strategy.
   :feedback_d: This is close but not the specific strategy taught.

   What are the three basic steps in the recommended programming strategy?

.. mchoice:: buildprog_mc3
   :answer_a: To make the output look pretty
   :answer_b: To verify each section works before moving on
   :answer_c: To help other programmers understand your code
   :answer_d: To meet assignment requirements
   :correct: b
   :feedback_a: Diagnostic prints are for testing, not aesthetics.
   :feedback_b: Correct! Diagnostic prints help you verify your code works at each stage.
   :feedback_c: That's the purpose of comments, not diagnostic prints.
   :feedback_d: Diagnostic prints are a development tool, not a requirement.

   Why should you add diagnostic print statements while coding?

.. mchoice:: buildprog_mc4
   :answer_a: Leave all print statements in the final version
   :answer_b: Delete all comments to make code shorter
   :answer_c: Remove diagnostic prints and simplify comments
   :answer_d: Rewrite everything from scratch
   :correct: c
   :feedback_a: Diagnostic prints should be removed from the final version.
   :feedback_b: Good comments help others (and you!) understand your code.
   :feedback_c: Correct! Clean up means removing test prints and keeping useful comments.
   :feedback_d: No need to rewrite - just clean up what you have.

   What should you do during the "Clean Up" phase?

.. mchoice:: buildprog_mc5
   :answer_a: Use [] to pull out the item
   :answer_b: Use a for loop
   :answer_c: Use an if statement
   :answer_d: Use the accumulator pattern
   :correct: a
   :feedback_a: Correct! Use brackets [] for indexing into sequences.
   :feedback_b: for loops are for repetition, not item extraction.
   :feedback_c: if statements are for conditionals, not item extraction.
   :feedback_d: Accumulator patterns are for building up values over iterations.

   According to the checklist, if you need to pull an item from a list or string, what should you use?

.. mchoice:: buildprog_mc6
   :answer_a: Copy it immediately and start editing
   :answer_b: Understand it first, then copy and edit
   :answer_c: Never copy code from the textbook
   :answer_d: Copy it at the very end of your program
   :correct: b
   :feedback_a: You must understand the code BEFORE editing it.
   :feedback_b: Correct! Understanding first prevents confusion and errors.
   :feedback_c: Copying is fine when done correctly - after understanding.
   :feedback_d: Copying can happen during development, not just at the end.

   When you find a code snippet in the textbook that's similar to what you need, what should you do?

.. mchoice:: buildprog_mc7
   :answer_a: String methods
   :answer_b: List methods
   :answer_c: A for loop
   :answer_d: An if/else statement
   :correct: c
   :feedback_a: String methods transform strings, not repeat operations.
   :feedback_b: List methods modify lists, not repeat operations.
   :feedback_c: Correct! for loops are for repeating operations multiple times.
   :feedback_d: if/else is for conditionals, not repetition.

   If an operation needs to be done multiple times, what Python structure should you use?

.. mchoice:: buildprog_mc8
   :answer_a: At the beginning of your program
   :answer_b: After writing all your code
   :answer_c: After each section of code you write
   :answer_d: Only if something breaks
   :correct: c
   :feedback_a: You should test as you build, not just at the start.
   :feedback_b: Testing only at the end makes debugging much harder.
   :feedback_c: Correct! Test each section before moving to the next one.
   :feedback_d: Test proactively, not reactively.

   When should you test your code?

.. mchoice:: buildprog_mc9
   :answer_a: They should all be deleted
   :answer_b: Keep only the ones that help explain the code
   :answer_c: Keep all of them for documentation
   :answer_d: Comments don't matter
   :correct: b
   :feedback_a: Good comments are valuable documentation.
   :feedback_b: Correct! Keep comments that provide useful information, remove obvious ones.
   :feedback_c: Too many obvious comments can clutter code.
   :feedback_d: Comments are important for readability and maintenance.

   After cleaning up your code, what should you do with comments?

.. mchoice:: buildprog_mc10
   :answer_a: Use a for loop
   :answer_b: Use the accumulator pattern
   :answer_c: Use an if statement
   :answer_d: Use dictionary methods
   :correct: c
   :feedback_a: for loops are for repetition, not conditionals.
   :feedback_b: Accumulator patterns are for building up values.
   :feedback_c: Correct! if statements control whether code runs based on conditions.
   :feedback_d: Dictionary methods are for working with dictionaries.

   If an operation should only occur under certain circumstances, what should you use?

Parsons Problems
----------------

.. parsonsprob:: buildprog_parsons1
   :numbered: left
   :adaptive:

   Arrange the blocks to show the correct order of the three-step programming strategy.
   -----
   # Step 1: Sketch an Outline
   =====
   # Write comments describing what you want to do
   =====
   # Step 2: Code One Section at a Time
   =====
   # Write code for first section
   =====
   # Add diagnostic prints to test
   =====
   # Verify it works before continuing
   =====
   # Step 3: Clean Up
   =====
   # Remove diagnostic prints
   =====
   # Simplify comments

.. parsonsprob:: buildprog_parsons2
   :numbered: left
   :adaptive:

   Arrange the blocks to build an outline for summing numbers in a list.
   -----
   # Initialize accumulator variable
   =====
   # Loop through each number in the list
   =====
   # Add current number to accumulator
   =====
   # Print final sum
   =====
   # Print intermediate values #distractor

.. parsonsprob:: buildprog_parsons3
   :numbered: left
   :adaptive:

   Arrange the blocks to create an incremental development approach for counting vowels in a string.
   -----
   # Initialize counter to 0
   count = 0
   =====
   count = [] #distractor
   =====
   # Loop through each character
   for char in text:
   =====
       # Check if character is a vowel
       if char.lower() in 'aeiou':
   =====
       if char in 'aeiou': #distractor
   =====
           # Increment counter
           count += 1
   =====
           count = count + char #distractor
   =====
   # Return the final count
   return count

.. parsonsprob:: buildprog_parsons4
   :numbered: left
   :adaptive:

   Arrange the blocks to show how to incrementally test a list filtering operation.
   -----
   # Initialize empty result list
   result = []
   print("Starting with empty list:", result)
   =====
   # Loop through source list
   for item in source_list:
   =====
       print("Processing item:", item)
   =====
       # Check if item meets criteria
       if item > 10:
   =====
           # Add to result list
           result.append(item)
   =====
           print("Added to result:", item)
   =====
   # Print final result
   print("Final result:", result)

Active Code Problems
--------------------

.. activecode:: buildprog_ac1
   :autograde: unittest

   Following the three-step strategy, write a program that counts how many even numbers are in a list.
   
   Step 1: Write outline comments first.
   Step 2: Code incrementally (you can add diagnostic prints while developing).
   Step 3: Final version should be clean.

   ~~~~
   numbers = [12, 7, 5, 18, 3, 22, 9, 14]

   # Your code here

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           # Check that a variable exists for the count
           self.assertIn('even_count', dir(), "Create a variable to store the count")
           self.assertEqual(even_count, 4, "Should count 4 even numbers in the list")

   myTests().main()

.. activecode:: buildprog_ac2
   :autograde: unittest

   Using the incremental approach, write a program that finds the longest word in a list.
   
   Hint: Use the accumulator pattern with a variable tracking the longest word found so far.

   ~~~~
   words = ["apple", "banana", "kiwi", "strawberry", "grape"]

   # Your code here

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn('longest', dir(), "Create a variable to store the longest word")
           self.assertEqual(longest, "strawberry", "Should find 'strawberry' as the longest word")

   myTests().main()

.. activecode:: buildprog_ac3
   :autograde: unittest

   Build a program incrementally that creates a dictionary counting how many times each letter appears in a word.
   
   Example: "hello" → {'h': 1, 'e': 1, 'l': 2, 'o': 1}

   ~~~~
   word = "programming"

   # Your code here

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn('letter_count', dir(), "Create a dictionary variable")
           self.assertEqual(letter_count['g'], 2, "Should count 2 'g's")
           self.assertEqual(letter_count['r'], 2, "Should count 2 'r's")
           self.assertEqual(letter_count['m'], 2, "Should count 2 'm's")

   myTests().main()

.. activecode:: buildprog_ac4
   :autograde: unittest

   Write a program that filters a list of names to only include names that start with a vowel.
   
   Use the incremental strategy: outline, code with tests, clean up.

   ~~~~
   names = ["Alice", "Bob", "Emma", "Oscar", "Charlie", "Ivy", "David"]

   # Your code here

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn('vowel_names', dir(), "Create a list for results")
           self.assertEqual(sorted(vowel_names), sorted(["Alice", "Emma", "Oscar", "Ivy"]), 
                          "Should include only names starting with vowels")

   myTests().main()

Debugging Problems
------------------

.. activecode:: buildprog_debug1
   :autograde: unittest

   This code was written without following the incremental strategy. It has bugs and poor structure. Fix it to correctly sum all numbers divisible by 3.

   ~~~~
   numbers = [3, 7, 9, 12, 15, 22, 27, 30]
   for n in numbers:
       if n % 3:
           total = total + n
   print(total)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(total, 96, "Should sum numbers divisible by 3: 3+9+12+15+27+30=96")

   myTests().main()

.. activecode:: buildprog_debug2
   :autograde: unittest

   This code wasn't tested incrementally and has multiple issues. Fix it to create a list of squares of even numbers.

   ~~~~
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   
   for num in numbers:
       if num % 2 == 0:
           squares.append(num ** 2)
   
   print(squares)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertEqual(squares, [4, 16, 36, 64, 100], 
                          "Should contain squares of even numbers")

   myTests().main()

.. activecode:: buildprog_debug3
   :autograde: unittest

   This code has leftover diagnostic prints and poor variable names from not following the cleanup step. Fix it to be clean and readable.

   ~~~~
   x = []
   print("START")
   for thing in ["cat", "dog", "bird", "fish"]:
       print("Processing:", thing)
       if len(thing) > 3:
           print("Adding:", thing)
           x.append(thing)
           print("Current x:", x)
   print("DONE")
   print(x)

   # After cleanup, only the final result should print: ['bird', 'fish']

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           # Check for better variable names (not 'x' or 'thing')
           self.assertIn('long_words', dir(), "Use a descriptive variable name instead of 'x'")
           self.assertEqual(long_words, ['bird', 'fish'], "Should filter words longer than 3 characters")

   myTests().main()

Applied Problems
----------------

.. activecode:: buildprog_applied1
   :autograde: unittest

   **Real-world scenario:** You're building a grade calculator.
   
   Following the three-step strategy, write a program that:
   1. Takes a list of test scores
   2. Removes the lowest score
   3. Calculates the average of remaining scores
   
   Outline first, code incrementally, clean up at the end.

   ~~~~
   test_scores = [85, 92, 78, 95, 88, 73, 90]

   # Step 1: Write your outline as comments

   # Step 2: Code each section with diagnostic prints

   # Step 3: Clean up (remove diagnostics, keep useful comments)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn('average', dir(), "Create a variable for the average")
           self.assertAlmostEqual(average, 88.0, 1, 
                                "After removing lowest (73), average of remaining 6 scores should be 88.0")

   myTests().main()

.. activecode:: buildprog_applied2
   :autograde: unittest

   **Real-world scenario:** You're analyzing customer data.
   
   Build a program that takes a list of customer ages and categorizes them:
   - "minor": under 18
   - "adult": 18-64
   - "senior": 65+
   
   Return a dictionary with counts for each category.

   ~~~~
   ages = [15, 25, 67, 42, 16, 70, 33, 8, 55, 72, 19]

   # Your outline and code here

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn('age_categories', dir(), "Create a dictionary for categories")
           self.assertEqual(age_categories['minor'], 3, "Should count 3 minors (15, 16, 8)")
           self.assertEqual(age_categories['adult'], 5, "Should count 5 adults")
           self.assertEqual(age_categories['senior'], 3, "Should count 3 seniors")

   myTests().main()

.. activecode:: buildprog_applied3
   :autograde: unittest

   **Real-world scenario:** Text analysis tool.
   
   Write a program that takes a sentence and creates a dictionary where:
   - Keys are word lengths (1, 2, 3, etc.)
   - Values are lists of words with that length
   
   Example: "I love coding" → {1: ['I'], 4: ['love'], 6: ['coding']}

   ~~~~
   sentence = "The quick brown fox jumps over the lazy dog"

   # Your code here

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def testOne(self):
           self.assertIn('word_lengths', dir(), "Create a dictionary variable")
           self.assertEqual(len(word_lengths[3]), 4, "Should have 4 three-letter words (The, fox, the, dog)")
           self.assertEqual(len(word_lengths[5]), 3, "Should have 3 five-letter words (quick, brown, jumps)")

   myTests().main()

Concept Application
-------------------

.. mchoice:: buildprog_concept1
   :multiple_answers:
   :answer_a: Initialize an empty list
   :answer_b: Loop through the input data
   :answer_c: Test with a print statement after each addition
   :answer_d: Write all code first, then test
   :correct: a,b,c
   :feedback_a: Correct! Start with initialization.
   :feedback_b: Correct! Loop through data to process each item.
   :feedback_c: Correct! Test incrementally with diagnostic prints.
   :feedback_d: This violates the "code one section at a time" principle.

   Which steps follow the "code one section at a time" strategy for building a filtered list? (Select all that apply)

.. mchoice:: buildprog_concept2
   :answer_a: print("---------- x is now:", x, "----------")
   :answer_b: # x should be 5 here
   :answer_c: return x
   :answer_d: x = 5
   :correct: a
   :feedback_a: Correct! Diagnostic prints help track variable values during development.
   :feedback_b: This is a comment, not a diagnostic print.
   :feedback_c: return is for function output, not testing.
   :feedback_d: This is an assignment, not a test.

   Which line represents a good diagnostic print statement for testing?

Quick Reference: The Checklist
-------------------------------

.. important:: **When translating English to Python, ask:**

   **Extraction?**
      Use ``[]`` for lists, strings, dictionaries
   
   **String transformation?**
      Check string methods (``.upper()``, ``.split()``, ``.replace()``, etc.)
   
   **List modification?**
      Check list methods (``.append()``, ``.remove()``, ``.sort()``, etc.)
   
   **Repetition?**
      Use ``for`` loop:
      
      ::
      
         for <varname> in <seq>:
             <code block>
   
   **Conditional?**
      Use ``if`` statement:
      
      ::
      
         if <condition>:
             <if block>
         else:
             <else block>
   
   **Building up a value?**
      Use accumulator pattern:
      
      ::
      
         result = <initial_value>
         for <varname> in <seq>:
             result = <new_value>