#-----------imports & froms-----------
import datetime
from discord.ext import commands
import discord
import discord_components
from discord_components import Button, Select, SelectOption, ComponentsBot, interaction
from discord_components.component import ButtonStyle
import asyncio
import datetime
import discord
import datetime
import discord
import os
from os import listdir
import discord
from discord.ext.commands import CommandNotFound, ChannelNotFound
from idna import check_nfc
from ruamel.yaml import YAML
import json
import aiofiles
import requests
import time
#-----------imports & froms-----------



#---------------CONFIG--------------
with open('data/config.json') as f:
            config = json.load(f)
            if config.get('TOKEN') == "your_token_here":
                if not os.environ.get('TOKEN'):
                    self.run_wizard()
            else:
                token = config.get('TOKEN').strip('\"')
        return os.environ.get('TOKEN') or token

PREFIX = "+"
NAME = "Tr7hard"
TOKEN = token
ICON = "https://cdn.discordapp.com/avatars/993170609230073896/42779ca341225056ef6d69bffefaaf84.png?size=1024"
#---------------CONFIG--------------



#--------------Client--------------
intents = discord.Intents.default()
intents.members = True
client = ComponentsBot(f"{PREFIX}", intents=intents)
client.remove_command('help')
#--------------Client--------------

#---------on ready------------------

@client.event
async def on_ready():
    for file in ["welcome_channels.txt", "goodbye_channels.txt"]:
        async with aiofiles.open(file, mode="a") as temp:
            pass
        
    async with aiofiles.open("welcome_channels.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            client.welcome_channels[int(data[0])] = (int(data[1]), " ".join(data[2:]).strip("\n"))

    async with aiofiles.open("goodbye_channels.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            client.goodbye_channels[int(data[0])] = (int(data[1]), " ".join(data[2:]).strip("\n"))
    async with aiofiles.open("reaction_roles.txt", mode="a") as temp:
        pass
        
    async with aiofiles.open("reaction_roles.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            client.reaction_roles.append((int(data[0]), int(data[1]), data[2].strip("\n")))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{PREFIX}""help"))
    print('bot is ready ✅')
    print('code by & Reaxo')
    print('by Tr7Hard Team')
#---------on ready------------------

#------------lock & unlock----------------
@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
    await ctx.send('**Channel has been locked**')

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=True)
    await ctx.send('**Channel has been unlocked**')
#------------lock & unlock----------------

#----------hide & unhide------------
@client.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,view_channel=False)
    await ctx.send('**Channel has been hide**')

@client.command()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,view_channel=True)
    await ctx.send('**Channel has been unhide**')


#----------invites-----------
@client.command()
async def invites(ctx, user:discord.Member=None):
    if user is None:
        total_invites = 0
        for i in await ctx.guild.invites():
            if i.inviter == ctx.author:
                total_invites += i.uses
        await ctx.send(f"You've invited {total_invites} member{'' if total_invites == 1 else 's'} to the server!")
    else:
        total_invites = 0
        for i in await ctx.guild.invites():
            if i.inviter == user:
                total_invites += i.uses

        await ctx.send(f"{user} has invited {total_invites} member{'' if total_invites == 1 else 's'} to the server!")


#--------------giveaway time----------
def convert(time):
    pos = ["s", "m", "h", "d", "w"]
    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24, "w": 3600 * 24 * 7}
    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2

    return val * time_dict[unit]
#--------------giveaway time----------



#---------------ERROR---------------
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please complete your message!")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have access to this command")
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Wait this command is in cooldown")
#---------------ERROR---------------

#-------------help commands-----------
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help Commands !", description="This command is for getting to know other commands")
    embed.add_field(name="Moderation", value=f"{PREFIX}""`help_mod`", inline=True)
    embed.add_field(name="Help Ful", value=f"{PREFIX}""`help_ful`", inline=True)
    embed.add_field(name="Fun", value=f"{PREFIX}""`help_fun`", inline=True)
    await ctx.reply(embed=embed)

