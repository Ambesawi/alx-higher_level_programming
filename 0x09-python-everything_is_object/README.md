# 0x09. Python - Everything is object

## Overview 
This project explores Python's object-specific behaviors, addressing questions related to object mutability, aliasing, and immutability. The tasks aim to deepen your understanding of Python's object-oriented principles.

## Learning Objectives
Upon completion, you should be able to:

Explain why Python programming is considered awesome.
Differentiate between a class and an object or instance.
Distinguish between immutable and mutable objects.
Understand the concepts of reference, assignment, and aliasing.
Identify identical variables and variables linked to the same object.
Display variable identifiers (memory addresses) in Python.
Recognize mutable and immutable types.
Grasp how Python passes variables to functions.

## Resources
Objects and Values
Aliasing
Immutable vs Mutable Types
Mutation (Only this chapter)
Cloning lists
Python tuples: immutable but potentially changing


## Tasks
Task 0: Answer the questions about Python's object-specific behaviors.
Task 1: Answer the questions about Python's object-specific behaviors.
Task 2: Answer the questions about Python's object-specific behaviors.
Task 3: Answer the questions about Python's object-specific behaviors.
Task 4: Answer the questions about Python's object-specific behaviors.
Task 5: Answer the questions about Python's object-specific behaviors.

## Background Context

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```python
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
>>> 

>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
>>> 
