# 🚀 GitHub Cloud Connector API (FastAPI)

## 📌 Overview

The **GitHub Cloud Connector API** is a FastAPI-based backend service that integrates with the GitHub REST API to manage repositories, issues, and commits.

It provides endpoints to:

* Fetch user repositories (with visibility filtering)
* Retrieve issues for a repository
* Create new issues
* Fetch commit history of a repository

The application uses asynchronous programming with `httpx` for efficient API communication.

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/github-cloud-connector.git
cd github-cloud-connector
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token
```

> ⚠️ Never hardcode tokens in code. Always use environment variables.

---

## ▶️ How to Run the Project

```bash
uvicorn main:app --reload
```

API runs at:

```
http://127.0.0.1:8000
```

---

## 📄 API Documentation

* Swagger UI:
  http://127.0.0.1:8000/docs

* ReDoc:
  http://127.0.0.1:8000/redoc

---

## 🔗 API Endpoints

### 🔹 1. Get Repositories

```http
GET /repos?visibility=all
```

**Query Params:**

* `visibility` = `all` (default) | `public` | `private`

**Response:**

```json
{
  "count": 2,
  "data": [ ... ]
}
```

---

### 🔹 2. Get Issues for a Repository

```http
GET /repos/{owner}/{repo}/issues
```

**Example:**

```http
GET /repos/octocat/Hello-World/issues
```

---

### 🔹 3. Create Issue

```http
POST /repos/{owner}/{repo}/issues
```

**Request Body:**

```json
{
  "title": "Bug in API",
  "body": "Something is not working"
}
```

**Response:**

```json
{
  "message": "Issue created successfully",
  "issue_url": "https://github.com/...",
  "issue_number": 123
}
```

---

### 🔹 4. Get Commits of a Repository

```http
GET /repos/{owner}/{repo}/commits
```

**Response:**

```json
{
  "count": 10,
  "data": [ ... ]
}
```

---

## 🧠 Architecture & Design

### 🔹 Layered Structure

* **main.py** → API routes (controller layer)
* **services.py** → business logic layer
* **models.py** → request validation (Pydantic models)
* **github_client.py** → external GitHub API integration

---

### 🔹 Asynchronous Design

* Uses `async/await` for non-blocking I/O
* Improves performance when calling GitHub APIs

---

## 🔐 Authentication

* Uses **GitHub Personal Access Token**
* Token is stored securely using `.env`
* Passed in request headers when calling GitHub API

---

## ⚠️ Error Handling

Handled using:

* `httpx.HTTPStatusError`
* FastAPI `HTTPException`

### Examples:

* **401** → Invalid/expired GitHub token
* **404** → Repository not found
* **Other errors** → Generic failure messages

Logging is implemented using Python’s `logging` module for debugging.

---

## ✅ Validation

* Request validation handled via **Pydantic (`IssueCreate`)**
* Ensures:

  * `title` is required
  * `body` is required

---

## 📂 Project Structure

```
├── main.py              # API routes
├── services.py          # Business logic
├── models.py            # Pydantic schemas
├── github_client.py     # GitHub API calls
├── .env                 # Environment variables
├── requirements.txt
└── README.md
```

---

## 🧪 Testing the API

Use Swagger UI:

```
http://127.0.0.1:8000/docs
```

Or cURL:

```bash
curl http://127.0.0.1:8000/repos
```

---

## 🚀 Future Improvements

* Add pagination for repositories/issues
* Add caching layer (Redis)
* Improve filtering options
* Add unit & integration tests
* Dockerize the application
* Deploy to cloud (AWS / Azure)

---

