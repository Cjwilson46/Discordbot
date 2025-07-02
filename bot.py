import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from feeds import get_news

# Load tokens
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

# Set up bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    if not news_loop.is_running():
        news_loop.start()

@tasks.loop(hours=24)
async def news_loop():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        news = get_news()
        for chunk in [news[i:i+2000] for i in range(0, len(news), 2000)]:
            await channel.send(chunk)
    else:
        print("⚠️ Channel not found.")

@bot.command()
async def news(ctx):
    news = get_news()
    for chunk in [news[i:i+2000] for i in range(0, len(news), 2000)]:
        await ctx.send(chunk)

bot.run(TOKEN)
