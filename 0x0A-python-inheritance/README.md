# 0x0A. Python - Inheritance

## Overview

This project delves into the concept of inheritance in Python, exploring the relationship between superclass and subclass, understanding how inheritance allows the creation of classes based on existing ones, and utilizing various built-in functions related to inheritance.

## Learning Objectives

By completing this project, you should be able to:

- Explain the awesomeness of Python programming.
- Define terms such as superclass, base class, or parent class.
- Identify a subclass and understand its relationship with a superclass.
- List all attributes and methods of a class or instance.
- Know when an instance can have new attributes.
- Inherit a class from another.
- Define a class with multiple base classes.
- Understand the default class that every class inherits from.
- Override a method or attribute inherited from the base class.
- Access attributes or methods available by heritage to subclasses.
- Comprehend the purpose of inheritance.
- Use isinstance, issubclass, type, and super built-in functions appropriately.

## Resources

- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://www.geeksforgeeks.org/multiple-inheritance-in-python/)
- [Inheritance in Python](https://realpython.com/inheritance-composition-python/)
- [Learn to Program 10: Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

## Requirements

### Python Scripts

- **Allowed editors:** vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files should end with a newline character
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- The length of your files will be tested using wc

### Python Test Cases

- **Allowed editors:** vi, vim, emacs
- All files should end with a newline character
- All test files should be inside a folder `tests`
- All test files should be text files (extension: .txt)
- All tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All modules, classes, and functions should have proper documentation

**Note:** Avoid using the words `import` or `from` inside your comments.

## Tasks

1. **Task 0:** Create a class `BaseGeometry`.
2. **Task 1:** Create a class `Rectangle` that inherits from `BaseGeometry`.
3. **Task 2:** Add validation for the `width` and `height` of the `Rectangle` class.
4. **Task 3:** Create a class `Square` that inherits from `Rectangle`.
5. **Task 4:** Overwrite the `__str__` method in the `BaseGeometry` class.

**Note:** Work together on test cases to cover various scenarios and edge cases.

## Documentation

Ensure that all modules, classes, and functions have proper documentation. A documentation is not a simple word; it should be a real sentence explaining the purpose of the module, class, or method. The length of it will be verified.

```python
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
