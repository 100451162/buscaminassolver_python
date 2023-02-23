class Solver:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.columns = len(grid[0])

    def solve(self):
        self.mostrar_celda(0,0)

        return self.grid

    def mostrar_celda(self, row, col):

        if self.grid[col][row].oculto == False:
            return
        self.grid[col][row].oculto = False
        if self.grid[col][row].is_bomb == 0:
            raise Exception("Boom")
        if self.grid[col][row].n_near_bombs == 0:

            self.mostrar_todas_alrededor(row,col)

    def mostrar_todas_alrededor(self, row, col):
            print("Current: ",row," ",col)
            for i in range(3):
                for j in range(3):
                    a = i+ col - 1
                    b = j+row-1
                    if not (a < 0 or a >= self.columns  or b < 0 or b >= self.rows or (a == col and row == b)):
                        print("Expand: ", a, " ",b)
                        self.mostrar_celda(b,a)