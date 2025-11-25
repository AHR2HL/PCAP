..  Copyright (C)  Adam Roush.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Practice and Mastery
====================

.. index:: recursion practice, recursion assessment, base case, call stack, tail recursion, fibonacci, factorial, tree traversal, pitfalls

Introduction
------------

Welcome to the **Recursion Practice & Mastery** assessment. This mirrors the established structure you’ve seen in other chapters:

- **Vocabulary Review** — precision on terms (8 MCQs)
- **Conceptual Understanding** — reason about behavior & performance (8 MCQs)
- **Parsons Problems** — assemble correct recursive solutions (5)
- **Coding Challenges** — implement recursive functions with tests (10)
- **Debugging Challenges** — fix broken recursive code (5)
- **Self-Assessment Checklist** — track your mastery
- **Quick Reference Guide** — patterns and pitfalls at a glance

Work steadily, sketch call stacks, and lean on invariants. **You’ve got this!** 🚀

----

Part 1: Vocabulary Review
-------------------------------

.. index:: recursion vocabulary, base case, recursive case, call stack, tail recursion, memoization

Test your understanding of foundational terminology.

.. mchoice:: rec_practice_vocab_basecase
    :answer_a: The part of a recursive function that calls itself
    :answer_b: The stopping condition that returns without further recursion
    :answer_c: The first line of a function definition
    :answer_d: The case with the smallest input size that still recurses
    :correct: b
    :feedback_a: That’s the recursive case.
    :feedback_b: Correct! The base case stops the recursion.
    :feedback_c: That’s just syntax.
    :feedback_d: The base case must not recurse at all.

    What is the **base case**?

.. mchoice:: rec_practice_vocab_recursivecase
    :answer_a: Any branch that eventually calls the same function again
    :answer_b: Any branch that returns immediately
    :answer_c: A helper function that is non-recursive
    :answer_d: The outer wrapper around a function
    :correct: a
    :feedback_a: Correct! The recursive case makes the self-call on a smaller input.
    :feedback_b: That describes the base case.
    :feedback_c: Helpers can be recursive or not.
    :feedback_d: Outer wrappers are unrelated to recursion itself.

    What is a **recursive case**?

.. mchoice:: rec_practice_vocab_callstack
    :answer_a: The structure that tracks active function calls at runtime
    :answer_b: A data structure used only by recursive functions
    :answer_c: A Python list of results
    :answer_d: A memoization table
    :correct: a
    :feedback_a: Correct! The call stack holds stack frames for all active calls.
    :feedback_b: Iterative calls also use the call stack.
    :feedback_c: Lists are user-level data, not the runtime stack.
    :feedback_d: Memo tables live in user memory structures.

    What is the **call stack**?

.. mchoice:: rec_practice_vocab_tail
    :answer_a: A recursion where the recursive call is the final operation
    :answer_b: A recursion that has no base case
    :answer_c: Any recursion with two or more calls
    :answer_d: A recursion that always overflows the stack
    :correct: a
    :feedback_a: Correct! In tail recursion, nothing happens after the recursive call returns.
    :feedback_b: Lack of base case is a bug, not tail recursion.
    :feedback_c: Tail recursion can be single- or multi-branch; the key is “last action”.
    :feedback_d: Tail recursion isn’t inherently unsafe.

    What is **tail recursion**?

.. mchoice:: rec_practice_vocab_memo
    :answer_a: Caching results of expensive function calls
    :answer_b: Increasing the recursion limit
    :answer_c: Converting recursion to iteration
    :answer_d: Precomputing factorials only
    :correct: a
    :feedback_a: Correct! Memoization stores results keyed by inputs.
    :feedback_b: That changes stack depth, not caching.
    :feedback_c: That’s refactoring, not memoization.
    :feedback_d: Memoization applies broadly, not just factorial.

    What is **memoization**?

.. mchoice:: rec_practice_vocab_divideconquer
    :answer_a: Expanding the problem into larger subproblems
    :answer_b: Splitting the problem into smaller independent subproblems
    :answer_c: Using a single loop instead of recursion
    :answer_d: Eliminating base cases
    :correct: b
    :feedback_a: Larger subproblems won’t terminate.
    :feedback_b: Correct! Divide and conquer breaks into smaller pieces.
    :feedback_c: That’s iterative refactoring.
    :feedback_d: You always need base cases.

    What does **divide and conquer** mean in recursion?

.. mchoice:: rec_practice_vocab_stackoverflow
    :answer_a: A runtime error when too many calls accumulate on the call stack
    :answer_b: A list growing too large
    :answer_c: A variable assignment bug
    :answer_d: A type error
    :correct: a
    :feedback_a: Correct! Deep recursion can exceed the call stack capacity.
    :feedback_b: Lists are on the heap, not the call stack.
    :feedback_c: Not specific to call stacks.
    :feedback_d: Type errors are unrelated to stack depth.

    What is a **stack overflow**?

.. mchoice:: rec_practice_vocab_recvsiter
    :answer_a: Recursive solutions always use less memory
    :answer_b: Iterative solutions are always faster
    :answer_c: Tradeoffs depend on problem structure, overhead, and clarity
    :answer_d: Both are identical at runtime
    :correct: c
    :feedback_a: Not always—stack frames add overhead.
    :feedback_b: Not always—recursion can be elegant and comparable.
    :feedback_c: Correct! Evaluate asymptotics, constants, and readability.
    :feedback_d: They differ in control flow and stack use.

    How do **recursive vs iterative** solutions compare?

