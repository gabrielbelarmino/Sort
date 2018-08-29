import sys

def selection(List):
#   varre vetor a partir do item inicial    
    for indice in range(0,len(List)):
#       associa indice do item menor        
        indic_men = indice
#       laco verificador do menor item        
        for j in range(indice+1,len(List)):
            if List[j] < List[indic_men]:
                indic_men = j
#       troca caso lista esteja desordenada                
        if List[indice] != List[indic_men]:
            auxiliar = List[indice]
            List[indice] = List[indic_men]
            List[indic_men] = auxiliar

def insertion(List):
#   inicia pelo segundo (pivo) elemento comparando aos antecessores   
    for indice in range(1,len(List)):
#       atualiza o pivo        
        pivo = List[indice]
        j = indice - 1
#       laco compara com todos os antecessores        
        while j >= 0 and List[j] > pivo:
#           Se o antecessor for maior realiza a troca            
            List[j+1] = List[j]
            j = j-1
#       encontra o local do pivo apos o laco    
        List[j+1] = pivo


def particiona(List, l, r):
#   pivo ultimo elemento    
    pivo =  List[r]
    i = l - 1
#   Dividir vetor comparando pivo
    for j in range(l,r):
        if List[j] <= pivo:
            i += 1
            auxiliar = List[i]
            List[i] = List[j]
            List[j] = auxiliar
#    Associar ultimo Elemento         
    i += 1
    auxiliar = List[i]
    List[i] = List[r]
    List[r] = auxiliar
   # print(i)
    return i

def quick(List, l, r):
    if l < r :
#         Agrupa itens maiores e menores do que um pivo arbitrario da funcao        
        q = particiona(List, l, r)
#         Ordena recursivamente a primeira metade da tabela 
        quick(List, l, q-1)
#         Ordena recursivamente a segunda metade da tabela 
        quick(List, q+1, r)

def merge(List):
    if len(List)>1:
#       Divisao da Lista
        mid = len(List)//2
        midEsquerda = List[:mid]
        midDireita = List[mid:]
#       Recursao para tornar listas unitarias
        merge(midEsquerda)
        merge(midDireita)
#       Ordenacao
        i=0
        j=0
        k=0
        while i < len(midEsquerda) and j < len(midDireita):
            if midEsquerda[i] < midDireita[j]:
                List[k]=midEsquerda[i]
                i=i+1
            else:
                List[k]=midDireita[j]
                j=j+1
            k=k+1       

    #Caso sobre algum elemento (Lista Impar)
        while i < len(midEsquerda):
            List[k]=midEsquerda[i]
            i=i+1
            k=k+1

        while j < len(midDireita):
            List[k]=midDireita[j]
            j=j+1
            k=k+1    


def counting(List, valor_max):
    """in-place counting sort"""
    n = len(List)
    m = valor_max + 1
    tabela_index = [0] * m               # init with zeros
    for a in List:
        tabela_index[a] += 1             # count occurences
    i = 0
  #  List_Dest = [] * n
    print("Tabela de Indexaao: ",tabela_index)
    for a in range(len(tabela_index)):
        while 0 < tabela_index[a]:            # emit
            List[i] = a
            i += 1
            tabela_index[a] -= 1

def main():
    L = sys.argv[2].split(',')
    List = map(lambda x: int (x),L)
    if sys.argv[1] == "insertion":
        insertion(List)
        print(List)
    elif sys.argv[1] == "selection":
        selection(List)
        print(List)
    elif sys.argv[1] == "merge":
        merge(List)
        print(List)
    elif sys.argv[1] == "quick":
        quick(List,0,len(List)-1)
        print(List)
    elif sys.argv[1] == "counting":
        List_Res = counting(List,max(List))
        print(List)
    elif sys.argv[1] == "heap":
     #   heap(List,0,len(List)-1)
        print(List)           
    else:
        print("Selecao de algoritimo invalido!!")    
    
if __name__ == '__main__':
    main()          