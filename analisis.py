from conexion_sheets import obtener_datos

def contar_estado(registros, estado_buscado):
    total = 0
    for registro in registros:

        if registro.get("Estado de matrícula") == estado_buscado:
            total +=1
    return total

def agrupar_carrera(registros):
    resumen = {}
    for registro in registros:
        carrera = registro.get("Carrera")
        if carrera not in resumen:
           resumen[carrera] = 0
        resumen[carrera] += 1

    return resumen

datos = obtener_datos()
total_matriculados = contar_estado(datos, "Matrículado")
print(f"Total de alumnos matriculados:  {total_matriculados}")

alumnos_carrera = agrupar_carrera(datos)
print("Alumnos por carreara:", alumnos_carrera)

