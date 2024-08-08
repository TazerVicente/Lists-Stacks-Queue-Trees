class No:
    def __init__(self, v):
        self.valor = v
        self.esq = None
        self.dir = None
        self.pai = None

class Arvore:
    def __init__(self):
        self.raiz = None
    
    def clear_tree(self):
        self.raiz = None

    def inserir(self, n):
        n = No(n)
        if self.raiz == None:
            self.raiz = n
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
            print(f'{r.valor}')
            self.preordem(r.esq)
            self.preordem(r.dir)
    
    def ordem_decrescente(self, r):
        if r:
            self.ordem_decrescente(r.dir)
            print(r.valor, end=" ")
            self.ordem_decrescente(r.esq)

def main():
    A = Arvore()
    N = int(input())
    L = input().split()
    for i in L:
        A.inserir(int(i))
    A.ordem_decrescente(A.raiz)

if __name__ == "__main__":
    main()
