# -*- coding: utf-8 -*-
# Programa: Promedio de notas de estudiantes
# Autors: Ronar Salazar  y Ulises Antonio
# Descripción:
# Calcula el promedio de 5 estudiantes en 4 materias, usando listas, ciclos for,
# validación de datos (texto y numéricos), colores, tabla formateada y menú con opción de salida.
# Usamos listas enlazadas y las recorremos por medio de ciclo for, además usamos ciclos while para el menu principal
# Usuamos funciones de manera correcta y estructurada, cumpliendo con las buenas prácticas de modularización y reutilización de código.
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

# ---------- Funciones de validación ----------
def ingresar_texto(mensaje):
    ### Aquí valido un texto y valida que no sea numérico ni vacío.
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print(Fore.RED + "⚠️ El campo no puede estar vacío. Intente nuevamente.")
        elif texto.replace(" ", "").isalpha():
            return texto
        else:
            print(Fore.RED + "❌ Error: Debe ingresar texto (no números). Intente nuevamente.")


def ingresar_numero(mensaje):
    ### Pido un número flotante válido entre 0 y 10, sino no lo dejo pasar.
    while True:
        valor = input(mensaje).strip()
        try:
            num = float(valor)
            if 0 <= num <= 10:
                return num
            else:
                print(Fore.RED + "⚠️ La nota debe estar entre 0 y 10. Intente nuevamente.")
        except ValueError:
            print(Fore.RED + "❌ Error: Debe ingresar un número válido. Intente nuevamente.")


# ---------- Funciones principales ---------- 
def ingresar_datos():
    estudiantes = []
    materias = []

    print(Fore.CYAN + "\n=== Ingreso de datos ===")
    # Ingreso de nombres de materias
    for i in range(4):
        materia = ingresar_texto(Fore.YELLOW + f"Ingrese el nombre de la materia {i+1}: ")
        materias.append(materia)

    # Ingreso de estudiantes y notas
    for i in range(5):
        nombre = ingresar_texto(Fore.GREEN + f"\nIngrese el nombre del estudiante {i+1}: ")
        notas = []
        for j in range(4):
            nota = ingresar_numero(f"Ingrese la nota de {materias[j]} para {nombre}: ")
            notas.append(nota)
        promedio = sum(notas) / len(notas)
        estudiantes.append({"nombre": nombre, "notas": notas, "promedio": promedio})

    # Guardar datos en archivo
    with open("notas.txt", "w") as f:
        f.write("Materia: " + ", ".join(materias) + "\n")
        for e in estudiantes:
            f.write(f"{e['nombre']}: {', '.join(map(str, e['notas']))} | Promedio: {e['promedio']:.2f}\n")

    print(Fore.BLUE + "\n✅ Datos guardados correctamente en 'notas.txt'")
    mostrar_resultados(estudiantes, materias)


def mostrar_resultados(estudiantes, materias):
    print(Fore.MAGENTA + "\n=== Promedios de los estudiantes ===")
    headers = ["Estudiante"] + materias + ["Promedio"]
    tabla = []
    for e in estudiantes:
        fila = [e["nombre"]] + e["notas"] + [round(e["promedio"], 2)]
        tabla.append(fila)
    print(tabulate(tabla, headers=headers, tablefmt="fancy_grid", floatfmt=".2f"))

    print(Fore.CYAN + "\nResumen:")
    for e in estudiantes:
        color = Fore.GREEN if e['promedio'] >= 7 else Fore.RED
        print(color + f"{e['nombre']} → Promedio: {e['promedio']:.2f}")


def consultar_desde_archivo():
    print(Fore.MAGENTA + "\n=== Consulta desde archivo ===")
    try:
        with open("notas.txt", "r") as f:
            contenido = f.read()
            print(Fore.WHITE + "\n" + contenido)
    except FileNotFoundError:
        print(Fore.RED + "❌ No se encontró el archivo 'notas.txt'. Primero debe ingresar los datos.")


def salir_programa():
    print(Fore.CYAN + "\n¿Desea salir del programa? (s/n)")
    respuesta = input(Fore.WHITE + "→ ").strip().lower()
    if respuesta == "s":
        print(Fore.GREEN + "\n👋 Gracias por usar el programa. ¡Hasta luego!")
        exit(0)
    else:
        print(Fore.YELLOW + "\n🔁 Regresando al menú principal...")


# ---------- Programa principal ----------
while True:
    print(Fore.CYAN + "\n========= MENÚ PRINCIPAL =========")
    print(Fore.YELLOW + "1. Ingresar datos y calcular promedios")
    print("2. Consultar datos desde archivo")
    print("3. Salir del programa")
    print(Fore.CYAN + "=================================")

    opcion = input(Fore.WHITE + "Seleccione una opción: ")

    if opcion == "1":
        ingresar_datos()
    elif opcion == "2":
        consultar_desde_archivo()
    elif opcion == "3":
        salir_programa()
    else:
        print(Fore.RED + "⚠️ Opción no válida. Intente nuevamente.")
