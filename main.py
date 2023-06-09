#The client uses events to make it work
import os
import random
import discord 
from discord.ext import commands, tasks

#every bot command to start with a period
client = commands.Bot(command_prefix = ".") 

@client.event #this registers an event
async def on_ready():
  print('Jia bot is logged in as {0.user}'.format(client))
  #this is called when the bot is ready to start being used
  
@client.event
async def on_message(message):
  if message.content.startswith('$hello'):
    if message.author.id == 207251811504095232:
      await message.channel.send("hi jun!")
    else:
      await message.channel.send("hello")
  if message.content.startswith('$num'):
    value = random.randint(0, 100)
    await message.channel.send("random value is " + str(value))
  await client.process_commands(message)
 
@client.command(aliases = ["8ball"])
async def _8ball(ctx, *, question):
  responses =  ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.event
async def on_join():
  
  
#the id of eveyone who might use the bot
"""
players =  {'P' : 170311349975384064,
            'H' : 161262186033840129,
            'K' : 528004487655194625,
            'N' : 239853470142824449,
            'G' : 212712880124985346,
            'C' : 263063203892690945}
            
            
#a dictionary of dictsto store the money being moved through bets and buy backs
moneyOwed ={'P': {'h': 0, 'k': 0, 'n': 0, 'g': 0, 'c': 0, 'j': 0},
            'H': {'p': 0, 'k': 0, 'n': 0, 'g': 0, 'c': 0, 'j': 0},
            'K': {'h': 0, 'p': 0, 'n': 0, 'g': 0, 'c': 0, 'j': 0},
            'N': {'h': 0, 'k': 0, 'p': 0, 'g': 0, 'c': 0, 'j': 0},
            'G': {'h': 0, 'k': 0, 'n': 0, 'p': 0, 'c': 0, 'j': 0},
            'C': {'h': 0, 'k': 0, 'n': 0, 'g': 0, 'p': 0, 'j': 0},
            'J': {'h': 0, 'k': 0, 'n': 0, 'g': 0, 'p': 0, 'c': 0}}
            
#, check=check
@client.command(aliases = ["play"])
async def _play(ctx):
  await ctx.send("enter BUY-IN separated by ':', when finished write 'done'.")
  buy_in = await client.wait_for("message")
  while buy_in != "done":
    buyin_split = buy_in.split(":")
    for key in bIn_cOut.keys():
      if buyin_split[0] == key:
        bIn_cOut[key]['buyin'] == buyin_split[1]
    buy_in = await client.wait_for("message")
  await ctx.send("enter BUY-BACK separated by ':', when finished write 'done'.")      
  buy_back = await client.wait_for("message")
  while buy_back != "done":
    buyback_split = buy_back.split(":")
    for key, value in players.items():
      if client.author.id == value:
        moneyOwed[key][buyback_split[0]] = int(buyback_split[1])
    buy_back = await client.wait_for("message")
  await ctx.send("enter CASH-OUT separated by ':', when finished write 'done'.")
  cash_out = await client.wait_for("message")
  while cash_out != "done":
    cashout_split = cash_out.split(":")
    for key in bIn_cOut.keys():
      if cashout_split[0] == key:
        bIn_cOut[key]['cachout'] == cashout_split[1]
    cash_out = await client.wait_for("message")

  await ctx.send(*moneyOwed.items(), sep = "\n")

"""
  
client.run(os.getenv("JiaTOKEN"))
