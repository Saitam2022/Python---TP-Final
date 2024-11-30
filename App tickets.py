
import random  
  
# Diccionario para almacenar los tickets  
tickets = {}  
  
def generar_numero_ticket():  
    return random.randint(1000, 9999)  
  
def alta_ticket():  
    nombre = input("Ingrese su Nombre: ")  
    sector = input("Ingrese su Sector: ")  
    asunto = input("Ingrese Asunto: ")  
    problema = input("Ingrese un Mensaje: ")  
      
    numero_ticket = generar_numero_ticket()  
    tickets[numero_ticket] = {  
        "Nombre": nombre,  
        "Sector": sector,  
        "Asunto": asunto,  
        "Problema": problema  
    }  
      
    print(f"\nSe generó el siguiente Ticket\nNºTicket: {numero_ticket}")  
    print("Recordar su número de Ticket\n")  
      
    while True:  
        opcion = input("¿Desea generar un nuevo Ticket? (s/n): ").lower()  
        if opcion == 's':  
            alta_ticket()  
            break  
        elif opcion == 'n':  
            menu_principal()  
            break  
        else:  
            print("Opción no válida. Por favor, ingrese 's' o 'n'.")  
  
def leer_ticket():  
    try:  
        numero_ticket = int(input("Ingrese el número de Ticket: "))  
        if numero_ticket in tickets:  
            ticket = tickets[numero_ticket]  
            print(f"\nTicket Nº: {numero_ticket}")  
            print(f"Nombre: {ticket['Nombre']}")  
            print(f"Sector: {ticket['Sector']}")  
            print(f"Asunto: {ticket['Asunto']}")  
            print(f"Problema: {ticket['Problema']}\n")  
        else:  
            print("Ticket no encontrado.\n")  
    except ValueError:  
        print("Por favor, ingrese un número válido.\n")  
      
    while True:  
        opcion = input("¿Desea leer otro Ticket? (s/n): ").lower()  
        if opcion == 's':  
            leer_ticket()  
            break  
        elif opcion == 'n':  
            menu_principal()  
            break  
        else:  
            print("Opción no válida. Por favor, ingrese 's' o 'n'.")  
  
def salir():  
    confirmacion = input("¿Está seguro que desea salir? (s/n): ").lower()  
    if confirmacion == 's':  
        print("Saliendo del sistema. ¡Gracias!")  
        exit()  
    elif confirmacion == 'n':  
        menu_principal()  
    else:  
        print("Opción no válida. Por favor, ingrese 's' o 'n'.")  
        salir()  
  
def menu_principal():  
    print("Hola, Bienvenido al sistema de Tickets")  
    print("1 - Generar un Nuevo Ticket")  
    print("2 - Leer un Ticket")  
    print("3 - Salir")  
      
    while True:  
        try:  
            opcion = int(input("Seleccione una opción: "))  
            if opcion == 1:  
                alta_ticket()  
                break  
            elif opcion == 2:  
                leer_ticket()  
                break  
            elif opcion == 3:  
                salir()  
                break  
            else:  
                print("Opción no válida. Por favor, seleccione 1, 2 o 3.")  
        except ValueError:  
            print("Por favor, ingrese un número válido.")  
  
# Iniciar el programa  
menu_principal()  
