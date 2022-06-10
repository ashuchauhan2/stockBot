import discord
import os
from bs4 import BeautifulSoup
import requests
from discord.ext import commands

client = commands.Bot(command_prefix='!')


def getPrice(ticker):
    url = 'https://ca.finance.yahoo.com/quote/' + ticker
    page = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;   Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33", })

    soup = BeautifulSoup(page.text, 'html.parser')
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text

    return (price)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def stock(ctx, arg):
    await ctx.send(getPrice(arg))


client.run(os.getenv('TOKEN'))