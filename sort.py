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

def main():
    L = sys.argv[2].split(',')
    List = map(lambda x: int (x),L)
    if sys.argv[1] == "insertion":
        insertion(List)
        print(List)
    elif sys.argv[1] == "selection":
        selection(List)
        print(List)
    else:
        print("Selecao de algoritimo invalido!!")    
    
if __name__ == '__main__':
    main()          