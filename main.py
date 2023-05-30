# ALUMNOS_EXAMEN

alumnos = [
    {
        "id": 1,
        "nombre": "Juan Pérez",
        "edad": 18,
        "curso": 12
    },
    {
        "id": 2,
        "nombre": "María López",
        "edad": 17,
        "curso": 11
    },
    {
        "id": 3,
        "nombre": "Pedro Gómez",
        "edad": 19,
        "curso": 12
    }
]

for alumno in alumnos:
    print(f'id: {alumno["id"]}')
    print(f'nombre: {alumno["nombre"]}')
    print(f'edad: {alumno["edad"]}')
    print(f'curso: {alumno["curso"]}')
    print("#############")
