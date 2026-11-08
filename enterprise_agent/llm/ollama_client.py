def query_ollama(prompt):
    import requests

    response = requests.post("http://localhost:11434/api/generate", json={
       "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    })

    data = response.json()

    # Safe handling
    if "response" in data:
        return data["response"]
    elif "message" in data:
        return data["message"]["content"]
    elif "error" in data:
        return f"❌ Error: {data['error']}"
    else:
        return f"⚠️ Unexpected response: {data}"