class No:
    def __init__(self, v):
        self.valor = v
        self.prox = None

    def imprimir(self):
        return(self.valor)

class Pilha:
    def __init__(self):
        self.base = None
        self.topo = None

    def empilhar(self, n):
        n = No(n)
        if self.base == None:
            self.base = n
            self.topo = n
        else:
            self.topo.prox = n
            self.topo = n

    def desempilhar(self):
        if self.base != None:
            temp = self.base
            if temp == self.topo:
                self.base = None
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

    def imprimir(self): #da base para o topo
        temp = self.base
        while temp != self.topo:
            print(temp.imprimir())
            temp = temp.prox
        print(self.topo.imprimir())

def main():
    p = Pilha() #Armazenar os valores
    for i in input().split():
        if i=="+" or i=="-" or i=="*" or i=="/":
            Op1 = int(p.desempilhar())
            Op2 = int(p.desempilhar())
            if i == "+":
                R = Op2 + Op1
                p.empilhar(R)
            if i == "-":
                R = Op2 - Op1
                p.empilhar(R)
            if i == "*":
                R = Op1 * Op2
                p.empilhar(R)
            if i == "/":
                R = Op2//Op1
                p.empilhar(R)
        else:
            p.empilhar(i)
    p.imprimir()

if __name__ == "__main__":
    main()
