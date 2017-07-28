class piece:
	row_change = []
	col_change = []
  	def __init__(self,name,coordinate):
            self.name = name
            self.coordinate = coordinate
        def possible_moves(self):
                row = self.coordinate[0]
                col = self.coordinate[1]
                possible_moves = []
                for position in zip(self.row_change,self.col_change):
                        if row+position[0] >= 0 and col+position[1] >= 0:
                                if row+position[0] <= 8 and col+position[1] <= 8:
                                        possible_moves.append([row+position[0],col+position[1]])
                return possible_moves
class pawn(piece):
	row_change = [1,1,1,2]
	col_change = [-1,0,1,0]

class rook(piece):
	row_change = [-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	col_change = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7]

class bishop(piece):
	row_change = [-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,7,6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7]
	col_change = [-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7]

class knight(piece):
	row_change = [2,2,-2,-2,1,-1,1,-1]
	col_change = [1,-1,-1,1,2,2,-2,-2]

class queen(piece):
        diagonal_row = [-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,7,6,5,4,3,2,1,-1,-2,-3,-4,-5,-6,-7]
	diagonal_col = [-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7]
	linear_row = [-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	linear_col = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7]
	row_change = diagonal_row+linear_row
	col_change = diagonal_col+linear_col

class king(piece):
	row_change = [1,1,1,0,0,-1,-1,-1]
	col_change = [-1,0,1,-1,1,-1,0,-1]

pawn = pawn(name='pawn',coordinate = [1,1])
print(pawn.possible_moves())
queen = queen(name='queen',coordinate = [5,5])
print(queen.possible_moves())
board = [['']*8]*8

