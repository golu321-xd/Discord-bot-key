import discord
from discord.ext import commands
import requests
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")  # render environment variable
BACKEND_URL = os.getenv("BACKEND_URL")  # render environment variable

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def getkey(ctx):
    username = ctx.author.name  # discord username use hoga

    response = requests.post(f"{BACKEND_URL}/getkey", json={"username": username})
    data = response.json()

    key = data['key']
    expiry = data['expiry']

    await ctx.author.send(f"✨ **Your Key:** `{key}`\n⏳ **Valid Till:** `{expiry}`")
    await ctx.send(f"{ctx.author.mention} check your DM!")

bot.run(TOKEN)
