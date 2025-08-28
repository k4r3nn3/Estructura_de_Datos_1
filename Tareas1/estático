# Modelo Estático: Automóvil como estructura fija (ADT con diccionario)
class AutomovilEstatico:
    def __init__(self, marca, modelo, color, anio):
        # Estructura estática: datos definidos al crear el objeto
        self._datos = {
            "marca": marca,
            "modelo": modelo,
            "color": color,
            "anio": anio
        }

    # Getter
    def get(self, clave):
        return self._datos.get(clave, None)

    # Setter
    def set(self, clave, valor):
        if clave in self._datos:
            self._datos[clave] = valor
        else:
            print(f"Error: '{clave}' no es un atributo válido.")

    # Mostrar información
    def mostrar(self):
        print("Automóvil (Estático):")
        for k, v in self._datos.items():
            print(f"  {k.capitalize()}: {v}")
