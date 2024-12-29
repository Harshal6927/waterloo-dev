import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

BOT = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@BOT.event
async def on_ready() -> None:
    """Load all cogs when the bot is ready"""
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await BOT.load_extension(f"cogs.{filename[:-3]}")

    print(f"{BOT.user} has connected to Discord!")


if __name__ == "__main__":
    try:
        BOT.run(os.environ["TOKEN"])
    except Exception as e:  # noqa: BLE001
        print(f"Failed to start the bot. Error: {e}")
