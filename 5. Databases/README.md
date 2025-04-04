# Introduction to Database

A **database** is an organized collection of data stored and accessed electronically. It allows for efficient management, retrieval, insertion, updating, and deletion of data. Databases are essential in modern computing, powering applications like websites, banking systems, inventory management, and more.

## **Key Concepts of Databases:**

1. **Structured Storage**  
   - Data is stored in a structured format, often using tables (in relational databases) or documents (in NoSQL databases).
   - Example: A customer database might store names, emails, and purchase history in rows and columns.

2. **Database Management System (DBMS)**  
   - Software that interacts with the database (e.g., MySQL, PostgreSQL, MongoDB, Oracle).  
   - Handles queries, security, backups, and data integrity.

3. **Types of Databases:**  
   - **Relational Databases (SQL)**  
     - Data is stored in tables with rows and columns.  
     - Uses **SQL (Structured Query Language)** for operations.  
     - Examples: MySQL, PostgreSQL, Microsoft SQL Server.  
     - Best for structured data with strict relationships (e.g., banking records).  

   - **NoSQL Databases**  
     - Flexible schemas for unstructured/semi-structured data.  
     - Types: Document (MongoDB), Key-Value (Redis), Graph (Neo4j), Column-family (Cassandra).  
     - Best for scalability (e.g., social media, IoT data).  

   - **NewSQL Databases**  
     - Combines SQL reliability with NoSQL scalability (e.g., Google Spanner).  

4. **ACID Properties (For Relational DBs)**  
   - **Atomicity** – Transactions succeed completely or fail entirely.  
   - **Consistency** – Data remains valid after transactions.  
   - **Isolation** – Concurrent transactions don’t interfere.  
   - **Durability** – Committed data survives crashes.  

5. **Common Operations:**  
   - **CRUD:** Create, Read, Update, Delete.  
   - **Querying:** Using SQL (e.g., `SELECT * FROM users WHERE age > 30`).  
   - **Indexing:** Speeds up searches (like a book index).  

### **Why Use a Database?**  

- **Efficiency:** Faster than file-based storage.  
- **Scalability:** Handles large data volumes.  
- **Security:** User access control & encryption.  
- **Concurrency:** Multiple users access data simultaneously.  

### **Example Use Cases:**  

- Storing user accounts for a website (SQL).  
- Real-time analytics on big data (NoSQL).  
- Financial transactions requiring strict accuracy (ACID-compliant DBs).
