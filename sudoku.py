#User function Template for python3

class Solution:
    def isSafe(self, mat, row, col, num):
        # Check row and column
        for i in range(9):
            if mat[row][i] == num or mat[i][col] == num:
                return False
        
        # Check 3x3 sub-grid
        startRow, startCol = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if mat[startRow + i][startCol + j] == num:
                    return False
        return True

    # Function to find an empty cell
    def findEmptyCell(self, mat):
        for i in range(9):
            for j in range(9):
                if mat[i][j] == 0:
                    return (i, j)  # Return the first empty cell
        return None  # No empty cells left, Sudoku is solved

    # Function to solve Sudoku using bac
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        
        # Your code here
        empty = self.findEmptyCell(mat)
        if not empty:
            return True  # No empty cells, Sudoku is solved

        row, col = empty

        for num in range(1, 10):  # Try numbers 1 to 9
            if self.isSafe(mat, row, col, num):
                mat[row][col] = num  # Place the number

                if self.solveSudoku(mat):  # Recursively solve the rest
                    return True
                
                mat[row][col] = 0  # Backtrack if placing 'num' leads to failure

        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends
