class Elemento:
    def __init__(self, v, pos):
        self.valor = v
        self.prox = None
        self.pos = pos

class Fila:
    def __init__(self):
        self.inicio = None

    def enfileirar(self, n, pos): # Enfileira os elementos que chegam
        if pos <= 13: # Definir a Posição Inicial do Processo
            if pos <= 6:
                if pos >3:
                    if pos == 4:
                        pos = "D"
                    elif pos == 5:
                        pos = "E"
                    elif pos == 6:
                        pos = "F"
                elif pos <= 3:
                    if pos == 3:
                        pos = "C"
                    elif pos == 2:
                        pos = "B"
                    elif pos == 1:
                        pos = "A"
            elif pos > 6:
                if pos <= 9:
                    if pos == 7:
                        pos = "G"
                    elif pos == 8:
                        pos = "H"
                    elif pos ==9:
                        pos = "I"
                elif pos >9:
                    if pos == 10:
                        pos = "J"
                    elif pos == 11:
                        pos = "K"
                    elif pos == 12:
                        pos = "L"
                    elif pos == 13:
                        pos = "M"
        elif pos > 13:
            if pos <= 19:
                if pos <= 16:
                    if pos == 14:
                        pos = "N"
                    elif pos == 15:
                        pos = "O"
                    elif pos == 16:
                        pos = "P"
                elif pos > 16:
                    if pos == 17:
                        pos = "Q"
                    elif pos == 18:
                        pos = "R"
                    elif pos == 19:
                        pos = "S"
            elif pos > 19:
                if pos <= 23:
                    if pos == 20:
                        pos = "T"
                    elif pos == 21:
                        pos = "U"
                    elif pos == 22:
                        pos = "V"
                    elif pos == 23:
                        pos = "W"
                elif pos > 23:
                    if pos == 24:
                        pos = "X"
                    elif pos == 25:
                        pos = "Y"
                    elif pos == 26:
                        pos = "Z"
        n = Elemento(n, pos)
        if self.inicio is None:
            self.inicio = n
        else:
            temp = self.inicio
            while temp.prox:
                temp = temp.prox
            temp.prox = n

    def desenfileirar(self): 
        if self.inicio:
            temp = self.inicio
            self.inicio = temp.prox
            return temp

    def imprimir(self):
        print("Imprimindo fila...")
        if self.inicio:
            temp = self.inicio
            while temp:
                print(f"Valor:{temp.valor} / Posição:{temp.pos}")
                temp = temp.prox

    def EnfileirarSimples(self, Valor, Posição):
        No = Elemento(Valor, Posição)
        if self.inicio is None:
            self.inicio = No
        else:
            temp = self.inicio
            while temp.prox != None:
                temp = temp.prox
            temp.prox = No

    def escalonamento(self, TempMax, TempSave, FilaSecundária):
        TempAtual = 0
        while self.inicio != None:
            if self.inicio.valor <= TempMax:
                TempAtual += self.inicio.valor
                a = self.inicio.pos
                FilaSecundária.EnfileirarSimples(TempAtual, a)
                self.desenfileirar()
            else:
                TempAtual += TempMax
                TempAtual += TempSave
                self.inicio.valor -= TempMax
                b = self.inicio.pos
                c = self.inicio.valor
                self.desenfileirar()
                self.EnfileirarSimples(c,b)

    def display(self):
        temp = self.inicio
        while temp != None:
            print(temp.pos, temp.valor)
            temp = temp.prox

def main():
    F = Fila()
    Fs = Fila()
    TempM, TempS = input().split()
    TempM, TempS = int(TempM), int(TempS)
    a = [int(i) for i in input().split()]
    pos=1
    for i in a:
        F.enfileirar(i, pos)
        pos+=1
    F.escalonamento(TempM, TempS, Fs)
    Fs.display()

if __name__ == "__main__":
    main()