---

Part 2: Conceptual Understanding
------------------------------------

.. index:: recursion concepts, complexity, base cases, termination, tail calls, call tree

.. mchoice:: rec_practice_concept_termination
    :answer_a: If a function has a base case, it will always terminate
    :answer_b: If each recursive step makes progress toward a base case, it will terminate
    :answer_c: Tail recursion guarantees termination
    :answer_d: If inputs are small, termination is irrelevant
    :correct: b
    :feedback_a: A base case is necessary but not sufficient—you must reach it.
    :feedback_b: Correct! Progress + reachable base case ⇒ termination.
    :feedback_c: Tail position alone doesn’t imply termination.
    :feedback_d: Inputs still must shrink toward the base case.

    What guarantees **termination** in recursion?

.. mchoice:: rec_practice_concept_calls
    :answer_a: The number of stack frames equals the maximum number of nested calls
    :answer_b: Python reuses a single frame for tail recursion
    :answer_c: The call stack grows and shrinks unpredictably
    :answer_d: The call stack is the same as global variables
    :correct: a
    :feedback_a: Correct! Depth equals nested calls at that point.
    :feedback_b: Python does not perform tail call elimination.
    :feedback_c: Growth is deterministic by call flow.
    :feedback_d: Globals are unrelated to the stack.

    Which is true of the **call stack** in Python?

.. mchoice:: rec_practice_concept_tailperf
    :answer_a: Tail recursion is optimized away by CPython
    :answer_b: Tail recursion avoids function call overhead in Python
    :answer_c: Tail recursion can improve clarity but not stack depth in Python
    :answer_d: Tail recursion never works
    :correct: c
    :feedback_a: CPython does not do TCO.
    :feedback_b: Without TCO, overhead remains.
    :feedback_c: Correct! Tail position can help reasoning but not depth.
    :feedback_d: Tail recursion does work; it’s just not optimized.

    What’s true about **tail recursion in Python**?

.. mchoice:: rec_practice_concept_fib
    :answer_a: Naive recursive Fibonacci is O(n)
    :answer_b: Naive recursive Fibonacci is O(φ^n) time and O(n) space
    :answer_c: Naive recursive Fibonacci is O(n log n)
    :answer_d: Naive recursive Fibonacci is O(1)
    :correct: b
    :feedback_a: It’s exponential time due to repeated work.
    :feedback_b: Correct! Exponential time, linear stack depth.
    :feedback_c: Not applicable here.
    :feedback_d: Definitely not constant.

    What are the complexity characteristics of **naive fib**, that is developing fibbonacci using recursion without any optimisation features??

.. mchoice:: rec_practice_concept_stackoverflow
    :answer_a: Increasing `sys.setrecursionlimit` always fixes infinite recursion
    :answer_b: Stack overflow is often a symptom of a missing/incorrect base case or progress step
    :answer_c: Python eliminates deep recursion automatically
    :answer_d: Using lists prevents stack overflow
    :correct: b
    :feedback_a: It may mask the bug but won’t fix it.
    :feedback_b: Correct! Inspect termination logic.
    :feedback_c: No automatic elimination.
    :feedback_d: Data structure choice doesn’t “turn off” the stack.

    What usually causes **stack overflow**?

.. mchoice:: rec_practice_concept_tree
    :answer_a: Tree traversals always require auxiliary data structures
    :answer_b: Recursion maps naturally to trees because node links define subproblems
    :answer_c: Iteration cannot traverse trees
    :answer_d: DFS is iterative-only
    :correct: b
    :feedback_a: You can traverse recursively with the call stack.
    :feedback_b: Correct! Recursion mirrors tree structure.
    :feedback_c: Iterative traversals exist (with explicit stacks/queues).
    :feedback_d: DFS is often expressed recursively.

    Why does **recursion suit tree traversal**?

.. mchoice:: rec_practice_concept_compare
    :answer_a: Choose recursion for every problem—it’s clearer
    :answer_b: Choose iteration whenever you see a loop in pseudocode
    :answer_c: Choose the form that makes correctness/termination obvious and meets performance needs
    :answer_d: Always convert recursion to tail recursion in Python
    :correct: c
    :feedback_a: No one-size-fits-all.
    :feedback_b: Pseudocode form isn’t a mandate.
    :feedback_c: Correct! Clarity + correctness + constraints guide the choice.
    :feedback_d: Tail recursion has no stack benefit in Python.

    How should you choose **recursion vs iteration**?

---

Part 3: Parsons Problems
---------------------------

.. index:: Parsons recursion, arrange blocks, call stack

Arrange the blocks to form correct solutions. Distractors are labeled.

.. parsonsprob:: rec_parsons_factorial_assessment
   :language: python
   :numbered: left
   :adaptive:

   Implement recursive factorial ``fact(n)`` with proper validation.
   -----
   def fact(n):
   =====
       if n in (0, 1):
   =====
           return 1
   =====
       return n * fact(n-1)
   =====
       return n + fact(n-1)  #distractor


.. parsonsprob:: rec_parsons_sumlist
   :language: python
   :numbered: left
   :adaptive:

   Sum a list recursively without using ``sum``.
   -----
   def rsum(xs):
   =====
       if not xs:
   =====
           return 0
   =====
       head = xs[0]
   =====
       tail = xs[1:]
   =====
       return head + rsum(tail)
   =====
       return rsum(xs)  #distractor
   =====
       head, tail = xs #distractor


