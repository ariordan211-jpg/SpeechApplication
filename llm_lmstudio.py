import requests
import json

LMSTUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"


def ask_llm(prompt, model="mistral-7b-instruct", timeout=60):
    headers = {"Content-Type": "application/json"}

    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        r = requests.post(
            LMSTUDIO_URL,
            headers=headers,
            json=data,
            timeout=timeout
        )

        # Try to parse JSON; if invalid, show raw text
        try:
            result = r.json()
        except Exception:
            print("❌ LLM Error: invalid JSON response:", r.text)
            return ""

        # Non-200 status -> print body for diagnosis
        if r.status_code != 200:
            print("❌ LLM HTTP Error:", r.status_code, r.text)
            return ""

        # OpenAI-style: {choices: [{message: {content: ...}}]}
        if isinstance(result, dict) and "choices" in result and result["choices"]:
            choice = result["choices"][0]
            if isinstance(choice, dict) and "message" in choice and "content" in choice["message"]:
                reply = choice["message"]["content"]
                print(f"\n🤖 AI: {reply}")
                return reply
            if isinstance(choice, dict) and "text" in choice:
                reply = choice["text"]
                print(f"\n🤖 AI: {reply}")
                return reply

        # Common LM Studio / other formats: outputs -> content/data
        if isinstance(result, dict) and "outputs" in result and result["outputs"]:
            out0 = result["outputs"][0]
            # Check common fields
            if isinstance(out0, dict):
                # nested data list
                if "data" in out0:
                    data_items = out0["data"]
                    # try to find a text field
                    for item in data_items:
                        if isinstance(item, dict):
                            if "text" in item:
                                reply = item["text"]
                                print(f"\n🤖 AI: {reply}")
                                return reply
                            if item.get("type") in ("output_text", "text") and "text" in item:
                                reply = item["text"]
                                print(f"\n🤖 AI: {reply}")
                                return reply
                # content may be list or string
                if "content" in out0:
                    content = out0["content"]
                    if isinstance(content, list):
                        for c in content:
                            if isinstance(c, dict) and "text" in c:
                                reply = c["text"]
                                print(f"\n🤖 AI: {reply}")
                                return reply
                    elif isinstance(content, str):
                        reply = content
                        print(f"\n🤖 AI: {reply}")
                        return reply
                if "generated_text" in out0:
                    reply = out0["generated_text"]
                    print(f"\n🤖 AI: {reply}")
                    return reply

        # Fallback: print the whole response for diagnosis
        print("❌ LLM Error: unexpected response structure:")
        print(json.dumps(result, indent=2))
        return ""

    except Exception as e:
        print("❌ LLM Error:", e)
        return ""
