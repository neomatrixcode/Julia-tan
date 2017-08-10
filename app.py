#!/usr/bin/env python3.6

from os import getenv
from subprocess import getoutput

from discord.ext.commands import Bot

separator = '#' * 40
description = '''Soy Julia-tan, el bot de Discord del servidor de JuliaLangEs!'''
bot = Bot(command_prefix='jl>', description=description)


@bot.event
async def on_ready():
    print(
        f"""
        {separator}
        
        Julia-tan JuliaLangEs Discord bot.
        
        BOT NAME: {bot.user.name}
        BOT ID  : {bot.user.id}
        
        {separator}
        """
    )


@bot.command()
async def julia(*, command: str):
    try:
        if command.startswith("```julia\n"):
            command = command[9:-3]
        elif command.startswith("```\n"):
            command = command[4:-3]
        elif command.startswith("`"):
            command = command[1:-1]

        result = getoutput(f"julia -e {command}")
        await bot.say(
            f"""
            ```julia
            julia> {command}
            {result}
            
            ```
            """
        )
    except error:
        await bot.say(
            f"""
            Ooopss...
            
            Comando: 
            
            ```julia
            {command}
            ```
            
            Error:
            
            ```python
            {error}
            ```
            
            """
        )


if __name__ == '__main__':
    bot.run(getenv("DISCORD_BOT_TOKEN"))
