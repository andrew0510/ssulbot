import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("Im , Good!")
    game = discord.Game('썰-SSUL')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 687160850644992030:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="썰-SSUL 이 올라왔나봐요!")
                        embed.add_field(name="공지 입니다!", value=msg, inline=True)
                        embed.set_footer(text=f"썰-SSUL (수한이)")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzQ2NTc4ODUxODc3ODc5ODY5.X0CXvQ.5asDLoejQeBLSPVs5Udo8iI77iw')
