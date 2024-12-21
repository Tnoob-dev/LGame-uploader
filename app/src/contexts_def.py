from src.APICalls import APICall
from src.game import add_game_online, add_game_offline
from rich import print as rprint
from src.settings import create_settings
import json

def offline_main():
    try:
        
        rprint("[bold red]Para salir en cualquier momento de la APP, presione Ctrl+C o simplemente termine el proceso[/bold red]")

        while True:
            add_game_offline()
                
    except Exception as e:
        rprint(f"\n[bold dark_red]Algo ocurrio[/bold dark_red] -> {e}\n")
        rprint("[bold yellow]Presione cualquier tecla para salir[/bold yellow]")
        input()
    

def online_main():
    create_settings()
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