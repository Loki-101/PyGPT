# PyGPT-3
Simple Python GPT-3 Discord Bot w/optional Pterodactyl Egg (**This is meant to serve as a base to customize your own version of this. It's not intended as standalone unless users are trusted; read security implications below**)

Inspiration for the Pterodactyl Egg was taken from ParkerVCP's generic Python egg. All credit to ParkerVCP for making great eggs and yolks (Docker Images that go with the Pterodactyl Eggs). https://github.com/parkervcp/eggs/tree/master/generic/python

This is as simple and efficient of a Python Discord Bot to interact with GPT-3 as I could make. I have gone over it numerous times doing things like combining if statements to improve efficiency. This is intended to be used with people you trust or as a base to create a more complex Bot. There are security issues if you use this bot as-is because I wanted to let it use Discord's Markdown Formatting to do cool stuff like this (Or attempt to; as you can see in the screenshot, the GPT-3 model of AI is not all-knowing and can make mistakes): ![image](https://user-images.githubusercontent.com/59907407/213577147-fcb07d45-40fa-4216-8301-180ca76c19c4.png)

The reason letting it format stuff like that is dangerous is because users can trick the bot into using things like @everyone or ^role myuser Admin. Some good ways to protect against this is to have the bot embed text, add checks to the code to prevent code injection techniques, and settings correct permissions for your actual Discord Bot when you invite it to your server so it can't do anything harmful. Again this is intended to serve as a base and make it easy for people to understand the code and build off of it. I even formatted the if statements to have one argument per line for readability. You have all of the control. **For reference, correct permissions for this bot currently are all three privileged intents and the bot permission with permissions added for "Send Messages" and "Read Messages/View Channels"**

The bot uses environmental variables rather than putting variables directly in the code for security reasons. The easiest way to use this bot is to give it only the permissions it needs rather than Administrator and use it in a Pterodactyl Panel Container so code injection attacks will bounce harmlessly off your isolated read-only filesystem docker container. Obviously there are countless ways to both use and improve upon this Bot depending on personal preferences.

This bot is designed to run in a specified channel only so that you can set a channel to slowmode to avoid overloading your API Key. You can get an api key at https://beta.openai.com.
The bot by default will only respond to messages that start with Hey and then the bot's name that you set in an environmental variable. Some examples:
Hey PyGPT-3, how are you doing today?
hey PyGPT-3, how are you doing today?
Hey pygpt-3 how are you doing today?

The Bot will convert the characters until the bot's name to lowercase and remove the comma if one exists, then capitalize the first character, so the actual prompt sent to the AI in these cases would just be "How are you doing today?"
