import discord
import requests
from bs4 import BeautifulSoup
import asyncio


intents = discord.Intents.all()
bot = discord.Client(intents=intents

async def update_status():
    while True:
        try:
            page = requests.get("https://serverlist.h1emu.com/us/")
            soup = BeautifulSoup(page.content, 'html.parser')
            table = soup.find_all('table')[0]
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                if len(cols) >= 2 and cols[1] == 'EXACT SERVERNAME FROM H1EMU SITE.':
                    status = cols[3]
                    game = discord.Game(name=f"{status} online in SERVERNAME")
                    await bot.change_presence(activity=game)
                    break
        except:
            pass
        await asyncio.sleep(30)


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    bot.loop.create_task(update_status())


if __name__ == '__main__':
    bot.run("TOKEN")
