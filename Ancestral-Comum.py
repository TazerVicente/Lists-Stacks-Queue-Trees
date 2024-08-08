class No:
    def __init__(self, v):
        self.valor = v
        self.esq = None
        self.dir = None
        self.pai = None
        self.next = None
        self.previous = None

    def imprimir(self):
        return(f"Valor:{self.valor}")

class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

    def impressao(self):
        if self.head == None:
            print ("Lista Vazia")
        else:
            print ("Imprimindo...")
            Atual = self.head
            while Atual != None:
                print (Atual.imprimir())
                Atual = Atual.next

    def append(self, valor):
        Nó = No(valor)
        if self.head == None:
            self.head = Nó
            self.tail = Nó
            self.head.previous = None
        else:
            Atual = self.head
            while Atual.next != None:
                Atual = Atual.next
            Atual.next = Nó
            Nó.previous = Atual
            self.tail = Nó
            self.tail.next = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, n):
        n = No(n)
        if self.raiz == None:
            self.raiz = n
            self.raiz.pai = None
        else:
            self.inserir_subarvore(self.raiz, n)

    def inserir_subarvore(self, r, n):
        if n.valor <= r.valor: # testa se esquerda
            if r.esq == None:
                r.esq = n
                n.pai = r
            else:
                self.inserir_subarvore(r.esq, n)
        else: # testa se direita
            if r.dir == None:
                r.dir = n
                n.pai = r
            else:
                self.inserir_subarvore(r.dir, n)

    def preordem(self, r):
        if r:
            if r.pai == None:
                print(f'Valor:{r.valor} / Pai: None')
            if r.pai != None:
                print (f'Valor:{r.valor} / Pai:{r.pai.valor}')
            self.preordem(r.esq)
            self.preordem(r.dir)

    def procura(self, r, Valor1):
        c = None
        if r != None:
            if Valor1 == r.valor:
                c = r
                return c
            else:
                if r.valor > Valor1:
                    return self.procura(r.esq, Valor1)
                else:   
                    return self.procura(r.dir, Valor1)

def ancestral_mais_próximo(Arvore, V1, V2):
    Q1 = Arvore.procura(Arvore.raiz, V1)
    Q2 = Arvore.procura(Arvore.raiz, V2)
    if Q1 and Q2 != None:
        L = Lista()
        while Q1 != None:
            L.append(Q1.valor)
            Q1 = Q1.pai
        Chave = 1
        while Q2 != None and Chave == 1:
            a = L.head
            while a != None:
                if a.valor == Q2.valor:
                    Chave = 0
                    print (a.valor)
                    break
                else:
                    a = a.next
            Q2 = Q2.pai
    elif Q1 != None and Q2 == None:
        print(Q1.valor)
    elif Q2 != None and Q1 == None:
        print(Q2.valor)
    elif Q1 == None and Q2 == None:
        print("NENHUM")

def main():
    a = Arvore()
    N = input() # Quantidade de Termos
    for i in input().split():
        a.inserir(int(i))
    V1, V2 = input().split()
    V1, V2 = int(V1), int(V2)
    ancestral_mais_próximo(a,V1,V2)

if __name__ == "__main__":
    main()
