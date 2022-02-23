
def solve(tab):
    # Revisa si hay un espacio vacio
    find = encontrar_vacio(tab)
    if not find:
        return True
    else:
        fila, col = find
    # Rellena el sudoku con los valores validos
    for i in range(1,10):
        if valid(tab, i, (fila, col)):
            tab[fila][col] = i

            if solve(tab):
                return True

            tab[fila][col] = 0

    return False

# Función para validar el valor que debe ir en cada espacio vacio
def valid(tab, num, pos):
    #  Revisar fila
    for i in range(len(tab[0])):
        if tab[pos[0]][i] == num and pos[1] != i:
            return False

    # Revisar columna
    for i in range(len(tab)):
        if tab[i][pos[1]] == num and pos[0] != i:
            return False

    # Revisar cuadro
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if tab[i][j] == num and (i, j) != pos:
                return False

    return True

# Imprime la tabla
def imprimir_tabla(tab):
    for i in range(len(tab)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(tab[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end="")

# Funcion encuentra un espacio vacio, los cuales son los 0 en la plantilla.
def encontrar_vacio(tab):
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if tab[i][j] == 0:
                return (i, j)  # fila, columna

    return None

