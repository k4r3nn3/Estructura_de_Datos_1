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

"""Modelo Dinámico: Registro de asistencia a clases
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
