import discord, asyncio, json
from discord.ext import commands

class OnMessage(commands.Cog): 
    def __init__(self, bot, *args, **kwargs):
        with open('settings.json') as f:
            data = json.load(f)
        
        self.redeem_channel = data['redeem_channel']
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:
            return

        if str(message.channel.id) != self.redeem_channel:
            return

        try:
            await message.delete()
        except:
            print('Error deleting message in redeem channel - maybe the member has a higher role priority?')


def setup(bot):
    bot.add_cog(OnMessage(bot))
    print('OnMessage cog has been loaded')