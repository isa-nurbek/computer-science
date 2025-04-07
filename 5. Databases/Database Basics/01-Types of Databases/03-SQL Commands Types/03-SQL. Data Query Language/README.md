# SQL: Data Query Language (DQL)

## SQL: Data Query Language (DQL) – Detailed Explanation with Examples

### 🔍 What is DQL?

**DQL (Data Query Language)** is a subset of SQL (Structured Query Language) used **to query and retrieve data from a database**. The primary and most commonly used DQL statement is:

> **`SELECT`**

DQL does **not modify** the data; it only **fetches** it based on given criteria.

---

### 🔧 How DQL Works

The `SELECT` statement in DQL follows a general syntax:

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
GROUP BY column
HAVING condition
ORDER BY column [ASC|DESC]
LIMIT number;
```

Each part serves a specific function:

| Clause      | Description                                           |
|-------------|-------------------------------------------------------|
| `SELECT`    | Specifies the columns to retrieve                     |
| `FROM`      | Indicates the table to query                          |
| `WHERE`     | Filters records based on condition                    |
| `GROUP BY`  | Groups rows with the same values in specified columns |
| `HAVING`    | Filters groups (used with GROUP BY)                   |
| `ORDER BY`  | Sorts the results                                     |
| `LIMIT`     | Restricts the number of returned records              |

---

### 🧪 Examples with Explanations

Let's use a sample table called `employees`:

| id | name      | department | salary |
|----|-----------|------------|--------|
| 1  | Alice     | HR         | 50000  |
| 2  | Bob       | IT         | 70000  |
| 3  | Charlie   | IT         | 60000  |
| 4  | Diana     | Marketing  | 55000  |
| 5  | Evan      | HR         | 52000  |

---

#### 1. **Basic SELECT**

```sql
SELECT name, salary FROM employees;
```

**Explanation:**  
Fetches the `name` and `salary` of all employees.

---

#### 2. **Filtering with WHERE**

```sql
SELECT * FROM employees WHERE department = 'IT';
```

**Explanation:**  
Returns all columns of employees in the IT department.

**Result:**

| id | name    | department | salary |
|----|---------|------------|--------|
| 2  | Bob     | IT         | 70000  |
| 3  | Charlie | IT         | 60000  |

---

#### 3. **Sorting Results with ORDER BY**

```sql
SELECT name, salary FROM employees ORDER BY salary DESC;
```

**Explanation:**  
Lists employee names and salaries, sorted from highest to lowest salary.

---

#### 4. **Limiting Results**

```sql
SELECT name FROM employees LIMIT 3;
```

**Explanation:**  
Returns the first 3 employee names (depending on DB engine default order or ORDER BY).

---

#### 5. **Grouping and Aggregation**

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

**Explanation:**  
Groups employees by department and shows the average salary for each department.

**Result:**

| department | avg_salary |
|------------|------------|
| HR         | 51000      |
| IT         | 65000      |
| Marketing  | 55000      |

---

#### 6. **Filtering Groups with HAVING**

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 55000;
```

**Explanation:**  
Same as above, but only departments where the average salary is greater than 55,000 are included.

---

### 🧠 Summary

| Feature        | Used For |
|----------------|----------|
| `SELECT`       | Retrieving columns |
| `WHERE`        | Filtering rows |
| `GROUP BY`     | Aggregating data |
| `HAVING`       | Filtering aggregates |
| `ORDER BY`     | Sorting data |
| `LIMIT`        | Limiting output |

---

## 🎯 PRACTICE EXERCISES

### 🔹 **Table: `employees`**

| id | name     | department | salary | hire_date  |
|----|----------|------------|--------|------------|
| 1  | Alice    | HR         | 50000  | 2020-01-15 |
| 2  | Bob      | IT         | 70000  | 2019-03-20 |
| 3  | Charlie  | IT         | 60000  | 2021-07-10 |
| 4  | Diana    | Marketing  | 55000  | 2018-11-05 |
| 5  | Evan     | HR         | 52000  | 2022-05-17 |

---

### ✅ Exercise 1: Basic SELECT  

**Q:** Get the names and salaries of all employees.  

```sql
SELECT name, salary FROM employees;
```

---

### ✅ Exercise 2: Filtering  

**Q:** List all employees in the IT department with salary over 65000.  

```sql
SELECT * FROM employees
WHERE department = 'IT' AND salary > 65000;
```

---

### ✅ Exercise 3: Sorting  

**Q:** Show all employee names and hire dates, sorted from newest to oldest.  

```sql
SELECT name, hire_date FROM employees
ORDER BY hire_date DESC;
```

---

### ✅ Exercise 4: Aggregation  

**Q:** What is the average salary in the company?  

```sql
SELECT AVG(salary) AS average_salary FROM employees;
```

---

### ✅ Exercise 5: Grouping  

**Q:** Show average salary by department.  

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

---

### ✅ Exercise 6: Filtering Groups with HAVING  

**Q:** Show departments with an average salary greater than 55000.  

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 55000;
```

---

### ✅ Exercise 7: LIMIT  

**Q:** Show the top 2 highest-paid employees.  

```sql
SELECT name, salary
FROM employees
ORDER BY salary DESC
LIMIT 2;
```

---

## 🏗️ MINI PROJECT – PAYROLL SYSTEM

### 🎯 Project Goal  

Build a **Payroll System** to track employee info, departments, and payments. We'll use DQL to **generate reports** and **filter data**.

---

### 🛠️ Schema

**Table: `employees`**

```sql
CREATE TABLE employees (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  department_id INT,
  hire_date DATE
);
```

**Table: `departments`**

```sql
CREATE TABLE departments (
  id INT PRIMARY KEY,
  name VARCHAR(50)
);
```

**Table: `salaries`**

```sql
CREATE TABLE salaries (
  employee_id INT,
  amount DECIMAL(10,2),
  pay_date DATE
);
```

---

### 🔍 Sample DQL Queries for the Project

#### 1. List all employees with their department names

```sql
SELECT e.name, d.name AS department
FROM employees e
JOIN departments d ON e.department_id = d.id;
```

---

#### 2. Get total salary paid to each employee

```sql
SELECT e.name, SUM(s.amount) AS total_paid
FROM employees e
JOIN salaries s ON e.id = s.employee_id
GROUP BY e.name;
```

---

#### 3. Get the highest-paid employee in total

```sql
SELECT e.name, SUM(s.amount) AS total_earned
FROM employees e
JOIN salaries s ON e.id = s.employee_id
GROUP BY e.name
ORDER BY total_earned DESC
LIMIT 1;
```

---

#### 4. Total salary cost by department

```sql
SELECT d.name AS department, SUM(s.amount) AS total_cost
FROM departments d
JOIN employees e ON d.id = e.department_id
JOIN salaries s ON e.id = s.employee_id
GROUP BY d.name;
```

---

#### 5. Employees hired in the last year

```sql
SELECT name, hire_date
FROM employees
WHERE hire_date >= CURRENT_DATE - INTERVAL '1 year';
```
