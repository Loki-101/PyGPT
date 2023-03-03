# Author: Loki
# Discord: Loki_101#3580
# Email: loki@crazycoder.dev

import openai
import discord
import os
import json

debug = os.getenv("DEBUG", False)
# Convert debug to boolean if string
if debug == "true":
    debug = True
openai.api_key = os.getenv("OPENAI_API_KEY")
discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")
bot_name = os.getenv("BOT_NAME").lower()
channel_id = os.getenv("CHANNEL_ID")

if debug:
    print("Bot Name", bot_name)
    print("Debug is set to", debug)
    print("Channel ID is set to", channel_id)

# Initialize the Discord client with all intents
client = discord.Client(intents=discord.Intents.all())

# Function to generate a response to a message using the OpenAI API
def generate_response(message, identifier):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant named {bot_name}."},
                {"role": "user", "content": message},
                {"role": "assistant", "content": ""}
            ],
            max_tokens=2000,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            user=f"{identifier}"
        )
    except Exception as e:
        if debug:
            print("Error Occured: ",e)
        return e
    if debug:
        print("API Response: ", json.dumps(response, indent=2))
    return response.choices[0].message.content

# Event listener for when a message is received on Discord
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    lowercase_content = message.content.lower()
    if lowercase_content.startswith(f"hey {bot_name}"):
        print("User: ", f"{message.author.name}, {message.author.id}")
        if debug:
            print("Original Prompt: ", message.content)
        # Modify the original prompt
        prompt = message.content[len(f"hey {bot_name}"):].lstrip(", ")
        if len(prompt) > 0 and prompt[0].isalpha():
            prompt = prompt[0].upper() + prompt[1:]
        print("Prompt: ", prompt)
        # Call generate_response with the modified prompt
        response = generate_response(prompt, message.author.id)
        # Send the response
        await message.channel.send(response)

client.run(discord_bot_token)
