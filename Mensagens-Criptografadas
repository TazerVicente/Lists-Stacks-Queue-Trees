class No:
    def __init__(self,valor1,valor2): # Criação do nó com 2 valores
        self.valor1 = valor1
        self.valor2 = valor2
        self.next = None
        self.previous = None

    def imprimir(self):
        return(f"Valores:{self.valor1} e {self.valor2}")

class lista_encadeada:
    def __init__(self): # Construtor da lista
        self.head = None
        self.tail = None

    def new_list(self):
        return(lista_encadeada())

    def append(self, valor1, valor2):
        Nó = No(valor1, valor2)
        if self.head == None:
            self.head = Nó
            self.tail = Nó
            self.tail.next = Nó
            self.head.previous = self.tail
        else:
            Atual = self.head
            while Atual.next != self.head:
                Atual = Atual.next
            Atual.next = Nó
            Nó.previous = Atual
            self.tail = Nó
            self.tail.next = self.head
            self.head.previous = self.tail

    def impressao(self):
        if self.head == None:
            print ("Lista Vazia")
        else:
            print ("Imprimindo...")
            Atual = self.head
            while True:
                print (Atual.imprimir())
                Atual = Atual.next
                if Atual == self.head:
                    break

    def size(self): # Diz a quantidade de termos na lista
        if self.head == None:
            return 0
        else:
            i=0
            Atual = self.head
            while True:
                Atual = Atual.next
                i+=1
                if Atual==self.head:
                    break
            return i

    def free_list(self):
        self.head == None
        self.tail == None

    def chave(self, chave):
        Próximo = None
        Atual = self.head
        B=self.size()
        if chave==0:
            return self
        elif chave > 0:
            if chave > (self.size()-1):
                while True:
                    if chave-self.size()<0:
                        break
                    else:
                        chave = chave - self.size()
            for k in range (chave):
                Prov = Atual.valor2
                for i in range(self.size()):
                    Próximo = Atual.next.valor2
                    Atual.next.valor2 = Prov
                    Prov = Próximo
                    Atual = Atual.next
        else:
            for k in range((-1)*chave):
                Prov = Atual.valor2
                for i in range(self.size()):
                    Previo = Atual.previous.valor2
                    Atual.previous.valor2 = Prov
                    Prov = Previo
                    Atual = Atual.previous

    def decifrar(self, l1, decifrado):
        O = l1.head
        for k in range(l1.size()):
            Atual = self.head
            for i in range(self.size()):
                if Atual.valor1 == O.valor1:
                    decifrado.append(Atual.valor2, 0)
                    break
                else:
                    Atual = Atual.next
            O = O.next
        return (decifrado)

    def cifrar(self, l1, cifrado):
        O = l1.head
        for k in range(l1.size()):
            Atual = self.head
            for i in range(self.size()):
                if Atual.valor2 == O.valor2:
                    cifrado.append(Atual.valor1, 0)
                    break
                else:
                    Atual = Atual.next
            O = O.next
        return (cifrado)

    def display(self):
        Atual = self.head
        Size = self.size()
        for k in range(Size):
            print (Atual.valor1, end="")
            Atual = Atual.next

def main():
    L = lista_encadeada()
    for i in range(26):
        a, b = input().split()
        a, b = str(a), str(b)
        L.append(a, b)
    Chave = int(input())
    L.chave(Chave)
    L1 = lista_encadeada() # Lista com a palavra pra decifrar
    L2 = lista_encadeada() # Lista com a palavra pra cifrar

    P1 = str(input()) # Palavra pra decifrar
    for i in P1:
        L1.append(str(i), 0)
    P2 = str(input()) # Palavra pra cifrar
    for i in P2:
        L2.append(0, str(i))

    D = lista_encadeada() # Palavra decifrada
    L.decifrar(L1, D)
    B = lista_encadeada() # Palavra cifrada
    L.cifrar(L2, B)

    D.display()
    print()
    B.display()
    print()

if __name__ == "__main__":
    main()
