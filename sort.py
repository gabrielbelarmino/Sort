import sys

def selection(List):
    for item in range(0,len(List)):
        i_min = item
        for j in range(item+1,len(List)):
            if List[j] < List[i_min]:
                i_min = j
        if List[item] != List[i_min]:
            temp = List[item]
            List[item] = List[i_min]
            List[i_min] = temp

def selection1(List):
    for index,item in enumerate(List):
        i_min = index
        for j in range(index+1,len(List)):
            if List[j] < List[i_min]:
                i_min = j
        if item != List[i_min]:
            auxiliar = item
            item = List[i_min]
            List[i_min] = auxiliar

def insertion(List):
    for item in range(1,len(List)):
        pivo = List[item]
        j = item - 1
        while j >= 0 and List[j] > pivo:
            List[j+1] = List[j]
            j = j-1
        List[j+1] = pivo

def insertion1(List):
    for (index,item) in enumerate(List[1:]):
        pivo = item
        j = index
        while j >= 0 and List[j] > pivo:
            List[j+1] = List[j]
            j = j-1
        List[j+1] = pivo

def main():
    L = sys.argv[1].split(',')
    List = map(lambda x: int (x),L)
#    print(List)
#    L = [2,-1,0,5,-10,10]
#    insertion(List)
#    insertion1(List)
    selection1(List)
    print(List)

if __name__ == '__main__':
    main()          