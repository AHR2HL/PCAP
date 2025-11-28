..  Copyright (C)  Paul Resnick and Lauren Murphy.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Testing Optional Parameters
============================

If a function takes an optional parameter, one of the edge cases to test for is when no parameter value is supplied during execution. That will test whether the default value is being set correctly when the parameter is omitted.

Consider the following function, which counts the number of "long enough" words in a list. What counts as long enough is determined by an optional parameter, ``min_length``.

.. activecode:: ac19_2_3

    def count_long_words(words, min_length=5):
        ct = 0
        for word in words:
            if len(word) >= min_length:
                ct += 1
        return ct

What return value tests could we write to check whether it is implemented correctly? First, we could construct a list of words that has words of many lengths, including a degenerate empty string that has length 0. One return value test would omit ``min_length`` and check that we got the right count. Other return value tests would supply ``min_length`` and would include the edge case where ``min_length`` is 0 and one where it is very large.

.. activecode:: ac19_2_3b

    def count_long_words(words, min_length=5):
        ct = 0
        for word in words:
            if len(word) >= min_length:
                ct += 1
        return ct

    test_words = ["", "1", "12", "123", "1234", "12345", "123456"]
    assert count_long_words(test_words) == 2
    assert count_long_words(test_words, min_length=0) == 7
    assert count_long_words(test_words, min_length=4) == 3
    assert count_long_words(test_words, min_length=100) == 0

**Check Your Understanding**

.. mchoice:: tc_optional_1
   :answer_a: count_long_words(test_words)
   :answer_b: count_long_words(test_words, min_length=5)
   :answer_c: count_long_words(test_words, 5)
   :answer_d: All of the above
   :correct: d
   :feedback_a: Correct - omitting min_length uses the default value of 5.
   :feedback_b: Correct - explicitly passing 5 should produce the same result.
   :feedback_c: Correct - passing 5 positionally also works.
   :feedback_d: Correct! All three should produce the same result since they all use min_length=5.

   Which function call(s) will use ``min_length=5`` when calling ``count_long_words``?

.. mchoice:: tc_optional_2
   :answer_a: To verify the default value is set correctly
   :answer_b: To check the function works when the parameter is omitted
   :answer_c: To ensure the function doesn't crash without the parameter
   :answer_d: All of the above
   :correct: d
   :feedback_a: Yes, this verifies the default works as intended.
   :feedback_b: Yes, users will often omit optional parameters.
   :feedback_c: Yes, this is a critical edge case.
   :feedback_d: Correct! Testing without the optional parameter validates all these important behaviors.

   Why is it important to test a function by omitting the optional parameter?

.. mchoice:: tc_optional_3
   :answer_a: Only test with the default value
   :answer_b: Test with the default value (omitted), a typical value, and boundary/edge values
   :answer_c: Only test edge cases like 0 and very large values
   :answer_d: Testing optional parameters is not necessary
   :correct: b
   :feedback_a: This misses important cases where users provide their own values.
   :feedback_b: Correct! Comprehensive testing includes default behavior, typical usage, and edge cases.
   :feedback_c: Edge cases are important but you also need to test typical usage.
   :feedback_d: Optional parameters need thorough testing since they have multiple code paths.

   What's the best strategy for testing functions with optional parameters?

.. mchoice:: tc_optional_4
   :answer_a: 0
   :answer_b: 2
   :answer_c: 5
   :answer_d: 7
   :correct: d
   :feedback_a: min_length=0 means count all words with length >= 0, which is all words.
   :feedback_b: That's the result when min_length=5 (the default).
   :feedback_c: That's the value of min_length, not the count.
   :feedback_d: Correct! With min_length=0, all 7 words qualify (even the empty string has length >= 0).

   Given ``test_words = ["", "1", "12", "123", "1234", "12345", "123456"]``, what does ``count_long_words(test_words, min_length=0)`` return?

.. mchoice:: tc_optional_5
   :answer_a: min_length=5, min_length=10, min_length=100
   :answer_b: min_length=0, min_length=7, min_length=100
   :answer_c: min_length=1, min_length=6, min_length=100
   :answer_d: No additional test cases are needed
   :correct: b
   :feedback_a: These miss the important edge case of 0 and don't test all boundary values.
   :feedback_b: Correct! Test 0 (minimum possible), 7 (length of longest word), and 100 (larger than any word).
   :feedback_c: These are reasonable but miss the important 0 edge case and the exact length boundary.
   :feedback_d: Multiple test cases are essential for optional parameters.

   Besides testing with the default value omitted, which additional test cases would provide the best coverage for ``count_long_words`` with ``test_words = ["", "1", "12", "123", "1234", "12345", "123456"]``?
