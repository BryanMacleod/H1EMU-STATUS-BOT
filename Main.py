import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import asyncio

# Create a bot object with a command prefix
bot = commands.Bot(command_prefix='!')

# Initialize the bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Function to update status
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
                if len(cols) >= 2 and cols[1] == 'SERVERNAME':
                    status = cols[3]
                    game = discord.Game(name=f"{status} online in SERVERNAME")
                    await bot.change_presence(activity=game)
                    break
        except:
            pass
        await asyncio.sleep(30)


# Run the bot
if __name__ == '__main__':
    bot.loop.create_task(update_status())
    bot.run("TOKEN_HERE")
