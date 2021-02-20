import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user and not message.content.startswith('-'):
    return

  msg = message.content

  if message.content.startswith('$hello'):
    await message.channel.send('Buenos dias!')

  pop_words = ['Popeye\'s', 'popeye\'s', 'Popeyes', 'popeyes', 'Chicken', 'chicken', 'Sandwich', 'sandwich']

  if any(word in msg for word in pop_words):
   await message.channel.send('Watch it, mortal. (Rule #8)')

  when_words = ['When', 'when']

  if any(word in msg for word in when_words):
    await message.channel.send('We Are the World, we are the children, we are the ones who make a brighter day so let\'s start giving!')

client.run(os.getenv('TOKEN'))