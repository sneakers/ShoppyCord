import discord, asyncio, datetime, json, requests
from discord.ext import commands

class RetrieveAll(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        with open('settings.json') as f:
            data = json.load(f)
            f.close()

        self.api_key = data['api_key']

    @commands.command()
    async def RetrieveAll(self, ctx):
        if not ctx.message.author.guild_permissions.administrator:
            return

        resp = requests.get('https://shoppy.gg/api/v1/orders/',
            headers={"Authorization": self.api_key}, verify = True)

        if resp.status_code == 401:
            print('Unauthorized: please ensure your API key is correct in settings.json')
            return
        
        await ctx.message.channel.send('Retrieving all orders, this may take a few seconds.')
        
        pages = resp.headers['X-Total-Pages']
        orders = []
        c = 0

        while c < int(pages):
            resp = requests.get(f'https://shoppy.gg/api/v1/orders/?page={c}',
            headers={"Authorization": self.api_key}, verify = True)

            order_list = json.loads(resp.content)

            for order in order_list:
                orders.append(order['id'])
            
            c += 1

        length = len(orders)
        await ctx.message.channel.send(f'Successfully retrieved {length} orders.')

        with open('used_ids', 'a') as f:
            for order in orders:
                f.write(f'{order}\n')

        await ctx.message.channel.send(f'Successfully wrote all orders to file.')

def setup(bot):
    bot.add_cog(RetrieveAll(bot))
    print('RetrieveAll cog has been loaded')