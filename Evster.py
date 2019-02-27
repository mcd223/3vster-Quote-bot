import discord
import asyncio
import random
import pickle
import os
import sys
import logging

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

logger = setup_logger('Members_Scanner', 'members_list.log')
logger.setLevel(logging.INFO)
logger.propagate = False
loggerTwo = setup_logger('Telemetry', 'commands.log')
loggerTwo.setLevel(logging.INFO)
loggerTwo.propagate = False

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Help Command: \n plz help')
    print('------')
    loggerTwo.info('Logged in as: %s ID: %s' % (client.user.name, client.user.id))
    await client.change_presence(game=discord.Game(name="plz help"))


@client.event
async def on_message(message):
    def logMembers():
        x = message.server.members
        for members in x:
            logger.info(members)
    def telemetry():
        loggerTwo.info('@ %s used: %s' %(message.author, message.content))
        logMembers()
    if message.content.startswith('plz quote'):
        messages = ["Austin ping me when your on", "Time to bandwagon Atlanta Reign", "But apex is  a bad game", "twitch.tv/3vster", "It’s Corey’s server, nty", "SINCE WHEN HAS DISCORD HAD A GIF BUTTON???",  "I made fun of someone with twitch.tv", "I hate servers *joins server 30 seconds later*", "Will why are you being so toxic? *5 minutes later* the freak are you doing you peice of shoot", "97 percent of teenagers would cry if they saw Jake Paul on a tower about to jump. If you are one of the 3 percent sitting there with popcorn, Screaming 'DO A BACKFLIP' then copy and paste this to all your discord servers.", "If you’d even stop to think for half a second it’s pretty obvious", "Maybe I have you blocked because you keep trying to ping me?", " Siberian https://upload.wikimedia.org/wikipedia/en/thumb/f/f3/Flag_of_Russia.svg/1200px-Flag_of_Russia.svg.png", "I have some more Evan quotes", "Here they are", "I PLAY WITH THEM INSTEAD OF YOU BECAUSE I WIN WITH THEM", "I’ve had him blocked since he ruined my 2s rank", "luck", "I have it too, stop pinging me Before I block you too", "@Squirtz YOUCAN GET INFINITE KEYS EVERY 10 LEVELS IS A KEY", "Trying to Carry -__('-')__-", "THE NEW HERO IN OVERWATCH SOUNDS LIKE FITZ", "One, I don’t make money from ads, two, I hit affiliate get rekt"]
        await client.send_message(message.channel, random.choice(messages))
        telemetry()
    if message.content.startswith('plz help'):
        await client.send_message(message.channel, '`plz quote`: Evan Quote \n `plz about`: about command \n `plz advert`: Adverts for Twitch.tv \n `plz id`: Tells your user id')
        telemetry()
    if message.content.startswith('plz about'):
        await client.send_message(message.channel, '```This bot is an Evan Bolten quote bot \n This bot was made by Jacob McDonnell```')
        telemetry()
    if message.content.startswith('plz advert'):
        await client.send_message(message.channel, 'twitch.tv/%s' %(message.content[11:]))
        telemetry()
    if message.content.startswith('plz restart') and message.author.id == '317026781708288024':
        telemetry()
        await client.send_message(message.channel, 'Restarting Bot...')
        restart_program()
    if message.content.startswith('plz id'):
        await client.send_message(message.channel, 'Your ID is %s' %(message.author.id))
        telemetry()
    #if message.content.startswith('plz pic'):
    #    await client.send_message(message.channel, '')
    #    telemetry()
    #if message.content.startswith('plz @'):
    #    games = ["Apex", "Rocket League", "Overwatch"]
    #    telemetry()
    if message.content.startswith('plz list'):
        x = message.server.members
        for members in x:
            await client.send_message(message.channel, "@%s" %(members))
        telemetry()

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

client.run("NTQ4NjE4MjU5MjIyNDk1MjU5.D1H9Yw.ihJz4CGZrwoJ3hB4OEjQ3i8T6KA")