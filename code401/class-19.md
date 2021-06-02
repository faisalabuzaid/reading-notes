# Python Regular Expression

Regular Expressions, often shortened as regex, are a sequence of characters used to check whether a pattern exists in a given text (string) or not. If you've ever used search engines, search and replace tools of word processors and text editors - you've already seen regular expressions in use. They are used at the server side to validate the format of email addresses or passwords during registration, used for parsing text data files to find, replace, or delete certain string, etc. They help in manipulating textual data, which is often a prerequisite for data science projects involving text mining.

## Regular Expressions in Python

The re library in Python provides several functions that make it a skill worth mastering.

-  match() function returns a match object if the text matches the pattern. Otherwise, it returns None.
    - search() you scan through the given string/sequence, looking for the first location where the regular expression produces a match.
    - group() returns the string matched by the re. 
    - [abc] - Matches a or b or c.
    - [a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).
    - \ - Backslash:
      - 1 - If the character following the backslash is a recognized escape character, then the special meaning of the term is taken.
      - 2 - Else if the character following the \ is not a recognized escape character, then the \ is treated like any other character and passed through.
      - 3 -  can be used in front of all the metacharacters to remove their special meaning.
   - \w - Lowercase 'w'. Matches any single letter, digit, or underscore.
   - \W - Uppercase 'W'. Matches any character not part of \w (lowercase w).
   - \s - Lowercase 's'. Matches a single whitespace character like: space, newline, tab, return.
   - \S - Uppercase 'S'. Matches any character not part of \s (lowercase s).
   - \d - Lowercase d. Matches decimal digit 0-9.
   - \D - Uppercase d. Matches any character that is not a decimal digit.
   - + symbol used after the \d in the example above is used for repetition. 
   - \t - Lowercase t. Matches tab.
   - \n - Lowercase n. Matches newline.
   - \r - Lowercase r. Matches return.
   - \A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.
   - \Z - Uppercase z. Matches only at the end of the string.
   - \b - Lowercase b. Matches only the beginning or end of the word.
   - * Checks if the preceding character appears zero or more times starting from that position.
   - ? Checks if the preceding character appears exactly zero or one time starting from that position.
   - {x} Repeat exactly x number of times.
   - {x,} Repeat at least x times or more.
   - {x, y} Repeat at least x times but no more than y times.
   -  ... represent the rest of the matching syntax. 
   - <.*> matched the whole string, right up to the second occurrence of >.

   ##  shutil — High-level File Operations:
  - The shutil module includes high-level file operations such as copying and archiving.
  - Copying Files
    - copyfile() copies the contents of the source to the destination and raises IOError if it does not have permission to write to the destination file.
  - Copying File Metadata
    - To copy the permissions from one file to another, use copymode().
  - Working With Directory Trees: shutil includes three functions for working with directory trees.
    - To copy a directory from one place to another, use copytree().
    - copytree() accepts two callable arguments to control its behavior.
    - ignore_patterns() is used to create an ignore function to skip copying Python source files.
  - Finding Files
    - The which() function scans a search path looking for a named file.
  - Archives
    -  get_archive_formats() returns a sequence of names and descriptions for formats supported on the current system.
  - File System Space
    - disk_usage() returns a tuple with the total space, the amount currently being used, and the amount remaining free.