@client.command()
async def help_mod(ctx):
    embed=discord.Embed(title="commands", color=0xFFFFFF)
    embed.add_field(name=f"{PREFIX}""ban (user) (reason)", value="this command for ban users")
    embed.add_field(name=f"{PREFIX}""unban (user)", value="this command for unban users")
    embed.add_field(name=f"{PREFIX}""kick (user) (reason)", value="this command for kick users")
    embed.add_field(name=f"{PREFIX}""mute (user) (reason)", value="this command for mute users")
    embed.add_field(name=f"{PREFIX}""unmute (user)", value="this command for unmute users")
    embed.add_field(name=f"{PREFIX}""setnick (user) (nick)", value="this command for set users nick")
    embed.add_field(name=f"{PREFIX}""clear (amount)", value="this command for clear messages")
    embed.add_field(name=f"{PREFIX}""lock (channel)", value="this command for lock channels")
    embed.add_field(name=f"{PREFIX}""unlock (channel)", value="this command for unlock channels")
    embed.add_field(name=f"{PREFIX}""hide (channel)", value="this command for hide channels")
    embed.add_field(name=f"{PREFIX}""unhide (channel)", value="this command for unhide channels")
    embed.add_field(name=f"{PREFIX}""giveaway", value="this command for create giveaway")
    embed.add_field(name=f"{PREFIX}""reroll (channel) (massage_id)", value="this command reroll the giveaway")
    embed.add_field(name=f"{PREFIX}""ticket", value="this command for send embed ticket")
    embed.add_field(name=f"{PREFIX}""set_welcome_channel (channel) (message)", value="this command for set a welcome channel")
    embed.add_field(name=f"{PREFIX}""set_goodbye_channel (channel) (message)", value="this command for set a goodbye channel")
    embed.add_field(name=f"{PREFIX}""send (text)", value="this command for send a message for announcement or reaction role message")
    embed.add_field(name=f"{PREFIX}""reaction (role) (message-id) (emoji)", value="this command for set a welcome channel")
    embed.set_author(name="Mod Commands", icon_url=f"{ICON}")
    embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

@client.command()
async def help_ful(ctx):
    embed=discord.Embed(title="commands", color=0xFFFFFF)
    embed.add_field(name=f"{PREFIX}""avatar (user)", value="this command for viewing users avatar")
    embed.add_field(name=f"{PREFIX}""invites (user)", value="this command for viewing users total invites")
    embed.add_field(name=f"{PREFIX}""members", value="this command for viewing memeber count")
    embed.add_field(name=f"{PREFIX}""password", value="this command for generate random password")
    embed.add_field(name=f"{PREFIX}""skin (player)", value="this command for viewing minecraft player skins")
    embed.add_field(name=f"{PREFIX}""head (player)", value="this command for viewing minecraft player heads")
    embed.set_author(name="Help Ful Commands", icon_url=f"{ICON}")
    embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

