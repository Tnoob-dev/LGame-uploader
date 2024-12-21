from pathlib import Path
import os
import json

def check_settings_folder():
    path = Path("./settings")
    if not os.path.exists(path):
        return True
    else:
        return False

def create_settings():
    path = Path("./settings")
    if check_settings_folder() is True:
        os.mkdir(path)
        ip = input("Introduzca la IP: ")

        with open(path / "settings.json", "w", encoding="utf-8") as file:
            json.dump({"IP": ip}, file, indent=4)