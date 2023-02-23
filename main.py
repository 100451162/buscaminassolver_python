from buscaminas_solver import Solver
import random

class Celda:
    def __init__(self):
        self.n_near_bombs = 0
        self.is_bomb = 0
        self.oculto = True

    def __repr__(self):
        return str([self.n_near_bombs, self.oculto, self.is_bomb])


def main():
    grid, n_bombs = generar_matriz(10,10,5)

    solver = Solver(grid, n_bombs)
    grid_v2 = solver.solve()

    for i in grid_v2:
        print(i)

def generar_matriz(rows,columns,bomb_percentage):
    grid = []
    n_bombs = 0
    """Generar bombas"""
    for col in range(0, columns):
        grid.append([])
        for row in range(0, rows):
            is_bomb = random.randint(0, bomb_percentage)
            celda = Celda()
            celda.is_bomb = is_bomb
            grid[col].append(celda)
            if(is_bomb == 0):
                n_bombs +=1


    """Generar near bombs"""
    for col in range(0, columns):
        for row in range(0, rows):
            if grid[col][row].is_bomb == 0:
                for i in range(3):
                    for j in range(3):
                        a = i+ col - 1
                        b = j+row-1
                        if not (a < 0 or a >= columns or b < 0 or b >= rows):
                            grid[i+col-1][j+row-1].n_near_bombs += 1


    print("Generating Grid: ")
    print("N of cells: "+ str(rows*columns))
    print("N bombs: "+ str(n_bombs))

    return grid, n_bombs

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
