this was very rushed, probably doesn't account for a few thins, few people have been asking me 2 release the code tho
:D

# ShoppyCord
A Discord bot to give roles based off of Shoppy.gg purchases, specifically made for Counter-Strike cheat configs.

## Table of contents

[Creating a Discord bot](https://discordpy.readthedocs.io/en/latest/discord.html)

[Installing the files](#installation)

[Getting your Shoppy API key](#Shoppy-API-Key)

[Configuring the bot](#Configuration)

[Adding products](#Adding-products)

[Redeeming products](#Redeeming-products)

[Retrieving all previous products](#Retrieving-all-previous-products)

## Installation

You will first need to install Python 3.8 or later, you can do that [here](https://www.python.org/downloads). Ensure that you select the option to 'add Python to PATH'.

Clone the repository

```git clone https://github.com/sneakers/ShoppyCord```

Navigate to the cloned repository (usually in 'My Documents\Github\ShoppyCord') and open a terminal in this directory. Type the following command

```pip install -r requirements.txt```

You run the bot using the command

```python main.py```

however you will need to follow the rest of the steps before doing this.

## Shoppy API Key

Log into Shoppy, and head over to the [following link](https://shoppy.gg/user/settings)

Scroll down until you see "API Key" and copy this somewhere, such as notepad. Make sure you don't give this key to anyone as they will be able to view sensitive information about your customers, such as IP addresses.

## Configuration

Open up the file "settings.json" in the root folder of ShoppyCord, you will see something like this:

```json 
{
	"bot_token": "",
	"admin_channel": "",
	"redeem_channel": "",
	"api_key": ""
}
```

Settings.json value | Information to enter
------------ | -------------
bot_token | Your Discord bot token
admin_channel | The channel ID where activation logs will be sent to
redeem_channel | The channel ID where customers will type the .redeem command, all messages other than ones from the bot will be deleted 
api_key | Your Shoppy API key 

You will need to have Discord developer mode enabled to get channel IDs. You can do this by going to settings and selecting "Appearance" in the Discord client.
After inputting all of these values, you can now start the bot using the command

```python main.py```

## Adding products

You can either add products directly through the "products.json" file or using a command with the bot. Adding through the file is pretty straight forward so this guide will only cover using the command.

**Note: Only admins can use these commands. Make sure you only give the administrator permission to those who you trust.**

To view all of the current products, you can type the command 

```.add```

and to add an actual product you will type the command

```.add [ProductID] [RoleName]```

To get a Shoppy product ID, you will need to visit your Shoppy store and click on the product. You can then extract the Product ID from the URL:

> https://shoppy.gg/product/3bSS0ac

The product ID for this would be '3bSS0ac'

So the command would be:

```.add 3bSS0ac gamesense.pub```

'gamesense.pub' being the Discord role name, this is **case sensitive** meaning that it has to be spelt EXACTLY the same as it shows on the role list. 

If you make an error with typing the role, you can just retype the command. Note that everytime you use this command it will override the previous role, you cannot have multiple roles per product and role names cannot have spaces in the role name. (Unless you edit it in the products.json)

## Redeeming products

In the redeem products channel, you can type the command 

```.rEmbed```

this will send a Discord embed to the channel and it will show your customers information on how to redeem their products. You will need the administrator permission to use this command.

To actually redeem the config, you type 

```.redeem PRODUCT_ID```

## Retrieving all previous products

If you have a sales history on Shoppy and all of your customers already have their desired roles, you can type 

```.retrieveAll```

this will go through all of your shoppy orders and mark all of them as used, meaning customers can't share the codes with their friends so they get access to the product(s) for free. 

This is optional, however if you choose to use this command make sure that all of your customers have their roles already, as they won't be able to use the code since it will be marked as used.
