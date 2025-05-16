N = int(input())
a,y = map(int,input().split())

drtn =[(-1,-1),(-1,0),(-1,1), 
              (0,-1),       (0,1),
              (1,-1),(1,0), (1,1)  ]
psbl_moves=[]

for a1,y1 in drtn:
    x1= a+a1
    y1= y+y1
    if 1<= x1 <=N and 1<= y1 <= N :
        psbl_moves.append((x1,y1))
psbl_moves.sort()

print(len(psbl_moves))
for move in psbl_moves:
    print(move[0],move[1])
