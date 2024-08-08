class No:
  def __init__(self, valor): # Criador dos nós
    self.valor = valor # Atribuição do valor ao nó
    self.next = None # Próximo nó

  def imprimir(self): # Função de imprimir os valores dos nós
    return(f"Valor: {self.valor}")

class List:
  def __init__(self): # Criador da lista
    self.head = None # Inicio da lista (Até agora vazia)
    self.tail = None # Final da Lista

  def inserir(self, valor): # Insere um valor no início da lista (No head)
    Nó = No(valor)
    if self.head == None:
      self.head = Nó
    else:
      Nó.prox = self.head
      self.head = Nó

  def new_list():
    return List()

  def append(self, valor): # Insere um valor no final da lista (No tails)
    Nó = No(valor)
    if self.head == None:
      self.head = Nó
    else:
      Atual = self.head
      while Atual.next != None:
        Atual = Atual.next
      Atual.next = Nó

  def impressao(self): # Imprime todos os elementos da lista
    if self.head == None:
      print ("Lista Vazia")
    else:
      print ("Imprimindo...")
      Atual = self.head
      while Atual != None:
        print (Atual.imprimir())
        Atual = Atual.next

  def free_list(self): # "Deleta" a lista
    self.head = None
    self.tail = None

  def remove(self,posicao): # Remove um elemento de uma deterinada posição
    Atual = self.head
    if posicao == 0:
      self.head = Atual.next
    else:
      i=0
      while i != (posicao-1):
        i+=1
        Atual = Atual.next
      Atual.next = Atual.next.next

  def size(self): # Diz a quantidade de termos na lista
    if self.head == None:
      return 0
    else:
      i=0
      Atual = self.head
      while Atual != None:
        Atual = Atual.next
        i+=1
      return i

  def inverte_sublista(self, v1, v2): # Função para a inversão
    if v1!=0:
      Sublista1 = List() # Intervalo anterior à inversão
      Sublista2 = List() # Intervalo que acontecerá a inversão
      Sublista3 = List() # Intervalo posterior à inversão
      Atual = self.head
      Sublista1.head = self.head
      i=0
      while Atual != None:
        if i==(v1-1):
          Sublista1.tail = Atual
        elif i==v1:
          Sublista2.head = Atual
          Sublista1.tail.next = None
        elif i==v2:
          Sublista2.tail = Atual
          Sublista3.head = Atual.next
          Atual.next = None
          break
        i+=1
        Atual = Atual.next

      Anterior = None
      Atual = Sublista2.head
      Sublista2.tail = Sublista2.head
      while Atual != None:
        Próximo = Atual.next
        Atual.next = Anterior
        Anterior = Atual
        Atual = Próximo
      Sublista2.head = Anterior
      Sublista1.tail.next = Sublista2.head
      Sublista2.tail.next = Sublista3.head
      self.head= Sublista1.head
      return(self)

    else:
      Sublista1 = List() # Intervalo que acontecerá a inversão
      Sublista2 = List() # Intervalo posterior à inversão
      Atual = self.head
      Sublista1.head = self.head
      i=0
      while Atual != None:
        if i==v2:
          Sublista1.tail = Atual
          Sublista2.head = Atual.next
          Sublista1.tail.next = None
          break
        i+=1
        Atual = Atual.next
      Anterior = None
      Atual = Sublista1.head
      Sublista1.tail = Sublista1.head
      while Atual != None:
        Próximo = Atual.next
        Atual.next = Anterior
        Anterior = Atual
        Atual = Próximo
      Sublista1.head= Anterior
      Sublista1.tail.next = Sublista2.head
      self.head = Sublista1.head
      return(self)

  def display(self):
    Atual = self.head
    Size = self.size()
    for k in range (0, Size):
      print (Atual.valor, end=" ")
      Atual = Atual.next

def main():
  L = List.new_list() # Lista
  Elemens = int(input()) # Quantidade de termos
  b = [int(i) for i in input().split()]

  for i in b:
    L.append(i)

  Trocas = int(input())
  for k in range(Trocas):
    p1, p2 = input().split()
    p1 = int(p1)
    p2 = int(p2)
    L.inverte_sublista(p1, p2)

  Remover = int(input())
  for j in range(Remover):
    Posição = int(input())
    L.remove(Posição)
  L.display()

if __name__ == "__main__":
  main()
