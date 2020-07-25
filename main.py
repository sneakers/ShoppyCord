import discord, json
from discord.ext import commands

bot = commands.Bot(command_prefix='.', case_insensitive=True)
extensions = ['cogs.redeem_embed', 'cogs.on_message', 'cogs.redeem_command']

with open('settings.json') as f:
  data = json.load(f)
  f.close()

def setup():
    token = data['bot_token']

    for xt in extensions:
        try:
            bot.load_extension(xt)
        except Exception as e:
            print(f'Failed to load extension {xt}')
            print(e)

    bot.run(token)

setup()