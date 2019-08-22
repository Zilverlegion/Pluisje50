import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'F2:21:36:78':
        if message.content == 'Hades'
            await message.channel.send('[table]')
            await message.channel.send('[*]NR[|]|Stad[|]|F2:[|]|Toren[|]|Muur[|]|God[|]|Aanwezig[|]|Bir/Lt[/*]')
            await message.channel.send('[*]1[|]|[town]?[/town][|]|21:36:78[|]|???[|]|??[|]Hades|[|]|????[|]|???[/*]')
            await message.channel.send('[/table]')

import

client = MyClient()
client.run('NjEzNzA1NTM5NTM2Mjg5ODI0.XV2njA.89RHDsyJx5D7T88qJm4IZNKcO7g')