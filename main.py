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

  if message.content.startswith('$hello'):
    await message.channel.send('Buenos dias!')

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

  if any(word in msg for word in butterdog_words):
    await message.channel.send('Dog wit da butta.')

  if any(word in msg for word in pop_words):
    await message.channel.send('Watch it, mortal. (Rule #8)')

  when_words = ['When', 'when']

  if any(word in msg for word in when_words):
    await message.channel.send('We Are the World, we are the children, we are the ones who make a brighter day so let\'s start giving!')

  amongus_words = ['Sus', 'sus', 'Imposter', 'imposter', 'Vent', 'vent', 
  'Vented', 'vented', 'Electrical', 'electrical', 'Admin', 'admin', 'Sussy', 
  'sussy', 'Among Us', 'Among us', 'among Us', 'among us', 'Amoongus', 
  'amoongus', 'Among', 'among', 'Amogus', 'amogus']

  amongus_images = [
    'https://i.pinimg.com/originals/82/92/9e/82929e981b875b03641ad272953d252e.png',
    'https://cdn.vox-cdn.com/thumbor/v_UxzvgVYV-_hB0B3n7aendMadY=/1400x1400/filters:format(png)/cdn.vox-cdn.com/uploads/chorus_asset/file/21899632/yu7VuiU.png',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnqj3rL5xzvfet31gJcfYBO0jUTxJGuUgdOg&usqp=CAU',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRssTpPo2wh-s1J5_gUYNiWGRF3vZHkjt2rng&usqp=CAU',
    'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f731f9d4-b940-4360-925f-efa56ad882a8/de7sg7i-9141d7c7-d999-48ce-9068-dde4c0e06cd0.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvZjczMWY5ZDQtYjk0MC00MzYwLTkyNWYtZWZhNTZhZDg4MmE4XC9kZTdzZzdpLTkxNDFkN2M3LWQ5OTktNDhjZS05MDY4LWRkZTRjMGUwNmNkMC5qcGcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.0vJFmC1vuZzBvVLOH_qRkkg2c06CIghXBc_UkoWE-Ao',
    'https://i.pinimg.com/474x/21/04/a2/2104a29b074c41d7a58445aaf01fdb4b.jpg',
    'https://i.ytimg.com/vi/6nkxWQKH4L8/maxresdefault.jpg',
    'https://i.ytimg.com/vi/ZHkZTqyZICw/hqdefault.jpg'
  ]

  if any(word in msg for word in amongus_words):
    await message.channel.send(random.choice(amongus_images))

keep_alive()
client.run(os.getenv('TOKEN'))