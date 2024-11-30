import secrets, string  
  
diccionario = {  
    'letras': string.ascii_letters,  
    'numeros': string.digits,  
    'caracteres': string.punctuation  
}  
  
def generar_contraseña(tipo):  
    longitud = int(input("Ingrese la longitud de la contraseña: "))  
    caracteres = ''.join(diccionario[t] for t in tipo)  
    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))  
    return contraseña  
  
def menu_generador_contraseña():  
    print("Seleccione una de las siguientes opciones:")  
    print("1. Generar contraseña solo de Letras.")  
    print("2. Generar contraseña solo de Números.")  
    print("3. Generar contraseña Letras y Números.")  
    print("4. Generar contraseña Letras, Números y Caracteres.")  
    print("0. Salir.")  
  
    while True:  
        opcion = input("Escriba la opción seleccionada: ")  
        if opcion == '1':  
            print("Contraseña generada:", generar_contraseña(['letras']))  
        elif opcion == '2':  
            print("Contraseña generada:", generar_contraseña(['numeros']))  
        elif opcion == '3':  
            print("Contraseña generada:", generar_contraseña(['letras', 'numeros']))  
        elif opcion == '4':  
            print("Contraseña generada:", generar_contraseña(['letras', 'numeros', 'caracteres']))  
        elif opcion == '0':  
            break  
        else:  
            print("Opción no válida. Por favor, intente de nuevo.")  
  
menu_generador_contraseña()  
