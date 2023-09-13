# Token NzAyMjk2ODcwMzg2NjYzNDY0.GpekrB.5_w1WJJm8m9K8mbdMDhfk9pwG7xCbu0dotuWpM
# URL https://discord.com/api/oauth2/authorize?client_id=702296870386663464&permissions=8&scope=bot
# Purpose: Demonstrates how to create and connect a discord bot to a channel
# 2023-09-02, Brett Robert Vital


# Discord Bot
import os
import random
import urllib
import webbrowser

import discord
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import youtube_dl
import json
import apiclient
import oauth2client
from apiclient.discovery import build

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

from dotenv import load_dotenv

load_dotenv()
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret_968308793038-ka7kdkjffsfjdiqm749hgsctf76pjjuu.apps.googleusercontent.com (1).json"
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
KEY = os.getenv('YOUTUBE_API_KEY')

intents = discord.Intents().all()
client = discord.Client(intents=intents)
print(TOKEN)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id:{guild.id})')
    print(len(guild.members))
    membersList = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {membersList}')


@client.event
async def on_member_join(member):
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
    channel = await client.fetch_channel(guild.id)
    await channel.send(
        f'Eat shit and die NIGGER. Welcome to hell {member.name}. The goals of this channel are to drive greens and '
        f'eat vagine!!!!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.lower().startswith('!hello'):
        await message.channel.send(
            f'Hello, {message.author}!'
        )
        return
    elif message.content.lower().startswith('!nick'):
        print(message.author)
        nicks_excuses = [
            'I have to jerk off my brother for the next 9 hours',
            'I am making food should take ten minutes (doesn\’t join for two hours)',
            'I\’m eating so I have to watch hentai to digest better',
            'I\’m chilling with my family',
            'Scouting for barn animals',
            'Cleaning out my gecko\’s asshole with my tongue',
            'I\’m being pussy cause you guys said mean words to me',
            'I wanna jerk off to hermione in hogwarts legacy',
            'I had a really hard day at my 13 dollar an hour job that is much more important and difficult than michael\’s',
            'I had to sleep in til 4pm cause I am a fat piece of garbage who peaked inside the womb',
            'I can\’t play fortnite because there are no females online',
            'I am too busy dreaming about keira and her curves to get on right now',
            'I have my cancer treatments today',
            'There is a 14 year old girl in my area who appears to be single and ready to mingle',
            'I\’m getting a haircut',
            'Sorry I just matched with keira on tinder again she says we can work it out.',
            'My mom has to drive me to school',
            'It\’s my nieces birthday tomorrow',
            ('I require myself to read 10 chapters a day but don’t know what a book is or how to read one so I end up '
             'just sticking it in my ass'),
            ('I have to be up for 12 hours straight tomorrow which will interfere with my regularly scheduled 15 hr '
             'sleep time'),
            'I am a piece of shit who is going nowhere in life',
            'I have no friends just people who enjoy shitting on me',
            'I need in to be in bed at an outrageously early time for no fucking reason because I hate my life and am '
            'nothing but a floating piece of garbage in the wind',
            'I gave my brother my hard drive for some reason',
        ]
        response = random.choice(nicks_excuses)
        await message.channel.send(response)
        return
    elif message.content.startswith('!play'):
        print('here')
        ytSearch = message.content[6:]
        print(ytSearch)
        urlformat = urllib.parse.quote(ytSearch)
        youtube = build('youtube', 'v3', developerKey=KEY)
        request = youtube.search().list(q=ytSearch, part='id', type='video')
        res = request.execute()
        videoId = res['items'][0]['id']['videoId']
        url = 'https://www.youtube.com/watch?v=' + videoId
        print(url)
        await message.channel.send(
            f'Here\'s the next video: {url}. Enjoy!'
        )

client.run(TOKEN)
