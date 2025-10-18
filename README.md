# 🛍️ E-commerce Monolith

This project is a **Python monolithic backend** built with **FastAPI**, implementing a complete CRUD system for a simple e-commerce application with three main entities:

- 👤 **Users**
- 📦 **Products**
- 🧾 **Orders**

The system runs in two containers:
1. **Backend (FastAPI)**
2. **Database (PostgreSQL)**

---

## 🧠 Project Structure

```
ecommerce/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── repositories/
│   ├── services/
│   └── routers/
│
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🐍 Technologies

- Python 3.11  
- FastAPI  
- SQLAlchemy  
- PostgreSQL  
- Docker & Docker Compose  
- Pydantic  

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/youruser/ecommerce-fastapi.git
cd ecommerce-fastapi
```

### 2. Create a `.env` file
```env
POSTGRES_USER=ecommerce_user
POSTGRES_PASSWORD=secretpassword
POSTGRES_DB=ecommerce_db
POSTGRES_HOST=db
POSTGRES_PORT=5432
DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```

---

## 🐳 Run with Docker

```bash
docker-compose up --build
```

| Service | Port | Description |
|----------|------|-------------|
| `ecommerce_app` | 8000 | FastAPI backend |
| `ecommerce_db` | 5433 | PostgreSQL database |

Interactive API documentation:  
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📚 Main Endpoints

| Method | Route | Description |
|--------|--------|-------------|
| `POST` | `/users` | Create a user |
| `GET` | `/users` | List all users |
| `GET` | `/users/{id}` | Get user by ID |
| `POST` | `/products` | Create a product |
| `GET` | `/products` | List all products |
| `PATCH` | `/products/{id}/stock/{stock}` | Update product stock |
| `POST` | `/orders` | Create an order |
| `GET` | `/orders` | List all orders |
| `GET` | `/orders/{id}` | Get order by ID |

---

## 🧩 Example Requests

### Create a User
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Create a Product
```json
{
  "name": "T-shirt",
  "price": 25.5,
  "stock": 50
}
```

### Create an Order
```json
{
  "user_id": 1,
  "product_id": 1,
  "quantity": 2
}
```

---

## 💾 Database Structure

- **users**
- **products**
- **orders**

Relations:
- A user can have many orders.  
- A product can belong to many orders.  
- An order belongs to one user and one product.

---

## 🧠 Architecture Flow

```
HTTP Client
 ↓
Router (FastAPI)
 ↓
Service (business logic)
 ↓
Repository (SQLAlchemy)
 ↓
PostgreSQL Database
```

---

## 🧹 Useful Commands

```bash
docker-compose down          # Stop containers
docker-compose down -v       # Stop and remove volumes
docker-compose up --build    # Rebuild containers
docker exec -it ecommerce_db psql -U ecommerce_user -d ecommerce_db
```

---