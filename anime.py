import discord
import requests
from embed import *

headers = {
    'x-rapidapi-key': "2ed26cb89emsh2b7cb079ec42fd9p15290cjsne485ef05078a",
    'x-rapidapi-host': "jikan1.p.rapidapi.com"
}


async def show_schedule(ctx, day):
    url = f"https://jikan1.p.rapidapi.com/schedule/{day}"
    response = requests.request("GET", url, headers=headers)
    print(response.text)


async def search_anime(bot, ctx, query):
    url = "https://jikan1.p.rapidapi.com/search/anime"
    querystring = {"q": query, "format": "json"}
    response = requests.request("GET", url, headers=headers, params=querystring).json()

    response_length = 5
    response_list  = []
    for i in range(response_length):
        response_list.append(response["results"][i])
    
    await create_list_embed(response_list, ctx)

    try:
        def valid_response(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel and int(m.content)>=1 and int(m.content)<=response_length
        
        msg = await bot.wait_for("message", check = valid_response , timeout = 15)

        if msg:
            await anime_detail(ctx, response_list[int(msg.content)-1])

    except asyncio.TimeoutError:
        await ctx.send("Cancelling due to timeout")

async def anime_detail(ctx, anime):
    start_date = anime['start_date']
    end_date = anime['end_date']

    aired_string = ""

    if(start_date is None):
        aired_string = "Not Yet Aired"
    elif(end_date is None):
        start_date_string = f"{start_date[5:7]}/{start_date[0:4]}"
        aired_string = f"{start_date_string} to ?"
    else:
        start_date_string = f"{start_date[5:7]}/{start_date[0:4]}"     
        end_date_string = f"{end_date[5:7]}/{end_date[0:4]}"
        aired_string = f"{start_date_string} to {end_date_string}"
    
    await create_anime_embed(title = anime['title'], url = anime['url'], synopsis = anime['synopsis'], image_url=anime['image_url'], score = anime['score'], episodes =  anime['episodes'], aired = aired_string, members = anime['members'], rated =  anime['rated'], ctx = ctx)
