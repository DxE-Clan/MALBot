import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import asyncio
import discord
import os
import time
import io

async def create_score_bargraph(ctx, percentage_list, votes_list):   
    x_labels = ['1','2','3','4','5','6','7','8','9','10']

    total_votes = 0
    for vote in votes_list:
        total_votes+=vote

    fig = plt.figure()
    plt.bar(x_labels, percentage_list)
    plt.xlabel("Score")
    plt.ylabel("Percentage")

    filename =  "test.png"
    plt.savefig(filename)

    await ctx.send(file = discord.File('test.png'))
    await ctx.send(f"Total votes: {total_votes}")

    plt.close()