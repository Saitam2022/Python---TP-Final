def mostrar_tablero(tablero):  
    for fila in tablero:  
        print("|".join(fila))  
        print("-" * 5)  
  
def verificar_ganador(tablero, jugador):  
    # Verificar las filas, columnas y diagonales  
    for i in range(3):  
        if all([celda == jugador for celda in tablero[i]]) or \
           all([tablero[j][i] == jugador for j in range(3)]):  
           return True  
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or \
       tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
       return True  
    return False  
  
def ta_te_ti_usuario_vs_usuario():  
    tablero = [[" " for _ in range(3)] for _ in range(3)]  
    jugador_actual = "X"  
    movimientos = 0  
  
    while movimientos < 9:  
        mostrar_tablero(tablero)  
        print(f"Turno del jugador {jugador_actual}")  
        fila = int(input("Ingrese la fila (0-2): "))  
        columna = int(input("Ingrese la columna (0-2): "))  
  
        if tablero[fila][columna] == " ":  
            tablero[fila][columna] = jugador_actual  
            movimientos += 1  
  
            if verificar_ganador(tablero, jugador_actual):  
                mostrar_tablero(tablero)  
                print(f"¡El jugador {jugador_actual} ha ganado!")  
                return  
  
            jugador_actual = "O" if jugador_actual == "X" else "X"  
        else:  
            print("Movimiento no válido. Intente de nuevo.")  
  
    mostrar_tablero(tablero)  
    print("¡Es un empate!")  
  
ta_te_ti_usuario_vs_usuario()  
