# 🍽️ Food Delivery API

A Django REST Framework backend for a food delivery application. It supports user authentication, restaurant and meal management, favorites system, cart functionality, and order checkout.

---

## 🚀 Features

- 🔐 JWT authentication (register, login, token refresh)
- 🏪 Restaurant management (with admin approval)
- 🍔 Meal creation and filtering (per restaurant)
- ❤️ Favorite meals toggle and list
- 🛒 Cart and order checkout system
- 👮 Admin dashboard support

---

## 🛠️ Tech Stack

- Django & Django REST Framework
- MySql (can switch to PostgreSQL/SQLite)
- JWT Authentication
- Stripe integration (soon)

---

## ⚠️ Notes

- This project is **under active development**, not 100% finished.
- Some features may be unstable or incomplete.

---

## 📡 API Endpoints

### 🔐 Authentication

| Method | Endpoint                  | Description                          |
|--------|---------------------------|--------------------------------------|
| POST   | `/api/account/register/`  | Register a new user                  |
| POST   | `/api/account/login/`     | Login using email and password       |
| POST   | `/api/token/`             | Get access and refresh tokens        |
| POST   | `/api/refresh/`           | Refresh access token using refresh   |

---

### 🏪 Restaurant

| Method | Endpoint                             | Description                             |
|--------|--------------------------------------|-----------------------------------------|
| GET    | `/api/restaurant/`                   | List all restaurants                    |
| POST   | `/api/restaurant/`                   | Create a restaurant (await approval)    |
| PUT    | `/api/restaurant/update-restaurant/` | Update authenticated user's restaurant  |
| DELETE | `/api/restaurant/delete-restaurant/` | Delete authenticated user's restaurant  |

---

### 🍔 Meals

| Method | Endpoint                          | Description                         |
|--------|-----------------------------------|-------------------------------------|
| GET    | `/api/meals/meals/`               | List all meals                      |
| POST   | `/api/meals/meals/`               | Create a new meal                   |
| PUT    | `/api/meals/meals/{meal_id}/`     | Update a meal                       |
| DELETE | `/api/meals/meals/{meal_id}/`     | Delete a meal                       |
| GET    | `/api/meals/meals/?meal_name=pizza` | Filter meals by name (e.g., pizza) |
| GET    | `/api/meals/meals/?category=food`   | Filter meals by category (e.g., food)|

---

### ❤️ Favorites

| Method | Endpoint                         | Description                    |
|--------|----------------------------------|--------------------------------|
| GET    | `/api/meals/favorite/`          | List favorite meals            |
| POST   | `/api/meals/favorite/`          | Add meal to favorites          |
| POST   | `/api/meals/favorite/toggle/`   | Toggle meal in/out of favorites|

---

### 🛒 Cart & Checkout

| Method | Endpoint                      | Description                       |
|--------|-------------------------------|-----------------------------------|
| GET    | `/api/cart/`                  | View cart items                   |
| POST   | `/api/cart/cart-items/`       | Add meal to cart by meal ID       |
| POST   | `/api/checkout/`              | Checkout and place the order      |

---

## ✅ How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/MohammedAldarwish/Food-Ordering-System.git
   cd Food-Ordering-System
   ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Apply migrations:
    ```bash 
    python manage.py migrate
    ```
4. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
5. Run the server:
    ```bash
    python manage.py runserver
    ```


