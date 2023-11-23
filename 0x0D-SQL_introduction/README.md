# SQL Introduction Project

## Description

This project covers the fundamentals of SQL and MySQL, introducing key concepts such as databases, relational databases, SQL syntax, and basic operations like creating tables and querying data.

## Learning Objectives

At the end of this project, you should be able to:

- Explain the concepts of databases, relational databases, and SQL.
- Create and alter databases in MySQL.
- Understand and use DDL (Data Definition Language) and DML (Data Manipulation Language) statements.
- Perform operations such as SELECT, INSERT, UPDATE, and DELETE on tables.
- Work with subqueries and MySQL functions.

## Installation

To install MySQL 8.0 on Ubuntu 20.04 LTS, follow these steps:

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version

$ sudo mysql


-- Select the 3 first students in Batch ID=3
-- Because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
