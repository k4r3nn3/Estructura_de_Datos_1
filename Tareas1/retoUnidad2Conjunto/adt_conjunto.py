# 
"""
Reto 2 ADT Conjunto
Tema: Sistema de filtros para una tienda online (ej: Mercado Libre)
"""

# === 1. Estructura Dinámica: Filtros de búsqueda (tamaños, colores, etc.) ===
class Nodo:
    def __init__(self, valor):
        self._valor = valor
        self._siguiente = None

class ConjuntoDinamico:
    """Usado para filtros dinámicos (ej: lista de marcas disponibles)"""
    def __init__(self):
        self._cabeza = None

    @property
    def elementos(self):
        lista = []
        actual = self._cabeza
        while actual:
            lista.append(actual._valor)
            actual = actual._siguiente
        return lista

    @elementos.setter
    def elementos(self, valores):
        self._cabeza = None
        for valor in valores:
            self.agregar(valor)

    def agregar(self, valor):
        if not self.contiene(valor):
            nuevo = Nodo(valor)
            nuevo._siguiente = self._cabeza
            self._cabeza = nuevo

    def contiene(self, valor):
        actual = self._cabeza
        while actual:
            if actual._valor == valor:
                return True
            actual = actual._siguiente
        return False

    def quitar(self, valor):
        actual = self._cabeza
        anterior = None
        while actual:
            if actual._valor == valor:
                if anterior:
                    anterior._siguiente = actual._siguiente
                else:
                    self._cabeza = actual._siguiente
                return True
            anterior = actual
            actual = actual._siguiente
        return False

    def __str__(self):
        return "{" + ", ".join(map(str, self.elementos)) + "}"


# === 2. Estructura Estática: Filtros predefinidos (ej: tallas en ropa) ===
class ConjuntoEstatico:
    """Usado cuando hay un número fijo de opciones (ej: tallas S, M, L, XL, XXL)"""
    def __init__(self, capacidad):
        self._capacidad = capacidad
        self._datos = [None] * capacidad
        self._tamanio = 0

    @property
    def elementos(self):
        return [self._datos[i] for i in range(self._tamanio)]

    @elementos.setter
    def elementos(self, valores):
        self._tamanio = 0
        for valor in valores:
            self.agregar(valor)

    def agregar(self, valor):
        if self._tamanio >= self._capacidad:
            raise OverflowError(f"Capacidad máxima alcanzada: {self._capacidad}")
        if not self.contiene(valor):
            self._datos[self._tamanio] = valor
            self._tamanio += 1

    def contiene(self, valor):
        return valor in self._datos[:self._tamanio]

    def quitar(self, valor):
        for i in range(self._tamanio):
            if self._datos[i] == valor:
                for j in range(i, self._tamanio - 1):
                    self._datos[j] = self._datos[j + 1]
                self._datos[self._tamanio - 1] = None
                self._tamanio -= 1
                return True
        return False

    def __str__(self):
        return "{" + ", ".join(map(str, self.elementos)) + "}"


# === 3. Persistencia en Disco: Guardar filtros favoritos del usuario ===
import json
import os

class ConjuntoEnDisco:
    """Guarda los filtros personalizados del usuario (ej: 'mis filtros frecuentes')"""
    def __init__(self, nombre_archivo):
        self._nombre_archivo = nombre_archivo
        self._elementos = []
        self.cargar()

    @property
    def elementos(self):
        return self._elementos.copy()

    @elementos.setter
    def elementos(self, valores):
        self._elementos = list(set(valores))
        self.guardar()

    def agregar(self, valor):
        if valor not in self._elementos:
            self._elementos.append(valor)
            self.guardar()

    def quitar(self, valor):
        if valor in self._elementos:
            self._elementos.remove(valor)
            self.guardar()
            return True
        return False

    def contiene(self, valor):
        return valor in self._elementos

    def guardar(self):
        with open(self._nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(self._elementos, f, ensure_ascii=False, indent=2)

    def cargar(self):
        if os.path.exists(self._nombre_archivo):
            try:
                with open(self._nombre_archivo, 'r', encoding='utf-8') as f:
                    self._elementos = json.load(f)
            except (json.JSONDecodeError, IOError):
                print(f"[!] Advertencia: No se pudo leer {self._nombre_archivo}. Iniciando vacío.")
                self._elementos = []
        else:
            self._elementos = []

    def __str__(self):
        return "{" + ", ".join(map(str, self.elementos)) + "}"


# === 4. Simulación: Filtros de una Tienda de Ropa ===
print("🛍️  INICIO: Sistema de Filtros - Tienda Online\n")

# --- Filtro Dinámico: Marcas disponibles (pueden crecer con nuevos productos)
print("🔹 1. Marcas disponibles (Dinámico)")
marcas = ConjuntoDinamico()
marcas.elementos = ["Nike", "Adidas", "Puma"]
print(f"Marcas iniciales: {marcas}")
marcas.agregar("Zara")
print(f"Tras agregar Zara: {marcas}")
marcas.quitar("Puma")
print(f"Tras quitar Puma: {marcas}\n")

# --- Filtro Estático: Tallas permitidas (limitadas a 5 opciones)
print("🔹 2. Tallas disponibles (Estático)")
tallas = ConjuntoEstatico(5)
tallas.elementos = ["S", "M", "L"]
print(f"Tallas iniciales: {tallas}")
tallas.agregar("XL")
print(f"Tras agregar XL: {tallas}")
try:
    tallas.agregar("XXL")
    tallas.agregar("XXXL")  # Esto causará overflow
except OverflowError as e:
    print(f"Error al agregar más tallas: {e}")
print()

# --- Filtro en Disco: Preferencias del usuario
print("🔹 3. Filtros favoritos del usuario (en disco)")
favoritos = ConjuntoEnDisco("filtros_usuario.json")
favoritos.elementos = ["color:rojo", "talla:M", "marca:Nike"]
print(f"Filtros favoritos: {favoritos}")
favoritos.agregar("descuento:50%")
print(f"Tras agregar nuevo filtro: {favoritos}")
favoritos.quitar("talla:M")
print(f"Tras quitar talla:M: {favoritos}")
print("✅ Revisa el archivo 'filtros_usuario.json' generado en tu carpeta.\n")

# --- Operaciones de búsqueda (como en Amazon)
print("🔍 5. Búsqueda avanzada con operaciones de conjuntos")
# Simulamos búsquedas como: "rojo ∩ talla:M ∩ en_oferta"
colores_rojos = ConjuntoDinamico()
colores_rojos.elementos = ["producto_001", "producto_002", "producto_005"]

talla_m = ConjuntoDinamico()
talla_m.elementos = ["producto_002", "producto_003", "producto_005"]

en_oferta = ConjuntoDinamico()
en_oferta.elementos = ["producto_002", "producto_004", "producto_005"]

# Intersección: productos que son rojos Y talla M Y están en oferta
def interseccion(c1, c2):
    resultado = ConjuntoDinamico()
    for elem in c1.elementos:
        if c2.contiene(elem):
            resultado.agregar(elem)
    return resultado

rojo_y_m = interseccion(colores_rojos, talla_m)
rojo_y_m_y_oferta = interseccion(rojo_y_m, en_oferta)

print(f"Productos rojos: {colores_rojos.elementos}")
print(f"Productos talla M: {talla_m.elementos}")
print(f"En oferta: {en_oferta.elementos}")
print(f"Resultado de búsqueda (rojo ∩ M ∩ oferta): {rojo_y_m_y_oferta.elementos}")
print("\n✅ ¡Tu sistema de filtros está listo para una tienda real!")
