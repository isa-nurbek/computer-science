# Introduction to SQL

## 🔷 What is SQL?

SQL (Structured Query Language) is the **standard language for managing and manipulating relational databases**. It allows you to **store, retrieve, modify, delete, and manage data** stored in databases like MySQL, PostgreSQL, SQL Server, SQLite, and Oracle.

---

## 🔷 How SQL Works

Relational databases store data in **tables** (like spreadsheets) with **rows and columns**.

When you write SQL statements, the **database engine** interprets and executes them. SQL statements can:

- **Query data** (read)
- **Insert data** (write)
- **Update or delete data**
- **Define or modify database structure** (schema)
- **Control access and permissions**

---

## 🔷 Types of SQL Commands

SQL commands are categorized into **five types**:

| Category                               | Purpose                              |
|----------------------------------------|--------------------------------------|
| **DDL** (Data Definition Language)     | Define and modify database structure |
| **DML** (Data Manipulation Language)   | Manage data within schema objects    |
| **DQL** (Data Query Language)          | Query data from tables               |
| **DCL** (Data Control Language)        | Control access to data               |
| **TCL** (Transaction Control Language) | Manage transactions                  |

---

## 🔹 1. DDL (Data Definition Language)

Used to define or modify database schema.

### Commands

- `CREATE`
- `ALTER`
- `DROP`
- `TRUNCATE`

### 🔸 Example: Creating a Table

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50),
    salary DECIMAL(10, 2)
);
```

**Explanation:**

- Creates a table `employees` with 4 columns: id, name, position, salary.
- `INT`, `VARCHAR`, and `DECIMAL` are data types.
- `PRIMARY KEY` ensures unique, non-null `id`.

---

## 🔹 2. DML (Data Manipulation Language)

Used to manipulate data stored in tables.

### Commands

- `INSERT`
- `UPDATE`
- `DELETE`

### 🔸 Example: Inserting a Row

```sql
INSERT INTO employees (id, name, position, salary)
VALUES (1, 'Alice Johnson', 'Developer', 75000.00);
```

**Explanation:**

- Inserts one employee record into `employees`.

### 🔸 Example: Updating a Record

```sql
UPDATE employees
SET salary = 80000.00
WHERE id = 1;
```

**Explanation:**

- Updates salary of the employee with id = 1.

### 🔸 Example: Deleting a Record

```sql
DELETE FROM employees
WHERE id = 1;
```

**Explanation:**

- Deletes the employee with id = 1 from the table.

---

## 🔹 3. DQL (Data Query Language)

Used to query data from the database.

### Command

- `SELECT`

### 🔸 Example: Selecting Data

```sql
SELECT name, position
FROM employees
WHERE salary > 70000;
```

**Explanation:**

- Returns names and positions of employees with salary greater than 70,000.

---

## 🔹 4. DCL (Data Control Language)

Used to control access to data in the database.

### Commands

- `GRANT`
- `REVOKE`

### 🔸 Example: Granting Permissions

```sql
GRANT SELECT, INSERT ON employees TO user123;
```

**Explanation:**

- Grants `user123` permission to `SELECT` and `INSERT` data into `employees`.

---

## 🔹 5. TCL (Transaction Control Language)

Used to manage changes made by DML statements.

### Commands

- `COMMIT`
- `ROLLBACK`
- `SAVEPOINT`

### 🔸 Example: Using a Transaction

```sql
BEGIN;
INSERT INTO employees (id, name, position, salary)
VALUES (2, 'Bob Smith', 'Manager', 95000.00);

UPDATE employees
SET salary = 100000.00
WHERE id = 2;

