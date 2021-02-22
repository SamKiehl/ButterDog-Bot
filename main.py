import discord
import random
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  hello_responses = [
    'Bonjour',
    'Buenos Dias',
    'Hola',
    'Privet',
    'Nǐ hǎo',
    'Ciao',
    'Konnichiwa',
    'Guten Tag',
    'Hallo',
    'Hej',
    'Shalom',
    'Hi'
  ]

  if message.content.startswith('!!hello'):
    await message.channel.send(random.choice(hello_responses))

  pop_words = ['Popeye\'s', 'popeye\'s', 'Popeyes', 'popeyes', 'Chicken', 'chicken', 'Sandwich', 'sandwich']

  butterdog_words = [
    'Butter Dog',
    'Butter dog',
    'butter Dog',
    'butter dog',
    'ButterDog',
    'Butterdog',
    'butterDog',
    'butterdog',
    'Budda Dog',
    'Budda dog',
    'budda Dog',
    'budda dog'
  ]

  true_words = [
    'TRUE',
    'TRUE!',
    'True',
    'True!',
    'true',
    'true!',
    '!!TRUE!!'
  ]

  true_responses = [
    'TRUE',
    'TRUE!',
    'True',
    'True!',
    'true',
    'true!',
    'I wholeheartedly agree!',
    'Factual',
    '!False!',
    'BASED!',
    'Based!',
    'REDPILLED!'
  ]

  if any(word in msg for word in butterdog_words):
    await message.channel.send('Dog wit da butta.')

  if any(word in msg for word in pop_words):
    await message.channel.send('Watch it, mortal. (Rule #8)')

  if any(word in msg for word in true_words):
      await message.channel.send(random.choice(true_responses))

  when_words = ['When', 'when']

  if any(word in msg for word in when_words):
    await message.channel.send('We Are the World, we are the children, we are the ones who make a brighter day so let\'s start giving!')

  amongus_words = ['Sus', 'sus', 'Imposter', 'imposter', 'Vent', 'vent', 
  'Vented', 'vented', 'Electrical', 'electrical', 'Admin', 'admin', 'Sussy', 
  'sussy', 'Among Us', 'Among us', 'among Us', 'among us', 'Amoongus', 
  'amoongus', 'Among', 'among', 'Amogus', 'amogus']

  amongus_images = [
    'SUS!'
    'WHEN THE IMPOSTER IS SUS!'
    'IMPOSTER!?'
  ]

  if any(word in msg for word in amongus_words):
    await message.channel.send(random.choice(amongus_images))

keep_alive()
client.run(os.getenv('TOKEN'))