import discord as d
import json
import requests

client = d.Client()


@client.event #initiate
async def on_ready():
    print(f'We are ready to rumble with {client.user}')


def random_joke():

    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    json_data = json.loads(response.text)
    print(json_data)
    if 'setup' in json_data:
        setup = json_data['setup']
        delivery = json_data['delivery']
        joke = setup+"\n"+delivery
        return joke
    else:
        joke = json_data['joke']
        return joke


@client.event #Display the event activity
async def on_message(message):
    print(f'{message.channel} : {message.author} : {message.author.name} : {message.content}')
    daxter_guild = client.get_guild(815090919384547418) #discord server ID

    if "-daxter" == message.content.lower(): #test welcome message
        await message.channel.send("Bot Daxter at your service.")
    elif "-mcount" == message.content.lower(): #member count
        await message.channel.send(f'User count is {daxter_guild.member_count}')
    elif "-joke" == message.content.lower(): #returns a random joke
        joke = random_joke()
        await message.channel.send(f'''
                    {joke}
    ''')
    elif "-mstatus" == message.content.lower(): #member status
        online = 0
        offline = 0
        idle = 0
        for m in daxter_guild.members:
            print(f'm.status: {m.status}')
            if str(m.status) == "online":
                online += 1
            if str(m.status) == "offline":
                offline += 1
            else:
                idle += 1

        await message.channel.send(f'Online: {online} , Offline: {offline}, Idle: {idle}')

token = open('token.txt','r')
client.run(token.read())



