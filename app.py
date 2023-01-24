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
def generate_response(message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=(f"{message}\n"),
            max_tokens=3000, # Max Tokens in any request is 4000, but the prompt also takes up tokens. If you want a larger prompt and smaller response, shrink this.
            temperature=0.5,
            top_p=1
        )
    except openai.exceptions.OpenAiError as e:
        if debug:
            print("Error Occured: ",e)
        return None
    if debug:
        print("API Response: ", json.dumps(response, indent=2))
    return response.choices[0].text

# Event listener for when a message is received on Discord
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    lowercase_content = message.content.lower()
    if lowercase_content.startswith(f"hey {bot_name}") \
        and str(message.channel.id) == str(channel_id):
        if debug:
            print("Original prompt: ", message.content)
        message_parts = lowercase_content.split(f"hey {bot_name}")
        new_prompt = message_parts[1].lstrip()
        response = generate_response(new_prompt)
        if response:
            await message.channel.send(response)
        if debug:
            print("Prompt: ", new_prompt)

client.run(discord_bot_token)
