from discord.ext import commands
from discord.ext.commands import Context, command


class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @command(name="sync", aliases=["Sync"])
    async def sync(self, ctx: Context) -> None:
        """Globally syncs slash commands."""
        if ctx.author.id in (
            293926911875219456,
            852961987729555466,
        ):
            await self.bot.tree.sync()
            await ctx.send("Tree synced")
        else:
            await ctx.send("You are not authorized to use this command")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Admin(bot))
