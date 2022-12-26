import lightbulb

bot = lightbulb.BotApp(token=open('tokens/token_ds.txt', 'r').read(), default_enabled_guilds=(int(open('tokens/ds_channel_id.txt', 'r').read())))

@bot.command
@lightbulb.command('msg_asmv', 'Saudação Asimov Academy')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond('*Olá Comunidade Asimov Academy!*')

#Piadas

import random

joke1 = "Dois litros de leite atravessaram a rua e foram atropelados. Um morreu, o outro não, por quê?\nPor que um deles era Longa Vida...\n(puuutz)"
joke2= "Por que o elefante não pega fogo?\nPorque ele já é cinza\n(sem comentários)"
joke3 = "Se o cachorro tivesse religião, qual seria?\nCão-domblé\n(HAHAHA!)"
joke4 = "O que o cavalo foi fazer no orelhão?\nPassar um trote...\n(eu quero morrer)"
joke5 = "O que dá o cruzamento de pão, queijo e um macaco?\nX-panzé\n(kakakakaka)"
joke6 = "O que o tomate foi fazer no banco?\nFoi tirar extrato...\n(kskskskskks)"
joke7 = "O que a galinha foi fazer na igreja?\nAssistir a Missa do Galo.\n(aguenta aí!)"
joke8 = "Como as enzimas se reproduzem?\nFica uma enzima da outra\n(hueheuehue)"
joke9 = "Por que a Coca-Cola e a Fanta se dão muito bem?\nPorque se a Fanta quebra, a Coca-'Cola'!\n (péeessima!)"
joke10 = "Por que não é bom guardar o quibe no freezer?\nPorque lá dentro ele esfirra!\n(óóó!!!)"

piadas = [joke1, joke2, joke3, joke4, joke5, joke6, joke7, joke8, joke9, joke10]
@bot.command
@lightbulb.command('piada', 'Receba uma piada!')
@lightbulb.implements(lightbulb.SlashCommand)

async def joke(ctx):
    n = random.randint(1,10)
    await ctx.respond(f"*{piadas[n]}*")

#Calculadora
@bot.command
@lightbulb.command('calculadora', 'Calculadora')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_calculator(ctx):
    pass

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('soma', 'Operação de Adição')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def soma(ctx):
    r = ctx.options.n1 + ctx.options.n2
    await ctx.respond(f"*O resultado é  **{r}***")

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('subtracao', 'Operação de Subtração')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subtracao(ctx):
    r = ctx.options.n1 - ctx.options.n2
    await ctx.respond(f"*O resultado é  **{r}***")

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('multiplicacao', 'Operação de Multiplicação')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def multiplicacao(ctx):
    r = ctx.options.n1 * ctx.options.n2
    await ctx.respond(f"*O resultado é  **{round(r, 1)}***")

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('divisao', 'Operação de Divisão')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def divisao(ctx):
    r = ctx.options.n1 / ctx.options.n2
    await ctx.respond(f"*O resultado é  **{round(r, 1)}***")

#Temperatura
import requests
import string

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('tokens/api_weather_key.txt', 'r').read()

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

@bot.command
@lightbulb.option('pais', 'País', type=str)
@lightbulb.option('cidade', 'Cidade', type=str)
@lightbulb.command('temperatura', 'Informe uma cidade e seu país para saber as condições climáticas atuais! ')
@lightbulb.implements(lightbulb.SlashCommand)

async def temperatura(ctx):
    country = ctx.options.pais
    CITY = string.capwords(ctx.options.cidade) + "," + country[0:2].lower()

    url = BASE_URL + "q=" + CITY + "&APPID=" + API_KEY 
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    umidade = response['main']['humidity']
    vento = response['wind']['speed']

    temp_celsius = str(round(kelvin_to_celsius(temp_kelvin)))

    await ctx.respond(f'```A temperatura atual em {string.capwords(ctx.options.cidade)} é de {temp_celsius}°c\ne a umidade do ar: {umidade}% com ventanias de {vento}m/s```')
bot.run()