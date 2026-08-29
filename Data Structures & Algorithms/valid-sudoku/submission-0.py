class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        lignesVerification = collections.defaultdict(set)
        columnVerification = collections.defaultdict(set)
        cellsVerification = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                if (board[i][j] in lignesVerification[i] or board[i][j] in columnVerification[j] or board[i][j] in cellsVerification[(i//3,j//3)]):
                    return False
                
                lignesVerification[i].add(board[i][j])
                columnVerification[j].add(board[i][j])
                cellsVerification[(i//3,j//3)].add(board[i][j])
            
        return True