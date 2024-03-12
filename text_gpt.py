from httpx import Response
from openai import OpenAI
from apikey import apikey
import os 

os.environ['OPEN_API_KEY']= apikey
#craeting client and using this client to send different commands
client =  OpenAI()
prompt = "write a poem about a cat"
#to get a response in different diff formats like to get an image, text etc chatcompletion is one such option which allow us to talk with AI

response=client.chat.completion.create()
model=" gpt-3.5-turbo"
messages={"role":"user","content": "prompt"}

#giving it models and other parameters
print("response")
print(response
      #inside thw emessssage we have response inside the message we have choices we r taking the second one