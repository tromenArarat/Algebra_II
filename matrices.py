import random

def NumeroRandom(n):
    # Generar un número aleatorio entre -n y n
    return random.randint(-n, n)

def crear_identidad(m, n):
    if m != n:
        print("No se puede crear una matriz identidad, ya que la matriz no es cuadrada.")
        return None
    
    identidad = []
    for i in range(m):
        fila = []
        for j in range(n):
            x = 1 if i == j else 0
            fila.append(x)
        identidad.append(fila)
        print(" ".join([f"{x:2}" for x in fila]))
    return identidad

def main():
    A = []
    B = []
    
    print("Ingrese cantidad de columnas:")
    m = int(input())
    print("Ingrese cantidad de filas:")
    n = int(input())
    
    # Nomenclar la matriz
    for i in range(1, m + 1):
        a = ""
        for j in range(1, n + 1):
            a += f"a{i}{j} "
        print(a)
    print("----------")
    print("Matriz A con valores random:")

    # Crear la primera matriz con valores aleatorios entre -10 y 10
    for i in range(m):
        fila = []
        for j in range(n):
            x = NumeroRandom(10)
            fila.append(x)
        A.append(fila)
        print(" ".join([f"{x:2}" for x in fila])) 
    
    print("Matriz B con valores random:")
    
    # Crear la segunda matriz con valores aleatorios entre -10 y 10
    for i in range(m):
        fila = []
        for j in range(n):
            x = NumeroRandom(10)
            fila.append(x)
        B.append(fila)
        print(" ".join([f"{x:2}" for x in fila]))  # Imprime la fila formateada
    
    print("Suma las matrices:")

    R = []
    
    # Sumar las dos matrices
    for i in range(m):
        fila = []
        for j in range(n):
            x = A[i][j] + B[i][j]
            fila.append(x)
        R.append(fila)
        print(" ".join([f"{x:2}" for x in fila]))  # Imprime la fila sumada

    # Multiplicar la primera matriz por un escalar
    print("Ingrese escalar:")
    alpha = int(input())
    print("Matriz A multiplicada por escalar:")
    for i in range(m):
        fila = []
        for j in range(n):
            x = alpha * A[i][j]
            fila.append(x)
        print(" ".join([f"{x:2}" for x in fila]))

    # Matriz identidad
    print("Matriz identidad:")
    crear_identidad(m, n)

if __name__ == "__main__":
    main()
