import discord
import random
import asyncio
import re
import json
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = ['I.', 'i.'])

disablelist = 'disablelist.json'
hatelist = 'hatelist.json'
lovelist = 'lovelist.json'

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('with your feelings'))
	print('bot started')

@client.command()
async def hate(ctx, *args):
	# ensure proper usage
	with open(disablelist) as readfile:
		data = json.load(readfile)
	if ctx.author.id in data:
		await ctx.message.add_reaction('\N{CROSS MARK}')
		return
	if len(args) < 1:
		await ctx.send(f"Either tag someone or paste their user ID")
		return
	rx = re.search("[0-9]+", args[0])
	if rx:
		usrID = int(rx[0])
	else:
		await ctx.send(f"Either tag someone or paste their user ID. {args[0]} is useless to me.")
		return
	if usrID in data:
		await ctx.message.add_reaction('\N{CROSS MARK}')
		return

	# rule out edge cases
	if usrID == 196890612769751040:
		await ctx.send('impossible...')
		return
	if (usrID == client.user.id) or (usrID == ctx.author.id):
		await ctx.send('I hate u too <3')
		return

	# intended usage
	try:
		user = await client.fetch_user(usrID)
		await ctx.message.add_reaction('\N{SERIOUS FACE WITH SYMBOLS COVERING MOUTH}')
	except:
		await ctx.send(f"Either tag someone or paste their user ID. {args[0]} is neither.")
		return

	with open(hatelist) as readfile:
		data = json.load(readfile)
	await user.send(random.choice(data))
	if len(args)>1 and args[1] == 'anon':
		try:
			await ctx.message.delete()
		except:
			await ctx.send(f"Couldn't delete your message soz :/")
@client.command()
async def love(ctx, *args):
	# ensure proper usage
	with open(disablelist) as readfile:
		data = json.load(readfile)
	if ctx.author.id in data:
		await ctx.message.add_reaction('\N{CROSS MARK}')
		return
	if len(args) < 1:
		await ctx.send('good for you!')
		return
	rx = re.search("[0-9]+", args[0])
	if rx:
		usrID = int(rx[0])
	else:
		await ctx.send(f"Either tag someone or paste their user ID. {args[0]} is useless to me.")
		return
	if usrID in data:
		await ctx.message.add_reaction('\N{CROSS MARK}')
		return

	# rule out edge cases
	if (usrID == client.user.id) or (usrID == ctx.author.id):
		await ctx.send('wow')
		return

	# intended usage
	try:
		user = await client.fetch_user(usrID)
		await ctx.message.add_reaction('\N{BABY ANGEL}')
	except:
		await ctx.send(f"Either tag someone or paste their user ID. {args[0]} is neither.")
		return
	with open(lovelist) as readfile:
		data = json.load(readfile)
	await user.send(random.choice(data))
	if len(args)>1 and args[1] == 'anon':
		try:
			await ctx.message.delete()
		except:
			await ctx.send(f"Couldn't delete your message soz :/")

@client.command()
async def disable(ctx):
	with open(disablelist) as readfile:
		data = json.load(readfile)
	if ctx.author.id in data:
		await ctx.send("you've already opted out")
	else:
		data.append(ctx.author.id)
		with open(disablelist, 'w', encoding='utf8') as outfile:
			json.dump(data, outfile, indent=4)
		await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

@client.command()
async def enable(ctx):
	with open(disablelist) as readfile:
		data = json.load(readfile)
	if ctx.author.id in data:
		data.remove(ctx.author.id)
		with open(disablelist, 'w', encoding='utf8') as outfile:
			json.dump(data, outfile, indent=4)
		await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')
	else:
		await ctx.send("you've already opted in")

@client.command()
async def addhate(ctx, *, args):
	with open(hatelist) as readfile:
		data = json.load(readfile)
	if args in data:
		await ctx.send("this already exists")
	else:
		data.append(args)
		with open(hatelist, 'w', encoding='utf8') as outfile:
			json.dump(data, outfile, indent=4)
		await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')

@client.command()
async def addlove(ctx, *, args):
	with open(lovelist) as readfile:
		data = json.load(readfile)
	if args in data:
		await ctx.send("this already exists")
	else:
		data.append(args)
		with open(lovelist, 'w', encoding='utf8') as outfile:
			json.dump(data, outfile, indent=4)
		await ctx.message.add_reaction('\N{WHITE HEAVY CHECK MARK}')


client.run('discord_token')
