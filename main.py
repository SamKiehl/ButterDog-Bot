import discord
import random
import os
import time
from keep_alive import keep_alive
client = discord.Client()

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
  'Hi',
  '.... . .-.. .-.. ---'
  ]

sam_words = [
  'Sam',
  'sam',
  'SAM',

  'Kiehl',
  'kiehl',
  'KIEHL'
]

inrange_responses = [
  'Yeah, you\'re in range.',
  'You should probably move.',
  ':regional_indicator_r: :regional_indicator_u: :regional_indicator_n: ',
  ':thumbsdown: ',
  'Nah you\'re not in range.',
  ':thumbsup:',
  'You\'re good.',
  'No, he\'s too far.'
]

morse_letters = [
  '.-',   #0 A
  '-...', #1 B
  '-.-.', #2 C
  '-..',  #3 D
  '.',    #4 E
  '..-.', #5 F
  '--.',  #6 G
  '....', #7 H
  '..',   #8 I
  '.---', #9 J
  '-.-', #10 K
  '.-..',#11 L
  '--',  #12 M
  '-.',  #13 N
  '---', #14 O
  '.--.',#15 P
  '--.-',#16 Q
  '.-.', #17 R
  '...', #18 S
  '-',   #19 T
  '..-', #20 U
  '...-',#21 V
  '.--', #22 W
  '-..-',#23 X
  '-.--',#24 Y
  '--..',#25 Z

  '.----',  #26 1
  '..---',  #27 2
  '...--',  #28 3
  '....-',  #29 4
  '.....',  #30 5
  '-....',  #31 6
  '--...',  #32 7
  '---..',  #33 8
  '----.',  #34 9
  '-----',  #35 0

  '/',  #36 [SPACE]
]
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
pop_words = [
  'Popeye\'s', 
  'popeye\'s', 
  'Popeyes', 
  'popeyes', 
  'Chicken', 
  'chicken', 
  'Sandwich', 
  'sandwich'
]
coin_responses = [
  ':regional_indicator_h: Heads',
  ':regional_indicator_t: Tails'
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
cringe_words = [
  'Schnieder',
  'SCHNIEDER',
  'schnieder',
  'Schnieds',
  'SCHNIEDS',
  'schnieds',
  'Schneider',
  'SCHNEIDER',
  'schneider',
  'Schneids',
  'SCHNEIDS',
  'schneids'
]
when_words = [
  'When', 
  'when'
]
amongus_words = [
  'Sus', 
  'sus', 
  'Imposter', 
  'imposter', 
  'Vent', 
  'vent', 
  'Vented', 
  'vented', 
  'Electrical', 
  'electrical', 
  'Admin', 
  'admin', 
  'Sussy', 
  'sussy', 
  'Among Us', 
  'Among us', 
  'among Us', 
  'among us', 
  'Amoongus', 
  'amoongus', 
  'Among', 
  'among', 
  'Amogus', 
  'amogus'
]
amongus_responses = [
  'SUS!',
  'WHEN THE IMPOSTER IS SUS!',
  'IMPOSTER!?',
  'ඞ'
]
im_words = [
  'im ',
  'i\'m ',
  'Im ',
  'i\'m ',
  'IM ',
  'I\'M '
]
eight_ball_responses = [
  'It is certain', 
  'It is decidedly so', 
  'Without a doubt', 
  'Yes definitely', 
  'You may rely on it', 
  'As I see it, yes', 
  'Most likely', 
  'Outlook good', 
  'Yes', 
  'Signs point to yes',

  'Don\'t count on it',
  'My reply is no', 
  'My sources say no', 
  'Outlook not so good', 
  'Very doubtful',

  'Reply hazy try again', 
  'Ask again later', 
  'Better not tell you now', 
  'Cannot predict now', 
  'Concentrate and ask again'
]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if message.content.startswith('!!hello'):
    await message.channel.send(random.choice(hello_responses))

  if message.content.startswith('!!sum'):
    getrid = msg.split('!!sum ', 1)[1]
    nums = getrid.split(', ')
    output = []
    for x in range(len(nums)):
      output.append(float(nums[x]))
   

    await message.channel.send('=> ' + str(sum(output)))
  
  if message.content.startswith('!!8ball'):
    await message.channel.send(random.choice(eight_ball_responses))

  if message.content.startswith('!!hortonhearsa'):
        channel = message.channel
        this = await channel.send(random.choice(true_responses))

        def check(m):
            return m.channel == channel

        msg = await client.wait_for('message', check=check)
        await this.edit(content="Who?")
        await channel.send('Asked?')

  if message.content.startswith('!!catch'):
        channel = message.channel
        this = await channel.send(random.choice(eight_ball_responses))

        def check(m):
            return m.channel == channel

        msg = await client.wait_for('message', check=check)
        await this.edit(content="https://cdn.discordapp.com/attachments/812028715953029123/832822116067704832/j7hyEM.png")
        msg = message.content
        await channel.send('https://cdn.discordapp.com/attachments/812028715953029123/832822250355949589/oqcptj21hq151.png')
  
  if message.content.startswith('!!inrange'):
    await message.channel.send(random.choice(inrange_responses))
    time.sleep(3)
    await message.channel.send('I think.')
  
  if message.content.startswith('!!morse'):
    morse = msg.split('!!morse ', 1)[1]
    morseout = ''
    for c in range(len(morse)):
      if morse[c] == 'A' or morse[c] == 'a':
        morseout += morse_letters[0]
      elif morse[c] == 'B' or morse[c] == 'b':
        morseout += morse_letters[1]
      elif morse[c] == 'C' or morse[c] == 'c':
        morseout += morse_letters[2]
      elif morse[c] == 'D' or morse[c] == 'd':
        morseout += morse_letters[3]
      elif morse[c] == 'E' or morse[c] == 'e':
        morseout += morse_letters[4]
      elif morse[c] == 'F' or morse[c] == 'f':
        morseout += morse_letters[5]
      elif morse[c] == 'G' or morse[c] == 'g':
        morseout += morse_letters[6]
      elif morse[c] == 'H' or morse[c] == 'h':
        morseout += morse_letters[7]
      elif morse[c] == 'I' or morse[c] == 'i':
        morseout += morse_letters[8]
      elif morse[c] == 'J' or morse[c] == 'j':
        morseout += morse_letters[9]
      elif morse[c] == 'K' or morse[c] == 'k':
        morseout += morse_letters[10]
      elif morse[c] == 'L' or morse[c] == 'l':
        morseout += morse_letters[11]
      elif morse[c] == 'M' or morse[c] == 'm':
        morseout += morse_letters[12]
      elif morse[c] == 'N' or morse[c] == 'n':
        morseout += morse_letters[13]
      elif morse[c] == 'O' or morse[c] == 'o':
        morseout += morse_letters[14]
      elif morse[c] == 'P' or morse[c] == 'p':
        morseout += morse_letters[15]
      elif morse[c] == 'Q' or morse[c] == 'q':
        morseout += morse_letters[16]
      elif morse[c] == 'R' or morse[c] == 'r':
        morseout += morse_letters[17]
      elif morse[c] == 'S' or morse[c] == 's':
        morseout += morse_letters[18]
      elif morse[c] == 'T' or morse[c] == 't':
        morseout += morse_letters[19]
      elif morse[c] == 'U' or morse[c] == 'u':
        morseout += morse_letters[20]
      elif morse[c] == 'V' or morse[c] == 'v':
        morseout += morse_letters[21]
      elif morse[c] == 'W' or morse[c] == 'w':
        morseout += morse_letters[22]
      elif morse[c] == 'X' or morse[c] == 'x':
        morseout += morse_letters[23]
      elif morse[c] == 'Y' or morse[c] == 'y':
        morseout += morse_letters[24]
      elif morse[c] == 'Z' or morse[c] == 'z':
        morseout += morse_letters[25]

      elif morse[c] == '1':
        morseout += morse_letters[26]
      elif morse[c] == '2':
        morseout += morse_letters[27]
      elif morse[c] == '3':
        morseout += morse_letters[28]
      elif morse[c] == '4':
        morseout += morse_letters[29]
      elif morse[c] == '5':
        morseout += morse_letters[30]
      elif morse[c] == '6':
        morseout += morse_letters[31]
      elif morse[c] == '7':
        morseout += morse_letters[32]
      elif morse[c] == '8':
        morseout += morse_letters[33]
      elif morse[c] == '9':
        morseout += morse_letters[34]
      elif morse[c] == '0':
        morseout += morse_letters[35]
      elif morse[c] == ' ' or morse[c] == '_':
        morseout += morse_letters[36]
      morseout += ' '
      ++c

    await message.channel.send(morseout)

  
  if message.content.startswith('!!coin'):
    await message.channel.send(random.choice(coin_responses))

  if message.content.startswith('!!d'):
    dnum = int(msg.split('!!d', 1)[1])
    await message.channel.send(random.randint(1, dnum))

  if message.content.startswith('!!d'):
    dnum = int(msg.split('!!d ', 1)[1])
    await message.channel.send(random.randint(1, dnum))

  if any(word in msg for word in butterdog_words):
      await message.channel.send('Dog wit da butta.')

  if any(word in msg for word in im_words):
    for word in im_words:
      if msg.find(word) != -1:
        x = word
        im = msg.split(x, 1)[1]
    await message.channel.send('Hi ' + im + ' , i\'m dad!')

  if any(word in msg for word in pop_words):
      await message.channel.send('Watch it, mortal. (Rule #8)')

  if any(word in msg for word in true_words):
      await message.channel.send(random.choice(true_responses))

  if any(word in msg for word in cringe_words):
      await message.channel.send(':face_vomiting:')


  if any(word in msg for word in when_words):
    await message.channel.send('We Are the World, we are the children, we are the ones who make a brighter day so let\'s start giving!')

  if any(word in msg for word in amongus_words):
    await message.channel.send(random.choice(amongus_responses))

keep_alive()
client.run(os.getenv('TOKEN'))