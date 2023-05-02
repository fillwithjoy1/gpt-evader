import openai

openai.api_key = open('env', 'r').read()

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": input("Hello I am EvadeGPT, how can I help you today?")}
    ]
)

print(completion.choices[0].message['content'])
