#listas
#a=['abc', 0, 6, [1, 2, 3]] ... é tipo uma string
#a[0] -> 'abc'
#a[-1] -> [1, 2, 3]
#a[-1][0] -> [2]
 #da p fazer matriz com isso: c = [[2,5],[1,0]]
#isso representa c = | 2 5
#                    | 1 0
#c=[3,2,4]
#del(c[2]) deleta um elemento da lista
#c.remove(2) exclui o primeiro elemento 3 que aparece na lista
#c.append6)
#c.pop(1) retorna o valor da posição 1
#c.insert
#split: 'faz bem aaa'.split(' ')
#dicionário: a = {'um' : 'one', 'dois' : 'two', 'tres' : 'three'}



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
        

#q3 da lista - tem que retornar uma nova lista
def soma(lista1, lista2):
    x=0
    c=[]
    while x<len(lista1):
        a=lista1[x]+lista2[x]
        c.append(a)
        x+=1
    return c


#q4 da lista - exibir a lista, inclusive as listas dentro dela
def exibir(lista):
    for i in range(0, len(lista)):
        if type(lista[i])==list:
            exibir(lista[i])
        else: print (lista[i])
        i+=1

#q5 da lista        #as retas nao estao sendo desenhadas corretamente!
from turtle import*
from math import*
def reta(reta):
    up()
    goto(reta[1][0] ,reta[0][1])
    down()
    right(atan(reta[0][0]))
    forward(reta[1][1]-reta[1][0])
    left(reta[0][0])
    
def retas(listas):
    n=0
    while n<len(listas):
        reta(listas[n])
        n+=1

comando=[[-0.5, 300],[0,400] ],[[0.5,  300], [-400,0]],[[-1.3, -300], [-335,0] ],[[1.3,  -300], [0,335] ]

# histograma
def histograma(texto):
    d = dict()
    for c in texto:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
        
    return d

#notas pelo dicionário

alunos = {'joão':[4,7,8],'maria':[6,7,5],'chico':[10,9,6],'rafael':[10,2,10]}
pesos = [0.3,0.3,0.4]
def notas():
    for k in alunos:
        media=0
        for c in range(3):
            media+=pesos[c]*alunos[k][c]
        print(k,media)
        
                 
def media_final():
    media_final = alunos
    for k in alunos:
        media=0
        for c in range(3):
            media+=pesos[c]*alunos[k][c]
        media_final[k].append(media)
    print(media_final)
    
def media_truncada():  # INCOMPLETA
    a={}
    media_final()
    for c in range(10):
        for a in alunos:
            if alunos[a][3]-c <1 and alunos[a][3]-c >=0:
                b=[alunos[a],alunos[a][4]]
                a={c:b}
                a[1].append(alunos[a][3])
    print(a)
