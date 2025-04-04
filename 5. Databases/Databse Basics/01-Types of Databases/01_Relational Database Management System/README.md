# Relational Database Management System (RDBMS)

A **Relational Database Management System (RDBMS)** is a type of database management system that stores data in a **structured format using rows and columns**. It is based on the **relational model** proposed by **E.F. Codd** in 1970.

## 🔷 1. What is a Relational Database?

A **relational database** stores data in **tables (also called relations)**. Each table represents **an entity**, and each row in the table is a **record** (also called a tuple) of that entity. The columns represent the **attributes (fields)** of the entity.

---

## 🔷 2. Structure of an RDBMS

### ➤ Tables

A table is the core component. Here’s an example:

**Customer Table:**

| CustomerID | Name     | Email               | City       |
|------------|----------|---------------------|------------|
| 1          | Alice    | <alice@example.com> | New York   |
| 2          | Bob      | <bob@example.com>   | Los Angeles|

Each row = a record  
Each column = an attribute

### ➤ Schema

The schema defines the structure of the database: what tables exist, their columns, data types, constraints, etc.

---

## 🔷 3. Keys in RDBMS

### ➤ Primary Key

Uniquely identifies each record in a table.  
→ Example: `CustomerID` in the `Customer` table.

### ➤ Foreign Key

A field that creates a relationship between two tables.  
→ Example: A `CustomerID` in an `Orders` table refers to the `CustomerID` in the `Customer` table.

### ➤ Candidate Key & Composite Key

- **Candidate Key**: A set of fields that could serve as a unique identifier.
- **Composite Key**: A key made up of more than one field.

---

## 🔷 4. Relationships in RDBMS

RDBMSs can represent various types of relationships:

| Type               | Example                                                                |
|--------------------|------------------------------------------------------------------------|
| One-to-One         | Each user has one passport                                             |
| One-to-Many        | One customer can place many orders                                     |
| Many-to-Many       | Students enroll in multiple courses, and each course has many students |

**Example**:

**Order Table:**

| OrderID | CustomerID | Amount |
|---------|------------|--------|
| 101     | 1          | 250    |
| 102     | 2          | 300    |
| 103     | 1          | 180    |

Here, `CustomerID` in the Order table is a foreign key referencing the `Customer` table. This forms a **one-to-many** relationship.

---

## 🔷 5. How It Works

Here’s how an RDBMS operates:

### 1. **Data Storage**

- Stores data in structured tables with predefined columns and data types.
- Uses indexes to speed up searches and queries.

### 2. **Data Manipulation**

Uses **SQL (Structured Query Language)** to interact with data:

- `SELECT`: retrieve data
- `INSERT`: add new records
- `UPDATE`: modify records
- `DELETE`: remove records

**Example**:

```sql
SELECT * FROM Customer WHERE City = 'New York';
```

### 3. **Data Integrity**

Maintains data accuracy using:

- Constraints (`NOT NULL`, `UNIQUE`, `CHECK`, `DEFAULT`)
- Referential Integrity (via foreign keys)

### 4. **Transactions**

Ensures consistency using **ACID** properties:

- **Atomicity**: all operations in a transaction complete or none do
- **Consistency**: database remains in valid state
- **Isolation**: concurrent transactions don’t interfere
- **Durability**: committed data is saved permanently

**Example**:

```sql
BEGIN;
UPDATE Account SET Balance = Balance - 100 WHERE AccountID = 1;
UPDATE Account SET Balance = Balance + 100 WHERE AccountID = 2;
COMMIT;
```

### 5. **Concurrency Control**

Allows multiple users to access the DB simultaneously using **locking**, **isolation levels**, and **MVCC** (Multi-Version Concurrency Control).

---

## 🔷 6. Examples of RDBMS Software

| RDBMS                | Description                                |
|----------------------|--------------------------------------------|
| MySQL                | Open-source, widely used in web apps       |
| PostgreSQL           | Open-source, powerful features & ACID      |
| Oracle DB            | Enterprise-level, secure, scalable         |
| Microsoft SQL Server | Widely used in corporate environments      |
| SQLite               | Lightweight, serverless                    |

---

## 🔷 7. Advantages of RDBMS

- **Structured & organized data**
- **Data integrity and security**
- **Scalability**
- **Supports complex queries**
- **Data normalization** (removes redundancy)

---

## 🔷 8. Real-World Example

Let’s say you run an **e-commerce store**:

### Tables

- `Customers(CustomerID, Name, Email)`
- `Orders(OrderID, CustomerID, OrderDate)`
- `Products(ProductID, Name, Price)`
- `OrderDetails(OrderID, ProductID, Quantity)`

### Relationships

- `Customers` to `Orders`: one-to-many
- `Orders` to `OrderDetails`: one-to-many
- `Products` to `OrderDetails`: many-to-many

This structure helps answer questions like:

- Which customers bought a specific product?
- How much revenue was generated in March?
- What’s the order history of a customer?

---

## 🔷 9. Summary

An **RDBMS** is a system to manage structured data efficiently using:

- Tables for storage
- SQL for operations
- Keys for relationships
- ACID for data integrity
- Relationships for flexibility

It’s the backbone of many applications in **finance**, **e-commerce**, **healthcare**, **education**, etc.
