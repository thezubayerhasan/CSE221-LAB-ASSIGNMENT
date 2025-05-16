z =int(input())
ad_mat = [[0]*z for i in range(z)]

for i in range(z):
    elems= list(map(int,input().split()))
    k = elems [0]           
    nodes = elems[1:]  
    for nodee in nodes:
        ad_mat[i][nodee]= 1  
for r in ad_mat:
    print(' '.join(map(str,r)))

