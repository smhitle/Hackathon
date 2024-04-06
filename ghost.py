

class ghost:
    def __init__(self, x, y, c, i, j, color, canvas):
        self.color = color
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.c = c
        self.canvas = canvas
        self.body = self.canvas.create_oval(x*c, y*c, (x*c)+c, (y*c)+c, fill=color)

        self.xdir = 0
        self.ydir = 0

    def move(self):
        pass

    def display(self):
        pass

    def update(self):
        self.canvas.move(self.body, self.xdir*self.c, self.ydir*self.c)
        self.x += self.xdir
        self.y += self.ydir

    def up(self, event):
        self.xdir = 0
        self.ydir = 1

    def down(self, event):
        self.xdir = 0
        self.ydir = -1

    def left(self, event):
        self.xdir = -1
        self.ydir = 0

    def right(self, event):
        self.xdir = 1
        self.ydir = 0
