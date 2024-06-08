import os 
os.system ("cls")

def iniciar_sesion():
    # Solicitar al usuario que ingrese su nombre de usuario y contraseña
    usuario = input("Ingrese su nombre de usuario de Steam: ")
    contraseña = input("Ingrese su contraseña: ")
    
    # Verificar si la contraseña es correcta
    if contraseña != "admin":
        print("Error: Contraseña incorrecta.")
        return False
    else:
        print("Inicio de sesión exitoso.")
        return True
    

def menu_principal():
    print("Bienvenido al menú principal:")
    print("1. Elegir juego")
    print("2. Comprar")
    print("3. Cerrar sesión")

def elegir_juego():
    print("Elija un juego:")
    print("1. Fallout")
    print("2. Resident Evil")

def comprar():
    print("Seleccione un juego para comprar:")
    print("1. Counter")
    print("2. Hollow Knight")

def pagar_tarjeta():
    # Solicitar número de tarjeta de crédito
    tarjeta = input("Ingrese el número de su tarjeta de crédito: ")
    if len(tarjeta) != 9:
        print("Error: El número de tarjeta debe tener exactamente 9 dígitos.")
    else:
        print("Compra realizada con éxito.")

def main():
    # Iniciar sesión
    sesion_iniciada = iniciar_sesion()
    
    if not sesion_iniciada:
        return
    
    while True:
        # Mostrar el menú principal y solicitar la elección del usuario
        menu_principal()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Mostrar opciones de juego
            elegir_juego()
            opcion_juego = input("Seleccione un juego: ")
            if opcion_juego == "1":
                print("Has elegido jugar Fallout.")
            elif opcion_juego == "2":
                print("Has elegido jugar Resident Evil.")
            else:
                print("Opción no válida.")
        elif opcion == "2":
            # Mostrar opciones de compra
            comprar()
            opcion_compra = input("Seleccione un juego para comprar: ")
            if opcion_compra == "1" or opcion_compra == "2":
                pagar_tarjeta()
            else:
                print("Opción no válida.")
        elif opcion == "3":
            print("Sesión cerrada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
