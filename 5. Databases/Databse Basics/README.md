# Database Basics

Databases are organized collections of data that allow for efficient storage, retrieval, and manipulation of information. Here are the fundamental concepts:

## Core Concepts

1. **Database**: A structured set of data held in a computer
2. **DBMS (Database Management System)**: Software that interacts with databases (e.g., MySQL, PostgreSQL, Oracle)
3. **Table**: A collection of related data organized in rows and columns
4. **Record/Row**: A single entry in a table
5. **Field/Column**: A single piece of data about an item in a table

## Types of Databases

1. **Relational Databases (SQL)**:
   - Organize data into tables with relationships
   - Use SQL (Structured Query Language)
   - Examples: MySQL, PostgreSQL, SQL Server

2. **NoSQL Databases**:
   - Document stores (MongoDB)
   - Key-value stores (Redis)
   - Wide-column stores (Cassandra)
   - Graph databases (Neo4j)

## Basic SQL Commands

```sql
-- Create a table
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Insert data
INSERT INTO users (id, name, email) VALUES (1, 'John Doe', 'john@example.com');

-- Query data
SELECT * FROM users WHERE id = 1;

-- Update data
UPDATE users SET email = 'john.doe@example.com' WHERE id = 1;

-- Delete data
DELETE FROM users WHERE id = 1;
```

## Database Design Principles

1. **Normalization**: Organizing data to minimize redundancy
2. **Primary Keys**: Unique identifiers for records
3. **Foreign Keys**: Fields that link to primary keys in other tables
4. **Indexes**: Structures that improve data retrieval speed
