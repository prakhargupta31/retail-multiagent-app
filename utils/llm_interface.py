import requests

def query_mistral(prompt):
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={"model": "mistral", "prompt": prompt, "stream": False}
        )
        return response.json().get('response', 'No response from LLM.')
    except Exception as e:
        return f"LLM query failed: {e}"
