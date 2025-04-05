# **SQL `CREATE` Statement: Detailed Explanation**

The `CREATE` statement in SQL is used to define new database objects such as tables, views, indexes, schemas, and databases. The most commonly used `CREATE` statement is for creating tables.

---

## **1. Basic Syntax**

The general syntax for creating a table is:

```sql
CREATE TABLE table_name (
    column1 datatype constraints,
    column2 datatype constraints,
    ...
);
```

- `table_name` → The name of the table being created.
- `column1, column2, ...` → The columns of the table.
- `datatype` → Defines the type of data that the column will store (e.g., `INT`, `VARCHAR(255)`, `DATE`, etc.).
- `constraints` → Defines rules for the column (e.g., `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `FOREIGN KEY`, etc.).

---

## **2. Example of Creating a Table**

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
```

### **Explanation:**

- `employee_id` is an `INT` and serves as the `PRIMARY KEY`, meaning it must be unique and not `NULL`.
- `first_name` and `last_name` are `VARCHAR(50)`, meaning they store strings up to 50 characters.
- `email` is `VARCHAR(100)` and must be unique (`UNIQUE` constraint).
- `hire_date` is a `DATE` and cannot be `NULL` (`NOT NULL` constraint).
- `department_id` is an `INT` and serves as a `FOREIGN KEY` linking to the `departments` table.

---

## **3. Creating Other Database Objects**

### **Creating a Database**

```sql
CREATE DATABASE company_db;
```

This creates a new database named `company_db`.

---

### **Creating a Schema**

A schema is a logical grouping of database objects.

```sql
CREATE SCHEMA sales_schema;
```

This creates a schema called `sales_schema` where tables and views can be organized.

---

### **Creating an Index**

```sql
CREATE INDEX idx_employee_email ON employees(email);
```

This creates an index on the `email` column to speed up searches.

---

### **Creating a View**

```sql
CREATE VIEW employee_info AS
SELECT employee_id, first_name, last_name, email
FROM employees;
```

This creates a virtual table (`VIEW`) that stores a predefined query result.

---

### **Creating a Table with Default Values**

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) DEFAULT 0.00
);
```

- The `DEFAULT` constraint sets a default price of `0.00` if no value is provided.

---

## **4. Pitfalls and Best Practices**

### **Pitfalls:**

1. **Not Specifying Constraints Properly**
   - If constraints like `NOT NULL` or `PRIMARY KEY` are missing, the table might allow invalid or duplicate data.

2. **Choosing Incorrect Data Types**
   - Using `VARCHAR(255)` when `VARCHAR(50)` is sufficient wastes storage.
   - Using `FLOAT` for financial values can lead to rounding errors; `DECIMAL` is preferred.

3. **Not Normalizing Data**
   - Avoid redundant columns by normalizing tables (e.g., using `FOREIGN KEY` instead of duplicating department names in every row).

4. **Forgetting to Index Frequently Queried Columns**
   - Failing to add indexes on frequently searched columns (e.g., `email` in an `employees` table) can slow down queries.

5. **Hard-Coding Defaults Without Consideration**
   - Setting default values (e.g., `0.00` for prices) can cause unintended issues if an actual value is expected.

---

### **Best Practices:**

✅ **Use Constraints Properly** → Define `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, and `FOREIGN KEY` constraints to maintain data integrity.

✅ **Choose the Right Data Types** → Use appropriate types (`VARCHAR`, `TEXT`, `INT`, `DECIMAL`) based on the expected data.

✅ **Normalize Tables** → Avoid redundant data by properly structuring relationships.

✅ **Index Frequently Queried Columns** → Speed up lookups using `INDEX` but avoid excessive indexing as it impacts `INSERT/UPDATE/DELETE` performance.

✅ **Use `IF NOT EXISTS` When Creating Objects** → Prevent errors if the object already exists:

```sql
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL
);
```

✅ **Follow Naming Conventions** → Use meaningful and consistent names for tables, columns, and constraints.

✅ **Consider Performance and Scalability** → Think about future scalability when designing tables (e.g., partitioning large tables, optimizing storage).

---

## **5. Modifying Tables After Creation**

- **Adding a Column:**

  ```sql
  ALTER TABLE employees ADD phone_number VARCHAR(20);
  ```