.. parsonsprob:: rec_parsons_tailacc
    :language: python
    :numbered: left
    :adaptive:

    Tail-recursive style factorial using a parameter.

    -----
    def fact_tail(n, acc=1):
    =====
        if n in (0, 1):
    =====
            return acc
    =====
        return fact_tail(n-1, acc*n)
    =====
        return acc * fact_tail(n-1)  #distractor (not tail)

**Binary Tree Search Problem**

A **binary tree** is a data structure where each node has at most two children (left and right). Here's a simple example:

::

        5
       / \
      3   8
     / \   \
    1   4   9

Each node has a ``value``, a ``left`` child, and a ``right`` child (which can be ``None``).

.. parsonsprob:: recursion_binary_tree_search
   :language: python
   :adaptive:
   :numbered: left

   Arrange the blocks to create a recursive function that searches for a target value in a binary tree.
   The function should return ``True`` if the value is found, ``False`` otherwise.

   **Node class (already provided):**

   .. code-block:: python

       class TreeNode:
           def __init__(self, value):
               self.value = value
               self.left = None
               self.right = None

   **Example:**

   .. code-block:: python

       # Tree structure:
       #     5
       #    / \
       #   3   8
       root = TreeNode(5)
       root.left = TreeNode(3)
       root.right = TreeNode(8)

       search_tree(root, 8)   # Returns True
       search_tree(root, 10)  # Returns False
   -----
   def search_tree(node, target):
   =====
   def search_tree(node, target, left, right): #distractor
   =====
       if node is None:
   =====
       if node == None: #distractor
   =====
           return False
   =====
       if node.value == target:
   =====
       if node == target: #distractor
   =====
           return True
   =====
       left_result = search_tree(node.left, target)
   =====
       left_result = search_tree(node.left) #distractor
   =====
       right_result = search_tree(node.right, target)
   =====
       return left_result or right_result
   =====
       return left_result and right_result #distractor

.. parsonsprob:: rec_parsons_binary_search
    :language: python
    :adaptive:
    :numbered: left

    Recursive binary search on a sorted list returning index or -1.
    -----
    def rbin_search(xs, target, lo=0, hi=None):
    =====
       if hi is None:
    =====
            hi = len(xs) - 1
    =====
       if lo > hi:
    =====
            return -1
    =====
       mid = (lo + hi) // 2
    =====
        if xs[mid] == target:
    =====
            return mid
    =====
        if xs[mid] < target:
    =====
            return rbin_search(xs, target, mid+1, hi)
    =====
        return rbin_search(xs, target, lo, mid-1)
    =====
       return rbin_search(xs, target, lo, hi)  #distractor
    ---

Part 4: Coding Challenges
--------------------------

.. index:: recursion coding challenges, unit tests, autograder

Build these recursive functions. **Do not** use loops unless instructed. Each activity includes unit tests.

**Challenge 1: Factorial**

.. activecode:: rec_practice_code_factorial
   :language: python
   :autograde: unittest

   Create a function ``factorial(n)`` that:
   - Computes n! recursively
   - Raises ValueError if n < 0
   - Returns 1 for n = 0 or n = 1
   - Must use recursion (no loops!)

   Example::

       factorial(0)  # 1
       factorial(5)  # 120
       factorial(-1) # Raises ValueError

   ~~~~
   def factorial(n):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_base_cases(self):
           self.assertEqual(factorial(0), 1)
           self.assertEqual(factorial(1), 1)

       def test_small_values(self):
           self.assertEqual(factorial(5), 120)
           self.assertEqual(factorial(3), 6)

       def test_negative(self):
           with self.assertRaises(ValueError):
               factorial(-1)

       def test_recursion_enforced(self):
           # Enforce recursion
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_code_factorial_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def factorial(n):
          if n < 0:
              raise ValueError("n must be >= 0")
          if n in (0, 1):
              return 1
          return n * factorial(n - 1)

**Challenge 2: Sum of Digits**

