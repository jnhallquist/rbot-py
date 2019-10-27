import discord
import json

with open('secrets.json') as json_data:
    secrets = json.load(json_data)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$rbot help'):
        await message.author.send('TBA: HELP INFORMATION')

client.run(secrets["bot_token"])
