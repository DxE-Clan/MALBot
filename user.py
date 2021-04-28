import discord
import requests
import asyncio
from embed import *

headers = {
    'x-rapidapi-key': "2ed26cb89emsh2b7cb079ec42fd9p15290cjsne485ef05078a",
    'x-rapidapi-host': "jikan1.p.rapidapi.com"
}

async def check_user_anime(ctx, username, anime_title):
    url = f"https://jikan1.p.rapidapi.com/user/{username}/animelist/all"
    querystring = {"search":anime_title}

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    anime_response = response['anime']

    if(len(anime_response)==0):
        await ctx.send(f"Anime not on {username}'s list")
    else:
        anime_response = anime_response[0]
        watch_status_num = anime_response['watching_status']
        watching_status = ""
        if(watch_status_num==1):
            watching_status = "Currently Watching"
        elif(watch_status_num==2):
            watching_status = "Completed"
        elif(watch_status_num==3):
            watching_status = "On Hold"
        elif(watch_status_num==4): 
            watching_status = "Dropped"
        else:
            watching_status = "Plan to Watch"

        await create_user_anime_detail(
            anime_response['url'],
            anime_response['title'],
            anime_response['image_url'],
            username,
            watching_status,
            anime_response['watched_episodes'],
            anime_response['total_episodes'],
            anime_response['score'],
            ctx
        )


async def get_completed_user_list(ctx, username, next_step):
    url = f"https://jikan1.p.rapidapi.com/user/{username}/animelist/completed"
    querystring = {"sort":"descending","order_by":"score"}

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    response_list = response["anime"]

    if (next_step == "top"):
        await get_user_top(ctx, response_list, username)
    
async def get_user_top(ctx, response_list, username):
    anime_title_list = []
    anime_score_list = []

    url = f"https://myanimelist.net/animelist/{username}?status=2&order=4&order2=0"

    for i in range(min(10, len(response_list))):
        anime_title_list.append(response_list[i]["title"])
        anime_score_list.append(response_list[i]["score"])

    await create_user_top_embed(anime_title_list, anime_score_list, url, ctx)