.. activecode:: rec_practice_code_sumdigits
   :language: python
   :autograde: unittest

   Create a function ``sum_digits(n)`` that:
   - Computes the sum of all decimal digits in n
   - Works for n >= 0
   - Must use recursion (no loops!)

   **Hint:** Use modulo (%) to get the last digit, and integer division (//) to remove it.

   Example::

       sum_digits(0)     # 0
       sum_digits(7)     # 7
       sum_digits(42)    # 6  (4 + 2)
       sum_digits(9999)  # 36 (9 + 9 + 9 + 9)

   ~~~~
   def sum_digits(n):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_single_digit(self):
           self.assertEqual(sum_digits(0), 0)
           self.assertEqual(sum_digits(7), 7)

       def test_multiple_digits(self):
           self.assertEqual(sum_digits(42), 6)
           self.assertEqual(sum_digits(123), 6)
           self.assertEqual(sum_digits(9999), 36)

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_code_sumdigits_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def sum_digits(n):
          if n < 10:
              return n
          return n % 10 + sum_digits(n // 10)

**Challenge 3: Reverse a String**

.. activecode:: rec_practice_code_reverse
   :language: python
   :autograde: unittest

   Create a function ``rreverse(s)`` that:
   - Reverses a string recursively
   - Works for empty strings and single characters
   - Must use recursion (no loops!)

   **Hint:** Take the last character and add it to the reversed rest of the string.

   Example::

       rreverse("")      # ""
       rreverse("a")     # "a"
       rreverse("abc")   # "cba"
       rreverse("hello") # "olleh"

   ~~~~
   def rreverse(s):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_base_cases(self):
           self.assertEqual(rreverse(""), "")
           self.assertEqual(rreverse("a"), "a")

       def test_short_strings(self):
           self.assertEqual(rreverse("abc"), "cba")
           self.assertEqual(rreverse("hello"), "olleh")

       def test_palindrome(self):
           self.assertEqual(rreverse("racecar"), "racecar")

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_code_reverse_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def rreverse(s):
          if len(s) <= 1:
              return s
          return s[-1] + rreverse(s[:-1])

**Challenge 4: Flatten Nested Lists**

.. activecode:: rec_practice_code_flatten
   :language: python
   :autograde: unittest

   Create a function ``flatten(xs)`` that:
   - Takes a nested list (lists within lists)
   - Returns a flat list with all non-list elements
   - Must use recursion (no loops!)

   **Hint:** Check if the first element is a list. If so, flatten it and combine with the flattened rest.

   Example::

       flatten([1, [2, [3]], 4])  # [1, 2, 3, 4]
       flatten([])                # []
       flatten([[[1]]])           # [1]
       flatten([[[]]])            # []

   ~~~~
   def flatten(xs):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_empty(self):
           self.assertEqual(flatten([]), [])
           self.assertEqual(flatten([[[]]]), [])

       def test_flat_already(self):
           self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])

       def test_nested(self):
           self.assertEqual(flatten([1, [2, [3]], 4]), [1, 2, 3, 4])
           self.assertEqual(flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])

       def test_deeply_nested(self):
           self.assertEqual(flatten([[[1]]]), [1])
           self.assertEqual(flatten([1, [2, [3, [4, [5]]]]]), [1, 2, 3, 4, 5])

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_code_flatten_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def flatten(xs):
          # Base case: empty list
          if not xs:
              return []

          # Check if first element is a list
          if isinstance(xs[0], list):
              # Flatten the first element and combine with flattened rest
              return flatten(xs[0]) + flatten(xs[1:])

          # First element is not a list, keep it and flatten the rest
          return [xs[0]] + flatten(xs[1:])

**Challenge 5: Binary Search (Index)**

.. activecode:: rec_practice_code_rbinsearch
   :language: python
   :autograde: unittest

   Create a function ``rbin_search(xs, target, lo=0, hi=None)`` that:
   - Performs binary search recursively on a sorted list
   - Returns the index of target if found
   - Returns -1 if target is not in the list
   - Must use recursion (no loops!)

   **Parameters:**
   - ``xs``: sorted list to search
   - ``target``: value to find
   - ``lo``: start index (default 0)
   - ``hi``: end index (default None, meaning len(xs)-1)

   Example::

       rbin_search([1, 2, 4, 5, 9], 4)   # 2
       rbin_search([1, 2, 4, 5, 9], 9)   # 4
       rbin_search([1, 2, 3], 7)         # -1

   ~~~~
   def rbin_search(xs, target, lo=0, hi=None):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_empty(self):
           self.assertEqual(rbin_search([], 5), -1)

       def test_single_element(self):
           self.assertEqual(rbin_search([5], 5), 0)
           self.assertEqual(rbin_search([5], 3), -1)

       def test_found_various_positions(self):
           xs = [1, 2, 4, 5, 9]
           self.assertEqual(rbin_search(xs, 1), 0)  # First
           self.assertEqual(rbin_search(xs, 4), 2)  # Middle
           self.assertEqual(rbin_search(xs, 9), 4)  # Last

       def test_not_found(self):
           xs = [1, 2, 4, 5, 9]
           self.assertEqual(rbin_search(xs, 0), -1)   # Too small
           self.assertEqual(rbin_search(xs, 10), -1)  # Too large
           self.assertEqual(rbin_search(xs, 3), -1)   # Between elements

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_code_rbinsearch_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def rbin_search(xs, target, lo=0, hi=None):
          # Initialize hi if not provided
          if hi is None:
              hi = len(xs) - 1

          # Base case: search space is empty
          if lo > hi:
              return -1

          # Find middle element
          mid = (lo + hi) // 2

          # Check if we found the target
          if xs[mid] == target:
              return mid

          # Target is in the right half
          if xs[mid] < target:
              return rbin_search(xs, target, mid + 1, hi)

          # Target is in the left half
          return rbin_search(xs, target, lo, mid - 1)

**Challenge 6: Palindrome Check**

.. activecode:: rec_practice_code_pal
   :language: python
   :autograde: unittest

   Create a function ``rpal(s)`` that:
   - Checks if a string is a palindrome (reads same forwards and backwards)
   - Returns True if palindrome, False otherwise
   - Must use recursion (no loops!)

   **Hint:** Compare first and last characters. If they match, check if the middle is a palindrome.

   Example::

       rpal("")          # True (empty string is palindrome)
       rpal("a")         # True (single character)
       rpal("racecar")   # True
       rpal("hello")     # False

   ~~~~
   def rpal(s):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_empty_and_single(self):
           self.assertTrue(rpal(""))
           self.assertTrue(rpal("a"))

       def test_even_length_palindromes(self):
           self.assertTrue(rpal("aa"))
           self.assertTrue(rpal("abba"))
           self.assertTrue(rpal("noon"))

       def test_odd_length_palindromes(self):
           self.assertTrue(rpal("aba"))
           self.assertTrue(rpal("racecar"))
           self.assertTrue(rpal("madam"))

       def test_not_palindromes(self):
           self.assertFalse(rpal("ab"))
           self.assertFalse(rpal("abca"))
           self.assertFalse(rpal("hello"))

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_code_pal_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def rpal(s):
          # Base case: empty string or single character
          if len(s) <= 1:
              return True

          # Check if first and last characters match
          if s[0] != s[-1]:
              return False

          # Recursively check the middle substring
          return rpal(s[1:-1])

