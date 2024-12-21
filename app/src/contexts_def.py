from pathlib import Path
from src.APICalls import APICall
from src.game import add_game_online, add_game_offline
from rich import print as rprint
from src.settings import create_settings, check_settings_folder
import json
import os

def offline_main():
    try:
        if check_settings_folder():
            os.mkdir(Path("./settings"))
            with open(Path("./settings") / "settings.json", "w", encoding="utf-8") as file:
                json.dump({"IP": ""}, file, indent=4)
                
        rprint("[bold red]Para salir en cualquier momento de la APP, presione Ctrl+C o simplemente termine el proceso[/bold red]")

        while True:
            add_game_offline()
                
    except Exception as e:
        rprint(f"\n[bold dark_red]Algo ocurrio[/bold dark_red] -> {e}\n")
        rprint("[bold yellow]Presione cualquier tecla para salir[/bold yellow]")
        input()
    

def online_main():
    if check_settings_folder():
        create_settings()
    else:
        settings_path = Path("./settings/settings.json")
        if not settings_path.exists():
            with open(settings_path, "w", encoding="utf-8") as file:
                json.dump({"IP": ""}, file, indent=4)

        with open(settings_path, "r", encoding="utf-8") as file:
            settings = json.load(file)
            if settings["IP"] == "":
                ip = input("Introduzca la IP: ")
                settings["IP"] = ip
                with open(settings_path, "w", encoding="utf-8") as file:
                    json.dump(settings, file, indent=4)
                    
    rprint("[bold cyan]Conectando con la IP...[/bold cyan]")
    file = open("./settings/settings.json", "r", encoding="utf-8")
    api = APICall(ip=json.load(file)["IP"])

    try:
        
        if api.is_alive():
            rprint("La [bold magenta]API[/bold magenta] esta [bold green]activa[/bold green]")
            rprint("[bold red]Para salir en cualquier momento de la APP, presione Ctrl+C o simplemente termine el proceso[/bold red]")

            while True:
                add_game_online(api)
                
    except Exception as e:
        rprint(f"\n[bold dark_red]Algo ocurrio[/bold dark_red] -> {e}\n")
        rprint("[bold yellow]Presione cualquier tecla para salir[/bold yellow]")
        input()