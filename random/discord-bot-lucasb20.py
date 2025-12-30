import discord, random
import senhadale
#global vars for ease of use
client = discord.Client()
guild = discord.Guild
monkey = "🐒"
respostas = ["https://tenor.com/view/4lan-maozinha-chaves-pcc-post-gif-19231028", "fdp ", "metsu fdp", "tiko fdp"]
impostor = ["assassino", "sus", "amogus", "among", "us", "impostor"]
@client.event
async def on_ready():
    print('Logged in as {0.user}'
    .format(client))
@client.event
async def on_message(message):
        msg = message.content
        if message.author == client.user:
            return

        if any(word in msg for word in ["'-'", "4lan", monkey, ":O"]):
            await message.channel.send(random.choice(respostas) + ' ' + monkey)

        if any(word in msg for word in impostor):
            await message.channel.send("SUS SUS SUS SUS USS AHAHAHAHA SUS SUS IMPOSTOR AMOGUS SUS SUSU S AAHAHAHA HAHA HAHS QUER OUVIR OUTRA PIADA MURRAY?  O QUÊ VOCÊ CONSEGUE QUANDO CRUZA UM DOENTE MENTAL SOLITÁRIO COM A SOCIEDADE QUE ABANDONA ELE E TRATA COMO UM LIXO ESSE CARA EU TE DIGO O QUÊ VOCÊ CONSEGUE VOCÊ CONSEGUE A MERDA QUE MERECE AHAHAHAH")

client.run(senhadale.senha)

