import time
#0 represents blanks on the grid 
#treat 0 as value z which is the unknown numbers on the grid
grid_9x9 = [
    [4,5,0,0,0,0,0,0,0],
    [0,0,2,0,7,0,6,3,0],
    [0,0,0,0,0,0,0,2,8],
    [0,0,0,9,5,0,0,0,0],
    [0,8,6,0,0,0,2,0,0],
    [0,2,0,6,0,0,7,5,0],
    [0,0,0,0,0,0,4,7,6],
    [0,7,0,0,4,5,0,0,0],
    [0,0,8,0,0,9,0,0,0],
]

#backtrack algorithm
start = time.time()
def algo(grid_9x9):
    find = find_x(grid_9x9)
    if not find:
        return True
    else: 
        row,col = find

    for i in range(1,10):
        if check_x(grid_9x9,i,(row,col)):
            grid_9x9[row][col]= i 
            
            if algo(grid_9x9):
                return True
            
            grid_9x9[row][col] = 0

    return False




#x and y are possitions, and z is the numbers on the grid 
def print_grid(grid_9x9):
    for i in range(len(grid_9x9)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - ")

        for j in range (len(grid_9x9[0])):
            if j % 3 == 0 and j != 0:
                print("|", end ="")

            if j == 8:
                print(grid_9x9[i][j])
            else:
                print(str(grid_9x9[i][j]) + " ", end ="")

#finding the x value 
def find_x(grid_9x9):
    for x in range(len(grid_9x9)):
        for j in range(len(grid_9x9[0])):
            if grid_9x9[x][j] == 0:
                return (x,j) #row for y,x 
    return None


#checking for the numbers on the grid if it fits or not 
def check_x(grid_9x9,number,position):
    #checking the row 
    for i in range(len(grid_9x9[0])):
        if grid_9x9[position[0]][i] == number and position[1] !=i:
            return False
        
    #check column
    for i in range(len(grid_9x9)):
        if grid_9x9[i][position[1]] == number and position[1] !=i:
            return False
        
    #check one of the 9 boxes
    box_x = position[1]//3
    box_y = position[0]//3
    for i in range(box_y*3, box_y*3 +3):
        for j in range(box_x*3, box_x*3 +3):
            if grid_9x9[i][j] == number and (i,j) != position:
                return False
            
    return True


print_grid(grid_9x9)
algo(grid_9x9)
print("___________________")
print_grid(grid_9x9)
end = time.time()

print("it took ", end-start, "seconds to do this sudoku problem")
