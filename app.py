from os import getenv
from subprocess import getoutput

from discord.ext.commands import Bot

commands.Bot()

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
async def julia(command: str):
    try:
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
        await bot.say(f"JULIA_TAN_ERROR: {error}")


if __name__ == '__main__':
    bot.run(getenv("DISCORD_BOT_TOKEN"))
