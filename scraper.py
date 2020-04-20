import discord

client = discord.Client()

# Runs when the program is started
@client.event
async def on_ready():
    # Define which channel I want to scrape. The bot will automatically generate the server
    channel = client.get_channel(CHANNEL ID (as an int))
    # Iterate through every message in the channel
    async for message in channel.history(oldest_first=True):
        # If the message isn't an empty string...
        if len(message.content) > 0:
            # Print the message
            print(message.content)

# Actually run the program
client.run(BOT TOKEN (as a str))
