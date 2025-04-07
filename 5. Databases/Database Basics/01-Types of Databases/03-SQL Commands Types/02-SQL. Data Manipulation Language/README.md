# SQL: Data Manipulation Language (DML)

## 🔍 SQL: **Data Manipulation Language (DML)** – Detailed Explanation with Examples

---

## 📌 What is DML?

**DML (Data Manipulation Language)** is a subset of SQL used to manage data **inside tables**. It allows you to **retrieve, insert, update, and delete** data in relational databases.

> 🧠 While **DDL (Data Definition Language)** defines *structure*, **DML** handles *data*.

---

## 🔧 Common DML Commands

| Command   | Purpose                          |
|-----------|----------------------------------|
| `SELECT`  | Retrieve data from tables        |
| `INSERT`  | Add new data to a table          |
| `UPDATE`  | Modify existing data             |
| `DELETE`  | Remove data from a table         |

---

## 1. 🧠 `SELECT` – Read/Retrieve Data

### 📄 Syntax

```sql
SELECT column1, column2 FROM table_name WHERE condition;
```

### ✅ Example

```sql
SELECT name, age FROM employees WHERE department = 'HR';
```

### 🧾 Explanation

- `SELECT name, age`: We want these two columns.
- `FROM employees`: We're querying the `employees` table.
- `WHERE department = 'HR'`: Only rows where the department is HR.

---

## 2. 🆕 `INSERT` – Add New Data

### 📄 Syntax

```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```

### ✅ Example

```sql
INSERT INTO employees (name, age, department) VALUES ('Alice', 30, 'Finance');
```

### 🧾 Explanation

- Adds a new row to the `employees` table.
- `name = 'Alice'`, `age = 30`, `department = 'Finance'`.

---

## 3. 🛠️ `UPDATE` – Modify Existing Data

### 📄 Syntax

```sql
UPDATE table_name SET column1 = value1 WHERE condition;
```

### ✅ Example

```sql
UPDATE employees SET department = 'Marketing' WHERE name = 'Alice';
```

### 🧾 Explanation

- Modifies the `department` for the employee named 'Alice'.
- Only rows where `name = 'Alice'` will be updated.

---

## 4. ❌ `DELETE` – Remove Data

### 📄 Syntax

```sql
DELETE FROM table_name WHERE condition;
```

### ✅ Example

```sql
DELETE FROM employees WHERE age < 25;
```

### 🧾 Explanation

- Deletes all rows from `employees` where the `age` is less than 25.

> ⚠️ **Warning**: Omitting the `WHERE` clause will delete **all rows** in the table.

---

### 🧩 A Sample Table: `employees`

| id | name  | age | department |
|----|-------|-----|------------|
| 1  | John  | 28  | HR         |
| 2  | Alice | 30  | Finance    |
| 3  | Bob   | 22  | IT         |

### Let's Apply DML Step-by-Step

#### 1. `SELECT`

```sql
SELECT * FROM employees WHERE age > 25;
```

✔️ Shows John and Alice.

#### 2. `INSERT`

```sql
INSERT INTO employees (name, age, department) VALUES ('Diana', 27, 'IT');
```

🆕 Adds Diana to the table.

#### 3. `UPDATE`

```sql
UPDATE employees SET department = 'HR' WHERE name = 'Diana';
```

🔁 Diana’s department changed to HR.

#### 4. `DELETE`

```sql
DELETE FROM employees WHERE name = 'Bob';
```

🗑️ Bob is removed from the table.

---

### ✅ Best Practices

- Always **use WHERE** with `UPDATE` and `DELETE` to avoid affecting all rows.
- Use **transactions** (with `BEGIN`, `COMMIT`, and `ROLLBACK`) for safety in complex operations.
- You can combine `SELECT` with **joins, aggregates, and subqueries** for powerful data analysis.

---

## DML Practice Problems

Let's dive into **DML Practice Problems** first, then cover **transactions and rollback** with examples.

---

## ✅ Part 1: DML Practice Problems

We'll use this sample table:

### Table: `students`

| id | name     | age | grade |
|----|----------|-----|-------|
| 1  | Alice    | 20  | B     |
| 2  | Bob      | 19  | C     |
| 3  | Charlie  | 21  | A     |
| 4  | Diana    | 22  | B     |

---

### 🔄 Problem 1: Select students older than 20

```sql
SELECT * FROM students WHERE age > 20;
```

**Expected Result**: Charlie and Diana

---

### ➕ Problem 2: Add a new student "Eve", age 20, grade "A"

```sql
INSERT INTO students (name, age, grade) VALUES ('Eve', 20, 'A');
```

---

### 📝 Problem 3: Update "Bob"'s grade to "B+"

```sql
UPDATE students SET grade = 'B+' WHERE name = 'Bob';
```

---

### ❌ Problem 4: Delete students with grade "C"

```sql
DELETE FROM students WHERE grade = 'C';
```

---

### 🔍 Problem 5: Select names of students with grade "A" or "B+"

```sql
SELECT name FROM students WHERE grade IN ('A', 'B+');
```

---

## 💡 Part 2: Transactions and Rollback in DML

### 🎯 What are Transactions?

A **transaction** is a group of SQL operations that are executed as a **single unit**. It's either **fully completed** or **fully reversed**.

### ✅ Commands

| Command     | Purpose                            |
|-------------|------------------------------------|
| `BEGIN`     | Starts a transaction               |
| `COMMIT`    | Saves all changes made             |
| `ROLLBACK`  | Undoes all changes since `BEGIN`   |

---

### 🔁 Example Scenario with Rollback

```sql
-- Start transaction
BEGIN;

-- Step 1: Insert new student
INSERT INTO students (name, age, grade) VALUES ('Frank', 23, 'D');

-- Step 2: Oops! We realize we made a mistake (grade should be 'B')
ROLLBACK;

-- Now: No change is saved, 'Frank' was never added
```

### ✅ Now let's do it correctly

```sql
BEGIN;

-- Insert new student with correct data
INSERT INTO students (name, age, grade) VALUES ('Frank', 23, 'B');

-- All good? Commit it!
COMMIT;
```

---

### 💥 Rollback with Update Example

```sql
BEGIN;

UPDATE students SET grade = 'F' WHERE name = 'Charlie';

-- Realize this was a mistake!
ROLLBACK;

-- Charlie's grade is restored to the original value.
```

---

### 🧠 Why Use Transactions?

- Ensure **data integrity**
- Useful in **multi-step operations** (e.g. transferring money)
- Allow **safe testing** before committing changes

---
