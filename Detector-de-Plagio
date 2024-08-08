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

  def impressao(self): # Imprime todos os elementos da lista
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
    else:
      Atual = self.head
      while Atual.next != None:
        Atual = Atual.next
      Atual.next = Nó

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

  def comparar(list1, list2):
    Cabeca= list1.head # Inicio da suposta parte plagiada
    Atual= list2.head # Inicio da parte que tem o plágio
    p=0
    for k in range(list2.size()):
      Comparador = Cabeca
      a=0
      while Atual != None and Comparador != None:
        if Atual.valor == Comparador.valor:
          Plagio = Atual
          d=p
          c=0
          while Plagio != None and Comparador != None:
            for j in range(list1.size()):
              if Plagio.valor == Comparador.valor:
                c+=1
                if c==(list1.size()):
                  print(f"Plagio encontrado na posicao {d}!")
                  a=1
              Plagio = Plagio.next
              Comparador = Comparador.next
              if Plagio == None or Comparador == None:
                break
        else:
          p+=1
          Atual = Atual.next
      if a==1:
        break
      if Atual == None:
        print("Nenhum plagio detectado!")
        break
      else:
        p+=1
        Atual = Atual.next

def main():
  L1 = str(input())
  L2 = str(input())

  Lista_original = List()
  Lista_comparativa = List()

  for i in L1:
    Lista_original.append(i)
  for i in L2:
    Lista_comparativa.append(i)

  List.comparar(Lista_original, Lista_comparativa)

if __name__=="__main__":
  main()
