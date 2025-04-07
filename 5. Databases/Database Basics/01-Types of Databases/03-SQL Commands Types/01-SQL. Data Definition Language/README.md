# SQL. Data Definition Language (DDL)

Let's dive deep into **SQL: Data Definition Language (DDL)** — how it works, what it does, and explore detailed examples with clear explanations.

## 🧠 What is Data Definition Language (DDL)?

**DDL** is a subset of **SQL (Structured Query Language)** that is used to **define, modify, and delete** database **schemas, tables, and other objects** like views, indexes, procedures, etc.

It **describes the structure** of the data, rather than the data itself.

---

## 📦 Common DDL Commands

| Command       | Description                                               |
|---------------|-----------------------------------------------------------|
| `CREATE`      | Creates a new table, database, view, index, etc.          |
| `ALTER`       | Modifies an existing object (table, column, etc.)         |
| `DROP`        | Deletes an object permanently                             |
| `TRUNCATE`    | Removes all rows from a table but keeps the structure     |
| `RENAME`      | Renames an object (table, column, etc.)                   |

---

## 🧱 1. `CREATE` – Creating Objects

### Example 1: Create a Table

```sql
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);
```

### 🔍 Explanation

- `CREATE TABLE employees` creates a new table named `employees`.
- `emp_id INT PRIMARY KEY`: Integer column; unique identifier.
- `name VARCHAR(100)`: A string up to 100 characters.
- `salary DECIMAL(10,2)`: 10 digits total, 2 after decimal (e.g., 99999999.99).
- `hire_date DATE`: Date column.

This defines the structure — it **doesn't add data**, just reserves a format in the DB.

---

## 🔁 2. `ALTER` – Modifying Existing Objects

### Example 2a: Add a Column

```sql
ALTER TABLE employees
ADD email VARCHAR(100);
```

Adds a new `email` column to the `employees` table.

### Example 2b: Modify a Column

```sql
ALTER TABLE employees
MODIFY salary DECIMAL(12, 2);
```

Changes `salary` column to allow larger values.

### Example 2c: Drop a Column

```sql
ALTER TABLE employees
DROP COLUMN department;
```

Removes the `department` column from the table.

---

## ❌ 3. `DROP` – Deleting Objects

### Example 3: Drop a Table

```sql
DROP TABLE employees;
```

This **deletes the table permanently** from the database, along with all data inside it. **Cannot be rolled back** in most systems without backups.

---

## 🚿 4. `TRUNCATE` – Remove Data (Keep Structure)

### Example 4: Truncate Table

```sql
TRUNCATE TABLE employees;
```

This deletes **all rows** in the table but **keeps the table structure** for reuse. Unlike `DELETE`, `TRUNCATE` is:

- Faster
- Cannot be rolled back in most systems
- Does not fire triggers in many DBMS

---

## ✏️ 5. `RENAME` – Renaming Objects

### Example 5: Rename a Table

```sql
RENAME TABLE employees TO staff;
```

Changes the table name from `employees` to `staff`.

---

## 🛠️ Other Objects Created with DDL

### Example: Create a Database

```sql
CREATE DATABASE company_db;
```

Creates a new database.

### Example: Create an Index

```sql
CREATE INDEX idx_salary ON employees(salary);
```

Creates an index on the `salary` column to speed up queries.

---

## 💡 Summary

| Command    | Action                                        |
|------------|-----------------------------------------------|
| `CREATE`   | Define new structures (table, database, etc.) |
| `ALTER`    | Change existing structures                    |
| `DROP`     | Delete objects permanently                    |
| `TRUNCATE` | Clear data but keep structure                 |
| `RENAME`   | Change the name of objects                    |

---

If you'd like, I can also:

- Give you **practice exercises**
- Show how these commands look in **different databases** (MySQL vs PostgreSQL)
- Show you **DDL scripts** for a sample project

---

## 📁 Sample DDL Script for a Small Project

Let’s design a small **Employee Management System** with:

- `departments` table
- `employees` table
- `projects` table
- `employee_project` join table

```sql
-- Create Departments
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) UNIQUE
);

-- Create Employees
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10, 2),
    hire_date DATE,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Create Projects
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    start_date DATE,
    end_date DATE
);

-- Many-to-Many: Employees assigned to Projects
CREATE TABLE employee_project (
    emp_id INT,
    project_id INT,
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
```

This setup covers:

- Relationships (1:M and M:N)
- Foreign keys
- Composite primary keys