- **Removing a Column:**

  ```sql
  ALTER TABLE employees DROP COLUMN phone_number;
  ```

- **Changing Data Type:**

  ```sql
  ALTER TABLE employees MODIFY COLUMN first_name VARCHAR(100);
  ```

---

## **Conclusion**

The `CREATE` statement is foundational in SQL for defining database structures. Using best practices and avoiding pitfalls ensures efficient, scalable, and maintainable databases. Properly designed tables with correct constraints and indexing improve performance and data integrity.

---

## Advanced CREATE Examples with Constraints and Optimizations

## **1. Advanced Constraints in `CREATE TABLE`**

Constraints help maintain data integrity. Here’s a table using multiple constraints effectively.

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2) CHECK (total_amount >= 0),
    status ENUM('pending', 'shipped', 'delivered', 'canceled') NOT NULL DEFAULT 'pending',
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);
```

### **🔍 Explanation of Constraints:**

- **`PRIMARY KEY AUTO_INCREMENT`** → Ensures `order_id` is unique and automatically increments.
- **`NOT NULL`** → Ensures values cannot be `NULL` (e.g., `customer_id` and `status`).
- **`DEFAULT CURRENT_TIMESTAMP`** → Sets `order_date` to the current time if no value is provided.
- **`CHECK (total_amount >= 0)`** → Prevents negative values for `total_amount`.
- **`ENUM`** → Restricts `status` to a predefined set of values.
- **`FOREIGN KEY ON DELETE CASCADE`** → If a customer is deleted, all their orders will also be deleted automatically.

---

## **2. Optimized Table Design with Partitioning**

Partitioning can improve query performance on large datasets.

```sql
CREATE TABLE logs (
    log_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    log_date DATE NOT NULL,
    message TEXT
) PARTITION BY RANGE (YEAR(log_date)) (
    PARTITION p2019 VALUES LESS THAN (2020),
    PARTITION p2020 VALUES LESS THAN (2021),
    PARTITION p2021 VALUES LESS THAN (2022),
    PARTITION p_future VALUES LESS THAN MAXVALUE
);
```

### **🔍 Explanation:**

- **Partitioning by Year (`RANGE`)** improves query performance by keeping relevant data in specific partitions.
- **`MAXVALUE`** ensures future data is stored correctly.

🛠 **When to Use Partitioning?**

- When working with **very large tables** (e.g., logs, event tracking).
- If queries are **often filtered by a partitioned column** (e.g., `WHERE log_date BETWEEN '2021-01-01' AND '2021-12-31'`).

---

## **3. Creating a Table with JSON and Indexing for Performance**

### **🚀 Storing JSON Data Efficiently**

```sql
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    metadata JSON DEFAULT NULL,
    INDEX idx_metadata ((CAST(metadata->'$.age' AS UNSIGNED)))
);
```

**🔍 Explanation:**

- **JSON Data Type** → Stores dynamic key-value pairs in the `metadata` column.
- **JSON Indexing** → Indexes `metadata->'$.age'` to improve query speed when searching users by age.

📌 **Querying JSON:**

```sql
SELECT * FROM users WHERE JSON_EXTRACT(metadata, '$.age') > 30;
```

---

## **4. Creating a Composite Primary Key**

Composite keys use multiple columns to uniquely identify a record.

```sql
CREATE TABLE course_enrollments (
    student_id INT,
    course_id INT,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

**🔍 Explanation:**

- **`PRIMARY KEY (student_id, course_id)`** → Prevents duplicate enrollments for the same student in the same course.
- **`FOREIGN KEY`** → Enforces referential integrity.

---

## **5. Using Indexes for Query Optimization**

Indexes speed up searches but increase storage and `INSERT/UPDATE/DELETE` time.

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    salary DECIMAL(10,2),
    INDEX idx_department_salary (department_id, salary)
);
```

**🔍 Explanation:**

- **`INDEX idx_department_salary (department_id, salary)`** → Optimizes queries like:

  ```sql
  SELECT * FROM employees WHERE department_id = 3 AND salary > 50000;
  ```

🛠 **Indexing Best Practices:**

- Use **indexes on frequently searched columns** (e.g., `email`, `order_date`).
- Avoid **indexing columns that are updated frequently**, as it slows down writes.
- Consider **composite indexes** for queries filtering by multiple columns.

---

## **6. Creating a Temporary Table**

Temporary tables exist only during the session.

```sql
CREATE TEMPORARY TABLE temp_sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    sale_amount DECIMAL(10,2)
);
```

📌 **Why Use Temporary Tables?**

- Useful for **storing intermediate results** in complex queries.
- Automatically **deleted when the session ends**.

---

## **7. Creating a Table with Generated Columns**

Generated columns store computed values.

```sql
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(10,2) NOT NULL,
    tax DECIMAL(10,2) GENERATED ALWAYS AS (amount * 0.08) STORED
);
```

📌 **Benefits of Generated Columns:**

- Saves computation time during queries.
- Reduces redundancy by avoiding manually storing computed values.

---

## **8. Using `IF NOT EXISTS` to Prevent Errors**

Avoid errors if a table already exists.

```sql
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

