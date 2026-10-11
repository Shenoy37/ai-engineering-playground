import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

#load the .env file
load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
        raise ValueError("API key not found")
client  = Groq(api_key=my_api_key)
model = "openai/gpt-oss-20b"

role ="user"
prompt = "Who is sidshe37 on medium blogging site"

message = {"role":role, "content":prompt}

messages =[message]

# making the api call 
response  = client.chat.completions.create(model = model, messages = messages)
ans = response.choices[0].message.content
print(ans)




