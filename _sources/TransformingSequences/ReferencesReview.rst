..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. qnum::
   :prefix: seqmut-3-
   :start: 1

.. index:: aliases

Review of References
----------------------

If we execute these assignment statements,

.. sourcecode:: python

    a = "banana"
    b = "banana"

we know that ``a`` and ``b`` will refer to a string with the letters
``"banana"``. But we don't know yet whether they point to the *same* string.

There are two possible ways the Python interpreter could arrange its internal states:

.. image:: Figures/refdiag1.png
   :alt: List illustration

or

.. image:: Figures/refdiag2.png
   :alt: List illustration

In one case, ``a`` and ``b`` refer to two different string objects that have the same
value. In the second case, they refer to the same object. Remember that an object is something a variable can
refer to.

We can test whether two names refer to the same object using the *is*
operator.  The *is* operator will return true if the two references are to the same object.  In other words, the references are the same.  Try our example from above.

.. activecode:: ac8_3_1

    a = "banana"
    b = "banana"

    print(a is b)

The answer is ``True``. This tells us that both ``a`` and ``b`` refer to the same object, and that it is the second
of the two reference diagrams that describes the relationship. Python assigns every object a unique id and when we
ask ``a is b`` what python is really doing is checking to see if id(a) == id(b).

.. activecode:: ac8_3_2

    a = "banana"
    b = "banana"

    print(id(a))
    print(id(b))

Since strings are *immutable*, the Python interpreter often optimizes resources by making two names that refer to the same string value
refer to the same object. You shouldn't count on this (that is, use ``==`` to compare strings, not ``is``), but don't be surprised if you find that two variables,each bound to the string "banana", have the same id..

This is not the case with lists, which never share an id just because they have the same contents. Consider the following example. Here, ``a`` and ``b`` refer to two different lists,
each of which happens to have the same element values. They need to have different ids so that mutations of list ``a`` do not affect list ``b``.

.. activecode:: ac8_3_3

    a = [81,82,83]
    b = [81,82,83]

    print(a is b)

    print(a == b)

    print(id(a))
    print(id(b))

The reference diagram for this example looks like this:

.. image:: Figures/refdiag3.png
   :alt: Reference diagram for equal different lists

``a`` and ``b`` have equivalent values but do not refer to the same object. Because their contents are equivalent, `a==b` evaluates to True; because they are not the same object, `a is b` evaluates to False.


Aliasing
--------

Since variables refer to objects, if we assign one variable to another, both
variables refer to the same object:

.. activecode:: ac8_4_1

    a = [81, 82, 83]
    b = a
    print(a is b)

In this case, the reference diagram looks like this:

.. image:: Figures/refdiag4.png
   :alt: State snapshot for multiple references (aliases) to a list

Because the same list has two different names, ``a`` and ``b``, we say that it
is **aliased**. Changes made with one alias affect the other.  In the codelens example below, you can see that ``a`` and ``b`` refer
to the same list after executing the assignment statement ``b = a``.


.. activecode:: ac8_4_2

    a = [81,82,83]
    b = [81,82,83]
    print(a is b)

    b = a
    print(a == b)
    print(a is b)

    b[0] = 5
    print(a)



Although this behavior can be useful, it is sometimes unexpected or
undesirable. In general, it is safer to avoid aliasing when you are working
with mutable objects. Of course, for immutable objects, there's no problem.
That's why Python is free to alias strings and integers when it sees an opportunity to
economize.

**Check your understanding**


.. mchoice:: question8_1_3
   :answer_a: ['Jamboree', 'get-together', 'party']
   :answer_b: ['celebration']
   :answer_c: ['celebration', 'Jamboree', 'get-together', 'party']
   :answer_d: ['Jamboree', 'get-together', 'party', 'celebration']
   :correct: a
   :feedback_a: Yes, the value of y has been reassigned to the value of w.
   :feedback_b: No, that was the inital value of y, but y has changed.
   :feedback_c: No, when we assign a list to another list it does not concatenate the lists together.
   :feedback_d: No, when we assign a list to another list it does not concatenate the lists together.
   :practice: T

   What is the value of y after the following code has been evaluated:

   .. code-block:: python

      w = ['Jamboree', 'get-together', 'party']
      y = ['celebration']
      y = w



.. mchoice:: question8_4_1
   :answer_a: [4,2,8,6,5]
   :answer_b: [4,2,8,999,5]
   :correct: b
   :feedback_a: blist is not a copy of alist, it is a reference to the list alist refers to.
   :feedback_b: Yes, since alist and blist both reference the same list, changes to one also change the other.
   :practice: T

   What is printed by the following statements?

   .. code-block:: python

     alist = [4,2,8,6,5]
     blist = alist
     blist[3] = 999
     print(alist)

Cloning Lists
-------------

If we want to modify a list and also keep a copy of the original, we need to be
able to make a copy of the list itself, not just the reference. This process is
sometimes called **cloning**, to avoid the ambiguity of the word copy.

The easiest way to clone a list is to use the slice operator.

Taking any slice of ``a`` creates a new list. In this case the slice happens to
consist of the whole list.

.. activecode:: clens8_5_1

    a = [81,82,83]

    b = a[:]       # make a clone using slice
    print(a == b)
    print(a is b)

    b[0] = 5

    print(a)
    print(b)

Now we are free to make changes to ``b`` without worrying about ``a``.  Again, we can clearly see in
codelens that ``a`` and ``b`` are entirely different list objects.

**Check your understanding**

.. mchoice:: question8_5_1
   :answer_a: [4,2,8,999,5,4,2,8,6,5]
   :answer_b: [4,2,8,999,5]
   :answer_c: [4,2,8,6,5]
   :correct: c
   :feedback_a: print alist not print blist
   :feedback_b: blist is changed, not alist.
   :feedback_c: Yes, alist was unchanged by the assignment statement. blist was a copy of the references in alist.
   :practice: T

   What is printed by the following statements?

   .. code-block:: python

     alist = [4,2,8,6,5]
     blist = alist * 2
     blist[3] = 999
     print(alist)
