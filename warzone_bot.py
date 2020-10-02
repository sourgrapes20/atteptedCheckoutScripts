import requests
import re
import discord
from discord.ext import commands


TOKEN = 'NzE1Mzk4ODIzNDY3NTQ4NzEz.XtQMSg.a_duGRsqSq5itSHqymoqgOywypo'

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("We are up and ready to go")

@client.command()
async def stats(ctx):
    await ctx.send("command recieved")
    searchStrKda = 'displayType":"NumberPrecision2"},"weeklyHeadshotPct":{"rank":null,"percentile":null,"displayName":"Headshot Pct","displayCategory":"Weekly","category":"weekly","metadata":{},"'
    searchStrKills = 'game","displayCategory":"Weekly","category":"weekly","metadata":{},"value":'
    searchStrDamage = 'u002Fgame","displayCategory":"Weekly","category":"weekly","metadata":{},"value":'

    urls = ['https://cod.tracker.gg/warzone/profile/xbl/Enugras/overview','https://cod.tracker.gg/warzone/profile/battlenet/L%C7%BEADED%231897/overview','https://cod.tracker.gg/warzone/profile/psn/Ball1nNati0n/overview','https://cod.tracker.gg/warzone/profile/battlenet/prashugopi%231927/overview','https://cod.tracker.gg/warzone/profile/psn/COOLJESH123/overview','https://cod.tracker.gg/warzone/profile/psn/sssn99/overview','https://cod.tracker.gg/warzone/profile/psn/SgSingh43/overview','https://cod.tracker.gg/warzone/profile/atvi/SVP_2svp2_SVP/overview']
    names = ['Sargune','Muk','BallerzGAYtion','Parchu','Cooljesh','5k','Ash','Wams']
    final_kda = []
    final_kills_game = []
    final_damage_game = []


    for a in urls:
        allHtml = requests.get(a)
        soup = allHtml.text
        #print(soup)
        result = [m.start() for m in re.finditer(searchStrKda, soup)]
        i = 0
        result1 = ""
        endScrape = False
        while i < 100:
            if (soup[result[1]-50+i]) == ",":
                endScrape = not endScrape
            elif endScrape==True:
                result1 = result1 + (soup[result[1]-50+i])
            i = i+1
        weeklyKda = re.findall(r'\b\d+\b', result1)
        final_kda.append(weeklyKda)
        #FINAL_KDA IS COMPLETE NOW FIND DAMAGE/GAME
        result1 = ""
        i = 0
        result = [m.start() for m in re.finditer(searchStrKills, soup)]
        while i < 90:
            result1 = result1 + (soup[result[0]+i])
            i = i+1
        killsPerGame = re.findall(r'\b\d+\b', result1)
        final_kills_game.append(killsPerGame)
        #FINAL_KILLS_GAME IS COMPLETE NOW FIND DAMAGE/GAME
        result1 = ""
        i = 0
        result = [m.start() for m in re.finditer(searchStrDamage, soup)]
        while i < 100:
            result1 = result1 + (soup[result[2]+i])
            i = i+1
        damagePerGame = re.findall(r'\b\d+\b', result1)
        final_damage_game.append(damagePerGame)
        #FOUND DAMAGE PER GAME

    final_string = "```"
    i = 0
    while i < len(names):
        final_string = final_string + names[i] + " past weeks kda: "
        numberCrunch = final_kda[i][0] + '.' + final_kda[i][1]
        final_string = final_string + numberCrunch + "\n"
        final_string = final_string + names[i] + " past weeks kills/game: "
        numberCrunch = final_kills_game[i][0] + '.' + final_kills_game[i][1]
        final_string = final_string + numberCrunch + "\n"
        final_string = final_string + names[i] + " past weeks damage/game: "
        final_string = final_string + final_damage_game[i][0] + "\n\n"
        i = i+1
    
    final_string = final_string + "```"



    #print(final_kda)
    #print(final_kills_game)
    #print(final_damage_game)
    await ctx.send(final_string)

@client.command()
async def stop(ctx):
    await ctx.send("Shutting down.")
    await client.logout()

client.run(TOKEN)