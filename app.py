import discord
from discord.ext import commands
import random

description = '''soy julia-tang, un bot de ayuda!'''
bot = commands.Bot(command_prefix='>', description=description)

@bot.event
async def on_ready():
    print('Yo soy')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hola():
    """Suma dos numeros."""
    await bot.say("Hola!!!")

@bot.command()
async def suma(left : int, right : int):
    """Suma dos numeros."""
    await bot.say(left + right)

@bot.command()
async def unido(member : discord.Member):
    """Dice cuando se unio un miembro."""
    await bot.say('{0.name} se unio el {0.joined_at}'.format(member))

@bot.command()
async def ejecuta(comando:str):
    await bot.say('ejecutando {}'.format(comando))


    # elif message.content.startswith('!acevedo'):
    #     import requests
    #     r = requests.post("https://neomatrix.herokuapp.com/graphql", data={'query': '{ neomatrix{ nombre email } }'})
    #     await client.send_message(message.channel, 'los datos son {} '.format(r.text))


bot.run("MzQ0OTIzODQzNjE1MzkxNzQ1.DG0PBQ.F5JANrRjCIvpenMfzmLBisYxaXo")
