import discord
import os
import random

TOKEN = 'token' #put your token here

client = discord.Client()

@client.event
async def on_ready():
    #sets Wiggles' online game status
    print("Mew!")
    await client.change_presence(activity=discord.Game(name="Looking for treats"))

@client.event
async def on_message(message):
    #so the bot doesn't talk to itself
    if message.author == client.user:
        return

    #gives users a list  of valid commands
    if message.content.startswith('!wiggles help'):
        await message.channel.send('Meow! I heard you need help. Here are a list of valid commands:')
        await message.channel.send('!wiggles')
        await message.channel.send('!wiggles pic')
        await message.channel.send('You can also say hi wiggles, I love wiggles, or just say her name on its own.')
    #says hi if user types !wiggles command or says wiggles
    if message.content.startswith('wiggles'):
        await message.channel.send('Meow')
    if message.content.startswith('!wiggles'):
        await message.channel.send('Meow')
    if message.content.startswith('hi wiggles'):
        await message.channel.send('Meow')

    #sending a random cat picture
    if message.content.startswith('!wiggles pic'):
        imgList = os.listdir("dir goes here") #put your own local file path here
        imgString = random.choice(imgList)
        path = "dir here followed by /" + imgString #put the same local file path followed by /
        await message.channel.send(file=discord.File(path))

    #sending a <3
    if message.content.startswith('I love wiggles'):
        await message.channel.send(':heart:')
    if message.content.startswith('I love Wiggles'):
        await message.channel.send(':heart:')



client.run("token") #your token goes here
