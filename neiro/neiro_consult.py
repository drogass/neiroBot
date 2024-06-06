import requests

async def get_sovet(message_text):
    prompt = {
        "modelUri": "gpt://b1gkbkunfo0mj3gav2sv/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Ты - можешь дать хорший совет в любой ситуации"
            },
            {
                "role": "user",
                "text": message_text
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVN1rNjmRApcQLqS1wmAbHX5-LUOwtUdtl2H4iB"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()

    # Print the entire response for debugging
    print("Full API response:", result)

    # Check if 'result' key is in the response
    if 'result' in result and 'alternatives' in result['result']:
        return result['result']['alternatives'][0]['message']['text']
    else:
        error_message = "Error: 'result' key not found in the response or 'alternatives' key missing in 'result'"
        print(error_message)
        if 'error' in result:
            error_message += f"\nAPI Error: {result['error']}"
        return error_message