---

## **Best Practices Summary ✅**

| 🔍 **Best Practice**       | ✅ **Why It’s Important**                                     |
|----------------------------|----------------------------------------------------------------|
| Use `NOT NULL` constraints | Prevents accidental `NULL` values in critical columns.         |
| Use `DEFAULT` values       | Avoids `NULL` issues and provides fallback values.             |
| Optimize indexes           | Speeds up queries but use wisely to avoid slowing down writes. |
| Normalize data             | Prevents redundant data and improves consistency.              |
| Partition large tables     | Helps manage massive datasets efficiently.                     |
| Use JSON carefully         | Great for dynamic data, but indexing is necessary.             |
| Choose correct data types  | Avoid unnecessary space usage and improve performance.         |

---

## **Conclusion:**

A well-structured `CREATE` statement improves performance, data integrity, and scalability. Using **constraints, indexes, partitioning, and JSON storage** effectively ensures a well-optimized database.

---

## SQL triggers, stored procedures, and real-world schema design

Let's dive into **SQL triggers, stored procedures, and real-world schema design** in detail.

## **1️⃣ SQL Triggers**

A **trigger** is an automated SQL procedure that executes before or after an event (`INSERT`, `UPDATE`, `DELETE`) on a table.

### **Basic Syntax**

```sql
CREATE TRIGGER trigger_name
BEFORE | AFTER INSERT | UPDATE | DELETE
ON table_name
FOR EACH ROW
BEGIN
    -- SQL statements;
END;
```

---

### **🔹 Example 1: Logging Changes in an `employees` Table**

```sql
CREATE TABLE employee_audit (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    action_type VARCHAR(10),
    change_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Now, we create a **trigger** to log updates:

```sql
CREATE TRIGGER after_employee_update
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employee_audit (employee_id, action_type)
    VALUES (OLD.employee_id, 'UPDATE');
END;
```

📌 **How It Works:**

- This trigger runs **after an `UPDATE`** on `employees`.
- It inserts a record into `employee_audit`, logging the **employee ID** and **action type**.

---

### **🔹 Example 2: Prevent Negative Salaries**

```sql
CREATE TRIGGER prevent_negative_salary
BEFORE INSERT OR UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Salary cannot be negative';
    END IF;
END;
```

📌 **How It Works:**

- If a new `salary` is negative, an error is thrown.

---

### **Best Practices for Triggers**

✅ **Use triggers for logging and validation** but not for complex business logic.  
✅ **Avoid recursive triggers**, as they can cause infinite loops.  
✅ **Minimize performance impact** by keeping trigger logic lightweight.  

---

## **2️⃣ SQL Stored Procedures**

A **stored procedure** is a reusable block of SQL code stored in the database, which can accept **input parameters**, execute SQL, and return results.

**Basic Syntax:**

```sql
CREATE PROCEDURE procedure_name (param1 datatype, param2 datatype)
BEGIN
    -- SQL statements;
END;
```

---

### **🔹 Example 1: Get Employee Details**

```sql
CREATE PROCEDURE GetEmployee(IN emp_id INT)
BEGIN
    SELECT * FROM employees WHERE employee_id = emp_id;
