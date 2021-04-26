import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import asyncio
import decimal
import discord
import os
import time
import io

async def create_score_bargraph(ctx, percentage_list, votes_list, anime_title):
    x_labels = ['1','2','3','4','5','6','7','8','9','10']
    total_votes = 0

    for vote in votes_list:
        total_votes += vote

    fig = plt.figure()
    plt.bar(x_labels, percentage_list)
    plt.title(anime_title)
    plt.xlabel("Score")
    plt.ylabel("Percentage")
    filename = "score_bargraph.png"
    plt.savefig(filename)

    await ctx.send(file = discord.File('score_bargraph.png'))
    await ctx.send(f"Total votes: {total_votes}")

    plt.close()

async def create_watch_piechart(ctx, watch_type_list, total_watched, anime_title):
    labels = ["Watching", "Completed", "On Hold", "Dropped", "Plan to Watch"]
    colors = ["green", "blue", "yellow", "red", "grey"]
    patches, texts = plt.pie(watch_type_list, colors = colors, autopct = '%0.2f%%', startangle = 90, radius = 10)
    plt.legend(labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()

    filename = "watch_piechart.png"
    plt.savefig(filename)

    await ctx.send(file = discord.File("watch_piechart.png"))
    await ctx.send(f"Total Entries on Anime Lists: {total_watched}")

    plt.close()
