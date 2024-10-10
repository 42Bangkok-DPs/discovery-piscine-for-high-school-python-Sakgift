def checkmate(board):#creates
    king_row , king_col = None, None #None as in emptyspaces(Not king)
    for x, row in enumerate(board):#enumerate (toomanyvariables)
        if "K" in row:
            king_row , king_col = x , row.index("K")#index find K
            break
    if king_row is None or king_col is None:
        return "FAIL"# no king
    
    def check_pawn(row, col):#row is hori and col is vert
        if row > 0:#row 0 is the top row so this checks if it is on the top row 
            if col > 0 and board[row-1][col-1] == "P" : return True #-1(left)+1(Right)for rows and viseversa for col
            if col < len(board[0]) - 1 and board[row-1][col+1] == "P": return True
        return False
    
    def check_bishop(row, col):#move diagonal = all 4 directions
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]#(Left up)(left dowm)(right up)(right down)
        for d in directions:
            r, c =row + d[0], col + d[1]#hori index is [0] and vert is [1]
            while 0 <= r < len(board) and 0 <= c < len(board[0]):
                if board[r][c] == "B": return True 
                if board[r][c] != '.': break #if doesnt see empty space it stop loop
                r, c = r + d[0], c + d[1]
            return False
        
    def check_rook(row, col):#straight left right up down
        directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
        for d in directions:
            r, c =row + d[0], col + d[1]
            while 0 <= r < len(board) and 0 <= c < len(board[0]):
                if board[r][c] == "R": return True
                if board[r][c] != ".": break
                r, c = r + d[0], c + d[1]# if return same False
            return False
        
    def check_queen(row, col):
        # Queen combines the moves of Rook and Bishop
        return check_rook(row, col) or check_bishop(row, col)
    
    if check_pawn(king_row, king_col) or check_bishop(king_row, king_col) or check_rook(king_row, king_col) or check_queen(king_row, king_col):
        return "Success"
    
    return "FAIL"

#boards
board_use = [
    ".......",
    "...P...",
    "..K....",
    ".......",
]
print(checkmate(board_use))  # Should return "Fail"