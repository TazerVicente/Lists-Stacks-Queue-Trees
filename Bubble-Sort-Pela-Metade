import numpy as np

def ordena(ent):
    comparacoes = 0
    movimentacoes = 0

    ordenado = np.zeros(len(ent)).astype(int)
    ordenado[0] = ent[0]

    for i in np.arange(1, len(ent)):
        ordenado[i] = ent[i]
        j = i-1 #vizinho anterior
        while j >= 0:
            comparacoes += 1
            if ordenado[j+1] < ordenado[j]:
                movimentacoes += 1
                temp = ordenado[j]
                ordenado[j] = ordenado[j+1]
                ordenado[j+1] = temp
            else:
                break
            j -= 1

    print(f"Comparacoes {comparacoes}")
    print(f"Movimentacoes {movimentacoes}")
    return ordenado

def bubble_sort(vetor_inteiro, tamanho):
    if tamanho%2 == 1:
        n = tamanho + 1
    else:
        n = tamanho

    for k in range (1, (n//2)+1):
        movimentacoes = 0
        for i in range(tamanho-1, 0, -1):
            if vetor_inteiro[i] < vetor_inteiro[i-1]:
                movimentacoes += 1
                vetor_inteiro [i], vetor_inteiro[i-1] = vetor_inteiro[i-1], vetor_inteiro[i]
        print (movimentacoes)
    return(vetor_inteiro)

def main():
    tamanho = int(input())
    Array = np.fromstring(input(), dtype=int, sep=" ")
    bubble_sort(Array, tamanho)
    print(*Array)

if __name__ == '__main__':
    main()
