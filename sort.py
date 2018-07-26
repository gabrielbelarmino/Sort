import sys

def selection(List):
    for indice in range(0,len(List)):
        indic_min = indice
        for j in range(indice+1,len(List)):
            if List[j] < List[indic_min]:
                indic_min = j
        if List[indice] != List[indic_min]:
            temp = List[indice]
            List[indice] = List[indic_min]
            List[indic_min] = temp

def insertion(List):
    for indice in range(1,len(List)):
        pivo = List[indice]
        j = indice - 1
        while j >= 0 and List[j] > pivo:
            List[j+1] = List[j]
            j = j-1
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
        print("Segundo argumento invalido")    
    
if __name__ == '__main__':
    main()          