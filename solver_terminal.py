
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(bo): # function that solves the sudoku, using recursion (my first time!!)
    find = find_empty(bo) # setting a variable for finding the next empty zero position
    if not find: # if find couldn't find another zero
        return True # return True, because that means the board must be solved
    else:
        row, col = find # set find equal to the position that we did find in the returned tuple
    
    for i in range(1,10): # loop through 1-9 inclusively of 9
        if valid(bo, i, (row, col)): # check if adding that number into the board creates a valid solution
            bo[row][col] = i # if it's valid, add it into the board

            if solve(bo): # call solve again, with that new value added continue until...
                return True # the board is solved correctly, if not
            
            bo[row][col] = 0 # reset that value to 0
    # if we loop through all numbers, and non of them are valid, we...
    return False # return False, which forces it to reset the bo[row][col] to zero, because that solution doesn't work

def valid(bo, num, pos): # a function to check if a number works in given position, bo=board, num=number to try, pos=position on board (tuple)
    # Check row
    for i in range(len(bo[0])): # loop through the size of the board
        if bo[pos[0]][i] == num and pos[1] != i: # if the row positions equal the number we tried, and we don't include the number we just inserted
            return False # the num is not valid
    
    # Check column
    for i in range(len(bo)): # loop through the length of rows
        if bo[i][pos[1]] == num and pos[0] != i: # if the column positions equal the number we tried, and we don't include the number we just inserted
            return False # the num is not valid
    
    # Check box
    box_X = pos[1] // 3 # value is either 0, 1, or 2, horizontal box position
    box_Y = pos[0] // 3 # value is either 0, 1, or 2, vertical box position

    for i in range(box_Y * 3, box_Y * 3 + 3): # loop through the 3 row values
        for j in range(box_X * 3, box_X * 3 + 3): # loop through the 3 col values
            if bo[i][j] == num and (i,j) != pos: # if the box value = our checked value, and we aren't checking the position we just submitted...
                return False # the num is not valid
    
    return True # otherwise, return true, this position is valid

def print_board(bo): # a function to print out the current state of the board variable
    for i in range(len(bo)): # loop through the board rows
        if i % 3 == 0 and i != 0: # if the board row is a third and is not the first row
            print("- - - - - - - - - - - - ") # print a divider line

        for j in range(len(bo[0])): # loop through the values in each row
            if j % 3 == 0 and j != 0: # if the value is divisible by 3 and not 0
                print(" | ", end="") # print a grid divider without printing a new line (\n)

            if j == 8: # if we reach the end of the row's values
                print(bo[i][j]) # print the value with a new line (\n)
            else: # if we're not at the end of the row...
                print(str(bo[i][j]) + " ", end="") # print the board value (as string) without a new line

def find_empty(bo): # a function to find the next board value that's empty (value=0)
    for i in range(len(bo)): # loop through the board rows
        for j in range(len(bo[0])): # loop through the 9 values in each row
            if bo[i][j] == 0: # if that board value is 0
                return (i, j) # return a tuple with it's location (row, col)
    
    return None # if there is no squares = 0, return None (to trigger the "if not" in solve)

print_board(board)
solve(board)
print("-------------------------")
print_board(board)