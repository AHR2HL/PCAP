..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Testing Conditionals
=====================

Ideally, you want tests that will cover both the typical execution of your program and tests for unusual things that might happen, which are called **edge cases**.

If the code has conditional blocks (``if..elif..else``) then you'll want to have tests that check that the right block executes when you expect it to. For example, in the code below, z is set to the smaller of x and y, but if they are equal then we set z to 0. Our code even includes a comment to help us keep track of when we think the final code block should execute.

.. code-block:: python

    if x < y:
        z = x
    else:
        if x > y:
            z = y
        else:
            ## x must be equal to y
            z = 0

When you start to have complex conditionals, it's helpful to add comments like that, and once you do you might as well add an assert statement. If the assert ever causes an error, you'll be grateful to know right away that something has gone wrong and you'll have a good start on where to look for debugging. In this case, you'll never get an error, no matter the values of x and y.

.. activecode:: ac19_1c_1

    x = 3
    y = 4
    if x < y:
        z = x
    else:
        if x > y:
            z = y
        else:
            ## x must be equal to y
            assert x==y
            z = 0

Testing All Branches
--------------------

When testing conditionals, you need test cases that exercise **every branch**. The example below shows a grade classification function with assertions that verify we're in the expected branch. Try changing the ``score`` value to test each path.

.. activecode:: ac19_1c_2

    def classify_grade(score):
        """Classify a numeric score into a letter grade."""

        if score >= 90:
            assert score >= 90 and score <= 100, "A grade: score should be 90-100"
            return 'A'
        elif score >= 80:
            assert score >= 80 and score < 90, "B grade: score should be 80-89"
            return 'B'
        elif score >= 70:
            assert score >= 70 and score < 80, "C grade: score should be 70-79"
            return 'C'
        elif score >= 60:
            assert score >= 60 and score < 70, "D grade: score should be 60-69"
            return 'D'
        else:
            assert score < 60, "F grade: score should be below 60"
            return 'F'

    # Test different branches
    score = 85
    grade = classify_grade(score)
    print(f"Score {score} = Grade {grade}")

    # Try these test cases by changing score above:
    # 95 (A), 85 (B), 75 (C), 65 (D), 55 (F)
    # Edge cases: 90 (A), 80 (B), 70 (C), 60 (D)

.. important:: 🎯 Complete Branch Coverage

   **To thoroughly test conditionals, create test cases for:**

   1. **Each branch:** At least one test that executes each ``if``/``elif``/``else`` block
   2. **Boundary values:** Test the exact values where conditions change (e.g., 90, 80, 70, 60)
   3. **Typical values:** Test values clearly inside each range (e.g., 95, 85, 75)
   4. **Invalid values:** Test what happens with unexpected input (e.g., 150, -10)

   **In the example above:** Test scores like 95 (middle of A range), 90 (boundary), 85 (middle of B range), 80 (boundary), etc.

**Check Your Understanding**

.. mchoice:: tc_conditionals_1
   :answer_a: One test case is enough if the code runs without errors
   :answer_b: Test each branch at least once, plus test boundary values where conditions change
   :answer_c: Only test the most common case
   :answer_d: Testing conditionals is not necessary
   :correct: b
   :feedback_a: Code can run without errors but still have logic bugs in untested branches.
   :feedback_b: Correct! Complete testing requires exercising every branch and checking boundary conditions where behavior changes.
   :feedback_c: Uncommon cases often contain the most bugs—they need testing too.
   :feedback_d: Conditionals are complex logic that often contains bugs; they need thorough testing.

   When testing a function with multiple conditional branches (if/elif/else), what is the best testing strategy?
