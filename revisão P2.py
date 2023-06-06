def operação(M):
    m=len(M)-1
    n=0
    a=1
    b=1
    while n<len(M):
        a=a*M[n][n]
        b=b*M[m][n]
        n+=1
        m-=1
    return a-b
