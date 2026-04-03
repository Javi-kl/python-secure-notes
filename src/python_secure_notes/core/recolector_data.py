class RecolectorDatos:
    @staticmethod
    def recibir_titulo():
        titulo_input = input("Introduce el titulo.\n-> ").lower().strip()
        if not titulo_input:
            raise ValueError("Rellena todos los campos")

        if titulo_input.isdigit():
            raise ValueError("El titulo no puede contener solo digitos")

        if len(titulo_input) > 150:
            raise ValueError("Titulo demasiado largo. Max: 150 caracteres")
        return titulo_input

    @staticmethod
    def recibir_cuerpo():
        cuerpo_input = input("Introduce el cuerpo.\n-> ").lower()
        if not cuerpo_input:
            raise ValueError("Rellena todos los campos")

        if len(cuerpo_input) > 5000:
            raise ValueError("Cuerpo demasiado largo. Max: 5000 caracteres")
        return cuerpo_input

    @staticmethod
    def crear_contenido():
        titulo_input = RecolectorDatos.recibir_titulo()
        cuerpo_input = RecolectorDatos.recibir_cuerpo()
        contenido = {
            "titulo": titulo_input,
            "cuerpo": cuerpo_input,
        }
        return contenido