@client.command()
async def help_fun(ctx):
    embed=discord.Embed(title="commands", color=0xFFFFFF)
    embed.set_author(name="Help Fun Commands", icon_url=f"{ICON}")
    embed.add_field(name=f"{PREFIX}""ProMeasure (user)", value="This command is for you to find out how pro you ares")
    embed.add_field(name=f"{PREFIX}""NoobMeasure (user)", value="This command is for you to find out how noob you ares")
    embed.add_field(name=f"{PREFIX}""GayMeasure (user)", value="This command is for you to find out how gay you ares")
    embed.add_field(name=f"{PREFIX}""Love (user)", value="This command is to understand how much others love you")
    embed.add_field(name=f"{PREFIX}""Rick (user) (reason)", value="This command for Rick roll users")
    embed.add_field(name=f"{PREFIX}""Joke", value="This command for sending joke")
    embed.set_footer(text="Information requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
#-------------help commands-----------


#---------rick---------
@client.command()
async def rick(ctx, member: discord.Member, *, reason=None):
    embed=discord.Embed(title=f"U Got RickRolled {member} !", color=discord.Color.red())
    embed.add_field(name="Name:", value=member, inline=False)
    embed.add_field(name="Reason:", value=reason, inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/980884671065890826/997467504865710140/all-of-you-got-rick-rolled.jpg")
    await ctx.send(embed=embed)

@client.command()
async def Rick(ctx, member: discord.Member, *, reason=None):
    embed=discord.Embed(title=f"U Got RickRolled {member} !", color=discord.Color.red())
    embed.add_field(name="Name:", value=member, inline=False)
    embed.add_field(name="Reason:", value=reason, inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/980884671065890826/997467504865710140/all-of-you-got-rick-rolled.jpg")
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def joke(ctx):
    link = "http://api.icndb.com/jokes/random?firstName=John&lastName=Doe" 
    req = requests.get(link)
    data = req.json()
    joke = (data["value"]["joke"])
    embed = discord.Embed(title="Dad's joks :joy:",description=f"{joke}",color=0xFFFFFF)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/995358672932843530/997491410037129216/unknown.png")
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def Joke(ctx):
    link = "http://api.icndb.com/jokes/random?firstName=John&lastName=Doe" 
    req = requests.get(link)
    data = req.json()
    joke = (data["value"]["joke"])
    embed = discord.Embed(title="Dad's joks :joy:",description=f"{joke}",color=0xFFFFFF)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/995358672932843530/997491410037129216/unknown.png")
    await ctx.send(embed=embed)
#-------------SelfRole---------

@client.command()
@commands.has_permissions(kick_members=True)
async def send(ctx, *, massage):
    await ctx.send(massage)


client.reaction_roles = []
@client.command()
@commands.has_permissions(kick_members=True)
async def reaction(ctx, role: discord.Role=None, msg: discord.Message=None, emoji=None):
    if role != None and msg != None and emoji != None:
        await msg.add_reaction(emoji)
        client.reaction_roles.append((role.id, msg.id, str(emoji.encode("utf-8"))))
        
        async with aiofiles.open("reaction_roles.txt", mode="a") as file:
            emoji_utf = emoji.encode("utf-8")
            await file.write(f"{role.id} {msg.id} {emoji_utf}\n")

        await ctx.channel.send("Reaction has been set.")
        
    else:
        await ctx.send("Invalid arguments.")

@client.event
async def on_raw_reaction_add(payload):
    for role_id, msg_id, emoji in client.reaction_roles:
        if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
            await payload.member.add_roles(client.get_guild(payload.guild_id).get_role(role_id))
            return

@client.event
async def on_raw_reaction_remove(payload):
    for role_id, msg_id, emoji in client.reaction_roles:
        if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
            guild = client.get_guild(payload.guild_id)
            await guild.get_member(payload.user_id).remove_roles(guild.get_role(role_id))
            return
#-----------Self-Role--------------



#------------ticket-------------------
id_category = 980875953301491793
id_channel_ticket_logs = 981042522241511524
embed_color = 0xfcd005 


@client.command()
@commands.has_permissions(administrator=True)
async def ticket(ctx):
    await ctx.message.delete()


    embed = discord.Embed(title ='Tickets', description ="Welcome to tickets system <:8965vslticket:997486768079249418>", color=embed_color) 


    embed.set_image(url='https://cdn.discordapp.com/attachments/995358672932843530/996853302006386768/reaxo_cover2.png')

    await ctx.send(
        embed = embed,

        components = [
            Button(
                custom_id = 'Ticket',
                label = "Create a ticket",
                style = ButtonStyle.green,
                emoji ='🔧')
        ]
    )


@client.event
async def on_button_click(interaction):

    canal = interaction.channel
    canal_logs = interaction.guild.get_channel(id_channel_ticket_logs)

    if interaction.component.custom_id == "Ticket":
        await interaction.send(

            components = [
                Select(
                    placeholder = "How can we help you?",
                    options = [
                        SelectOption(label="Question", value="question", description='If you have a simple question.', emoji='❔'),
                        SelectOption(label="Help", value="help", description='If you need help from us.', emoji='🔧'),
                        SelectOption(label="Report", value="report", description='To report a misbehaving user.', emoji='🚫'),
                    ],
                    custom_id = "menu")])



    elif interaction.component.custom_id == 'close_ticket':

        embed_cerrar_ticket = discord.Embed(description=f"⚠️ Are you sure you want to close the ticket?", color=embed_color)
        await canal.send(interaction.author.mention, embed=embed_cerrar_ticket, 
                        components = [[
                        Button(custom_id = 'close_yes', label = "Yes", style = ButtonStyle.green),
                        Button(custom_id = 'close_no', label = "No", style = ButtonStyle.red)]])


    elif interaction.component.custom_id == 'close_yes':

        await canal.delete()
        embed_logs = discord.Embed(title="Tickets", description=f"", timestamp = datetime.datetime.utcnow(), color=embed_color)
        embed_logs.add_field(name="Ticket", value=f"{canal.name}", inline=True)
        embed_logs.add_field(name="Closed by", value=f"{interaction.author.mention}", inline=False)
        embed_logs.set_thumbnail(url=interaction.author.avatar_url)
        await canal_logs.send(embed=embed_logs)


    elif interaction.component.custom_id == 'close_no':
        await interaction.message.delete()

@client.event
async def on_select_option(interaction):
    if interaction.component.custom_id == "menu":

        guild = interaction.guild
        category = discord.utils.get(interaction.guild.categories, id = id_category)


        if interaction.values[0] == 'question':

            channel = await guild.create_text_channel(name=f'❔┃{interaction.author.name}-ticket', category=category)
            

            await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await channel.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)
                                                

            await interaction.send(f'> The {channel.mention} channel was created to solve your questions.', delete_after= 3)

            embed_question = discord.Embed(title=f'Question - Hi {interaction.author.name}!', description='In this ticket we have an answer to your question.\n\nIf you cant get someone to help you, Only 1 time mention the staff for `🔔 Call staff', color=embed_color)
            embed_question.set_thumbnail(url=interaction.author.avatar_url)


            await channel.send(interaction.author.mention, embed=embed_question,
            

             components = [[
                    Button(custom_id = 'close_ticket', label = "Close ticket", style = ButtonStyle.red, emoji ='🔐')]])


        elif interaction.values[0] == 'help':

            channel = await guild.create_text_channel(name=f'🔧┃{interaction.author.name}-ticket', category=category)
            

            await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await channel.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)



            await interaction.send(f'> The {channel.mention} channel was created to help you.', delete_after= 3)

            embed_question = discord.Embed(title=f'Help - ¡Hi {interaction.author.name}!', description='In this ticket we can help you with whatever you need.\n\nIf you cant get someone to help you, Only 1 time mention the staff for `🔔 Call staff`.', color=embed_color)
            embed_question.set_thumbnail(url=interaction.author.avatar_url)


            await channel.send(interaction.author.mention, embed=embed_question, 

            components = [[
                    Button(custom_id = 'close_ticket', label = "Close ticket", style = ButtonStyle.red, emoji ='🔐')]])



        elif interaction.values[0] == 'report':


            channel = await guild.create_text_channel(name=f'🚫┃{interaction.author.name}-ticket', category=category)


            await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await channel.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)


            await interaction.send(f'> The {channel.mention} channel was created to report to the user.', delete_after= 3)


            embed_question = discord.Embed(title=f'Report - ¡Hi {interaction.author.name}!', description='In this ticket we can help you with your report.\n\nIf you cant get someone to help you, Only 1 time mention the staff for `🔔 Call staff`.', color=embed_color)
            embed_question.set_thumbnail(url=interaction.author.avatar_url)

            await channel.send(interaction.author.mention, embed=embed_question, 
            

            components = [[
                    Button(custom_id = 'close_ticket', label = "Close ticket", style = ButtonStyle.red, emoji ='🔐')]])
