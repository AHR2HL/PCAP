..  Copyright (C)  Paul Resnick.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Checking Other Assumptions
===========================

We can also check other assumptions about the values of variables, in addition to their types. For example, we could check that a list has fewer than 10 items.

.. activecode:: ac19_1b_3

    lst = ['a', 'b', 'c']

    assert len(lst) < 10

Common Assumptions Worth Testing
---------------------------------

Beyond types and sizes, many other assumptions should be validated to prevent subtle bugs.

**Assumption 1: Values Are Within Valid Ranges**

When working with numeric data, values often have natural boundaries. Testing these assumptions prevents logic errors and invalid calculations.

.. activecode:: ac19_assumptions_1

    # Testing percentage values
    discount_rate = 0.15
    assert 0 <= discount_rate <= 1, "Discount rate must be between 0 and 1"

    # Testing age values
    age = 25
    assert 0 < age < 150, "Age must be positive and reasonable"

    # Testing temperature in Celsius
    temperature = 22
    assert -273.15 <= temperature, "Temperature can't be below absolute zero"

    print("All range checks passed!")

**Assumption 2: Collections Are Not Empty**

Many operations fail or produce meaningless results on empty collections. Always check when an empty collection would break your logic.

.. activecode:: ac19_assumptions_2

    def calculate_average(numbers):
        assert len(numbers) > 0, "Cannot calculate average of empty list"
        return sum(numbers) / len(numbers)

    scores = [85, 92, 78, 95]
    avg = calculate_average(scores)
    print(f"Average: {avg}")

    # This will fail with a clear message
    empty_scores = []
    avg2 = calculate_average(empty_scores)

**Assumption 3: Related Values Have Logical Relationships**

When variables depend on each other, test that their relationships make sense.

.. activecode:: ac19_assumptions_3

    # Date range validation
    start_year = 2020
    end_year = 2024
    assert start_year <= end_year, "Start year must be before or equal to end year"

    # Price and discount validation
    original_price = 100
    sale_price = 75
    assert sale_price <= original_price, "Sale price can't exceed original price"

    # Coordinate boundaries
    min_x, max_x = 0, 100
    x_position = 50
    assert min_x <= x_position <= max_x, f"Position {x_position} outside bounds [{min_x}, {max_x}]"

    print("All relationship checks passed!")

.. important:: 🎯 When to Add Assertion Checks

   **High-value assertion targets:**

   ========================  ====================================  ================================
   Situation                 Example                                Why Check?
   ========================  ====================================  ================================
   User input                Age, prices, quantities                Users make mistakes
   External data             API responses, file contents           Can't control format/values
   Algorithm preconditions   List not empty, denominator ≠ 0        Prevents crashes or wrong results
   Business logic            Discount ≤ original price              Protects against logic errors
   Loop invariants           Counter stays within bounds            Catches infinite loop bugs
   ========================  ====================================  ================================

Practical Example: Validating Student Records
----------------------------------------------

Here's a realistic example combining multiple assumption checks:

.. activecode:: ac19_assumptions_4

    def process_student_record(student):
        """Process a student record with comprehensive validation."""

        # Type checks
        assert type(student) == dict, "Student record must be a dictionary"

        # Required fields exist
        required_fields = ['name', 'age', 'grades']
        for field in required_fields:
            assert field in student, f"Missing required field: {field}"

        # Value range checks
        assert 5 <= student['age'] <= 100, "Invalid age"
        assert len(student['grades']) > 0, "Student must have at least one grade"

        # Grade validity
        for grade in student['grades']:
            assert 0 <= grade <= 100, f"Invalid grade: {grade}"

        # Calculate and return average
        avg = sum(student['grades']) / len(student['grades'])
        return avg

    # Valid student
    student1 = {
        'name': 'Alice',
        'age': 16,
        'grades': [85, 92, 88, 95]
    }

    print(f"Average grade: {process_student_record(student1)}")

    # Try with invalid data (uncomment to see error)
    # student2 = {'name': 'Bob', 'age': 16, 'grades': [150, 85]}
    # process_student_record(student2)  # Will fail: Invalid grade

.. admonition:: 💡 Assertion Messages Are Documentation

   Good assertion messages serve two purposes:

   1. **Immediate debugging:** Tell you exactly what went wrong
   2. **Code documentation:** Explain what the code expects

   Compare:

   ::

      # ❌ Unclear
      assert x > 0

      # ✅ Clear
      assert x > 0, f"Withdrawal amount must be positive, got {x}"

**Check Your Understanding**

.. mchoice:: tc_assumptions_1
   :answer_a: To make the code run faster
   :answer_b: To catch logic errors early when invalid values are encountered
   :answer_c: To convert values to the correct range
   :answer_d: To replace if statements
   :correct: b
   :feedback_a: Assertions add a small performance cost, not a benefit.
   :feedback_b: Correct! Range assertions catch invalid values immediately, preventing them from causing problems later.
   :feedback_c: Assertions check but don't modify values.
   :feedback_d: Assertions are for checking assumptions, not control flow.

   Why is it important to check that values are within valid ranges (e.g., ``0 <= discount <= 1``)?

.. mchoice:: tc_assumptions_2
   :answer_a: assert len(items) > 0
   :answer_b: assert items != []
   :answer_c: assert items
   :answer_d: All of the above
   :correct: d
   :feedback_a: This explicitly checks the length is greater than zero.
   :feedback_b: This checks the list is not an empty list.
   :feedback_c: Empty collections are "falsy" in Python, so this works too.
   :feedback_d: Correct! All three will catch empty collections, though option a is most explicit.

   Which assertion would catch an empty list before calculating its average?