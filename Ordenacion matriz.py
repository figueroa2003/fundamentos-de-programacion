def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


if __name__ == "__main__":
    matriz = [
        [3, 1, 2],
        [6, 5, 4],
        [9, 7, 8]
    ]

    print("Matriz original:")
    for fila in matriz:
        print(fila)

    fila_a_ordenar = 1  # Índice de la fila que deseas ordenar

    if 0 <= fila_a_ordenar < len(matriz):
        bubble_sort(matriz[fila_a_ordenar])
        print(f"\nMatriz con la fila {fila_a_ordenar} ordenada:")
        for fila in matriz:
            print(fila)
    else:
        print("Índice de fila fuera de rango.")
