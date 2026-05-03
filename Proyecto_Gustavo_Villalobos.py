def registro(): #registrar los usuarios en nomina
    try:
        print("Registrar Empleado")
        nuevo = { #diccionario para establecer el molde del empleado
            "nombre": input("Ingrese el nombre del empleado: "),
            "Salario": float(input("Ingrese el salario del empleado: ")),
            "Dias": int(input("Ingrese los dias trabajados: "))
        }
        empleados.append(nuevo) #agregar el nuevo empleado a la lista
        print("Empleado registrado exitosamente.")
        return
    except ValueError:
        print(f"Ocurrio un error: {e}")


empleados = []
aux = 160000

if __name__ == "__main__":
    try:
        print("¡Hola! Bienvenido al proyecto de Gustavo Villalobos.")
        # Aquí puedes agregar el código principal de tu proyecto
        opc= input("¿Qué deseas hacer? (1: Registrar Empleado, 2: Calcular Nomina, 3: Salir): ")
        while opc != "3":
            if opc == "1":
                registro()
            elif opc == "2":
                nomina()
            else:
                print("Opción no válida. Por favor, elige una opción válida.")
            opc= input("¿Qué deseas hacer? (1: Registrar Empleado, 2: Calcular Nomina, 3: Salir): ")

    except ValueError:
        print(f"valor invalido")
    except TypeError:
        print("Ocurrio un error")
    except Exception as e:
        print(f"Ocurrió un error: {e}")