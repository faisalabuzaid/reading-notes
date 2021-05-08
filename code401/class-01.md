# Big O notation
- Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. 

- _In computer science_, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows (it is useful in the analysis of algorithms).


Here is a list of classes of functions that are commonly encountered when analyzing the running time of an algorithm:

   - O(1) : it describes an algorithm that will always execute in the same time (or space) regardless of the size of the input data set.

   - O(N) : it describes an algorithm whose performance will grow linearly and in direct proportion to the size of the input data set.

   - O(N2) : it represents an algorithm whose performance is directly proportional to the square of the size of the input data set.

   - O(2^N) : it denotes an algorithm whose growth doubles with each addition to the input data set. 
   
   The growth curve of an O(2N) function is exponential - starting off very shallow, then rising meteorically.

----------
# Python Names and Values
- As in many programming languages, a Python assignment statement associates a symbolic name on the left-hand side with a value on the right-hand side. In Python, we say that names refer to values, or a name is a reference to a value:

     x = 23

- There’s no rule that says a value can only have one name. An assignment statement can make a second (or third, ...) name refer to the same value.

      x = 23
      y = x
Now x and y both refer to the same value

- Python keeps track of how many references each value has, and automatically cleans up values that have none. This is called “garbage collection,” and means that you don’t have to get rid of values, they go away by themselves when they are no longer needed.

- An important fact about assignment: assignment never copies data.
When values have more than one name, it’s easy to get confused and think of it as two names and two values:

      x = 23
      y = x
      # "Now I have two values: x and y!"
      # NO: you have two names, but only one value.

Assigning a value to a name never copies the data, it never makes a new value.

-----

# Python 3 Module of the Week
 ## Text
The str class is the most obvious text processing tool available to Python programmers, but there are plenty of other tools in the standard library to make advanced text manipulation simple.

Programs may use string.Template as a simple way to parameterize strings beyond the features of str objects. While not as feature-rich as templates defined by many of the web frameworks or extension modules available from the Python Package Index, string.Template is a good middle ground for user-modifiable templates in which dynamic values need to be inserted into otherwise static text.

  - string — Text Constants and Templates

        Purpose : Contains constants and classes for working with text.

  - textWrap — Formatting Text Paragraphs

        Purpose : Formatting text by adjusting where line breaks occur in a paragraph.

  - re — Regular Expressions

        Purpose : Searching within and changing text using formal patterns.

  - difflib — Compare Sequences

        Purpose : Compare sequences, especially lines of text.

# Data Structures

Python includes several standard programming data structures, such as list, tuple, dict, and set, as part of its built-in types. Many applications do not require other structures, but when they do, the standard library provides powerful and well-tested versions that are ready to be used.

# Algorithms

Python includes several modules for implementing algorithms elegantly and concisely using whatever style is most appropriate for the task. It supports purely procedural, object oriented, and functional styles and all three styles are frequently mixed within different parts of the same program.

# Dates and Times

Python does not include native types for dates and times as it does for int, float, and str, but there are three modules for manipulating date and time values in several representations.