END;
```

📌 **Calling the Procedure:**

```sql
CALL GetEmployee(101);
```

🔹 This retrieves the employee with `employee_id = 101`.

---

### **🔹 Example 2: Increase Salary by Percentage**

```sql
CREATE PROCEDURE IncreaseSalary(IN emp_id INT, IN percentage DECIMAL(5,2))
BEGIN
    UPDATE employees
    SET salary = salary + (salary * percentage / 100)
    WHERE employee_id = emp_id;
END;
```

📌 **Calling the Procedure:**

```sql
CALL IncreaseSalary(102, 10);
```

🔹 This increases **employee 102's salary** by 10%.

---

### **🔹 Example 3: Returning a Value**

```sql
CREATE PROCEDURE CountEmployees(OUT total INT)
BEGIN
    SELECT COUNT(*) INTO total FROM employees;
END;
```

📌 **Calling the Procedure:**

```sql
CALL CountEmployees(@count);
SELECT @count;
```

🔹 This gets the total employee count.

---

### **Best Practices for Stored Procedures**

✅ **Use procedures for complex business logic** to reduce repeated SQL.  
✅ **Use `IN`, `OUT`, and `INOUT` parameters** for flexibility.  
✅ **Optimize performance** by avoiding unnecessary computations inside procedures.  

---

## **3️⃣ Real-World Schema Design**

Now, let's design a **real-world relational database**.

## **📌 Scenario: E-Commerce System**

We need to create a **schema** for an e-commerce store with:

- `customers`
- `products`
- `orders`
- `order_items`
- `payments`

---

### **🔹 1. Customers Table**

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

🔹 **Why?**

- `AUTO_INCREMENT` for unique customer IDs.
- `UNIQUE` email ensures no duplicates.
- `created_at` logs when the customer signed up.

---

### **🔹 2. Products Table**

```sql
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) CHECK (price > 0),
    stock_quantity INT CHECK (stock_quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

🔹 **Why?**

- `CHECK (price > 0)` ensures positive prices.
- `CHECK (stock_quantity >= 0)` prevents negative stock.

---

### **🔹 3. Orders Table**

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10,2) CHECK (total_amount >= 0),
    status ENUM('pending', 'shipped', 'delivered', 'canceled') NOT NULL DEFAULT 'pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);
