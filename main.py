# Token NzAyMjk2ODcwMzg2NjYzNDY0.GpekrB.5_w1WJJm8m9K8mbdMDhfk9pwG7xCbu0dotuWpM
# URL https://discord.com/api/oauth2/authorize?client_id=702296870386663464&permissions=8&scope=bot
# Purpose: Demonstrates how to create and connect a discord bot to a channel
# 2023-09-02, Brett Robert Vital


# Discord Bot
import os
import random
import urllib
import pafy
import discord
from apiclient.discovery import build
from discord import FFmpegPCMAudio
import asyncio

import discord
import youtube_dl

import main

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

from dotenv import load_dotenv
from discord.ext import commands

youtube_dl.utils.bug_reports_message = lambda: ''

load_dotenv()
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret_968308793038-ka7kdkjffsfjdiqm749hgsctf76pjjuu.apps.googleusercontent.com (1).json"
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
KEY = os.getenv('YOUTUBE_API_KEY')
logFile = open("apiRequest.log", "r")
requestToday = int(logFile.read())
logFile.close()
intents = discord.Intents().all()
client = discord.Client(intents=intents)
print(TOKEN)
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
videoQueue = []
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="joins a voice channel")
    async def join(self, ctx):
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            return await ctx.send('You need to be in a voice channel to use this command!')

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            vc = await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
            vc = ctx.voice_client

    @commands.command(description="streams music")
    async def play(self, ctx, *, url):
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send('Now playing: {}'.format(player.title))

    @commands.command(description="stops and disconnects the bot from voice")
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()


def setup(bot):
    bot.add_cog(Music(bot))


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
        channel = message.channel
        voice = discord.utils.get(message.guild.voice_channels, name=channel.name)
        voice_client = discord.utils.get(client.voice_clients, guild=GUILD)
        if voice_client is None:
            voice_client = await voice.connect()
        else:
            await voice_client.move_to(channel)
        if main.requestToday > 99:
            await message.channel.send(
                f'Sorry you are out of requests for the day please try again tomorrow'
            )
            return
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
        main.logFile = open("apiRequest.log", "w")
        main.requestToday = main.requestToday + 1
        main.logFile.write(f'{main.requestToday}')
        main.logFile.close()
        await play(message, url, voice_client)
        return


async def play(ctx, url, voice_client):
    await ctx.channel.send(url)
    song = pafy.new(url)
    audio = song.getbestaudio()
    source = FFmpegPCMAudio(audio.url, **FFMPEG_OPTIONS)
    voice_client.play(source)
    return

client.run(TOKEN)
