import discord
import asyncio

async def create_anime_embed(title, url, synopsis, image_url, score, episodes, aired, members, rated, ctx):
    embed=discord.Embed(title=title, url=url, description=synopsis, color=0xff0000)
    embed.set_thumbnail(url=image_url)
    embed.add_field(name="Score", value=score, inline=True)
    embed.add_field(name="Rated", value=rated, inline=True)
    embed.add_field(name="Aired", value=aired, inline=False)
    embed.add_field(name="Members", value=members, inline=True)
    embed.add_field(name="Episodes", value=episodes, inline=True)
    await ctx.send(embed=embed)

async def create_anime_list_embed(response_list, ctx):
    description_text = "Message the desired number to select the anime you are looking for from this list"
    embed = discord.Embed(title = "Search Results", description = description_text, color=0xff0000)

    for i in range(len(response_list)):
        embed.add_field(name=f"{i+1})", value = f"{response_list[i]['title']}", inline=False)
    
    await ctx.send(embed = embed)

async def create_schedule_list_embed(anime_list, day, ctx):
    embed = discord.Embed(title = f"Schedule for {day}", color=0xff0000)

    for i in range(len(anime_list)):
        mal_id = anime_list[i]["mal_id"]
        url = f"https://myanimelist.net/anime/{mal_id}/"
        title = anime_list[i]["title"]
        score = anime_list[i]["score"]

        embed.add_field(name=title, value = url, inline=True)
        embed.add_field(name = "score", value = score, inline = True)
        embed.add_field(name = "\u200b" , value = "\u200b", inline = False)
    
    await ctx.send(embed = embed)