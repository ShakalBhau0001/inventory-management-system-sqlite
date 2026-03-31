# 📦 Inventory-Management-System-SQLite

### Inventory Management System with Relational Database Design

**Inventory-Management-System-SQLite** is a **Python-based application** that demonstrates structured database design using SQLite for managing inventory data.

It is designed for **students and developers** to understand how real-world inventory systems handle data organization, relationships, and operations using a relational database.

All operations are **local**, ensuring **offline usability and data privacy**.

---

## ✨ Key Principles

1. **Database-focused** – emphasizes relational database design concepts  
2. **Structured architecture** – separation of database logic and application logic  
3. **Practical implementation** – real-world inventory use case  

This project is educational, yet practical, showcasing how inventory systems are built using structured database schemas and CRUD operations.

---

## 🧩 Database Overview

The system is built around three core tables:

### 👤 Users
- Handles authentication and access control  
- Stores hashed passwords for basic security  

### 🗂️ Categories
- Organizes inventory into logical groups  
- Enables efficient filtering and management  

### 📦 Items
- Core inventory table storing product details  
- Includes:
  - Quantity tracking  
  - Price management  
  - Minimum stock level (for alerts)  
  - Supplier information  
  - Date tracking  

---

## 🔗 Relationships

- One-to-Many relationship between **Categories** and **Items**  
- Each item is linked to a category using a **foreign key (category_id)**  

> Ensures proper data organization and relational integrity.

---

## ⚙️ Database Features

- Relational schema using **SQLite**  
- Primary Key and Foreign Key constraints  
- Default values for consistency  
- Seed data initialization for quick setup  
- Full CRUD operations (Create, Read, Update, Delete)  

---

## 📁 Project Structure

```bash
inventory-management-system-sqlite/
├── main.py                # Main application entry point

```

> Database operations are managed through a centralized database manager for modularity.

---

## 🚀 Getting Started

####1️⃣ Clone Repository
```bash
git clone https://github.com/ShakalBhau0001/inventory-management-system-sqlite.git  
cd inventory-management-system-sqlite
```

####2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

####3️⃣ Run Application
```bash 
python main.py
``` 

---

## 🗄️ Database Schema (Concept)
- Users(id, username, password, role)
- Categories(id, name, description)
- Items(id, name, category_id, quantity, price, min_stock, supplier, date_added)

> Designed to maintain normalization and data integrity.

---

## 🌱 Seed Data

The database is preloaded with:
    - Default categories (Electronics, Clothing, Food, etc.)
    - Sample inventory items

> Enables immediate testing and demonstration.

---

## ⚠️ Disclaimer

This project is **educational** and intended for learning database design and application development concepts.
It is **not production-ready** and lacks advanced security and scalability features.

---

## 🛣️ Roadmap

- Low stock alert system
- Advanced filtering and search
- User role-based access control
- GUI improvements / dashboard
- Data export functionality

---

## 🪪 Author

> Developer: **Shakal Bhau**
 
> GitHub: **[ShakalBhau0001](https://github.com/ShakalBhau0001)**

---