**Challenge 7: Count Leaves (Tree)**

.. activecode:: rec_practice_code_countleaves
   :language: python
   :autograde: unittest

   Create a function ``count_leaves(node)`` that:
   - Counts the number of leaf nodes in a binary tree
   - A leaf is a node with no children (both left and right are None)
   - Returns 0 for an empty tree (None)
   - Must use recursion (no loops!)

   **Binary Tree Structure:**
   - Each node has: ``val``, ``left``, ``right``
   - ``None`` represents an empty tree

   **Hint:** A leaf has no children. For other nodes, sum the leaves in left and right subtrees.

   Example::

       #     1
       #    / \
       #   2   3
       #      /
       #     4
       # This tree has 2 leaves: nodes 2 and 4

       tree = Node(1, Node(2), Node(3, Node(4)))
       count_leaves(tree)  # 2

   ~~~~
   class Node:
       def __init__(self, val, left=None, right=None):
           self.val = val
           self.left = left
           self.right = right

   def count_leaves(node):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_empty_tree(self):
           self.assertEqual(count_leaves(None), 0)

       def test_single_node(self):
           tree = Node(1)
           self.assertEqual(count_leaves(tree), 1)

       def test_two_leaves(self):
           # Tree: 1 with children 2, 3 (both leaves)
           tree = Node(1, Node(2), Node(3))
           self.assertEqual(count_leaves(tree), 2)

       def test_mixed_tree(self):
           # Tree from example: 1 -> 2, 3 -> 4
           tree = Node(1, Node(2), Node(3, Node(4)))
           self.assertEqual(count_leaves(tree), 2)

       def test_all_left(self):
           # Chain: 1 -> 2 -> 3 (only 3 is leaf)
           tree = Node(1, Node(2, Node(3)))
           self.assertEqual(count_leaves(tree), 1)

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_code_countleaves_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      class Node:
          def __init__(self, val, left=None, right=None):
              self.val = val
              self.left = left
              self.right = right

      def count_leaves(node):
          # Base case: empty tree
          if node is None:
              return 0

          # Base case: leaf node (no children)
          if node.left is None and node.right is None:
              return 1

          # Recursive case: sum leaves in left and right subtrees
          return count_leaves(node.left) + count_leaves(node.right)

**Challenge 8: All Paths (Backtracking)**

.. activecode:: rec_practice_code_allpaths
   :language: python
   :autograde: unittest

   Create a function ``count_paths(m, n)`` that:
   - Counts all possible paths from top-left (0,0) to bottom-right (m-1, n-1)
   - Can only move right or down (no diagonal, no up, no left)
   - Grid dimensions are m rows by n columns
   - Raises ValueError if m or n is not positive
   - Must use recursion (no loops!)

   **Grid Example (3x3):**

   ::

       Start → → →
         ↓     ↓   ↓
         ↓     ↓   ↓
         ↓ → → → End

   **Hint:** At each position, you can go right or down. Total paths = paths going right + paths going down.

   Example::

       count_paths(1, 1)  # 1 (already at destination)
       count_paths(2, 2)  # 2 paths
       count_paths(3, 2)  # 3 paths
       count_paths(0, 2)  # Raises ValueError

   ~~~~
   def count_paths(m, n):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_single_cell(self):
           self.assertEqual(count_paths(1, 1), 1)

       def test_single_row(self):
           self.assertEqual(count_paths(1, 5), 1)

       def test_single_column(self):
           self.assertEqual(count_paths(5, 1), 1)

       def test_small_grids(self):
           self.assertEqual(count_paths(2, 2), 2)
           self.assertEqual(count_paths(3, 2), 3)
           self.assertEqual(count_paths(2, 3), 3)

       def test_larger_grid(self):
           self.assertEqual(count_paths(3, 3), 6)
           self.assertEqual(count_paths(4, 3), 10)

       def test_invalid_dimensions(self):
           with self.assertRaises(ValueError):
               count_paths(0, 2)
           with self.assertRaises(ValueError):
               count_paths(2, 0)
           with self.assertRaises(ValueError):
               count_paths(-1, 3)

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_code_allpaths_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def count_paths(m, n):
          # Validate input
          if m <= 0 or n <= 0:
              raise ValueError("dims must be positive")

          # Base case: single row or single column (only one path)
          if m == 1 or n == 1:
              return 1

          # Recursive case: sum paths from moving right and moving down
          # Move down: reduce rows by 1
          # Move right: reduce columns by 1
          return count_paths(m - 1, n) + count_paths(m, n - 1)

**Challenge 9: Call Stack Trace**

