#!/usr/bin/env julia

module JuliaTanBot


export julia_tan

using PyCall

@pyimport textwrap
@pyimport discord.ext.commands as discord

function julia_tan()
    dd  = textwrap.dedent
    bot = discord.Bot(command_prefix = "j", description = "bot julia tan")
    separador = "#" ^ 80
    
    py"""
    import re
    patron = \"^(\s*|\s*`\s* |\s*```\s+|\s*```julia\s+)(.*?)(\s*\s*`\s*|\s*```\s* |)$\"
    """

    py"""
    @$bot.event
    async def on_ready():
        print($dd(
            '''
            {0}

            Julia-tan JuliaLangEs Discord bot.

            BOT NAME: {1}
            BOT ID  : {2}

            {0}
            '''.format(
                $separador,
                $bot.user.name,
                $bot.user.id
            )
        ))
    """

    py"""
    @$bot.command()
    async def l(*, entrada: str):
        eval  = $eval
        parse = $parse
        entrada= entrada.replace(\"\n\", \";\")
        comando   = re.match(patron, entrada)
        print(\"Entrada: \",entrada)
        print(\"Comando: \",comando)
        if (comando!=None):
            comando=comando.group(0)
            resultado = eval(parse(comando))
        else:
            resultado = eval(parse(entrada))
        comando= comando.replace(\";\", \"\n        julia> \")
        print(\"Resultado: \",resultado)
        await $bot.say($dd(
            '''
            ```julia
            julia> {0}
            {1}
            ```
            '''.format(comando, resultado)
        ))
    """

    bot[:run](ENV["DISCORD_BOT_TOKEN"])
end

end  # module

using JuliaTanBot


julia_tan()
