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

---

Let’s see hands-on example using SQL commands and how to normalize a database design from scratch.

## 🔶 PART 1: Hands-on SQL Example

Imagine a **Library Management System**. Here's how we can model it and interact using SQL.

### ✅ Step 1: Create Tables

```sql
-- Book Table
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(100),
    Author VARCHAR(100),
    Genre VARCHAR(50)
);

-- Member Table
CREATE TABLE Members (
    MemberID INT PRIMARY KEY,
    Name VARCHAR(100),
    JoinDate DATE
);

-- Borrow Table (Relationship between Members and Books)
CREATE TABLE BorrowedBooks (
    BorrowID INT PRIMARY KEY,
    BookID INT,
    MemberID INT,
    BorrowDate DATE,
    ReturnDate DATE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
```

---

### ✅ Step 2: Insert Some Data

```sql
-- Insert Books
INSERT INTO Books VALUES (1, '1984', 'George Orwell', 'Dystopian');
INSERT INTO Books VALUES (2, 'To Kill a Mockingbird', 'Harper Lee', 'Classic');

-- Insert Members
INSERT INTO Members VALUES (1, 'Alice Smith', '2023-01-10');
INSERT INTO Members VALUES (2, 'Bob Johnson', '2023-02-15');

-- Insert Borrowed Records
INSERT INTO BorrowedBooks VALUES (1, 1, 1, '2023-03-01', '2023-03-15');
INSERT INTO BorrowedBooks VALUES (2, 2, 2, '2023-03-05', NULL);
```

---

### ✅ Step 3: Run Queries

- **Find all borrowed books:**

```sql
SELECT Title, Name, BorrowDate, ReturnDate
FROM BorrowedBooks
JOIN Books ON BorrowedBooks.BookID = Books.BookID
JOIN Members ON BorrowedBooks.MemberID = Members.MemberID;
```

- **List members who haven't returned books:**

```sql
SELECT Name, Title
FROM BorrowedBooks
JOIN Books ON BorrowedBooks.BookID = Books.BookID
JOIN Members ON BorrowedBooks.MemberID = Members.MemberID
WHERE ReturnDate IS NULL;
```

---

## 🔶 PART 2: Database Normalization

**Normalization** is the process of structuring a database to reduce redundancy and improve data integrity.

Let’s walk through the steps using a **Student Course Registration** system.

---

### 🎯 Raw Table (Unnormalized / Flat Table)

| StudentID | StudentName | Course1  | Course2  | Course3  |
|-----------|-------------|----------|----------|----------|
| 1         | Alice       | Math     | Physics  | NULL     |
| 2         | Bob         | English  | History  | Math     |

Problems:

- Redundant course names
- Difficult to query
- Not scalable (Course4, Course5...?)

---

### ✅ First Normal Form (1NF)

**Rule**: Atomic columns (no multivalued fields)

Break into separate rows for each course:

| StudentID | StudentName | Course   |
|-----------|-------------|----------|
| 1         | Alice       | Math     |
| 1         | Alice       | Physics  |
| 2         | Bob         | English  |
| 2         | Bob         | History  |
| 2         | Bob         | Math     |

---

### ✅ Second Normal Form (2NF)

**Rule**: Remove partial dependencies (non-key attributes depend on the whole key)

Split into:

**Students Table:**

| StudentID | StudentName |
|-----------|-------------|
| 1         | Alice       |
| 2         | Bob         |

**Courses Table:**

| CourseID | CourseName |
|----------|------------|
| 101      | Math       |
| 102      | Physics    |
| 103      | English    |
| 104      | History    |

**StudentCourses Table:**

| StudentID | CourseID |
|-----------|----------|
| 1         | 101      |
| 1         | 102      |
| 2         | 103      |
| 2         | 104      |
| 2         | 101      |

---

### ✅ Third Normal Form (3NF)

**Rule**: Remove transitive dependencies (non-key fields depending on other non-key fields)

Already satisfied in this case!

---

## 🔸 Summary

| Step | Goal                         | Action                           |
|------|------------------------------|----------------------------------|
| 1NF  | Remove repeating groups      | Atomic values                    |
| 2NF  | Remove partial dependency    | Split into related tables        |
| 3NF  | Remove transitive dependency | Ensure fields depend on key only |