#------------ticket-------------------


#-------------bad word & link blocker--------------
filtered_words = ["kir","kos","nane","nanat","jagh","koon","https://","discord.gg","sex","sik","gaeidam","haroom zade","harum zade","lapaei","fuck","shit","shet","fucking"]

@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
         await msg.delete()

    await client.process_commands(msg)
#-------------bad word & link blocker--------------


#---------------mc commands-------------
@client.command()
async def skin(ctx, player):
    embed=discord.Embed(title="Skin " f"{player}",url="https://mineskin.eu/download/"f"{player}",description="Download Link",color=0x08000)
    embed.set_image(url="https://mineskin.eu/armor/body/"f"{player}""/100.png")
    await ctx.send(embed=embed)

    


@client.command()
async def Skin(ctx, player):
    embed=discord.Embed(title="Skin " f"{player}",url="https://mineskin.eu/download/"f"{player}",description="Download Link",color=0x08000)
    embed.set_image(url="https://mineskin.eu/armor/body/"f"{player}""/100.png")
    await ctx.send(embed=embed)

@client.command()
async def head(ctx, player):
    embed=discord.Embed(title="head " f"{player}",url="https://mineskin.eu/helm/"f"{player}""/100.png",description="Download Link",color=0x000FF)
    embed.set_image(url="https://mineskin.eu/helm/"f"{player}""/100.png")
    await ctx.send(embed=embed)
#---------------mc commands-------------

