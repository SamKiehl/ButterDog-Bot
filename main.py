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

  amongus_words = ['Sus', 'sus', 'Imposter', 'imposter', 'Vent', 'vent', 
  'Vented', 'vented', 'Electrical', 'electrical', 'Admin', 'admin',
  'Airpod Shotty', 'Airpod shotty', 'airpod Shotty' 'airpod shotty', 'Sussy', 
  'sussy', 'Among Us', 'Among us', 'among Us', 'among us', 'Amoongus', 
  'amoongus', 'Among', 'among']

  if any(word in msg for word in amongus_words):
    await message.channel.send('https://i.pinimg.com/originals/82/92/9e/82929e981b875b03641ad272953d252e.png')


client.run(os.getenv('TOKEN'))