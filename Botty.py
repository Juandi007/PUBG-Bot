import discord
import asyncio

from pypubg import core

# Connect to PUBG API
pubg = core.PUBGAPI('698f74e1-4159-4f6e-87d0-4366b611c85d')

# Connect to Discord API
client = discord.Client()

# Botty!
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	# !test command
	# Send 'Hello, world!' message in channel
    if message.content.startswith('!test'):
    	await client.send_message(message.channel, 'Hello, world!')

    # !pubg command
    # Send player's kill count in the specified game mode
    # Usage: '!pubg-<playerName>-<gameMode>'
    if message.content.startswith('!pubg'):
    	player = message.content.split('-')[1];
    	mode = message.content.split('-')[2];

    	stats = api.player_mode_stats(player, mode, game_region='na')

    	sendThis = player + " kills : " + str(stats[0]['Stats'][21]['ValueInt'])

    	await client.send_message(message.channel, sendThis)

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

# Run Botty
client.run('MzM5MTc2MTk4OTkzMzQ2NTYx.DFgMBQ.J29F-7ikmvEiNhTqsL9PsrDGxKE')