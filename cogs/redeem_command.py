import discord, asyncio, datetime, requests, json
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter

class RedeemCommand(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        with open('settings.json') as f:
            data = json.load(f)
            f.close()

        self.data = data
        self.api_key = data['api_key']
        self.bot = bot

    @commands.command()
    async def redeem(self, ctx, key):
        with open('used_ids') as f:
            used_ids = f.read().splitlines()
            f.close()

        if key in used_ids:
            message = await ctx.send(f'<@{ctx.message.author.id}>, that code has already been used. Please contact the server owner if you have swapped accounts.')
            await asyncio.sleep(5)
            await message.delete()
            return

        resp = requests.get(f'https://shoppy.gg/api/v1/orders/{key}',
            headers={"Authorization": self.api_key}, verify = True)

        if resp.status_code == 401:
            print('Unauthorized: please ensure your API key is correct in settings.json')
            return

        if resp.status_code != 200:
            message = await ctx.send(f'<@{ctx.message.author.id}>, that code was not found, make sure you typed it correctly.')
            await asyncio.sleep(5)
            await message.delete()
            return

        json_data = json.loads(resp.text)
        delivered = json_data['delivered']

        if delivered != 1:
            message = await ctx.send(f'<@{ctx.message.author.id}>, this product has not been paid for.')
            await asyncio.sleep(5)
            await message.delete()
            return

        resp = json.loads(resp.text)
        product_id = resp['product']['id']

        with open('products.json') as f:
            data = json.load(f)
            f.close()

        if product_id not in data.keys():
            message = await ctx.send(f'<@{ctx.message.author.id}>, this product has not been set up yet, please tell the server owner to set it up then retry again.')
            await asyncio.sleep(5)
            await message.delete()
            return

        role_name = data[product_id]
        role = discord.utils.get(ctx.guild.roles, name=role_name)

        if role is None:
            message = await ctx.send(f'<@{ctx.message.author.id}>, there was an error getting the role, please ensure the server owner has given the bot right permissions and the roles are spelled correctly.')
            await asyncio.sleep(5)
            await message.delete()
            return

        if role in ctx.author.roles:
            message = await ctx.send(f'<@{ctx.message.author.id}>, you already have this products role.')
            await asyncio.sleep(5)
            await message.delete()
            return

        try:
            await ctx.message.author.add_roles(discord.utils.get(ctx.guild.roles, name=role_name))
            
            with open('used_ids', 'a') as f:
                f.write(f'{key}\n')
                f.close()

            channel_id = self.data['admin_channel']

            try:
                if channel_id != None:
                    channel = self.bot.get_channel(int(channel_id))

                    embed = discord.Embed(colour=0x202225, timestamp=datetime.datetime.now())
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.set_footer(text=f'User ID: {ctx.message.author.id}')

                    embed.add_field(name='**User**', value=f'{ctx.message.author.mention}') 
                    embed.add_field(name='**Product ID**', value=key, inline=False)
                    embed.add_field(name='**Role given**', value=role_name, inline=False)

                    message = await channel.send(embed=embed)
            except Exception as e:
                print(e)
                print('Error sending successful role webhook')

            message = await ctx.send(f'<@{ctx.message.author.id}>, your role has been added.')
            await asyncio.sleep(5)
            await message.delete()


        except Exception as e:
            print(f'[{ctx.author.name}] {e}')
            message = await ctx.send(f'<@{ctx.message.author.id}>, there was an error, please contact the server owner.')
            await asyncio.sleep(5)
            await message.delete()
            return

def setup(bot):
    bot.add_cog(RedeemCommand(bot))
    print('RedeemCommand cog has been loaded')