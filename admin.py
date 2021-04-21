import discord
import asyncio

async def delete_messages(ctx, amount):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
        messages.append(message)
    
    await channel.delete_messages(messages)