```

🔹 **Why?**

- `ENUM` keeps track of order status.
- `ON DELETE CASCADE` removes orders if a customer is deleted.

---

### **🔹 4. Order Items (Many-to-Many Relationship)**

```sql
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT CHECK (quantity > 0),
    price DECIMAL(10,2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

🔹 **Why?**

- `ON DELETE CASCADE` removes items when an order is deleted.
- Stores `price` separately to preserve historical prices.

---

### **🔹 5. Payments Table**

```sql
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    amount DECIMAL(10,2) CHECK (amount > 0),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method ENUM('credit_card', 'paypal', 'bank_transfer'),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);
```

🔹 **Why?**

- `CHECK (amount > 0)` ensures valid payments.
- `ENUM` restricts payment methods.

---

### **🔹 Relationships Between Tables**

| **Table**                  | **Relationship**                                            |
|----------------------------|-------------------------------------------------------------|
| `customers` → `orders`     | **One-to-Many** (One customer can have many orders)         |
| `orders` → `order_items`   | **One-to-Many** (One order can have multiple items)         |
| `products` → `order_items` | **One-to-Many** (One product can appear in multiple orders) |
| `orders` → `payments`      | **One-to-One** (Each order has one payment)                 |

---

## **Best Practices for Schema Design**

✅ **Normalize the database** (Avoid redundant data).  
✅ **Use `FOREIGN KEYS`** for data integrity.  
✅ **Index frequently searched columns** (e.g., `email`, `order_date`).  
✅ **Partition large tables** (e.g., historical `orders`).  
✅ **Avoid over-indexing** (Too many indexes slow down writes).  

---

## **🎯 Summary**

We covered:
✅ **Triggers** (Automated actions)  
✅ **Stored Procedures** (Reusable SQL logic)  
✅ **Real-World Schema Design** (E-commerce system)  

---

## Database Indexing: Concepts, Types & Best Practices

## **1️⃣ What is an Index?**

An **index** is a data structure that speeds up queries by reducing the amount of data scanned. It's like an index in a book—rather than scanning every page, you can jump directly to the relevant section.

---

## **2️⃣ Types of Indexes in SQL**

### **🔹 1. Primary Index (Clustered Index)**

- A **clustered index** determines the **physical order** of rows in a table.
- Every table **can have only one clustered index** (usually the `PRIMARY KEY`).
- Improves performance for **range-based queries** (e.g., `BETWEEN`, `ORDER BY`).

#### **Example**

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,  -- Automatically creates a clustered index
    name VARCHAR(100),
    salary DECIMAL(10,2)
);
```

📌 **Since `PRIMARY KEY` is indexed, searches on `employee_id` are optimized.**

---

### **🔹 2. Secondary Index (Non-Clustered Index)**

- **Stores pointers to the actual data**, instead of sorting it.
- **Multiple non-clustered indexes** can exist in a table.
- Useful for **frequently searched columns**.

**Example:**

```sql
CREATE INDEX idx_employee_name ON employees (name);
```

📌 **Now, queries like `WHERE name = 'John Doe'` run faster.**

---

### **🔹 3. Composite Index (Multi-Column Index)**

- An index on **multiple columns**, used when queries involve multiple fields.
- **Column order matters** (e.g., an index on `(A, B)` can be used for `A` or `A, B`, but not for `B` alone).

**Example:**

```sql
CREATE INDEX idx_employee_salary ON employees (department_id, salary);
```

📌 **Speeds up queries like:**

```sql
SELECT * FROM employees WHERE department_id = 3 AND salary > 50000;
```

---

### **🔹 4. Unique Index**

- Ensures column values are **unique**, preventing duplicates.

**Example:**

```sql
CREATE UNIQUE INDEX idx_email_unique ON customers (email);
```

📌 **Ensures that no two customers have the same email.**

---

### **🔹 5. Full-Text Index**

- Used for **fast text searches**, often in large datasets.

**Example:**

```sql
CREATE FULLTEXT INDEX idx_product_desc ON products (description);
```

📌 **Speeds up searches like:**

```sql
SELECT * FROM products WHERE MATCH(description) AGAINST('gaming laptop');
```

---

### **🔹 6. Partial Index (Filtered Index)**

- Indexes only a **subset of rows**, reducing storage costs.

**Example:**

```sql
CREATE INDEX idx_active_users ON users (status) WHERE status = 'active';
```

📌 **Speeds up queries that filter for active users while saving space.**

---

### **🔹 7. Covering Index**

- An index that **stores all columns** needed for a query, avoiding extra lookups.

**Example:**

```sql
CREATE INDEX idx_order_summary ON orders (customer_id, order_date, total_amount);
```

📌 **Now, queries like**:

```sql
SELECT customer_id, order_date, total_amount FROM orders WHERE customer_id = 123;
```

**can be served directly from the index!**

---

## **3️⃣ When to Use Indexes?**

✅ **Columns frequently used in WHERE, JOIN, ORDER BY, or GROUP BY**  
✅ **Columns with high selectivity** (many unique values, e.g., `email`)  
✅ **Indexes should cover all columns used in WHERE + SELECT**  

🚫 **Avoid Indexing:**

- Columns with **low cardinality** (few unique values, e.g., `gender` with only `M/F`).
- Frequently updated columns (every `INSERT/UPDATE/DELETE` requires index maintenance).
- Small tables (full-table scans might be faster than index lookups).

---

## **4️⃣ How to Check Index Usage?**

### **🔍 Using `EXPLAIN`**

You can analyze query performance using:

```sql
EXPLAIN SELECT * FROM employees WHERE name = 'John Doe';
```

📌 **Look for `Using index`** → It means the index is working!

---

## **5️⃣ Indexing Best Practices ✅**

| Best Practice                                      | Why?                                                          |
|----------------------------------------------------|---------------------------------------------------------------|
| **Use Indexing on High-Selectivity Columns**       | Boosts performance for queries filtering unique values.       |
| **Avoid Over-Indexing**                            | Each index slows down `INSERT/UPDATE/DELETE`.                 |
| **Use Composite Indexes for Multi-Column Queries** | Reduces lookup time for queries using multiple fields.        |
| **Leverage Covering Indexes**                      | Speeds up queries by storing all needed columns in the index. |
| **Monitor Performance with `EXPLAIN`**             | Helps check if queries are using indexes effectively.         |
| **Drop Unused Indexes**                            | Saves storage space and speeds up writes.                     |