.. activecode:: rec_practice_code_trace
   :language: python
   :autograde: unittest

   Create a function ``trace_args(n)`` that:
   - Returns a list of all arguments seen during the recursive calls
   - Implements the pattern: f(n) = f(n-1) + 1, with base case f(0) = 0
   - The list should show the sequence: [0, 1, 2, ..., n]
   - Must use recursion (no loops!)

   **What's happening:**
   - ``trace_args(3)`` calls ``trace_args(2)``
   - ``trace_args(2)`` calls ``trace_args(1)``
   - ``trace_args(1)`` calls ``trace_args(0)``
   - ``trace_args(0)`` returns [0]
   - Each level adds its own n to the list

   **Hint:** Base case returns [0]. Recursive case returns the trace of (n-1) with n appended.

   Example::

       trace_args(0)  # [0]
       trace_args(1)  # [0, 1]
       trace_args(4)  # [0, 1, 2, 3, 4]

   ~~~~
   def trace_args(n):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_base_case(self):
           self.assertEqual(trace_args(0), [0])

       def test_small_values(self):
           self.assertEqual(trace_args(1), [0, 1])
           self.assertEqual(trace_args(2), [0, 1, 2])
           self.assertEqual(trace_args(3), [0, 1, 2, 3])

       def test_larger_value(self):
           self.assertEqual(trace_args(4), [0, 1, 2, 3, 4])
           self.assertEqual(trace_args(5), [0, 1, 2, 3, 4, 5])

       def test_sequence_length(self):
           result = trace_args(10)
           self.assertEqual(len(result), 11)
           self.assertEqual(result[0], 0)
           self.assertEqual(result[-1], 10)

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_code_trace_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def trace_args(n):
          # Base case: n = 0, return list with just 0
          if n == 0:
              return [0]

          # Recursive case: get trace of (n-1) and append n
          return trace_args(n - 1) + [n]

**Challenge 10: Fibonacci with Memoization**

.. activecode:: rec_practice_code_fibmemo
   :language: python
   :autograde: unittest

   Create a function ``fib(n, memo=None)`` that:
   - Computes the nth Fibonacci number recursively
   - Uses memoization to cache results (top-down dynamic programming)
   - Base cases: fib(0) = 0, fib(1) = 1
   - Recursive formula: fib(n) = fib(n-1) + fib(n-2)
   - Must use recursion with memoization!

   **Why memoization?**
   - Without it: fib(30) makes ~2.7 million recursive calls
   - With it: fib(30) makes only 31 recursive calls
   - Stores results in a dictionary to avoid recalculating

   **Hint:** Check if n is in memo. If not, calculate it recursively and store it before returning.

   Example::

       fib(0)   # 0
       fib(1)   # 1
       fib(5)   # 5  (0, 1, 1, 2, 3, 5)
       fib(10)  # 55

   ~~~~
   def fib(n, memo=None):
       # Your code here
       pass

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_base_cases(self):
           self.assertEqual(fib(0), 0)
           self.assertEqual(fib(1), 1)

       def test_small_values(self):
           self.assertEqual(fib(2), 1)
           self.assertEqual(fib(3), 2)
           self.assertEqual(fib(4), 3)
           self.assertEqual(fib(5), 5)

       def test_medium_values(self):
           self.assertEqual(fib(10), 55)
           self.assertEqual(fib(15), 610)

       def test_larger_value(self):
           # This would be very slow without memoization
           self.assertEqual(fib(20), 6765)

       def test_efficiency(self):
           # Test that it can handle reasonably large n quickly
           # Without memoization, fib(30) would take forever
           result = fib(30)
           self.assertEqual(result, 832040)

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_code_fibmemo_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   .. code-block:: python

      def fib(n, memo=None):
          # Initialize memo dictionary if not provided
          if memo is None:
              memo = {}

          # Check if result is already cached
          if n in memo:
              return memo[n]

          # Base cases: fib(0) = 0, fib(1) = 1
          if n < 2:
              memo[n] = n
          else:
              # Recursive case: fib(n) = fib(n-1) + fib(n-2)
              memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

          return memo[n]

-----

Part 5: Debugging Challenges
-----------------------------

.. index:: recursion debugging, infinite recursion, off-by-one, wrong base case

Fix the bugs. Run, observe errors, then correct them. Reveal solutions when ready.

**Debug 1**

.. activecode:: rec_practice_debug_progress
   :language: python
   :autograde: unittest

   This function intends to count down to zero. Fix it!
   ~~~~
   def countdown(n):
       if n == 0:
           return [0]
       return [n] + countdown(n)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_base_case(self):
           self.assertEqual(countdown(0), [0])

       def test_countdown_small(self):
           self.assertEqual(countdown(3), [3, 2, 1, 0])
           self.assertEqual(countdown(1), [1, 0])

       def test_countdown_larger(self):
           self.assertEqual(countdown(5), [5, 4, 3, 2, 1, 0])

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_debug_progress_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Problem:** The recursive call ``countdown(n)`` doesn't make progress toward the base case - it calls itself with the same value infinitely!

   **Fix:** Decrease ``n`` to make progress toward the base case:

   .. code-block:: python

      def countdown(n):
          if n == 0:
              return [0]
          return [n] + countdown(n - 1)  # Fixed: n-1 makes progress

      print(countdown(3))  # [3, 2, 1, 0]

**Debug 2**

