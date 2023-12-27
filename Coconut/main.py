import discord

client = discord.Client(intents=discord.Intents.all())


def run(token: str):
    client.run(token)
