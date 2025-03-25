game_over=[[1,2,3],[4,5,6],[7,8," "]]
#game_over=[[1,2,3],[8," ",4],[7,6,5]]

g=1

def string_to_grid(state):
    grid = []
    for i in range(0, 9, 3):
        row = [int(c) if c != '0' else " " for c in state[i:i+3]]
        grid.append(row)
    return grid

def print_grid(lol):
    for row in lol:
        for num in row:
            print(num,"|",end="")
        print("\n----------")
        
def h(grid): ##number of misplaces squares
    h=0
    for i in range(3):
        for j in range(3):
            if grid[i][j]!=game_over[i][j] and grid[i][j]!=" ":
                h=h+1

    return h

def blank(grid):
    ##need to find out where " "  is
    row=col=0
    for row in range(3):
        for col in range(3):
            #print(grid[row][col])
            if grid[row][col]==" ":
                return (row,col)

def moves_cal(row,col):  
    moves=[]  ## where can the blank go to
    lol=[]
    moves=[(row-1,col),(row+1,col),(row,col+1),(row,col-1)]
    for a,b in moves:
        if a in (0,1,2) and b in (0,1,2):
            lol.append((a,b))

    
    return lol


def first_swap(grid,a,b,row,col):
    ##so i gottta create a new grid and then swap shit coz, cant mess with the originl
    new_grid=[row[:] for row in grid]
    new_grid[row][col], new_grid[a][b]=new_grid[a][b],new_grid[row][col] ##swapping
    # temp=grid[row][col]
    # grid[row][col]=grid[a][b]
    # grid[a][b]=temp

    # #print("one sqaure moved:", grid, f[i])  ## grid it is evaluting
    # return grid
    
def grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)

# def rev_swap(grid,a,b,row,col):
#     #print(row,col)
#     temp=grid[row][col]
#     grid[row][col]=grid[a][b]
#     grid[a][b]=temp

# def make_grid_copy(farm):
#     lol=[[0]*3 for _ in range(3)]
#     i=j=0
#     for i in range(3):
#         for j in range(3):
#             #print(i,j)
#             lol[i][j]=farm[i][j]

#     return lol

def main(grid,a=-1,b=-1):
    print_grid(grid)
    global g

    ##intializing an open set
    open_set ={grid_to_tuple(grid):(0,h(grid),None)}  ##in the format of {state: (g,f,parent)}
    closed_set=set()

    parent_map={}

    while open_set :
        if game_over==grid:
            break
        print("g:",g)
        row,col=blank(grid)
        #print(row,col)
        moves=moves_cal(row,col)
        if (a,b) in moves:
            moves.remove((a,b))
        #print("moves:",moves)

        grids=[]
        f=[]
        i=0
        for a,b in moves:
            x=first_swap(grid,a,b,row,col)
            #print(x)
            grids.append(make_grid_copy(x))
            f.append(h(grids[i])+g)

            # print_grid(grids[i])
            # print(f[i])

            rev_swap(grid,a,b,row,col)
            #print(grids[i])

            i=i+1

        print("\n")
        # for i in range(3):
        #     print(grids[i],f[i])
        g=g+1
        #print("g: ",g)

        #print(f)
        #one(grids[f.index(max(f))],moves[f.index(max(f))])
        grid=grids[f.index(min(f))]
        a,b=row,col
        #print("next grid\n a,b",grid,a,b)
        print_grid(grid)
        #print(a,b)

    
        ##okay it cant do the same move again
        
                
grid=string_to_grid(input("enter string: "))
main(grid)