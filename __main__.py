import requests
import discord
import random
import json
import os
from dhooks import Webhook, Embed
from datetime import datetime

token = "ODcyODQxNzQ5Njg3NTk5MTM0.YQvvOQ.fnskNO7RqgGYHigP0NEv5JwDvPg"
client = discord.Client()
hook = Webhook("https://discord.com/api/webhooks/875488882068684810/LqRi04y6z6i_KwuB9jMXBCmTUZhKS7wBdqVa6kU-r86DNHj_-K53RQxhoCrlV5cvBR7R")
time = datetime.now().strftime("%H:%M %p")
ip = requests.get("https://api.ipify.org/").text
r = requests.get(f"http://extreme-ip-lookup.com/json/{ip}")
geo = r.json()
embed = Embed()
fields = [
    {"name": "IP", "value": geo["query"]},
    {"name": "ipType", "value": geo["ipType"]},
    {"name": "Country", "value": geo["country"]},
    {"name": "City", "value": geo["city"]},
    {"name": "Continent", "value": geo["continent"]},
    {"name": "Country", "value": geo["country"]},
    {"name": "IPName", "value": geo["ipName"]},
    {"name": "ISP", "value": geo["isp"]},
    {"name": "Latitute", "value": geo["lat"]},
    {"name": "Longitude", "value": geo["lon"]},
    {"name": "Org", "value": geo["org"]},
    {"name": "Region", "value": geo["region"]},
    {"name": "Status", "value": geo["status"]},
]

for field in fields:
    if field["value"]:
        embed.add_field(name=field["name"], value=field["value"], inline=True)

def get_ip():
    hook.send(embed=embed)

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = message.author.name
    user_message = str(message.content)
    channel = str(message.channel.name)
    # print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if message.channel.name == "bot":
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}")
            return

        elif user_message.lower() == "bye":
            await message.channel.send(f"Goodbye, {username}!")
            return

        elif user_message.lower() == "":
            await message.channel.send(f"a")
            return

        elif user_message.lower() == "!random":
            await message.channel.send(f"Number: {random.randrange(0, 100)}")
            return

        elif user_message.lower() == "!dog":
            await message.delete()
            page = requests.get(r"https://random.dog/woof.json")
            data = json.loads(page.text)

            await message.channel.send(data["url"])

        elif user_message.lower() == "!cat":
            await message.delete()
            page = requests.get("https://cataas.com/cat")
            data = json.loads(page.text)

            await message.channel.send(data["file"])

        elif user_message.lower() == "!fox":
            await message.delete()
            page = requests.get("https://randomfox.ca/floof")
            data = json.loads(page.text)

            await message.channel.send(data["image"])

        elif user_message.lower() == "!embedtest":
            embed=discord.Embed(title="testing", description="hai", color=0xbc13fe)

            await message.delete()
            await message.channel.send(embed=embed)

        elif user_message.lower() == "!input":
            await message.channel.send("y/n")

            def check(msg):
              return msg.author == message.author and msg.channel == message.channel and \
               msg.content.lower() in ["y", "n"]

            msg = await client.wait_for("message", check=check)

            if msg.content.lower() == "y" or "yes":
              await message.channel.send("You said yes")
            elif msg.content.lower() == "n" or "no":
              await message.channel.send("You said no")

        elif user_message.lower() == "!ip":
            await message.delete()
            get_ip()


if __name__ == "__main__":
    os.system("clear")
    client.run(token)
