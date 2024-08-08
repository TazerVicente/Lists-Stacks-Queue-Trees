class Elemento:
    def __init__(self, v):
        self.valor = v
        self.prox = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.topo = None

    def enfileirar(self, n): 
        if self.inicio is None:
            self.inicio = n
            self.topo = n
        else:
            temp = self.inicio
            while temp.prox:
                temp = temp.prox
            temp.prox = n
            self.topo = n

    def desenfileirar(self):
        if self.inicio:
            temp = self.inicio
            self.inicio = temp.prox
            return temp

    def desempilhar(self):
        if self.inicio != None:
            temp = self.inicio
            if temp == self.topo:
                self.inicio = None
                self.topo = None
                a = temp.valor
                del temp
                return a
            else:
                while temp.prox != self.topo:
                    temp = temp.prox
                self.topo = temp
                temp = temp.prox
                a = temp.valor
                del temp
                return a

    def imprimir(self):
        print("Imprimindo fila...")
        if self.inicio:
            temp = self.inicio
            while temp:
                print(f"{temp.valor}")
                temp = temp.prox

class No:
    def __init__(self, v, label):
        self.valor = v
        self.label = label
        self.esq = None
        self.dir = None
        self.pai = None

class Heap:
    def __init__(self):
        self.raiz = None

    def inserir(self, n, label):
        n = No(n, label)
        if self.raiz == None:
            self.raiz = n
        else:
            self.inserir_subarvore(self.raiz, n)

    def inserir_subarvore(self, r, n):
        f = Fila()
        f.enfileirar(Elemento(r))
        procurar = True
        while procurar:
            raiz_temp = (f.desenfileirar())
            raiz_temp = raiz_temp.valor
            label_temp = raiz_temp.label
            if raiz_temp.esq:
                f.enfileirar(Elemento(raiz_temp.esq))
                if raiz_temp.dir:
                    f.enfileirar(Elemento(raiz_temp.dir))
                else: # se direita eh None
                    raiz_temp.dir = n
                    n.pai = raiz_temp
                    self.fix_up(n)
                    procurar = False
            else: # se esquerda eh None
                raiz_temp.esq = n
                n.pai = raiz_temp
                n.pai.label = label_temp
                self.fix_up(n)
                procurar = False

    def fix_up(self, n):
        if n.pai:
            if n.valor < n.pai.valor:
                temp = n.pai.valor
                temp_l = n.pai.label
                n.pai.valor = n.valor
                n.pai.label = n.label
                n.valor = temp
                n.label = temp_l
                self.fix_up(n.pai)

    def imprimir(self):
        f = Fila()
        f.enfileirar(Elemento(self.raiz))
        print("Imprimindo Heap...")
        while f.inicio:
            temp = (f.desenfileirar()).valor
            print(f"{temp.valor}")
            if temp.esq:
                f.enfileirar(Elemento(temp.esq))
            if temp.dir:
                f.enfileirar(Elemento(temp.dir))

    def preordem(self, r):
        if r:
            if r.pai == None:
                print(f'Valor:{r.valor} / Pai: None / Label: {r.label}' )
            if r.pai != None:
                print (f'Valor:{r.valor} / Pai:{r.pai.valor} / Label: {r.label}')
            self.preordem(r.esq)
            self.preordem(r.dir)

    def remover(self, raiz):
        f = Fila()
        f.enfileirar(Elemento(raiz))
        procurar = 1
        while procurar==1:
            raiz_temp = (f.desenfileirar()).valor
            if raiz_temp.esq:
                f.enfileirar(Elemento(raiz_temp.esq))
                a = raiz_temp.esq
                if raiz_temp.dir:
                    f.enfileirar(Elemento(raiz_temp.dir))
                    a = raiz_temp.dir
                else: # se direita é None
                    procurar = 0
            else: # se esquerda é None
                procurar = 0
        self.raiz.valor = a.valor
        self.raiz.label = a.label
        temp = a.pai
        if temp.esq.valor == a.valor and temp.esq.label == a.label:
            temp.esq = None
        elif temp.dir.valor == a.valor and temp.dir.label == a.label:
            temp.dir = None
        self.fix_down(self.raiz)
    
    def fix_down(self, raiz):
        D = raiz.dir
        E = raiz.esq
        if D == None and E != None:
            if raiz.valor > E.valor:
                valor_temp = raiz.valor
                label_temp = raiz.label
                raiz.valor = E.valor
                raiz.label = E.label
                E.label = label_temp
                E.valor = valor_temp
        elif D != None and E != None:
            if D.valor > E.valor:
                if E.valor < raiz.valor:
                    valor_temp = raiz.valor
                    label_temp = raiz.label
                    raiz.valor = E.valor
                    raiz.label = E.label
                    E.label = label_temp
                    E.valor = valor_temp
                    self.fix_down(raiz.esq)
            elif E.valor > D.valor:
                if D.valor < raiz.valor:
                    valor_temp = raiz.valor
                    label_temp = raiz.label
                    raiz.valor = D.valor
                    raiz.label = D.label
                    D.label = label_temp
                    D.valor = valor_temp
                    self.fix_down(raiz.dir)

    def pre_ordem_label(self, raiz):
        if raiz:
            print(raiz.label, end=" ")
            self.pre_ordem_label(raiz.esq)
            self.pre_ordem_label(raiz.dir)
    
def main():
    h = Heap()
    A, B = input().split() # A é a quantidade, B é a frequência
    A, B = int(A), int(B)
    Cont = 0 # Contador
    for i in range(A):
        Cont+=1
        Label, Valor = input().split()
        Label, Valor = str(Label), int(Valor)
        h.inserir(Valor, Label)
        if Cont == B:
            Cont = 0
            h.remover(h.raiz)
    h.pre_ordem_label(h.raiz)

if __name__ == "__main__":
    main()
