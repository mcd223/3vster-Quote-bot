import discord
import asyncio
import random
import pickle
import os
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Help Command: \n plz help')
    print('This bot was made by Jacob McDonnell')
    await client.change_presence(game=discord.Game(name="plz help"))

@client.event
async def on_message(message):
    if message.content.startswith('plz quote'):
        messages = ["Austin ping me when your on", "Time to bandwagon Atlanta Reign", "But apex is  a bad game", "twitch.tv/3vster", "It’s Corey’s server, nty", "SINCE WHEN HAS DISCORD HAD A GIF BUTTON???",  "I made fun of someone with twitch.tv", "I hate servers joins server 30 seconds later", "Will why are you being so toxic? 5 minutes later the freak are you doing you peice of shoot", "97% of teenagers would cry if they saw Jake Paul on a tower about to jump. If you are one of the 3% sitting there with popcorn, Screaming 'DO A BACKFLIP' then copy and paste this to all your discord servers.", "If you’d even stop to think for half a second it’s pretty obvious", "Maybe I have you blocked because you keep trying to ping me?", "https://cdn.discordapp.com/attachments/347164838524616704/548608108453167105/2012081215373021Flag_of_Russia.png Siberian",]
        await client.send_message(message.channel, random.choice(messages))
    if message.content.startswith('plz help'):
        await client.send_message(message.channel, 'plz quote: Evan Quote \n plz about: about command')
    if message.content.startswith('plz about'):
        await client.send_message(message.channel, 'This bot is an Evan Bolten quote bot \n This bot was made by Jacob McDonnell')	
client.run("NTQ4NjE4MjU5MjIyNDk1MjU5.D1H9Yw.ihJz4CGZrwoJ3hB4OEjQ3i8T6KA")