.. activecode:: rec_practice_debug_basecase
   :language: python
   :autograde: unittest

   Factorial is wrong. Fix it!
   ~~~~
   def bad_fact(n):
       if n == 2:
           return 1
       return n * bad_fact(n - 1)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_base_cases(self):
           self.assertEqual(bad_fact(0), 1)
           self.assertEqual(bad_fact(1), 1)

       def test_small_factorials(self):
           self.assertEqual(bad_fact(2), 2)
           self.assertEqual(bad_fact(3), 6)
           self.assertEqual(bad_fact(4), 24)

       def test_larger_factorial(self):
           self.assertEqual(bad_fact(5), 120)
           self.assertEqual(bad_fact(6), 720)

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_debug_basecase_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Problem:** The base case checks for ``n == 2`` instead of ``n == 0`` or ``n == 1``. This causes:

   - ``bad_fact(3)`` works by accident (3 * 2 * 1)
   - ``bad_fact(1)`` or ``bad_fact(0)`` causes infinite recursion!

   **Fix:** Use proper base case for factorial:

   .. code-block:: python

      def bad_fact(n):
          if n in (0, 1):
              return 1
          return n * bad_fact(n - 1)

      print(bad_fact(3))   # 6
      print(bad_fact(0))   # 1 (now works!)
      print(bad_fact(1))   # 1 (now works!)

**Debug 3: Factorial with Accumulator**

.. activecode:: rec_practice_debug_tail
   :language: python
   :autograde: unittest

   This factorial implementation uses an accumulator but has a bug. Fix it!
   ~~~~
   def fact_tail_bad(n, acc=1):
       if n in (0, 1):
           return acc
       return fact_tail_bad(n - 1) * n

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_base_cases(self):
           self.assertEqual(fact_tail_bad(0, 1), 1)
           self.assertEqual(fact_tail_bad(1, 1), 1)

       def test_small_factorials(self):
           self.assertEqual(fact_tail_bad(3), 6)
           self.assertEqual(fact_tail_bad(4), 24)
           self.assertEqual(fact_tail_bad(5), 120)

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_debug_tail_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Problem:** The function does work (multiplication) **after** the recursive call returns. This is NOT tail recursion!

   - ``fact_tail_bad(n-1)`` returns a value
   - Then we multiply that value by ``n``
   - This creates a pending operation on the call stack

   **True tail recursion:** The recursive call must be the **last** operation (nothing happens after it returns).

   **Fix:** Pass the work into the accumulator parameter:

   .. code-block:: python

      def fact_tail_bad(n, acc=1):
          if n in (0, 1):
              return acc
          return fact_tail_bad(n - 1, acc * n)  # Fixed: multiply before call

      print(fact_tail_bad(4))  # 24

**Debug 4: Binary Search Implementation**

.. activecode:: rec_practice_debug_bounds
   :language: python
   :autograde: unittest

   This binary search has a bug. Fix it!
   ~~~~
   def rbin_bad(xs, target, lo=0, hi=None):
       if hi is None:
           hi = len(xs)
       if lo >= hi:
           return -1
       mid = (lo + hi) // 2
       if xs[mid] == target:
           return mid
       if xs[mid] < target:
           return rbin_bad(xs, target, mid, hi)
       else:
           return rbin_bad(xs, target, lo, mid)

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_empty_list(self):
           self.assertEqual(rbin_bad([], 5), -1)

       def test_single_element(self):
           self.assertEqual(rbin_bad([5], 5), 0)
           self.assertEqual(rbin_bad([5], 3), -1)

       def test_found_various_positions(self):
           xs = [1, 2, 4, 5, 9]
           self.assertEqual(rbin_bad(xs, 1), 0)  # First
           self.assertEqual(rbin_bad(xs, 4), 2)  # Middle
           self.assertEqual(rbin_bad(xs, 9), 4)  # Last

       def test_not_found(self):
           xs = [1, 2, 4, 5, 9]
           self.assertEqual(rbin_bad(xs, 0), -1)   # Too small
           self.assertEqual(rbin_bad(xs, 10), -1)  # Too large
           self.assertEqual(rbin_bad(xs, 3), -1)   # Between elements

       def test_two_elements(self):
           self.assertEqual(rbin_bad([1, 3], 1), 0)
           self.assertEqual(rbin_bad([1, 3], 3), 1)
           self.assertEqual(rbin_bad([1, 3], 2), -1)

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_debug_bounds_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Problem:** The code has multiple related bugs with bounds:

   1. ``hi = len(xs)`` is exclusive (pointing past the end)
   2. But ``lo >= hi`` check assumes inclusive bounds
   3. Recursive calls use ``mid`` instead of ``mid+1`` or ``mid-1``
   4. This can cause infinite recursion (keeps checking same mid)

   **Fix:** Use consistent inclusive bounds throughout:

   .. code-block:: python

      def rbin_bad(xs, target, lo=0, hi=None):
          if hi is None:
              hi = len(xs) - 1  # Fixed: inclusive bound
          if lo > hi:           # Fixed: correct check for inclusive
              return -1
          mid = (lo + hi) // 2
          if xs[mid] == target:
              return mid
          if xs[mid] < target:
              return rbin_bad(xs, target, mid + 1, hi)  # Fixed: skip mid
          return rbin_bad(xs, target, lo, mid - 1)      # Fixed: skip mid

      print(rbin_bad([1, 2, 4, 5, 9], 4))  # 2

**Debug 5: Fibonacci with Caching**

