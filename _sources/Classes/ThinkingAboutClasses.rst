..  Copyright (C)  Paul Resnick, Jaclyn Cohen.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. _thinking_about_classes:

Thinking About Classes and Instances
------------------------------------

You can now imagine some reasons you may want to define a class. You have seen examples of creating types that are more complicated or specific than the ones built in to Python (like lists or strings). ``Turtle``, with all the instance variables and methods you learned about using earlier in the semester, is a class that programmers defined which is now included in the Python language. In this chapter, we defined ``Point`` with some functionality that can make it easier to write programs that involve ``x,y`` coordinate ``Point`` instances. And shortly, you'll see how you can define classes to represent objects in a game.

You can also use self-defined classes to hold data -- for example, data you get from making a request to a REST API.

Before you decide to define a new class, there are a few things to keep in mind, and questions you should ask yourself:

* **What is the data that you want to deal with?** (Data about a bunch of songs from iTunes? Data about a bunch of tweets from Twitter? Data about a bunch of hashtag searches on Twitter? Two numbers that represent coordinates of a point on a 2-dimensional plane?)

* **What will one instance of your class represent?** In other words, which sort of new *thing* in your program should have fancy functionality? One song? One hashtag? One tweet? One point? The answer to this question should help you decide what to call the class you define.

* **What information should each instance have as instance variables?** This is related to what an instance represents. See if you can make it into a sentence. *"Each instance represents one < song > and each < song > has an < artist > and a < title > as instance variables."* Or, *"Each instance represents a < Tweet > and each < Tweet > has a < user (who posted it) > and < a message content string > as instance variables."*

* **What instance methods should each instance have?** What should each instance be able to *do*? To continue using the same examples: Maybe each song has a method that uses a lyrics API to get a long string of its lyrics. Maybe each song has a method that returns a string of its artist's name. Or for a tweet, maybe each tweet has a method that returns the length of the tweet's message. (Go wild!)

* **What should the printed version of an instance look like?** (This question will help you determine how to write the ``__str__`` method.) Maybe, "Each song printed out will show the song title and the artist's name." or "Each Tweet printed out will show the username of the person who posted it and the message content of the tweet."

After considering those questions and making decisions about how you're going to get started with a class definition, you can begin to define your class.

Remember that a class definition, like a function definition, is a general description of what *every instance of the class should have*. (Every Point has an ``x`` and a ``y``.) The class instances are specific: e.g. the Point with *a specific x and y >.* You might have a Point with an ``x`` value of 3 and a ``y`` value of 2, so for that particular *instance* of the *class* ``Point``, you'd pass in ``3`` and ``2`` to the constructor, the ``__init__`` method, like so: ``new_point = Point(3,2)``, as you saw in the last sections.

**Worked Example: Designing a Book Class**

Let's apply these questions to design a Book class:

**1. What data?** Information about books (titles, authors, pages, ISBN)

**2. What does one instance represent?** One book

**3. What instance variables?** Each book has:
   - ``title`` (string)
   - ``author`` (string)
   - ``pages`` (int)
   - ``isbn`` (string)

**4. What instance methods?** Each book should be able to:
   - ``is_long()`` - returns True if over 500 pages
   - ``same_author(other_book)`` - compares authors
   - ``__lt__(other)`` - sort by title alphabetically

**5. What should __str__ look like?**
   - "'1984' by George Orwell (328 pages)"

**Implementation:**

.. activecode:: thinking_about_classes_example

    class Book:
        """Represents a book."""

        def __init__(self, title, author, pages, isbn):
            self.title = title
            self.author = author
            self.pages = pages
            self.isbn = isbn

        def is_long(self):
            """Returns True if book is over 500 pages."""
            return self.pages > 500

        def same_author(self, other_book):
            """Check if this book has same author as another."""
            return self.author == other_book.author

        def __lt__(self, other):
            """Sort alphabetically by title."""
            return self.title < other.title

        def __str__(self):
            return f"'{self.title}' by {self.author} ({self.pages} pages)"

    # Create instances
    book1 = Book("1984", "George Orwell", 328, "978-0451524935")
    book2 = Book("Animal Farm", "George Orwell", 112, "978-0451526342")
    book3 = Book("The Hobbit", "J.R.R. Tolkien", 310, "978-0547928227")

    # Use the methods
    print(book1)
    print(f"Is '1984' long? {book1.is_long()}")
    print(f"Same author as Animal Farm? {book1.same_author(book2)}")
    print(f"Same author as The Hobbit? {book1.same_author(book3)}")

    # Sort by title
    books = [book1, book2, book3]
    for book in sorted(books):
        print(f"  {book.title}")

**Output:**
::

   '1984' by George Orwell (328 pages)
   Is '1984' long? False
   Same author as Animal Farm? True
   Same author as The Hobbit? False
     1984
     Animal Farm
     The Hobbit

**When NOT to Create a Class**

❌ **Don't create a class when a simpler type works:**

.. code-block:: python

   # BAD: Overcomplicated
   class Temperature:
       def __init__(self, value):
           self.value = value

   temp = Temperature(25)
   print(temp.value)  # Just use: temp = 25

   # GOOD: Use built-in type
   temp = 25
   print(temp)

❌ **Don't create a class for a single use case:**

If you only need one instance ever, consider a dictionary or module-level variables instead.

✅ **DO create a class when:**
- You need multiple instances with different data
- Instances need behavior (methods)
- You need encapsulation or validation
- The concept has clear identity (Person, Book, Car)

**Design Challenge**

For each scenario, decide: Should you create a class? If yes, answer the 5 design questions.

**Scenario 1:** You're building a game with multiple enemies. Each enemy has health, attack power, and position.

**Scenario 2:** You need to store the user's username (just once).

**Scenario 3:** You're analyzing tweets. Each tweet has text, author, likes, retweets, and timestamp.

.. reveal:: design_challenge_solution
   :showtitle: Show Suggested Answers
   :hidetitle: Hide Answers

   **Scenario 1: YES - Create Enemy class**
   - Multiple instances (many enemies)
   - Each has unique state
   - Needs methods (attack, take_damage, move)

   **Scenario 2: NO - Just use a variable**
   - Only one instance needed
   - No behavior required
   - Simple: ``username = "Alice"``

   **Scenario 3: YES - Create Tweet class**
   - Multiple instances (many tweets)
   - Each has unique data
   - Needs methods (get_engagement, is_popular)