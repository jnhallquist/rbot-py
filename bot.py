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

    if message.author == client.user:
        return
    
    if message.content.startswith('$rbot set reminder'):
        def check(m):
          return m.content

        await message.author.send('What is the reminder you would like to set?')
        msg = await client.wait_for('message', check=check)
        reminder_content = msg.content

        await message.author.send('When would you like to be reminded?')
        msg = await client.wait_for('message', check=check)
        reminder_datetime = msg.content

        print((reminder_content, reminder_datetime))

client.run(secrets["bot_token"])
