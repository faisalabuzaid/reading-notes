# Class 02

# Unit tests and TDD (TEST-DRIVEN-DEVELOPMENT)

Unit tests are some pieces of code to exercise the input, the output and the behaviour of your code. You can write them anytime you want.
But Test-Driven Development is a strategy to think (and write!) tests first.

The API is pretty straightforward and your work was almost done. But with TDD we need to think about tests first. 

- unit tests are pieces of code to exercise input, output, and behavior of code

      - test-driven development is a way to write tests first

      - this makes it more dynamic for code to run.

- when creating tests we should separate them from module

- Other thing to care about is the structure. A convention widely used is the AAA : _Arrange_, _Act_ and _Assert_.

     - Arrange: you need to organize the data needed to execute that piece of code (input).

     - Act: here you will execute the code being tested (exercise the behaviour). 

     - Assert: after executing the code, you will check if the result (output) is the same as you were expecting.


# The Cycle

## The cycle is made by three steps:

    🆘 Write a unit test and make it fail (it needs to fail because the feature isn’t there, right? If this test passes, call the Ghostbusters, really)

    ✅ Write the feature and make the test pass! (you can dance after that)

    🔵 Refactor the code — the first version doesn’t need to be the beautiful one (don’t be shy)
    

![image](https://www.xenonstack.com/images/blog/Test-Driven-Development-Python.png)

# Recursion
The process in which a function calls itself and the corresponding function is called as recursive function
approach 1 - simply adding by one by one

     f(n) = 1 + 2 + 3..... + n
     approach 2 - Recursive adding

     f(n) = 1     n = 1
     f(n) = n + f(n-1) n>1

# Python Lists
## List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in _Python_ used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

## Python Collections (Arrays)
There are four collection data types in the Python programming language:

   - List : is a collection which is ordered and changeable. Allows duplicate members.

   - Tuple : is a collection which is ordered and unchangeable. Allows duplicate members.

   - Set : is a collection which is unordered and unindexed. No duplicate members.

   - Dictionary : is a collection which is ordered* and changeable. No duplicate members.


# Python Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

- Assigning a string to a variable is done with the variable name followed by an equal sign and the string

- You can assign a multiline string to a variable by using three quotes


## Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.