#-------------help_ful---------------
@client.command()
async def avatar(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    message = discord.Embed(title=str(member), color=discord.Colour.orange())
    message.set_image(url=member.avatar_url)
    await ctx.send(embed=message)


@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def setnick(ctx, member: discord. Member, *,nick):
    await member. edit(nick=nick)
    await ctx. send(f'Nickname was changed for {member.mention} ')

@client.command()
async def password(ctx):
    passwordgen = requests.get('https://www.passwordrandom.com/query?command=password')
    await ctx.reply("Your Password Generated : ||" + f"{passwordgen.text}" + "||")
    
#-------------help_ful---------------


#----------fun-------------

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def ProMeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    pro = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + pro.text + f" pro {member.mention}")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def NoobMeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    noob = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + noob.text + f" Noob {member.mention}")


@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def GayMeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    gay = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + gay.text + f" gay {member.mention}")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def Love(ctx, member: discord.Member):
    love = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send(f" {member.mention} is % " + love.text + " in love with you")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def promeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    pro = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + pro.text + f" pro {member.mention}")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def noobmeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    noob = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + noob.text + f" Noob {member.mention}")


@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def gaymeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    gay = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + gay.text + f" gay {member.mention}")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def love(ctx, member: discord.Member):
    love = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send(f" {member.mention} is % " + love.text + " in love with you")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def Promeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    pro = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + pro.text + f" pro {member.mention}")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def Noobmeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    noob = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + noob.text + f" Noob {member.mention}")


@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def Gaymeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    gay = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + gay.text + f" gay {member.mention}")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def proMeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    pro = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + pro.text + f" pro {member.mention}")

@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def noobMeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    noob = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + noob.text + f" Noob {member.mention}")


@client.command()
@commands.cooldown(1, 5, commands.BucketType.guild)
async def gayMeasure(ctx, member: discord.Member = None):
    if not member:member=ctx.message.author
    gay = requests.get('https://www.passwordrandom.com/query?command=int')
    await ctx.send("You Are % " + gay.text + f" gay {member.mention}")
#---------fun--------------



#------------welcomer-goodbyer----------
client.welcome_channels = {}
client.goodbye_channels = {}


@client.event
async def on_member_join(member):
    for guild_id in client.welcome_channels:
        if guild_id == member.guild.id:
            channel_id, message = client.welcome_channels[guild_id]
            embed=discord.Embed(title=f"<:9832vslhandshake:997483020506386494> {message} {member.name}",description="<:6533vslmodhammer:997483044158058558> please Read The Rules")
            embed.set_thumbnail(url=member.avatar_url)
            await client.get_guild(guild_id).get_channel(channel_id).send(embed=embed)
            return

@client.event
async def on_member_remove(member):
    for guild_id in client.goodbye_channels:
        if guild_id == member.guild.id:
            channel_id, message = client.goodbye_channels[guild_id]
            embed=discord.Embed(title=f"<:9832vslhandshake:997483020506386494> {message} {member.name}")
            embed.set_thumbnail(url=member.avatar_url)
            await client.get_guild(guild_id).get_channel(channel_id).send(embed=embed)
            return

@client.command()
async def set_welcome_channel(ctx, new_channel: discord.TextChannel=None, *, message=None):
    if new_channel != None and message != None:
        for channel in ctx.guild.channels:
            if channel == new_channel:
                client.welcome_channels[ctx.guild.id] = (channel.id, message)
                await ctx.channel.send(f"Welcome channel has been set to: {channel.name} with the message {message}")
                await channel.send("This is the new welcome channel!")
                async with aiofiles.open("welcome_channels.txt", mode="a") as file:
                    await file.write(f"{ctx.guild.id} {new_channel.id} {message}\n")

                return

        await ctx.channel.send("Couldn't find the given channel.")

    else:
        await ctx.channel.send("You didn't include the name of a welcome channel or a welcome message.")

@client.command()
async def set_goodbye_channel(ctx, new_channel: discord.TextChannel=None, *, message=None):
    if new_channel != None and message != None:
        for channel in ctx.guild.channels:
            if channel == new_channel:
                client.goodbye_channels[ctx.guild.id] = (channel.id, message)
                await ctx.channel.send(f"Goodbye channel has been set to: {channel.name} with the message {message}")
                await channel.send("This is the new goodbye channel!")
                
                async with aiofiles.open("goodbye_channels.txt", mode="a") as file:
                    await file.write(f"{ctx.guild.id} {new_channel.id} {message}\n")

                return

        await ctx.channel.send("Couldn't find the given channel.")

    else:
        await ctx.channel.send("You didn't include the name of a goodbye channel or a goodbye message.")
#------------welcomer-goodbyer----------

for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		client.load_extension(f"cogs.{fn[:-3]}")

client.run(TOKEN)
