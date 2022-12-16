import json
import discord
import os.path
import re
import responses
import sqlite3
import moderation

config = ''

with open('config.json', 'r') as conf_file:
    config = json.load(conf_file)

sqlite_connection = sqlite3.connect(r'Data\DataBase\sqlite_python.db')
sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS users (
                               user_id INTEGER PRIMARY KEY,
                               respect INTEGER NOT NULL,
                               warns INTEGER NOT NULL,
                               last_respect_data INTEGER NOT NULL);'''

cursor = sqlite_connection.cursor()
cursor.execute(sqlite_create_table_query)
sqlite_connection.commit()
cursor.close()

def has_prefix(message) -> bool:
    if re.fullmatch(rf'{config["prefix"]}.*', message):
        return True
    return False

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Client is ready')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Discord.py'))

@client.event
async def on_message(message):
    if moderation.moderation(message.content):
        await message.delete()
        return


    if message.author.bot:
        return

    if has_prefix(message.content):
        await responses.handle_response(message)


client.run(config['token'])