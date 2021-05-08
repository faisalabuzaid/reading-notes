# Classes and Objects
 - Almost everything in Python is an object, with its properties and methods.

 An object consists of : 

   1. State: It is represented by the attributes of an object. It also reflects the properties of an object.

   2. Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.

   3. Identity: It gives a unique name to an object and enables one object to interact with other objects.


 A Class is like an object constructor, or a "blueprint" for creating objects.

classes are basically a template to create objects.

 
 
 Some points on Python class:  

 - Classes are created by keyword class.

 - Attributes are the variables that belong to a class.

 - Attributes are always public and can be accessed using the dot (.) operator.

         Eg : Myclass.Myattribute


# Thinking Recursively

- Problems (in life and also in computer science) can often seem big and scary. But if we keep chipping away at them, more often than not we can break them down into smaller chunks trivial enough to solve. This is the essence of thinking recursively, and my aim in this article is to provide you, my dear reader, with the conceptual tools necessary to approach problems from this recursive point of view.

- Now that we have some intuition about recursion, let’s introduce the formal definition of a recursive function. A recursive function is a function defined in terms of itself via self-referential expressions.

- Recursive data structures and recursive functions go together like bread and butter. The recursive function’s structure can often be modeled after the definition of the recursive data structure it takes as an input. Let me demonstrate this by calculating the sum of all the elements of a list recursively:

# Pytest Fixtures and Coverage

- When writing a lot of tests, you may want some information common across all of them.
 
- This shared test information can be shared via Fixtures.

- Fixtures are identified by decorators

- the decorator should likely be given an argument of (scope='module') in order to have it apply to the whole file

- Coverage is a measure of how well the test suite covers the code

- coverage can be summarized in a human readable report

- it will highlight the areas that were not tested

- report is viewed with coverage html

- as things are tested, the percentage number goes up.
It is test progress, not coverage.

- the "." are tests passed successfully, "F" are tests failed, and "s" are tests skipped

