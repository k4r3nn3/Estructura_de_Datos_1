""" Modelo Estático: Plan de estudios de la carrera 
Descripción: Representación fija del plan de estudios oficial de la carrera.
Esta información no cambia frecuentemente.
Diccionario estático: Plan de estudios de Redes y Telecomunicaciones (UAGRM) """
plan_estudios = {
    "1-1": {"materia": "Cálculo I", "creditos": 6},
    "1-2": {"materia": "Física I", "creditos": 6},
    "2-1": {"materia": "Cálculo II", "creditos": 6},
    "2-2": {"materia": "Circuitos Eléctricos", "creditos": 6},
    "3-1": {"materia": "Señales y Sistemas", "creditos": 5},
    "3-2": {"materia": "Redes I", "creditos": 5},
    "4-1": {"materia": "Sistemas Lógicos Digitales", "creditos": 5},
    "4-2": {"materia": "Redes II", "creditos": 5},
    "5-1": {"materia": "Sistemas Operativos", "creditos": 5},
    "5-2": {"materia": "Seguridad en Redes", "creditos": 5}
}

def buscar_materia(codigo):
    return plan_estudios.get(codigo, "Materia no encontrada")

def mostrar_materias_semestre(semestre):
    print(f"Materias del semestre {semestre}:")
    for codigo, datos in plan_estudios.items():
        if codigo.startswith(semestre):
            print(f" - {datos['materia']} ({datos['creditos']} créditos)")

# Uso del sistema
print(buscar_materia("3-1"))
mostrar_materias_semestre("4")



"""  Modelo Dinámico: Registro de asistencia a clases
Modelo Dinámico: Registro de asistencia a clases Descripción: Un estudiante registra su entrada y salida de clases diariamente. Los datos cambian cada día.
"""
# Lista dinámica: registro de asistencia
asistencias = []

def registrar_entrada(materia, hora):
    asistencias.append({
        "materia": materia,
        "hora_entrada": hora,
        "tipo": "entrada"
    })

def registrar_salida(materia, hora):
    asistencias.append({
        "materia": materia,
        "hora_salida": hora,
        "tipo": "salida"
    })

def mostrar_asistencias():
    print("\nRegistro de asistencias:")
    for evento in asistencias:
        if evento["tipo"] == "entrada":
            print(f"Entró a {evento['materia']} a las {evento['hora_entrada']}")
        else:
            print(f"Salió de {evento['materia']} a las {evento['hora_salida']}")

def contar_clases(materia):
    return sum(1 for a in asistencias if a["materia"] == materia and a["tipo"] == "entrada")

# Uso del sistema
registrar_entrada("Redes de Computadoras I", "08:00")
registrar_salida("Redes de Computadoras I", "10:00")
registrar_entrada("Matemática II", "10:15")
registrar_salida("Matemática II", "12:15")

mostrar_asistencias()
print(f"Asistí a {contar_clases('Redes de Computadoras I')} clases de Redes I.")



"""    Modelo Persistente: Guardar calificaciones del estudiante en archivo JSON
Descripción: Guardar las calificaciones del estudiante para que no se pierdan al cerrar el programa."""

import json

def cargar_calificaciones(nombre_archivo="calificaciones_uagrm.json"):
    try:
        with open(nombre_archivo, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}

def guardar_calificaciones(calificaciones, nombre_archivo="calificaciones_uagrm.json"):
    with open(nombre_archivo, "w") as archivo:
        json.dump(calificaciones, archivo, indent=2)

def agregar_calificacion(materia, nota):
    calificaciones[materia] = nota
    print(f"Calificación de {materia}: {nota}")

def mostrar_calificaciones():
    print("\nCalificaciones del estudiante:")
    for materia, nota in calificaciones.items():
        print(f" - {materia}: {nota}")

# Uso del sistema
calificaciones = cargar_calificaciones()

agregar_calificacion("Redes de Computadoras I", 87)
agregar_calificacion("Matemática II", 74)
agregar_calificacion("Física I", 81)

mostrar_calificaciones()
guardar_calificaciones(calificaciones)


"""    Modelo Simulado: Sistema de préstamos del Laboratorio de Redes
Descripción: Simulación de un sistema donde los estudiantes piden prestado equipo del laboratorio (switches, routers, laptops). """

class PrestamoLaboratorio:
    def __init__(self):
        self.equipos = {
            "Router Cisco 2900": 3,
            "Switch Cisco 2960": 5,
            "Laptop HP": 10
        }
        self.historial = []

    def prestar_equipo(self, estudiante, equipo, cantidad):
        if self.equipos.get(equipo, 0) >= cantidad:
            self.equipos[equipo] -= cantidad
            self.historial.append({
                "estudiante": estudiante,
                "equipo": equipo,
                "cantidad": cantidad
            })
            print(f"✅ {cantidad} {equipo}(s) prestado(s) a {estudiante}.")
        else:
            print(f"❌ No hay suficientes {equipo} disponibles.")

    def mostrar_disponibilidad(self):
        print("\nEquipos disponibles en el laboratorio:")
        for equipo, cantidad in self.equipos.items():
            print(f" - {equipo}: {cantidad}")

    def mostrar_historial(self):
        print("\nHistorial de préstamos:")
        if not self.historial:
            print(" - No hay préstamos registrados.")
        else:
            for prestamo in self.historial:
                print(f" - {prestamo['estudiante']} → {prestamo['cantidad']} {prestamo['equipo']}")

# Uso del sistema
lab_redes = PrestamoLaboratorio()

lab_redes.prestar_equipo("Carlos Méndez", "Router Cisco 2900", 1)
lab_redes.prestar_equipo("Ana Pérez", "Laptop HP", 2)
lab_redes.prestar_equipo("Luis Gómez", "Switch Cisco 2960", 6)  # Demasiado

lab_redes.mostrar_disponibilidad()
lab_redes.mostrar_historial()



