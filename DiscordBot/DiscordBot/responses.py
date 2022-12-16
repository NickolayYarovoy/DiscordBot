import re
import discord
import numpy as np
import json
import respect
import funcs
import parse

config = ''

with open('config.json', 'r') as conf_file:
    config = json.load(conf_file)

def delete_prefix(message: str) -> str:
    return re.sub(rf'{config["prefix"]}', '', message, count = 1)

async def handle_response(message):
    author = message.author
    content = delete_prefix(message.content).lower()

    if content == 'photo':
        with open(rf'Data\Photoes\{np.random.randint(1, 16)}.jpg', 'rb') as f:
            photo = discord.File(f)
            await message.channel.send(file = photo)
    
    if re.match(r'respect|\+', content) != None:
        for user in message.mentions:
            if user != author:
                if not respect.add_respect(user.id):
                    await message.channel.send('This user has received respect within the last hour')

    if re.match(r'rating', content) != None:
        if content == 'rating':
            await message.channel.send(f'Rating of {author.mention} is {respect.get_respect(author.id)}')
        else:
            for user in message.mentions:
                await message.channel.send(f'Rating of {user.mention} is {respect.get_respect(user.id)}')

    if content == 'roll':
        await message.channel.send(f'{np.random.randint(1,7)}')

    if re.match(r'calculate ', content) != None:
        await message.channel.send(eval(re.sub('\^', '**', re.sub('calculate ', '', content))))

    if re.match(r'exchange', content) != None:
        currency = re.sub('exchange ', '', content)
        data = parse.get_currencies(currency)
        await message.channel.send(data)

    await message.delete()



