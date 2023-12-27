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


def run(token: str):
    client.run(token, log_handler=None)
