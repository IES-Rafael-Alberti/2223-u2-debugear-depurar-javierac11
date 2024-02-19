
def algoritmoBurbuja(numeros: list):
    lista_ordenada = numeros
    for i in range(1, len(numeros)):
        for j in range(0, len(numeros)-1):
            if lista_ordenada[j] > lista_ordenada[j + 1]:
                numero = lista_ordenada[j]
                lista_ordenada[j] = lista_ordenada[j+1]
                lista_ordenada[j + 1] = numero
    return lista_ordenada

if __name__ == "__main__":
    print()