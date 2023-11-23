# 0x07. Python - Test-driven development

## Background Context

**Important notice on intranet checks for Python projects:**

Starting from today:

- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything.
- The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD (Test-driven development) and think about all possible cases.
- We strongly encourage you to work together on test cases so that you don’t miss any edge case. But not in the implementation of them!
- Don’t trust the user, always think about all possible edge cases.

## Resources

Read or watch:

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until “26.2.3.7. Warnings” included)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)
- [Unittest module](https://docs.python.org/3/library/doctest.html)
- [Interactive and Non-interactive tests](https://docs.python.org/3/library/doctest.html)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General:**
- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

**Python Scripts:**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

**Python Test Cases:**
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- We strongly encourage you to work together on test cases so that you don’t miss any edge case – The Checker is checking for tests!
