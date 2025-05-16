
N,L= map(int,input().split())

def gcd(a,b):

    while b:
        a,b = b, a%b

    return a

adj_m = [[]for i in range(N+1)]


for i in range(1,N+1) :
    for j in range(1,N+1) :
        if i!=j and gcd(i, j)== 1 :
            adj_m[i].append(j)


    adj_m[i].sort()


for i in range(L)  :
    D, F = map(int,input().split())
    closest =  adj_m[D]
   
    if F > len(closest) :
        print (-1)

    else:
  
        print(closest [F - 1])
