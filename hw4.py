"""
Homework #4 - Sudoku Validator
"""
def main():
    file = input("Enter a file name: ")
    puzzle = []
    with open(file) as fp:
        for line in fp:
            line = line.strip()
            print(line)
            puzzle.append(list(line))
    if(valid(puzzle)):
        print("Puzzle is valid")
    else:
        print("Puzzle is invalid")
            
def valid(pzl):
    for i in range(9):
        for j in range(9):
            for coord in getRow(i,j):
                x,y = coord
                if(pzl[i][j]==pzl[x][y]):
                    return False
            for coord in getCol(i,j):
                x,y = coord
                if(pzl[i][j]==pzl[x][y]):
                    return False
            for coord in getSqr(i,j):
                x,y = coord
                if(pzl[i][j]==pzl[x][y]):
                    return False
    return True

def getRow(x,y):
    result=[]
    for i in range(9):
        if(y!=i):
            result.append((x,i))
    return result

def getCol(x,y):
    result=[]
    for i in range(9):
        if(x!=i):
            result.append((i,y))
    return result

def getSqr(x,y):
    result=[]
    for i in range((x//3)*3,((x//3)+1)*3):
        for j in range((y//3)*3,((y//3)+1)*3):
            if(i!=x or j!=y):
                result.append((i,j))
    return result
                
main()
