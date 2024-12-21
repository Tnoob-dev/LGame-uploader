from src.contexts_def import online_main, offline_main
from src.question import ask_on_off

def main():
    option = int(input("Seleccione un numero\n1.Online\n2.Offline\n\n"))
    if ask_on_off(option):
        online_main()
    result = ask_on_off(option)
    if result is None:
        print("Seleccion invalida, seleccione al una opcion de las que se le ofrece")
        return
    if result is True:
        offline_main()

if __name__ == "__main__":
    main()
