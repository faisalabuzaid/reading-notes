# Class 03
# FileIO and Exceptions
## Reading and Writing Files in Python

## What Is a File?
a file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable.These byte files are then translated into binary 1 and 0 for easier processing by the computer.

Files on most modern file systems are composed of three main parts:

 - Header : metadata about the contents of the file (file name, size, type, and so on).

 - Data : contents of the file as written by the creator or editor.

 - End of file (EOF) : special character that indicates the end of the file.


## File Paths
When you access a file on an operating system, a file path is required. The file path is a string that represents the location of a file. It’s broken up into three major parts:

  - Folder Path: the file folder location on the file system where subsequent folders are separated by a forward slash / (Unix) or backslash \ (Windows)

 - File Name: the actual name of the file

 - Extension: the end of the file path pre-pended with a period (.) used to indicate the file type. 

## Character Encodings
Another common problem that you may face is the encoding of the byte data. An encoding is a translation from byte data to human readable characters. This is typically done by assigning a numerical value to represent a character. The two most common encodings are the ASCII and UNICODE Formats. ASCII can only store 128 characters, while Unicode can contain up to 1,114,112 characters.

ASCII is actually a subset of Unicode (UTF-8), meaning that ASCII and Unicode share the same numerical to character values. It’s important to note that parsing a file with the incorrect character encoding can lead to failures or misrepresentation of the character

# Python Exceptions
A python program ends as soon as there is an error. The error can be syntax related or an exception - a syntax error occurs when the parser detects an incorrect statement - an arrow will indicate where the syntax error lies - an exception error occurs when syntactically Python Code results in an error - there are many built-in exception in Python and it will list the type

 - you can use raise to throw an exception if a condition occurs

        x = 5
        if x > 5:
        raise Exception('x should not exceed 5...')

 - instead of waiting for a program to crash in the middle of its coursek, you can make an assertion in Python

    - we assert that if a condition is true, then the program will continue, if it is false you can let the program throw an AssertionError exception.

 - the try and Except block is used to catch and handle exceptions

    - try: run this code....

    - except: execute this code when there is an exception

    - else: no exceptions? Run this code

    - finally: always run this code



- raise allows you to throw an exception at any time.

- assert enables you to verify if a certain condition is met and throw an exception if it isn’t.

- In the try clause, all statements are executed until an exception is encountered.

- except is used to catch and handle the exception(s) that are encountered in the try clause.

- else lets you code sections that should run only when no exceptions are encountered in the try clause.

- finally enables you to execute sections of code that should always run, with or without any previously encountered exceptions.