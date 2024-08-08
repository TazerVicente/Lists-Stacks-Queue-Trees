class No:
    def __init__(self,valor): # Criação do nó com 2 valores
        self.valor = valor
        self.next = None
        self.previous = None
    
    def imprimir(self):
        return(f"Valor:{self.valor}")
    
class Lista:
    def __init__(self):
        self.head = None
        self.tail = None

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
    
    def impressao(self):
        if self.head == None:
            print ("Lista Vazia")
        else:
            print ("Imprimindo...")
            Atual = self.head
            while Atual != None:
                print (Atual.imprimir())
                Atual = Atual.next
    
    def impressao_inversa(self):
        if self.tail == None:
            print("Lista Vazia")
        else:
            print ("Imprimindo")
            Atual = self.tail
            while Atual != None:
                print (Atual.imprimir())
                Atual = Atual.previous

    def trocar(self, valor, direção, vetor):
        vetor.valor = valor
        if str(direção) == "E" and vetor.previous == None:
            Nó = No("b")
            Atual = self.head
            Atual.previous = Nó
            Nó.next = Atual
            self.head = Nó
            self.head.previous = None
            vetor = self.head
        elif str(direção) == "D" and vetor.next == None:
            self.append("b")
            vetor = self.tail
        else:
            if str(direção) == "E":
                vetor = vetor.previous
            else:
                vetor = vetor.next
        return (vetor)
    
    def size(self):
        i=0
        if self.head == None:
            return i
        else:
            Atual = self.head
            while Atual != None:
                Atual = Atual.next
                i+=1
            return i
    
    def retirar(self, L):
        Atual = self.head
        while Atual != None:
            if Atual.valor == "b":
                Atual = Atual.next
            else:
                L.append(Atual.valor)
                Atual = Atual.next
        
    def display(self):
        Atual = self.head
        Size = self.size()
        for k in range(Size):
            print (Atual.valor, end="")
            Atual = Atual.next

def main():
    Lista_original = Lista()
    Inicio = str(input())
    for i in Inicio:
        Lista_original.append(i)
    Trocas = int(input())
    Vetor = Lista_original.head
    for k in range(Trocas):
        a , b = input().split()
        b = str(b)
        Vetor = Lista_original.trocar(a, b, Vetor)
    Lista_resposta = Lista()
    Lista_original.retirar(Lista_resposta)
    Lista_resposta.display()

if __name__ == "__main__":
    main()