.. activecode:: rec_practice_debug_memo
   :language: python
   :autograde: unittest

   This fibonacci implementation uses caching. Fix the bug!
   ~~~~
   def fib_bad(n, memo={}):
       if n in memo:
           return memo[n]
       if n <= 2:
           memo[n] = n
       else:
           memo[n] = fib_bad(n - 1) + fib_bad(n - 2)
       return memo[n]

   ====
   from unittest.gui import TestCaseGui

   class myTests(TestCaseGui):
       def test_base_cases(self):
           self.assertEqual(fib_bad(0), 0)
           self.assertEqual(fib_bad(1), 1)

       def test_small_fibonacci(self):
           self.assertEqual(fib_bad(2), 1)
           self.assertEqual(fib_bad(3), 2)
           self.assertEqual(fib_bad(5), 5)

       def test_larger_fibonacci(self):
           self.assertEqual(fib_bad(10), 55)
           self.assertEqual(fib_bad(15), 610)

       def test_with_custom_memo(self):
           # Should be able to use a fresh memo
           custom = {}
           result = fib_bad(5, custom)
           self.assertEqual(result, 5)
           # Memo should have been populated
           self.assertIn(5, custom)

       def test_independence(self):
           # Multiple calls should work independently
           result1 = fib_bad(4, {})
           result2 = fib_bad(4, {})
           self.assertEqual(result1, 3)
           self.assertEqual(result2, 3)

       def test_recursion_enforced(self):
           source = self.getEditorText()
           self.assertNotIn('for', source, "Do not use 'for' loops")
           self.assertNotIn('while', source, "Do not use 'while' loops")

   myTests().main()

.. reveal:: rec_practice_debug_memo_solution
   :showtitle: Show Solution
   :hidetitle: Hide Solution

   **Problem:** The default argument ``memo={}`` is created **once** when the function is defined, not each time it's called!

   This means:
   - The same dictionary is shared across **all** calls to the function
   - Previous cached values persist between separate function calls
   - This is Python's infamous "mutable default argument" bug
   - Can cause wrong results if you call the function in different contexts

   **Fix:** Use ``None`` as default and create a new dict inside the function:

   .. code-block:: python

      def fib_bad(n, memo=None):
          if memo is None:
              memo = {}  # Fresh dict for each top-level call
          if n in memo:
              return memo[n]
          if n < 2:
              memo[n] = n
          else:
              memo[n] = fib_bad(n - 1, memo) + fib_bad(n - 2, memo)
          return memo[n]

      print([fib_bad(i) for i in range(6)])  # [0, 1, 1, 2, 3, 5]

-----

Part 6: Self-Assessment Checklist
----------------------------------

.. index:: recursion checklist

Check off the skills you’ve mastered:

**Base & Recursive Cases**

.. code-block:: text

    □ I can state the base case(s) clearly
    □ I ensure each recursive call makes measurable progress
    □ I can argue termination using a decreasing metric

**Call Stack Visualization**

.. code-block:: text

    □ I can sketch call trees/frames for small inputs
    □ I can explain return flow from deepest call back to the top
    □ I can identify maximum stack depth from inputs

**Tail Recursion**

.. code-block:: text

    □ I can place the recursive call in tail position when appropriate
    □ I understand Python lacks tail-call optimization (no depth savings)
    □ I can convert accumulator-style recursion to iteration

**Patterns & Problems**

.. code-block:: text

    □ I can implement factorial, fibonacci (with memo), and binary search
    □ I can write recursive list processing (map/filter-like)
    □ I can traverse trees (pre/in/post-order) conceptually

**Pitfalls & Performance**

.. code-block:: text

    □ I avoid missing/incorrect base cases
    □ I avoid non-progressing recursion (infinite recursion)
    □ I reason about time/space; I use memoization when needed
    □ I know when iteration is clearer/faster in Python

---

Part 7: Quick Reference Guide
------------------------------

.. index:: recursion reference, cheat sheet, patterns

**General Template**

.. code-block:: python

    def recurse(problem):
        if is_base(problem):        # 1) Base case
            return base_value
        smaller = shrink(problem)   # 2) Make progress
        partial = recurse(smaller)  # 3) Self-call
        return combine(problem, partial)  # 4) Combine result

**Tail-Recursive with Accumulator (concept)**

.. code-block:: python

    def recurse_tail(problem, acc):
        if is_base(problem):
            return acc
        smaller, acc2 = shrink_and_update(problem, acc)
        return recurse_tail(smaller, acc2)

**Common Patterns**

.. code-block:: python

    # Factorial
    def fact(n):
        if n in (0, 1): return 1
        return n * fact(n-1)

    # Fibonacci (memoized)
    def fib(n, memo=None):
        if memo is None: memo = {}
        if n in memo: return memo[n]
        if n < 2: memo[n] = n
        else: memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]

    # Binary search (inclusive bounds)
    def rbin(xs, t, lo=0, hi=None):
        if hi is None: hi = len(xs)-1
        if lo > hi: return -1
        mid = (lo+hi)//2
        if xs[mid]==t: return mid
        if xs[mid] < t: return rbin(xs, t, mid+1, hi)
        return rbin(xs, t, lo, mid-1)

**Tree Traversal (pseudocode only)**

.. code-block:: text

    preorder(node):
      if node is null: return
      visit(node)
      preorder(node.left)
      preorder(node.right)

    inorder(node):
      if node is null: return
      inorder(node.left)
      visit(node)
      inorder(node.right)

    postorder(node):
      if node is null: return
      postorder(node.left)
      postorder(node.right)
      visit(node)

**Pitfalls**

.. code-block:: text

    • Missing/incorrect base case ⇒ infinite recursion or wrong results
    • No progress toward base ⇒ infinite recursion
    • Shared mutable defaults (e.g., memo={}) ⇒ cross-call contamination
    • Python has no TCO ⇒ deep recursion may overflow
    • Prefer iteration when stack depth/overhead are concerns

End of Assessment
-----------------

**Well done!** Take a breath and reflect on what felt natural and what didn’t. Revisit the checklist to identify the next 1–2 skills to reinforce.
