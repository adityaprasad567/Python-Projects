import os

from groq import Groq

client = Groq(
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)