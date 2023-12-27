import discord

from . import log_manager

client = discord.Client(intents=discord.Intents.all())

logger = log_manager.get_logger()
log_manager.set_logger(logger)


@client.event
async def on_ready():
    logger.info("Ready")


@client.event
async def on_connect():
    logger.info("Connected")


@client.event
async def on_disconnect():
    logger.warning("Disconnect")


@client.event
async def on_resumed():
    logger.info("Resumed")


@client.event
async def on_message(message: discord.Message):
    content = message.content
    commands = content.split()
    length = len(commands)
    send = message.channel.send


def run(token: str):
    client.run(token, log_handler=None)
