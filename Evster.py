import discord
import asyncio
import random
import pickle
import os
import sys
import logging
import re

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
loggerID = setup_logger('ID', 'ID.log')
loggerID.setLevel(logging.INFO)
loggerID.propagate = False

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
            logger.info("%s ID: %s" %(members, members.id))
    def telemetry():
        loggerTwo.info('@ %s used: %s' %(message.author, message.content))
        logMembers()
    def logID():
        open('ID.log', 'w').close()
        x = message.server.members
        for members in x:
            loggerID.info(members.id)
    if message.content.startswith('plz quote'):
        await client.send_message(message.channel, random.choice(open('quotes.txt').readlines()))
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
        print("Restarting Bot...")
        print('------')
        await client.send_message(message.channel, 'Restarting Bot...')
        restart_program()
    if message.content.startswith('plz id'):
        await client.send_message(message.channel, 'Your ID is %s' %(message.author.id))
        telemetry()
    #if message.content.startswith('plz pic'):
    #    await client.send_message(message.channel, '')
    #    telemetry()
    if message.content.startswith('plz mention'):
        logID()
        games = ["Apex", "Rocket League", "Overwatch"]
        id = random.choice(open('ID.log').readlines())[32:].rstrip()
        msg = '<@!%s> do you want to play %s' %(id ,random.choice(games))
        await client.send_message(message.channel, msg)
        telemetry()
    if message.content.startswith('plz list'):
        x = message.server.members
        for members in x:
            await client.send_message(message.channel, members)
        telemetry()
    if message.content.startswith('ping'):
        for user in message.mentions:
            msg = 'PONG {}'.format(user.mention)
            await client.send_message(message.channel, msg)
    if message.content.startswith('mention everyone') and message.author.id == '317026781708288024':
        x = message.server.members
        for members in x:
            msg = 'PONG {}'.format(members.mention)
            await client.send_message(message.channel, msg)
async def on_member_join(member):
    server = member.server
    games = ["Apex", "Rocket League", "Overwatch"]
    fmt = '{0.mention} do you want to play %s' %(random.choice(games))
    await client.send_message(server, fmt.format(member, server))
    
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)

client.run("NTQ4NjE4MjU5MjIyNDk1MjU5.D1H9Yw.ihJz4CGZrwoJ3hB4OEjQ3i8T6KA")