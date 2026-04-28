import os
import ssl
import httpx
from anthropic import Anthropic

# Create SSL context that doesn't verify certificates
# Needed because company firewall intercepts SSL traffic
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Create HTTP client with our custom SSL context
http_client = httpx.Client(verify=ssl_context)

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    http_client=http_client
)


def ask_llm(prompt):
    """Send a prompt to the LLM and return the response."""
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


if __name__ == "__main__":
    user_input = input("Ask something: ")
    print(ask_llm(user_input))

#testing new commit for ci
# re testing
