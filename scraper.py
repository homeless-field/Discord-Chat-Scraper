import discord

client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL ID INT)
    async for message in channel.history(oldest_first=True):
        if len(message.content) > 0:
            print(message.content)

client.run(BOT TOKEN STR)