COMMIT;
```

**Explanation:**

- Starts a transaction.
- Performs insert and update.
- `COMMIT` saves the changes.

If something goes wrong:

```sql
ROLLBACK;
```

Reverts changes made since the last `BEGIN`.

---

## 🔷 Real-World Example: Full Flow

### 1. Create a table

```sql
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(50),
    price DECIMAL(6, 2)
);
```

### 2. Insert data

```sql
INSERT INTO books VALUES (1, 'Clean Code', 'Robert C. Martin', 39.99);
INSERT INTO books VALUES (2, 'The Pragmatic Programmer', 'Andrew Hunt', 42.00);
```

### 3. Query data

```sql
SELECT * FROM books;
```

### 4. Update data

```sql
UPDATE books
SET price = 45.00
WHERE book_id = 2;
```

### 5. Delete data

```sql
DELETE FROM books
WHERE book_id = 1;
```

---

## 🔷 Summary Table

| Type | Command                               | Description                 |
|------|---------------------------------------|-----------------------------|
| DDL  | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Schema creation and changes |
| DML  | `INSERT`, `UPDATE`, `DELETE`          | Change data                 |
| DQL  | `SELECT`                              | Query data                  |
| DCL  | `GRANT`, `REVOKE`                     | Permission control          |
| TCL  | `COMMIT`, `ROLLBACK`, `SAVEPOINT`     | Transactions                |

---

Let's break down the advanced SQL topics in-depth, starting with **Subqueries**, then move on to **Joins**, **Indexing**, and **Performance Tuning** — all with explanations and examples.

## 🔷 1. **Subqueries** (Nested Queries)

A **subquery** is a query **inside another query**. Used for filtering, comparison, or transformation.

### 📌 Types of Subqueries

- **Scalar subquery** (returns one value)
- **Row subquery** (returns a row)
- **Table subquery** (returns multiple rows and columns)
- **Correlated subquery** (references outer query)

### 🔸 Example: Scalar Subquery

```sql
SELECT name
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);
```

**Explanation:**

- Inner query returns the highest salary.
- Outer query finds the employee(s) earning that.

---

### 🔸 Example: Correlated Subquery

```sql
SELECT e1.name
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e1.position = e2.position
);
```

**Explanation:**

- For each employee, it compares their salary to the **average salary in the same position**.

---

## 🔷 2. **Joins**

Joins combine rows from **two or more tables** based on related columns.

### 📌 Types of Joins

| Join Type    | Description                            |
|--------------|----------------------------------------|
| `INNER JOIN` | Returns only matching rows             |
| `LEFT JOIN`  | All rows from left, matched from right |
| `RIGHT JOIN` | All rows from right, matched from left |
| `FULL JOIN`  | All rows, matched or not               |
| `CROSS JOIN` | Cartesian product (all combinations)   |
| `SELF JOIN`  | Join a table with itself               |

---

### 🔸 Example: INNER JOIN

```sql
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
```

**Explanation:**

- Joins employees to departments where `department_id` matches.
- Returns only matched records.

---

### 🔸 Example: LEFT JOIN

```sql
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```

**Explanation:**

- Shows all employees even if they don’t belong to any department.
- `NULL` for departments where there's no match.

---

## 🔷 3. **Indexing**

Indexes speed up **search and retrieval** in large tables. Think of it like a book’s index.

### 📌 Types of Indexes

- **Single-column Index**
- **Composite Index** (multiple columns)
- **Unique Index** (prevents duplicate values)
- **Full-text Index** (for text search)
- **Clustered Index** (physically sorts table — only one per table)

---

### 🔸 Example: Creating an Index

```sql
CREATE INDEX idx_salary ON employees(salary);
```

**Explanation:**

- Speeds up queries that filter or sort by `salary`.

---

### 🔸 Index Use Case

```sql
SELECT * FROM employees
WHERE salary > 80000;
```

With `idx_salary`, this is **much faster** than scanning the entire table.

> ⚠️ Over-indexing slows down inserts/updates. Use wisely.

---

## 🔷 4. **Performance Tuning**

Optimizing queries and database design for speed and efficiency.

### 📌 Key Techniques

| Technique              | Description                                    |
|------------------------|------------------------------------------------|
| **Indexes**            | Speeds up SELECT queries                       |
| **Query Optimization** | Avoid `SELECT *`, use proper joins and filters |
| **Normalization**      | Reduce redundancy and improve integrity        |
| **Caching**            | Reduce repeated queries                        |
| **Partitioning**       | Split large tables                             |
| **EXPLAIN / ANALYZE**  | Analyze query execution plan                   |

---

### 🔸 Example: Use `EXPLAIN`

```sql
EXPLAIN SELECT * FROM employees WHERE salary > 80000;
```

**Output:**

- Shows whether it uses index or full table scan
- Helps detect bottlenecks

---

### 🔸 Optimization Tips

- Replace `SELECT *` with specific columns
- Use `LIMIT` with pagination
- Avoid unnecessary subqueries
- Use indexed columns in `WHERE`, `ORDER BY`, and `JOIN`

---

