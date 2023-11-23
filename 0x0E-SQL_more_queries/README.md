# SQL - More Queries

## Description

This project dives deeper into SQL, covering topics such as user management, privileges, constraints, subqueries, joins, and unions. The objective is to enhance your understanding of MySQL and database management.

## Learning Objectives

By the end of this project, you should be able to:

- Create and manage MySQL users.
- Grant privileges to users for databases or tables.
- Understand and use PRIMARY KEY and FOREIGN KEY constraints.
- Utilize NOT NULL and UNIQUE constraints.
- Retrieve data from multiple tables in a single query.
- Work with subqueries, JOIN, and UNION operations.

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

## Importing a SQL Dump
To import a SQL dump, use the following commands:

$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows

