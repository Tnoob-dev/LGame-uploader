from rich import print as rprint
from .APICalls import APICall

def add_game(api: APICall):
    json_structure = {
            "name": "",
            "image": "",
            "genre": [],
            "description": "",
            "trailer": "",
            "console": ""
        }

    name = str(input("Introduzca el nombre del juego: "))
    if name.strip():
        json_structure["name"] = name
    else:
        print("El texto no puede estar vacio")

    image = str(input("\nIntroduzca la ruta absoluta de la foto a la que pertenece el juego: "))
    if image.strip():
        json_structure["image"] = image
    else:
        print("El texto no puede estar vacio")

    genre = str(input("\nAhora introduzca el/los generos del juego, en caso de tener mas de uno, separelos por espacios EJ: [RPG Accion Sci-Fi]: "))
    if genre.strip():
        json_structure["genre"] = genre.split(" ")
    else:
        print("El texto no puede estar vacio")

    description = str(input("\nIntroduzca una breve descripcion sobre el juego: "))
    if description.strip():
        json_structure["description"] = description
    else:
        print("El texto no puede estar vacio")

    trailer = str(input("\nIntroduzca el enlace a donde lleva el trailer del juego: "))
    if trailer.strip():
        json_structure["trailer"] = trailer
    else:
        print("El texto no puede estar vacio")

    console = str(input("""\nPor ultimo diga a que consola pertenece este juego, escribala bien, las consolas disponibles son:
[PS2, PS3, PS4, PS5, XBOX 360, XBOX ONE, XBOX Series, Nintendo Switch, Wii, Wii U, DS, 3DS, PSP, PSVita, Android, PC, VR]
No se preocupe por el tema de las mayusculas o minusculas, solo escriba el nombre bien: """))
    if console.strip():
        json_structure["console"] = console.lower()
    else:
        print("El texto no puede estar vacio")

    st_code = api.add_games(json_structure)

    if st_code == 201:
        rprint("\n[bold dark_green]Juego añadido con exito :D[/bold dark_green] podemos pasar al siguiente")
    else:
        rprint(f"\n[bold dark_red]Error al añadir el juego. Código de estado: {st_code}[/bold dark_red]")