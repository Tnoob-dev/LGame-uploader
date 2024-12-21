from src.contexts_def import online_main, offline_main
from src.question import ask_on_off

def main():
    option = int(input("Seleccione un numero\n1.Online\n2.Offline\n\n"))
    if ask_on_off(option):
        online_main()
    elif not ask_on_off(option):
        offline_main()
    elif ask_on_off(option) is None:
        print("Seleccion invalida, seleccione al una opcion de las que se le ofrece")
        return

if __name__ == "__main__":
    main()
