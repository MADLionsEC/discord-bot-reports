import discord
from random import randint
from os import listdir

TOKEN = ''

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        msg = 'Hi {0.author.mention}! Use !report to get the SoloQ report of MAD Lions E.C. LoL pro team or ' \
              '!memes to laugh a bit ;)'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!report'):
        msg = 'There you have it, {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

        img_folder = 'images'
        patch_img_path = '{}/patch.png'.format(img_folder)
        picks_img_path = '{}/picks.png'.format(img_folder)

        await client.send_file(message.channel, patch_img_path)
        await client.send_file(message.channel, picks_img_path)

    if message.content.startswith('!meme'):
        msg_pool = ['haHAA', 'Hold my beer...', 'So much xD', 'Praise the memes!', 'Ayy lMaokai']
        msg = msg_pool[randint(0, len(msg_pool) - 1)]
        await client.send_message(message.channel, msg)

        memes_folder = 'memes'
        img_pool = listdir(memes_folder)
        img = img_pool[randint(0, len(img_pool) -1)]
        await client.send_file(message.channel, '{}/{}'.format(memes_folder, img))


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
