#Los datos
datos = {
    "Alumnos": [
        {
            "Nombre": "Juan",
            "Apellido": "Pérez",
            "DNI": "12345678A",
            "Fecha de nacimiento": "2005-02-15",
            "Tutor": "Carlos Pérez",
            "Notas": [8, 9, 7, 6],
            "Faltas": 2,
            "Amonestaciones": 1
        },
        {
            "Nombre": "María",
            "Apellido": "Gómez",
            "DNI": "23456789B",
            "Fecha de nacimiento": "2006-06-20",
            "Tutor": "Laura Gómez",
            "Notas": [10, 9, 9, 8],
            "Faltas": 1,
            "Amonestaciones": 0
        }
    ]
}

#Mostrar los datos
def mostrar_datos_alumno(datos, nombre):
    for alumno in datos["Alumnos"]:
        if alumno["Nombre"] == nombre:
            print(f"Nombre: {alumno['Nombre']} {alumno['Apellido']}")
            print(f"DNI: {alumno['DNI']}")
            print(f"Fecha de nacimiento: {alumno['Fecha de nacimiento']}")
            print(f"Tutor: {alumno['Tutor']}")
            print(f"Notas: {alumno['Notas']}")
            print(f"Faltas: {alumno['Faltas']}")
            print(f"Amonestaciones: {alumno['Amonestaciones']}")
            break
    else:
        print("Alumno no encontrado.")

# mostrar los datos
def modificar_datos_alumno(escuela, dni, campo, nuevo_valor):
    for alumno in escuela["Alumnos"]:
        if alumno["DNI"] == dni:
            if campo in alumno:
                alumno[campo] = nuevo_valor
                print(f"El campo {campo} ha sido actualizado.")
            else:
                print(f"El campo {campo} no existe.")
            break
    else:
        print("Alumno no encontrado.")

#agg los datos
def agregar_alumno(escuela, nombre, apellido, dni, fecha_nacimiento, tutor, notas, faltas, amonestaciones):
    nuevo_alumno = {
        "Nombre": nombre,
        "Apellido": apellido,
        "DNI": dni,
        "Fecha de nacimiento": fecha_nacimiento,
        "Tutor": tutor,
        "Notas": notas,
        "Faltas": faltas,
        "Amonestaciones": amonestaciones
    }
    escuela["Alumnos"].append(nuevo_alumno)
    print(f"Alumno {nombre} {apellido} agregado con éxito.")

#expulsar al alumno
def expulsar_alumno(escuela, dni):
    for alumno in escuela["Alumnos"]:
        if alumno["DNI"] == dni:
            escuela["Alumnos"].remove(alumno)
            print(f"Alumno {alumno['Nombre']} {alumno['Apellido']} expulsado.")
            break
    else:
        print("Alumno no encontrado.")

#ejecutar todo
def menu(escuela):
    while True:
        print("\nMenu de opciones:")
        print("1. Mostrar datos de un alumno")
        print("2. Modificar datos de un alumno")
        print("3. Agregar alumno")
        print("4. Expulsar alumno")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del alumno: ")
            mostrar_datos_alumno(datos, nombre)
        
        elif opcion == '2':
            dni = input("Ingrese el dni del alumno: ")
            campo = input("Ingrese el campo a modificar (Nombre, Apellido, Fecha de nacimiento, Tutor, Notas, Faltas, Amonestaciones): ")
            nuevo_valor = input("Ingrese el nuevo valor: ")
            if campo == "Notas":
                nuevo_valor = list(map(int, nuevo_valor.split(',')))  # Convierte la entrada a una lista de enteros
            elif campo in ["Faltas", "Amonestaciones"]:
                nuevo_valor = int(nuevo_valor)  # Convierte a entero
            modificar_datos_alumno(escuela, dni, campo, nuevo_valor)

        elif opcion == '3':
            nombre = input("Nombre del alumno: ")
            apellido = input("Apellido del alumno: ")
            dni = input("DNI del alumno: ")
            fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
            tutor = input("Nombre y apellido del tutor: ")
            notas = list(map(int, input("Notas (separadas por coma): ").split(',')))
            faltas = int(input("Cantidad de faltas: "))
            amonestaciones = int(input("Cantidad de amonestaciones: "))
            agregar_alumno(escuela, nombre, apellido, dni, fecha_nacimiento, tutor, notas, faltas, amonestaciones)

        elif opcion == '4':
            dni = input("Ingrese el DNI del alumno a expulsar: ")
            expulsar_alumno(escuela, dni)
        
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

#comenzar
menu(datos)
