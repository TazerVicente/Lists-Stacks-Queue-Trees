class No:
    def __init__(self,valor1,valor2): # Criação do nó com 2 valores
        self.valor1 = valor1
        self.valor2 = valor2
        self.nextvalor = None
        self.nextnome = None

    def imprimir(self):
        return(self.valor1, self.valor2)
    
class List():
    def __init__(self):
        self.valorhead = None
        self.nomehead = None
        self.valortail = None
        self.nometail = None

    def new_list(self):
        return (List())
    
    def adicionar(self, valor1, valor2):
        Nó = No(valor1, int(valor2))
        if self.valorhead == None: # Organizar por valores
            self.valorhead = Nó
            self.valortail = Nó
        else:
            if Nó.valor2 < self.valorhead.valor2:
                Prov = self.valorhead
                Nó.nextvalor = Prov
                self.valorhead = Nó
            else:
                if Nó.valor2 < self.valortail.valor2:
                    Atual = self.valorhead
                    while Atual.nextvalor.valor2 < Nó.valor2:
                        Atual = Atual.nextvalor
                    Nó.nextvalor = Atual.nextvalor
                    Atual.nextvalor = Nó
                elif Nó.valor2 > self.valortail.valor2:
                    Atual = self.valorhead
                    while Atual.nextvalor != None:
                        Atual = Atual.nextvalor
                    Atual.nextvalor = Nó
                    self.valortail = Atual.nextvalor

        if self.nomehead == None: # Organizar por nomes
            self.nomehead = Nó
            self.nometail = Nó
        else:
            if Nó.valor1 < self.nomehead.valor1:
                Prov = self.nomehead
                Nó.nextnome = Prov
                self.nomehead = Nó
            else:
                if Nó.valor1 < self.nometail.valor1:
                    Atual = self.nomehead
                    while Atual.nextnome.valor1 < Nó.valor1:
                        Atual = Atual.nextnome
                    Nó.nextnome = Atual.nextnome
                    Atual.nextnome = Nó
                elif Nó.valor1 > self.nometail.valor1:
                    Atual = self.nomehead
                    while Atual.nextnome != None:
                        Atual = Atual.nextnome
                    Atual.nextnome = Nó
                    self.nometail = Atual.nextnome

    def imprimir_valores(self):
        if self.valorhead == None:
            print ("Lista Vazia")
        else:
            print ("Imprimindo...")
            Atual = self.valorhead
            while Atual != None:
                print (Atual.imprimir())
                Atual = Atual.nextvalor
    
    def imprimir_nomes(self):
        if self.nomehead == None:
            print ("Lista Vazia")
        else:
            print ("Imprimindo...")
            Atual = self.nomehead
            while Atual != None:
                print(Atual.imprimir())
                Atual = Atual.nextnome
    
    def display(self):
        AtualV = self.valorhead
        AtualN = self.nomehead
        while AtualV != None or AtualN != None:
            print(*(AtualN.imprimir()), "|", *(AtualV.imprimir()))
            AtualV = AtualV.nextvalor
            AtualN = AtualN.nextnome

def main():
    L = List()
    Tamanho = int(input())
    for k in range (Tamanho):
        a, b = input().split()
        L.adicionar(a, b)
    L.display()

if __name__ == "__main__":
    main()
