import os
import requests
import json
import subprocess
import time
from colorama import Fore, init
from pystyle import Colors, Colorate, Center

init()

ascii_art = r'''

 █████   █████ █████ ██████████   ██████████   ██████████ ██████   █████    ██████████   ███████████ 
░░███   ░░███ ░░███ ░░███░░░░███ ░░███░░░░███ ░░███░░░░░█░░██████ ░░███    ░░███░░░░███ ░░███░░░░░███
 ░███    ░███  ░███  ░███   ░░███ ░███   ░░███ ░███  █ ░  ░███░███ ░███     ░███   ░░███ ░███    ░███
 ░███████████  ░███  ░███    ░███ ░███    ░███ ░██████    ░███░░███░███     ░███    ░███ ░██████████ 
 ░███░░░░░███  ░███  ░███    ░███ ░███    ░███ ░███░░█    ░███ ░░██████     ░███    ░███ ░███░░░░░███
 ░███    ░███  ░███  ░███    ███  ░███    ███  ░███ ░   █ ░███  ░░█████     ░███    ███  ░███    ░███
 █████   █████ █████ ██████████   ██████████   ██████████ █████  ░░█████    ██████████   ███████████ 
░░░░░   ░░░░░ ░░░░░ ░░░░░░░░░░   ░░░░░░░░░░   ░░░░░░░░░░ ░░░░░    ░░░░░    ░░░░░░░░░░   ░░░░░░░░░░░  
         
'''

credits = '''
        Credits:
    Github: @JohnEdgarHoover
    Discord: John_Edgar_Hoover
'''

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    colored_ascii_art = Colorate.Horizontal(Colors.white_to_green, ascii_art, 1)
    print(Center.XCenter(colored_ascii_art))
    print(Center.XCenter(credits))
    option_prompt = Colorate.Horizontal(Colors.white_to_green, "Enter Pseudo,IP ou ID Discord: ", 1)
    print(Center.XCenter(option_prompt), end="")

def search_database(query):
    database_folder = os.path.join(os.path.dirname(__file__), "Database")
    result = []
    if os.path.exists(database_folder):
        for filename in os.listdir(database_folder):
            if filename.endswith(".txt"):
                filepath = os.path.join(database_folder, filename)
                with open(filepath, "r", encoding="latin1") as file:
                    for line in file:
                        if query.lower() in line.lower():
                            result.append(line.strip())
    return result

def main():
    while True:
        display_menu()
        query = input().strip()
        if query.lower() == "exit":
            print("Exiting Database Searcher...")
            time.sleep(2)
            return
        print(f"Recherche dans les databases pour: {query}")
        search_result = search_database(query)
        if search_result:
            print("\nSearch Result:")
            for entry in search_result:
                print(entry)
        else:
            print("Aucune information trouvé.")
        while True:
            choice = input("\nVoulez-vous rechercher une autre personne ? (y/n): ").strip().lower()
            if choice == 'y':
                break
            elif choice == 'n':
                print("Exiting Database Searcher...")
                time.sleep(2)
                return
            else:
                print("Choix invalide. veuillez entrer 'y' or 'n'.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting Database Searcher...")
