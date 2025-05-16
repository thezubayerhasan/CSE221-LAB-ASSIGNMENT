def dfs(grd,r,c,R,H,vstd):

    direcc =[(-1,0),(1,0),(0,-1),(0,1)]
    stk=[(r,c)]
    vstd[r][c]= True
    dmd= 0
    
    while stk:
        x,y =stk.pop()
        if grd[x][y]=='D' :
            dmd += 1
        
        
        for dx,dy in direcc:
            n_x,n_y = x + dx,y + dy
                     
            if 0 <= n_x < R and 0 <= n_y < H and grd[n_x][n_y] != '#' and not vstd[n_x][n_y] :
                vstd[n_x][n_y]= True

                stk.append((n_x, n_y))
    

    return dmd


def solve():
    R,H = map(int,input().split())
    grd= [list(input().strip()) for i in range(R)]
    
    vstd = [[False]*H for i in range(R)]
    max_dmd = 0
    
    for i in range(R):
        for c in range(H):
            if grd[i][c] != '#' and not vstd[i][c]:
        
                dmd =dfs(grd,i,c,R,H,vstd)

                max_dmd= max(max_dmd,dmd)
    



    print(max_dmd)




solve()






