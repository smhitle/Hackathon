from tkinter import *
from pacman import pacman
from ghost import ghost

C = 36
X, Y = 20, 15


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Pacman")
        self.canvas = Canvas(self.root, height=C*Y, width=C*X)
        self.canvas.grid(row=0, column=0)

        for i in range(X):
            for j in range(Y):
                self.canvas.create_rectangle(i*C, j*C, (i*C)+C, (j*C)+C, fill='black', outline='grey')

        self.pacman = pacman(0, 0, C, X, Y, self.canvas, self.root)
        self.ghosts = []
        self.ghosts.append(ghost(0, 3, C, X, Y, "red", self.canvas))
        self.ghosts.append(ghost(0, 5, C, X, Y, "orange", self.canvas))
        self.ghosts.append(ghost(0, 10, C, X, Y, "cyan", self.canvas))
        self.ghosts.append(ghost(0, 14, C, X, Y, "pink", self.canvas))

        self.root.bind('<Up>', self.pacman.up)
        self.root.bind('<Left>', self.pacman.left)
        self.root.bind('<Right>', self.pacman.right)
        self.root.bind('<Down>', self.pacman.down)
        self.root.bind('w', self.pacman.up)
        self.root.bind('a', self.pacman.left)
        self.root.bind('d', self.pacman.right)
        self.root.bind('s', self.pacman.down)

        self.run()

    def run(self):

        while not self.checkdead():
            self.pacman.update()
            for ghost in self.ghosts:
                ghost.update()

        self.root.mainloop()

    def checkdead(self):
        for ghost in self.ghosts:
            if (ghost.x == self.pacman.x) and (ghost.y == self.pacman.y):
                return True

        return False


if __name__ == "__main__":
    obj = Main()
