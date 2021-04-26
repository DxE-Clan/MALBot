import discord
import requests
import decimal
from embed import *
from stats import *
from admin import *

headers = {
    'x-rapidapi-key': "2ed26cb89emsh2b7cb079ec42fd9p15290cjsne485ef05078a",
    'x-rapidapi-host': "jikan1.p.rapidapi.com"
}


async def show_schedule(ctx, day):
    url = f"https://jikan1.p.rapidapi.com/schedule/{day}"
    response = requests.request("GET", url, headers=headers).json()

    response_list = response[str(day)]

    anime_list = []

    for i in range(min(len(response_list), 10)):
        anime_list.append(response_list[i])

    await create_schedule_list_embed(anime_list, day, ctx)


async def search_anime(bot, ctx, query, next_step):
    url = "https://jikan1.p.rapidapi.com/search/anime"
    querystring = {"q": query, "format": "json"}
    response = requests.request("GET", url, headers=headers, params=querystring).json()

    response_length = 5
    response_list  = []
    for i in range(response_length):
        response_list.append(response["results"][i])

    await create_anime_list_embed(response_list, ctx)

    try:
        def valid_response(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel and int(m.content)>=1 and int(m.content)<=response_length

        msg = await bot.wait_for("message", check = valid_response, timeout = 15)

        if msg:
            selected_anime = response_list[int(msg.content)-1]

            await delete_messages(ctx, 2)

            if (next_step == "detail"):
                await anime_detail(ctx, selected_anime)
            elif (next_step == "stats"):
                #print(selected_anime['mal_id'])
                await anime_stats(ctx, selected_anime['mal_id'], selected_anime['title'])

    except asyncio.TimeoutError:
        await ctx.send("Cancelling due to timeout")

async def anime_detail(ctx, anime):
    start_date = anime['start_date']
    end_date = anime['end_date']

    aired_string = ""

    if (start_date is None):
        aired_string = "Not Yet Aired"
    elif (end_date is None):
        start_date_string = f"{start_date[5:7]}/{start_date[0:4]}"
        aired_string = f"{start_date_string} to ?"
    else:
        start_date_string = f"{start_date[5:7]}/{start_date[0:4]}"
        end_date_string = f"{end_date[5:7]}/{end_date[0:4]}"
        aired_string = f"{start_date_string} to {end_date_string}"

    await create_anime_embed(
        title = anime['title'],
        url = anime['url'],
        synopsis = anime['synopsis'],
        image_url=anime['image_url'],
        score = anime['score'],
        episodes =  anime['episodes'],
        aired = aired_string,
        members = anime['members'],
        rated =  anime['rated'], ctx = ctx
    )

async def anime_stats(ctx, anime_id, anime_title):
    url = f"https://jikan1.p.rapidapi.com/anime/{anime_id}/stats"
    response = requests.request("GET", url, headers = headers).json()

    percentage_list = []
    votes_list = []

    for i in range(10):
        percentage_list.append(response['scores'][f"{i+1}"]['percentage'])
        votes_list.append(response['scores'][f"{i+1}"]['votes'])

    watch_type_list = []

    with decimal.localcontext() as context:
        context.prec = 3
        watching = float((decimal.Decimal(int(response['watching'])) / decimal.Decimal(int(response['total']))) * 100)
        watch_type_list.append(watching)
        completed = float((decimal.Decimal(int(response['completed'])) / decimal.Decimal(int(response['total']))) * 100)
        watch_type_list.append(completed)
        on_hold = float((decimal.Decimal(int(response['on_hold'])) / decimal.Decimal(int(response['total']))) * 100)
        watch_type_list.append(on_hold)
        dropped = float((decimal.Decimal(int(response['dropped'])) / decimal.Decimal(int(response['total']))) * 100)
        watch_type_list.append(dropped)
        ptw = float((decimal.Decimal(int(response['plan_to_watch'])) / decimal.Decimal(int(response['total']))) * 100)
        watch_type_list.append(ptw)

    total_watched = int(response['total'])

    await create_score_bargraph(ctx, percentage_list, votes_list, anime_title)

    await create_watch_piechart(ctx, watch_type_list, total_watched, anime_title)
