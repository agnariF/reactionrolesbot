import os
import discord

intents = discord.Intents.default()
intents.reactions = True
intents.members = True

client = discord.Client(intents=intents)

ranks = {
    "unranked": "Unranked",
    "bronze": "Bronze",
    "silver": "Silver",
    "gold": "Gold",
    "platinum": "Platinum",
    "diamond": "Diamond",
    "champ": "Champ",
    "gc": "Grand Champ",
   }

@client.event
async def on_ready():
    print(f'{client.user.name} aka the noob has connected to Discord!')

"""                
Reaction added, gives rank
"""
        
@client.event
async def on_reaction_add(reaction, user):
    
    message = reaction.message

    if message.content == "Set your rank!":
    

        for emoji_name, role_name in ranks.items():
            if reaction.emoji.name == emoji_name:
                role = discord.utils.get(message.guild.roles, name=role_name)
                await user.add_roles(role)
                print("Added role " + role_name + " to " + str(user))

"""                
Reaction removed
"""
@client.event
async def on_reaction_remove(reaction, user):
    #print("on_reaction_remove")
    
    message = reaction.message
    if message.content == "Set your rank!":

        for emoji_name, role_name in ranks.items():
            if reaction.emoji.name == emoji_name:
                role = discord.utils.get(message.guild.roles, name=role_name)
                await user.remove_roles(role)
                print("Removed role " + role_name + " from " + str(user))


client.run(TOKEN)
