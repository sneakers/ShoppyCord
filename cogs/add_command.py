import discord, asyncio, datetime
from discord.ext import commands

class AddCommand(commands.Cog):
    @commands.command()
    async def rEmbed(self, ctx):
        if not ctx.message.author.guild_permissions.administrator:
            return

        embed = discord.Embed(colour=0x202225, description = """
            To get your config, type .redeem following your purchase ID

            ```.redeem XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX```
            If you have any issue redeeming your config please contact the server owner""")
        
        try:
            await ctx.message.channel.send(embed=embed)
        except:
            print('Error trying to send the embed command - maybe the bot doesn\'t have permission?')

def setup(bot):
    bot.add_cog(AddCommand(bot))
    print('AddCommand cog has been loaded')