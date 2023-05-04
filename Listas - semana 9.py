#listas
#a=['abc', 0, 6, [1, 2, 3]] ... é tipo uma string
#a[0] -> 'abc'
#a[-1] -> [1, 2, 3]
#a[-1][0] -> [2]
 #da p faser matriz com isso: c = [[2,5],[1,0]]
#isso representa c = | 2 5
#                    | 1 0


#questao 1 da lista
def ad(lista):
    for n in range(len(lista)):
        lista[n]+=1
        

#q2 da lista
def rev(lista):
    n=0
    i=len(lista)
    while n < len(lista)/2:
        a=lista[n]
        b=lista[i-1]
        lista[i-1]=a
        lista[n]=b
        n+=1
        i-=1

#q3 da lista
def soma_listas(lista1,lista2):
    for i in range (len(lista1)):
        a=lista1[i-1]
        b=lista2[i-1]
        lista1[i-1]+=b
        lista2[i-2]+=a
#N TA DANDO CERTO AINDA
