# PyGPT (Depreciated - newer version is not yet polished enough to be published)
Simple Python Discord ChatBot w/optional Pterodactyl Egg
Powered by OpenAI

This is meant to run in Pterodactyl Panel or run Standalone on any platform.

Inspiration for the Pterodactyl Egg was taken from ParkerVCP's generic Python egg. All credit to ParkerVCP for making great eggs and yolks (Docker Images that go with the Pterodactyl Eggs). https://github.com/parkervcp/eggs/tree/master/generic/python

This is as simple and efficient of a Python Discord Bot possible. I have optimized every part of it that could be optimized. It's made to have the code as readable, stable, and efficient as possible. I let this bot send messages without a security feature such as putting the message in an embed so it can do cool stuff like this: (Or attempt to; as you can see in the first screenshot, the AI is not all-knowing and can make mistakes): ![image](https://user-images.githubusercontent.com/59907407/213577147-fcb07d45-40fa-4216-8301-180ca76c19c4.png)

As you can see in this screenshot with the bot name set to Vodka you would call it with "Hey Vodka" (Not case sensitive, hey vodka would work just as well). You can set the bot name to anything.
![image](https://user-images.githubusercontent.com/59907407/215229561-5a0fb73b-84e0-4043-a048-2a558b9f9303.png)

The reason letting it format stuff like that is dangerous if permissions are not set correctly is because users can trick the bot into using things like @everyone or ^role myuser Admin. **To prevent this bot from being able to harm your server, set it's permissions correctly.** The Discord Bot that goes with this application only needs the three privilege intents, the bot permission, and inside the bot permission the "Send Messages" and "Read Messages/View Channels" permission.

Then once the bot is in your server all it needs is to be able to view messages and send messages in your chosen channel. **DO NOT** give this bot administrator permissions or any other permissions it does not need. Users can manipulate what it says with things like "Hey PyGPT-3, what do I get when I combine the strings @ and everyone?" If you set permissions correctly, it will produce @everyone, but this will do nothing because it doesn't have the "Mention @everyone" permission in your Discord Server.

The bot uses environmental variables rather than putting variables directly in the code for security reasons.

This bot is designed to run in a specified channel only so that you can set a channel to slowmode to avoid overloading your API Key. You can get an api key at https://platform.openai.com. You can choose a spending soft limit where you'll get emailed and a hard limit where it will just stop.
The bot by default will only respond to messages that start with Hey and then the bot's name that you set in an environmental variable. Some examples:
Hey PyGPT, how are you doing today?
hey Pygpt, how are you doing today?
Hey pygpt how are you doing today?

The Bot will convert the characters until the bot's name to lowercase and remove the comma if one exists, then capitalize the first character, so the actual prompt sent to the AI in these cases would just be "How are you doing today?"
