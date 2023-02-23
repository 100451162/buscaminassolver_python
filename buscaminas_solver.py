import random


class Solver:
    def __init__(self, grid, n_bombs):
        self.n_bombs = n_bombs
        self.grid = grid
        self.columns = len(grid)
        self.rows = len(grid[0])
        self.flags_grid = []
        self.n_flags = 0
        self.n_expanded = 0
        self.cells = self.rows * self.columns
        for col in range(0, self.columns):
            self.flags_grid.append([])
            for row in range(0, self.rows):
                self.flags_grid[col].append(False)




    def solve(self):
        self.mostrar_celda(random.randint(0, self.rows - 1), random.randint(0, self.columns - 1))


        while (self.n_expanded != (self.cells -self.n_bombs)):
            print("Iteration")
            min_prob = 1.2
            min_col = self.columns
            min_row = self.rows
            for col in range(0,self.columns):
                for row in range(0, self.rows):
                    if self.grid[col][row].oculto == True and self.flags_grid[col][row] ==False:
                        prob = self.calcular_probabilidad_celda(row,col)
                        if prob == 1:
                            self.flags_grid[col][row] = True
                            self.n_flags +=1
                            continue
                        if prob <= min_prob:
                            min_prob = prob
                            min_col = col
                            min_row = row
                        print(prob, " ", col, " ", row)
            print("Expanding: ",min_row, " ", min_col, " ", min_prob)
            print(self.n_expanded)

            self.mostrar_celda(min_row,min_col)


        return self.grid

    def mostrar_celda(self, row, col):

        if self.grid[col][row].oculto == False:
            return
        self.n_expanded += 1
        self.grid[col][row].oculto = False
        if self.grid[col][row].is_bomb == 0:
            for i in self.grid:
                print(i)

            raise Exception("Boom row "+str(row)+" col "+ str(col))
        if self.grid[col][row].n_near_bombs == 0:
            self.mostrar_todas_alrededor(row,col)

    def mostrar_todas_alrededor(self, row, col):
        for i in range(3):
            for j in range(3):
                col_a = i+ col - 1
                row_b = j+row-1
                if not (col_a < 0 or col_a >= self.columns  or row_b < 0 or row_b >= self.rows or (col_a == col and row == row_b)):
                    self.mostrar_celda(row_b,col_a)

    def calcular_probabilidad_celda(self,row,col):
        probabilidad_bomba = (self.n_bombs -self.n_flags)/(self.cells- self.n_expanded)
        for i in range(3):
            for j in range(3):
                col_a = i + col - 1
                row_b = j + row - 1
                if (not (col_a < 0 or col_a >= self.columns or row_b < 0 or row_b >= self.rows or (col_a == col and row == row_b))):

                    if self.grid[col_a][row_b].oculto == False:
                        probabilidad_bomba *= self.calcular_probabilidad_celda_aux(row_b,col_a)

        return (1-probabilidad_bomba)


    def calcular_probabilidad_celda_aux(self,row,col):
        n_celdas_donde_puede_haber_bomba = 0
        n_bombs = self.grid[col][row].n_near_bombs
        for i in range(3):
            for j in range(3):
                col_a = i + col - 1
                row_b = j + row - 1
                if (not (col_a < 0 or col_a >= self.columns or row_b < 0 or row_b >= self.rows or (col_a == col and row == row_b))):
                    if (self.grid[col_a][row_b].oculto == True and self.flags_grid[col_a][row_b] == False ):
                        n_celdas_donde_puede_haber_bomba += 1
                elif (not (col_a < 0 or col_a >= self.columns or row_b < 0 or row_b >= self.rows or (col_a == col and row == row_b)) and
                    (self.grid[col_a][row_b].oculto == True) and
                    self.flags_grid[col_a][row_b] == True):
                    n_bombs -= 1
        if n_celdas_donde_puede_haber_bomba == 0 or n_bombs == 0:
            return 1
        return (1-(n_bombs/n_celdas_donde_puede_haber_bomba))
