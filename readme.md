https://llm-app-6ymf.onrender.com/

# 🧪 Assignment: Build and Deploy a Simple LLM App with CI/CD

## 🎯 Objective

In this assignment, you will:

* Build a simple **LLM-powered application**
* Use **Git** for version control
* Set up a **CI/CD pipeline** using GitHub Actions
* Automatically test and simulate deployment

---

## 📚 What is an LLM?

An **LLM (Large Language Model)** is an AI model that can generate text, answer questions, and assist users.

Examples include:

* Chatbots
* Text summarizers
* Q&A systems

---

## 🛠️ Task Overview

You will create a **basic chatbot app** that:

* Takes user input
* Sends it to an LLM API
* Returns a response

Then you will:

* Push code to GitHub
* Set up CI/CD to test and deploy automatically

---

## 🧱 Step 1: Create the App

### Option: Python (Recommended)

Create a file called `app.py`:

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt):
response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[{"role": "user", "content": prompt}]
)
return response.choices[0].message.content

if __name__ == "__main__":
user_input = input("Ask something: ")
print(ask_llm(user_input))
```

---

## 🔐 Step 2: Set Environment Variable

Do NOT hardcode your API key.

Set it in your system:

**Mac/Linux**

```bash
export OPENAI_API_KEY="your_api_key"
```

**Windows**

```powershell
setx OPENAI_API_KEY "your_api_key"
```

---

## 🧪 Step 3: Add a Basic Test

Create a file `test_app.py`:

```python
from app import ask_llm

def test_response():
result = ask_llm("Say hello")
assert isinstance(result, str)
```

---

## 📦 Step 4: Initialize Git

```bash
git init
git add .
git commit -m "Initial LLM app"
```

Push to GitHub.

---

## ⚙️ Step 5: Add CI/CD Pipeline

Create file:

```
.github/workflows/ci.yml
```

Add:

```yaml
name: CI Pipeline

on:
push:
branches: [ "main" ]

jobs:
test:
runs-on: ubuntu-latest

steps:
- name: Checkout
uses: actions/checkout@v3

- name: Set up Python
uses: actions/setup-python@v4
with:
python-version: "3.10"

- name: Install dependencies
run: |
pip install openai pytest

- name: Run tests
run: pytest

- name: Deploy (Simulated)
run: echo "Deploying LLM app..."
```

---

## ⚠️ Important Note

CI will NOT have your API key by default.

To fix this:

* Go to GitHub repo → Settings → Secrets
* Add:

* `OPENAI_API_KEY`

---

## ✅ Expected Output

When you push code:

* Tests run automatically
* If tests pass → deployment step runs

---

## 📊 Evaluation Criteria

* ✔️ App connects to LLM API
* ✔️ Code runs without errors
* ✔️ Tests exist and pass
* ✔️ CI/CD pipeline works
* ✔️ Proper Git usage

---

## 🌱 Bonus (Optional)

* Add a simple web UI (Flask)
* Deploy to a cloud platform
* Add more prompts (summarizer, translator)

---

## 💡 Learning Outcomes

You will understand:

* Basics of LLM apps
* API integration
* CI/CD automation
* Secure key handling
* Real-world development workflow

---

## 🚀 Submission

Submit:

* GitHub repository link
* Screenshot of successful CI run
* Short explanation (3–5 sentences)

---


2

# 🧪 Assignment (Level 2): LLM Web App with CI/CD Pipeline

## 🎯 Objective

In this assignment, you will:

* Build a **web-based LLM application**
* Structure your project professionally
* Write **better tests (including API mocking)**
* Set up a **multi-step CI/CD pipeline**
* Simulate a **real deployment workflow**

---

## 🧠 Project Description

You will create a **web chatbot app** using an LLM API.

The app should:

* Accept user input from a web page
* Send it to an LLM
* Display the response

---

## 🧱 Tech Stack

* Backend: Python + Flask
* Testing: pytest
* CI/CD: GitHub Actions
* API: OpenAI API

---

## 📁 Project Structure

```
project/
│── app/
│ ├── main.py
│ ├── llm.py
│── tests/
│ ├── test_llm.py
│── requirements.txt
│── .github/workflows/ci.yml
│── README.md
```

---

## 🛠️ Step 1: Build the Flask App

### `app/main.py`

```python
from flask import Flask, request, jsonify
from llm import ask_llm

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
data = request.json
prompt = data.get("prompt", "")
response = ask_llm(prompt)
return jsonify({"response": response})

if __name__ == "__main__":
app.run(debug=True)
```

---

### `app/llm.py`

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt):
response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[{"role": "user", "content": prompt}]
)
return response.choices[0].message.content
```

---

## 🧪 Step 2: Add Proper Tests (Mock API)

### `tests/test_llm.py`

```python
from app.llm import ask_llm

def test_llm_mock(monkeypatch):
class MockResponse:
class Choice:
class Message:
content = "mocked response"
message = Message()
choices = [Choice()]

def mock_create(*args, **kwargs):
return MockResponse()

monkeypatch.setattr(
"app.llm.client.chat.completions.create",
mock_create
)

result = ask_llm("Hello")
assert result == "mocked response"
```

---

## 📦 Step 3: Requirements File

### `requirements.txt`

```
flask
openai
pytest
```

---

## ⚙️ Step 4: Advanced CI/CD Pipeline

Create:

```
.github/workflows/ci.yml
```

```yaml
name: LLM App CI/CD

on:
push:
branches: [ "main", "dev" ]
pull_request:

jobs:
test:
runs-on: ubuntu-latest

steps:
- name: Checkout code
uses: actions/checkout@v3

- name: Set up Python
uses: actions/setup-python@v4
with:
python-version: "3.10"

- name: Install dependencies
run: |
pip install -r requirements.txt

- name: Run tests
run: pytest

build:
needs: test
runs-on: ubuntu-latest

steps:
- name: Build step
run: echo "Building app..."

deploy:
needs: build
runs-on: ubuntu-latest

steps:
- name: Deploy step
run: echo "Deploying to staging..."
```

---

## 🔐 Step 5: Environment Variables

In GitHub:

* Go to Settings → Secrets
* Add:

* `OPENAI_API_KEY`

---

## 🌐 Step 6: Test the API Locally

Run:

```bash
python app/main.py
```

Test with:

```bash
curl -X POST http://127.0.0.1:5000/chat \
-H "Content-Type: application/json" \
-d '{"prompt":"Hello"}'
```

---

## ✅ Expected Outcome

* Web API works locally
* Tests pass using mocked LLM
* CI/CD pipeline runs:

* Test → Build → Deploy
* No API key exposed in code

---

## 📊 Evaluation Criteria

* ✔️ Clean project structure
* ✔️ Flask API works
* ✔️ Proper test mocking
* ✔️ CI/CD pipeline with multiple jobs
* ✔️ Secure API key usage

---

## 🌱 Bonus (Optional)

* Add a frontend (HTML/JS)
* Add logging
* Deploy to:

* Render
* Vercel (frontend only)

---

## 💡 Learning Outcomes

You will learn:

* Building real LLM-powered apps
* API design with Flask
* Mocking external APIs in tests
* Multi-stage CI/CD pipelines
* Production-like workflows

---

## 🚀 Submission

Submit:

* GitHub repository link
* Screenshot of CI pipeline success
* API test result (curl or Postman)
* Short explanation (5–7 sentences)

---


