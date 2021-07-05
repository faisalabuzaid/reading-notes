# Pythonisms

## Dunder Methods

What Are Dunder Methods?
In Python, special methods are a set of predefined methods you can use to enrich your classes. They are easy to recognize because they start and end with double underscores, for example __init__ or __str__.

As it quickly became tiresome to say under-under-method-under-under Pythonistas adopted the term “dunder methods”, a short form of “double under.”

## Iterators

How does the loop fetch individual elements from the object it is looping over? And how can you support the same programming style in your own Python objects?

- Iterators provide a sequence interface to Python objects that’s memory efficient and considered Pythonic. Behold the beauty of the for-in loop!
- To support iteration an object needs to implement the iterator protocol by providing the `__iter__` and `__next__` dunder methods.
- Class-based iterators are only one way to write iterable objects in Python. Also consider generators and generator expressions.

## Generators

What Are Python Generators?
 
 
Generators are a tricky subject in Python.you’ll make the leap from class-based iterators to using generator functions and the “yield” statement in no time.

- Generator functions are syntactic sugar for writing objects that support the iterator protocol. Generators abstract away much of the boilerplate code needed when writing class-based iterators.
- The yield statement allows you to temporarily suspend execution of a generator function and to pass back values from it.
- Generators start raising StopIteration exceptions after control flow leaves the generator function by any means other than a yield statement.