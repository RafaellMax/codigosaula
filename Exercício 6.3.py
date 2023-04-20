#palindromo com while
def is_palindrome(word):
    a=len(word)
    x=0
    y=0
    z=1
    while x<=len(word)/2:
        if word[y]==word[a-z]:
            y+=1
            z+=1
            x+=1
        if word[y]!=word[a-z]:
            return False
        return True

    

#palindromo com for

def is_palindrome_2(word):
    a=len(word)
    x=0
    y=0
    z=1
    for x in range(x,int(a/2)):
        if word[y]==word[a-z]:
            y+=1
            z+=1
            x+=1
        if word[y]!=word[a-z]:
            return False
        return True



#estimate_pi
import math

def fatorial(n):
    p=1
    while n>0:
        p=p*n
        n=n-1
    return p


def estimate_pi():
    sn=0
    sd=0
    k=0
    
    #soma
    while k<=50:
        num=fatorial(4*k)*(1103+26390*k)
        den=(fatorial(k))**4*396**(4*k)
        k+=1
        sn=sn+num
        sd=sd+den
        
    s=sd//sn

    pi=int((9801/2*math.sqrt(2))*s)
    return pi

