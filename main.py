# Импортируем найстройки бота
import conf
import discord
from discord.ext import commands





# intents = discord.Intents.default()
# intents.members = True
# # Создаём подключение бота
# client = discord.Client(intents = intents)


# @client.event
# async def on_message(message): 
# #<Message id=829999281070932028 
# # channel=<TextChannel id=827854405511544853 name='andrew-bot' position=17 nsfw=False news=False category_id=825215092731412490> type=<MessageType.default: 0> 
# # author=<Member id=601101669513560085 name='Ozen' discriminator='0182' bot=False nick='Андрей Ширяев'
#     #  guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=36>> flags=<MessageFlags value=0>>  





#     #Защита от дурока №1: Защита от рекурсии
#     if message.author == client.user:
#         return
#     #Защита от дурока №2: Защита от ответа бота боту
#     if message.author.bot:
#         return


#     #Бот отвечает только в комнате "Andrew-bot"
#     if message.channel.id == 827854405511544853: 
#         msg = None

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
#         #         for idx, channel in list(enumerate(message.author.guild.channels)):   Не робит
#         #             msg += f'{idx+1}. {channel.name} - {channle.id}\n'
        
#         #Защита от дурака №3: Проверка на пустоту
#         if msg:
#             await message.channel.send(msg)
            

        
# # Запускаем бота, используя токен из conf.py
# client.run(conf.bot_token)


bot = commands.Bot(command_prefix = "!")

@bot.command(name = "hello")
async def command_hello(ctx, *args):

    if ctx.channel.id == 827854405511544853: 
        msg = "Hello you!"
        await ctx.channel.send(msg)


bot.run(conf.bot_token)