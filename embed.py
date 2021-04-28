import discord
import asyncio

async def create_anime_embed(title, url, synopsis, image_url, score, episodes, aired, members, rated, ctx):
    embed = discord.Embed(title = title, url = url, description = synopsis, color = 0xff0000)
    embed.set_thumbnail(url = image_url)
    embed.add_field(name="Score", value=score, inline=True)
    embed.add_field(name="Rated", value=rated, inline=True)
    embed.add_field(name="Aired", value=aired, inline=False)
    embed.add_field(name="Members", value=members, inline=True)
    embed.add_field(name="Episodes", value=episodes, inline=True)
    await ctx.send(embed = embed)

async def create_anime_list_embed(response_list, ctx):
    description_text = "Message the desired number to select the anime you are looking for from this list"
    embed = discord.Embed(title = "Search Results", description = description_text, color = 0xff0000)

    for i in range(len(response_list)):
        embed.add_field(name = f"{i+1})", value = f"{response_list[i]['title']}", inline = False)

    await ctx.send(embed = embed)

async def create_schedule_list_embed(anime_list, day, ctx):
    embed = discord.Embed(title = f"Schedule for {day.capitalize()}", color=0xff0000)

    for i in range(len(anime_list)):
        mal_id = anime_list[i]["mal_id"]
        url = f"https://myanimelist.net/anime/{mal_id}/"
        title = anime_list[i]["title"]
        score = anime_list[i]["score"]

        embed.add_field(name = title, value = url, inline = True)
        embed.add_field(name = "score", value = score, inline = True)
        embed.add_field(name = "\u200b" , value = "\u200b", inline = False)

    await ctx.send(embed = embed)

async def create_user_top_embed(anime_title_list, anime_score_list, url, ctx):
    embed = discord.Embed(title = "Top Anime of User", url = url, color = 0xff0000)

    for i in range(len(anime_title_list)):
        anime_title = anime_title_list[i]
        score = anime_score_list[i]

        embed.add_field(name = f"{i+1}) {anime_title}", value = f"Score: {score}", inline = False)

    await ctx.send(embed = embed)

async def create_user_anime_detail(url, title, image_url, username, watch_status, watched_episodes, total_episodes, score_given, ctx):
    embed = discord.Embed(title=title, url=url, description = f"Anime in {username}'s list", color=0xff0000)
    embed.set_thumbnail(url=image_url)
    embed.add_field(name = "Watch Status", value = watch_status, inline = True)
    embed.add_field(name = "Score", value = score_given, inline = True)
    embed.add_field(name = "Episodes", value = f"{watched_episodes}/{total_episodes}", inline= False)

    await ctx.send(embed=embed)