def findelemListPos(lista, elemento):
    #Funcion que busca un elemento en la lista
    # SI lo encuentra devuelve la posicion
    # SINO lo encuentra devuelve -1
    for p in range(len(lista)):
        if elemento == lista[p]:
            return p
    return -1

def existfindElemList(list,elem):
    #Funcion que busca un elemento en la lista
    #Si lo encuentra devuelve True
    #SINO lo encuentra devuelve False
    for e in list:
        if e == elem:
            return True
    return False
