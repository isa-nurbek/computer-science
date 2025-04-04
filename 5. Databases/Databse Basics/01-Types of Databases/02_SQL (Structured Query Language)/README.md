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
