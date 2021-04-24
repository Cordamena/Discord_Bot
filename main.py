# Импортируем найстройки бота
import os
import conf
import discord
import img_headler as imh1
from discord.ext import commands




intents = discord.Intents.default()
intents.members = True
# # Создаём подключение бота
# client = discord.Client(intents = intents)


# @client.event
# async def on_message(message): 
# #<Message id=829999281070932028 
# # channel=<TextChannel id=827854405511544853 name='andrew-bot' position=17 nsfw=False news=False category_id=825215092731412490> type=<MessageType.default: 0> 
# # author=<Member id=601101669513560085 name='Ozen' discriminator='0182' bot=False nick='Андрей Ширяев'
#     #  guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=36>> flags=<MessageFlags value=0>>  





    # #Защита от дурока №1: Защита от рекурсии
    # if message.author == client.user:
    #     return
    # #Защита от дурока №2: Защита от ответа бота боту
    # if message.author.bot:
    #     return


    # #Бот отвечает только в комнате "Andrew-bot"
    # if message.channel.id == 827854405511544853: 
    #     msg = None

#         ctx = message.content.split(" ", maxsplit = 1)

#         #1 Задача
#         if ctx[0] == "/hello":
#             msg = f'Привет, {message.author.name}, я {client.user.name}'
        
#         #2 Задача
#         if ctx[0] == "/about_me":
#             msg = f'Здравствуйте, ваш id: "{message.author.id}", ваше имя: "{message.author.name}", ваш ник: "{message.author.nick}"'
        
#         #3 Задача
#         if ctx[0] == "/repeat":
#             msg = ctx[1] 
        
#         #4 Задача
#         # if ctx[0] == "/get_member":
#         #     if message.author.guild.name == "Bots":
#         #         for member in list(enumerate(message.author.guild.members)):   Не робит
#         #             if member.id == int(ctx[1])
#         #                 msg += f'он {member.name}'

#         #5 Задача 
#         if ctx[0] == "/get_members":
#             msg = ""
#             if message.author.guild.name == "Bots":
#                 for idx, member in list(enumerate(message.author.guild.members)):
#                     # "1. name (nick) id"
#                     msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else "" } - {member.id}\n'

#         #6 Задача
#         # if ctx == "/get_channels":
#         #     msg = ""
#         #     if message.author.guild.name == "Bots":
#         #         for idx, channel in list(enumerate(message.author.guild.channels)):   
#         #             msg += f'{idx+1}. {channel.name} - {channel.id}\n'
        
#         #Защита от дурака №3: Проверка на пустоту
#         if msg:
#             await message.channel.send(msg)
            

        
# # Запускаем бота, используя токен из conf.py
# client.run(conf.bot_token)


bot = commands.Bot(command_prefix = "!", intents=intents)




#Ответный привет
@bot.command(name = "hello")
async def command_hello(ctx, *args):

    if ctx.channel.id == 827854405511544853: 
        msg = "Hello you!"
        await ctx.channel.send(msg)

#Обо мне
@bot.command(name = "about_me")
async def command_about_me(ctx, *args):
    if ctx.channel.id == 827854405511544853: 
        msg = f'Здравствуйте, ваш id: "{ctx.author.id}", ваше имя: "{ctx.author.name}", ваш ник: "{ctx.author.nick}"'
        await ctx.channel.send(msg)

#Повтор слова/слов
@bot.command(name = "repeat")
async def command_repeat(ctx, *args):
    if ctx.channel.id == 827854405511544853: 
        msg = " ".join(args)
        await ctx.channel.send(msg)


#Список всех каналов
@bot.command(name = "get_channels")
async def command_get_channels(ctx, *args):
    if ctx.channel.id == 827854405511544853: 
        msg = " "
        if ctx.author.guild.name == "Bots":
            for idx, channel in list(enumerate(ctx.author.guild.channels)):  
                msg += f'{idx+1}. {channel.name} - {channel.id}\n'
        await ctx.channel.send(msg)



#Список всех участников
@bot.command(name = "get_members")
async def command_get_members(ctx, *args):
    if ctx.channel.id == 827854405511544853: 
        if ctx.author.guild.name == "Bots":
            msg=""
            for idx, member in list(enumerate(ctx.author.guild.members)):
                msg += f'{idx+1}. {member.name}, {member.nick} - {member.id}\n'
        await ctx.channel.send(msg)

channel = 827854405511544853

@bot.command(name="get_member")
async def get_member(ctx, member:discord.Member=None):
    msg = None
    global channel
    if ctx.channel.id == channel:

        if member:
            msg = f'Member: {member.name}, Nickname: {member.nick} - {member.id}'

        if msg == None:
            msg = "error"
        
        await ctx.channel.send(msg)



@bot.command(name="mk")
async def mk (ctx, fighter1:discord.Member=None, fighter2:discord.Member=None):
    global channel
    msg = None
    if ctx.channel.id == channel:
        if fighter1 and fighter2:
            await imh1.vs_create(fighter1.avatar_url, fighter2.avatar_url)


            msg = f'{fighter1.name} VS {fighter2.name}'
            await ctx.channel.send(file=discord.File(os.path.join("./img/result.png")))


@bot.command(name="mka")
async def mka (ctx, fighter1:discord.Member=None, fighter2:discord.Member=None):
    global channel
    if ctx.channel.id == channel:
        if fighter1 and fighter2:
            await imh1.vs_create_animated(fighter1.avatar_url, fighter2.avatar_url)

            await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))


@bot.command(name="join")
async def vc_join(ctx):
    msg =""
    global channel
    voice_channel = ctx.author.voice.channel

    if voice_channel:
        msg = f'Подключаюсь к {voice_channel.name}'
        await ctx.channel.send(msg)
        await voice_channel.connect()

@bot.command(name="leave")
async def vc_leave(ctx):
    msg =""
    global channel
    voice_channel = ctx.author.voice.channel

    if voice_channel:
        msg = f'Отключаюсь от {voice_channel.name}'
        await ctx.channel.send(msg)
        await ctx.voice_client.disconnect()



bot.run(conf.bot_token)