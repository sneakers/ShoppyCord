import discord, asyncio, json
from discord.ext import commands

class Add(commands.Cog):
    @commands.command()
    async def add(self, ctx, *args):
        if not ctx.message.author.guild_permissions.administrator:
            return

        length = len(args)

        with open('products.json') as f:
            message = f.read()
            f.close()           
        
        if length == 0:
            embed = discord.Embed(colour=0x202225, description = f"""
            ```json

            {message}
            ```

            To set a product ID to a role please use: .add [Product ID] [Role name]. 
            Please note that both of these values are case sensitive.""")

            await ctx.message.channel.send(embed=embed)
            return

        if length != 2:
            await ctx.message.channel.send('The correct usage is .add [Product ID] [Role name]. These values are case sensitive.')
            return

        message = json.loads(message)

        message[args[0]] = args[1]

        with open('products.json', 'w') as f:
            f.write(json.dumps(message, indent=2))
            f.close()

        embed = discord.Embed(colour=0x202225, description = 'Updated products.json successfully')

        await ctx.message.channel.send(embed=embed)
        return

        

def setup(bot):
    bot.add_cog(Add(bot))
    print('Add cog has been loaded')