from .core import menu_principal
import time


def ejecutar_programa():
    print("--- Iniciando ---")
    time.sleep(1)
    menu_principal()
    print("--- Saliendo ---")
    time.sleep(1)


if __name__ == "__main__":
    ejecutar_programa()
