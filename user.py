import discord
import requests
import asyncio
from embed import *

headers = {
    'x-rapidapi-key': "2ed26cb89emsh2b7cb079ec42fd9p15290cjsne485ef05078a",
    'x-rapidapi-host': "jikan1.p.rapidapi.com"
}

async def get_completed_user_list(ctx, username, next_step):
    url = f"https://jikan1.p.rapidapi.com/user/{username}/animelist/completed"
    querystring = {"sort":"descending","order_by":"score"}

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    response_list = response["anime"]

    if(next_step == "top"):
        await get_user_top(ctx, response_list, username)
    
    
async def get_user_top(ctx, response_list, username):
    anime_title_list = []
    anime_score_list = []

    url = f"https://myanimelist.net/animelist/{username}?status=2&order=4&order2=0"

    for i in range(min(10, len(response_list))):
        anime_title_list.append(response_list[i]["title"])
        anime_score_list.append(response_list[i]["score"])

    await create_user_top_embed(anime_title_list, anime_score_list, url, ctx)
    


