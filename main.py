import os
import requests
import random
import discord
import asyncio
import time
from dotenv.main import load_dotenv
from discord.ext import commands

from anime import *
from embed import *
from user import *

bot = commands.Bot(command_prefix="m.")

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print("Connected to discord")

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please input the required argument")
  elif isinstance(error, commands.CommandNotFound):
    await ctx.send("Command not found")
  elif isinstance(error, commands.CommandOnCooldown):
    await ctx.send("Please wait for cooldown to end")

# async def on_message(message):
#     await bot.process_commands(message)
#     content = message.content

@bot.command(name="searchanime", help="Seaches through the MAL Database to find an anime. Requires a Title to search")
async def search(ctx, *, query):
  await search_anime(bot, ctx, query, "detail")

@bot.command(name="schedule", help="prints the titles of anime that are airing on a given day at JST time")
async def schedule(ctx, day):
  day.lower
  await show_schedule(ctx, day)

@bot.command(name="stats", help="sends a graph of the scores and watch types of an anime")
async def stats(ctx, *, query):
  await search_anime(bot, ctx, query, "stats")

@bot.command(name="usercheck", help="Profile of User")
async def userprofile(ctx, *, query):
  tempQ = query
  username = tempQ.split()[0]
  query = query.split(None, 1)[1]
  await search_anime(bot, ctx, query, "usercheck", username)

@bot.command(name="topuser", help="List of Top Anime for User")
async def topuser(ctx, username):
  await get_completed_user_list(ctx, username, "top")

bot.run(TOKEN)
