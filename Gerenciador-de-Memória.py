class No:
    def __init__(self, Label, Valor):
        self.memory = Valor # Memória Utilizada no Processo
        self.label = Label # Identificação do processo
        self.next = None
        self.prev = None

    def imprimir(self):
        return(self.label, self.memory)
    
class List():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def Gerenciador(self,memória):
        Nó = No(0,memória)
        self.head = Nó
        Nó.next = None
        Nó.prev = None

    def Alocar(self, memória_utilizada, label):
        Atual = self.head
        while Atual != None:
            if Atual.label == 0 and Atual.memory >= memória_utilizada:
                if Atual.memory == memória_utilizada:
                    Atual.label = label
                else:
                    MP = int(Atual.memory) - int(memória_utilizada)
                    Nó = No(0, MP)
                    if Atual.next == None:
                        self.tail = Nó
                        Atual.next = Nó
                        Nó.next = None
                        Nó.prev = Atual
                        Atual.label = label
                        Atual.memory = memória_utilizada
                    else:
                        B = Atual.next
                        Nó.next = B
                        Atual.next = Nó
                        B.prev = Nó
                        Nó.prev = Atual
                        Atual.label = label
                        Atual.memory = memória_utilizada
                break
            Atual = Atual.next

    def Liberar(self, label): 
        Atual = self.head
        while Atual != None:
            if Atual.label == label:
                Atual.label = 0
                if Atual.next != None:
                    if Atual.next.label == 0:
                        Atual.memory = Atual.memory + Atual.next.memory
                        A = Atual.next
                        Atual.next = A.next
                        B = Atual.next
                        if B != None:
                            B.prev = Atual
                if Atual.prev != None:
                    if Atual.prev.label == 0: ############# ERRO ESTÁ AQUI ###################################
                        Atual = Atual.prev
                        Atual.memory = Atual.memory + Atual.next.memory
                        A = Atual.next
                        Atual.next = A.next
                        B = Atual.next
                        if B != None:
                            B.prev = Atual
                break
            Atual = Atual.next

    def size(self):
        i=0
        if self.head == None:
            return i
        else:
            Atual = self.head
            while Atual != None:
                i+= 1
                Atual = Atual.next
            return i

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
                Atual = Atual.prev

    def display(self):
        Atual = self.head
        Size = self.size()
        for k in range(Size):
            print (Atual.label, end=" ")
            Atual = Atual.next

    def memória_utilizada(self):
        Atual = self.head
        memória_utilizada = 0
        while Atual != None:
            if Atual.label != 0:
                memória_utilizada += Atual.memory
            Atual = Atual.next
        print (memória_utilizada)
    
    def memória_livre(self):
        Atual = self.head
        memória_livre = 0
        while Atual != None:
            if Atual.label == 0:
                memória_livre += Atual.memory
            Atual = Atual.next
        print (memória_livre)

def main():
    L = List()
    M, V = input().split()
    M, V = int(M), int(V)
    L.Gerenciador(M)
    for k in range (V):
        Op, Mem, Lab = input().split()
        Op, Mem, Lab = int(Op), int(Mem), str(Lab)
        if Op == 1:
            L.Alocar(Mem, Lab)
        elif Op == 0:
            L.Liberar(Lab)

    L.display()
    print()
    L.memória_utilizada()
    L.memória_livre()

if __name__ == "__main__":
    main()
