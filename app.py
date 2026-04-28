import os
from flask import Flask, request, jsonify, render_template_string
from anthropic import Anthropic

# Create Flask web app
app = Flask(__name__)

# Create Anthropic client
# No SSL bypass needed on Render - only needed on company network
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def ask_llm(prompt):
    """Send a prompt to the LLM and return the response."""
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


# HTML page for the chatbot UI
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>LLM Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 { color: #333; text-align: center; }
        form { display: flex; gap: 10px; margin: 20px 0; }
        input[type="text"] {
            flex: 1;
            padding: 12px;
            font-size: 16px;
            border: 2px solid #ddd;
            border-radius: 8px;
        }
        button {
            padding: 12px 24px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
        }
        button:hover { background-color: #45a049; }
        .answer {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #ddd;
            margin-top: 20px;
            white-space: pre-wrap;
        }
        .label { font-weight: bold; color: #555; }
    </style>
</head>
<body>
    <h1>LLM Chatbot</h1>
    <form method="POST">
        <input type="text" name="question" placeholder="Ask something..." required>
        <button type="submit">Ask</button>
    </form>
    {% if answer %}
    <div class="answer">
        <span class="label">Answer:</span><br><br>
        {{ answer }}
    </div>
    {% endif %}
</body>
</html>
"""


# Route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    if request.method == "POST":
        question = request.form["question"]
        answer = ask_llm(question)
    return render_template_string(HTML_PAGE, answer=answer)


# API endpoint
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data["question"]
    answer = ask_llm(question)
    return jsonify({"answer": answer})


# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


#testing
