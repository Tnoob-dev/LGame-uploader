import os
import json

def create_settings():
    if not os.path.exists("./settings/"):
        os.mkdir("./settings/")

        ip = input("Introduzca la IP: ")
        
        with open("./settings/settings.json", "w", encoding="utf-8") as file:
            json.dump({"IP": ip}, file, indent=4)
            