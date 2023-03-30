from turtle import*
import random
def quadrado(lado): #desenha um quadrado
    width(3)
    begin_fill()

    for _ in range(4):
        forward(lado)
        right(90)

    end_fill()


def forma (lado): #desenha um circulo
    width(3)
    begin_fill()

    for _ in range (30):
        forward(lado)
        right(12)
    end_fill()

def poligono (n): #desenha um poligono regular de lado n
    width(4)
    begin_fill()
    lado=random.randint(20,50)

    for _ in range(n):
        forward(lado)
        right(360/n)

    end_fill()

def varios (a): #desenha varios poligonos de numero aleatorio de lados(3,12)
    for _ in range(a):
        lado=random.randint(50,250)
        x=random.randint(-200,200)
        y=random.randint(-200,200)
        n=random.randint(3,9)
        
        up()
        goto(x,y)
        down()

        poligono(n)

def bloquinhos (n, lado): #constroi uma paredinha de n bloquinhos
    color("black","orange")
    for _ in range(n):
        quadrado(lado)
        forward(lado)

def arena (n, lado): #constrói quatro paredes
    color("black","red")
    speed(0)
    for _ in range(4):
        bloquinhos(n,lado)
        right(90)
           
def arenassa (n, lado, m=5): #constrói uma arena feita de arenas
    for _ in range(4):      #n é qnt de quadrados na areninha 
        for _ in range(m):   #lado é a largura de cada quadradinhho
            arena(n,lado)     #m é a quantidade de areninhas por arenassa
            forward(n*lado-1)
        right(90)

