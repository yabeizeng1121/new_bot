import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Retrieve the API token and URL from environment variables
API_TOKEN = os.getenv("API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"

# Set up the authorization headers
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def test_api_response():
    """Test that the Hugging Face API returns a valid response for a sample query."""
    # Define a sample payload with a question and context
    sample_payload = {
        "inputs": {
            "question": "Who is the president of the United States?",
            "context": "The current president of the United States is Joe Biden.",
        }
    }

    # Make a POST request to the API
    response = requests.post(API_URL, headers=headers, json=sample_payload)

    # Check that the response status code is 200 (OK)
    assert response.status_code == 200, "API did not return a successful response."

    # Optionally, check that the response contains an expected key, such as 'answer'
    response_data = response.json()
    assert "answer" in response_data, "API response does not contain 'answer' key."


# If you're running this file directly, execute the test
if __name__ == "__main__":
    test_api_response()
