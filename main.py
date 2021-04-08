import os
import requests
import random
import discord
import asyncio
import time
from discord.ext import commands
from mal import *
from anime import *
from embed import *

bot = commands.Bot(command_prefix="m.")

TOKEN = "DUMMY TOKEN"

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
  else:
    pass

# async def on_message(message):
#     await bot.process_commands(message)
#     content = message.content

@bot.command(name="searchanime", help="Seaches through the MAL Database to find an anime. Requires a Title to search")
async def search(ctx, *, query):
  await search_anime(bot, ctx, query)

@bot.command(name="schedule", help="prints the titles of anime that are airing on a given day at JST time")
async def schedule(ctx, day):
  day.lower
  await show_schedule(ctx, day)



bot.run(TOKEN)