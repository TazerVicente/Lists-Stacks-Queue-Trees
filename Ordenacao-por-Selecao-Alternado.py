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

def select_sort(vetor_inteiro, tamanho):
    int_total = 0
    int_pares = 0
    int_impar = 0
    for i in range (tamanho-1):
        if int_total == 0 or int_total%2 == 0:
            maior = int_pares
            for k in range(int_pares+1, tamanho):
                if vetor_inteiro[k] < vetor_inteiro[maior]:
                    maior = k
            vetor_inteiro[maior], vetor_inteiro[int_pares] = vetor_inteiro[int_pares], vetor_inteiro[maior]
            int_pares+=1
            print(*vetor_inteiro)
        else:
            menor = [(tamanho-1)-int_impar]
            menor2 = [(tamanho-1)-int_impar]
            for k in range((tamanho-1)-int_impar, -1, -1):
                if vetor_inteiro[k] > vetor_inteiro[menor]:
                    menor = k
            vetor_inteiro[menor], vetor_inteiro[menor2] = vetor_inteiro[menor2], vetor_inteiro[menor]
            int_impar+=1
            print(*vetor_inteiro)
        int_total+=1

def main():
    n = int(input())
    Array = np.fromstring(input(), dtype=int, sep=" ")
    select_sort(Array, n)

if __name__ == '__main__':
    main()
