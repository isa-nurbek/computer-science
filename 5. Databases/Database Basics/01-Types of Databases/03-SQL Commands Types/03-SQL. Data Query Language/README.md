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

