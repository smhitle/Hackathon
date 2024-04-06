

class pacman:
    def __init__(self, x, y, c, i, j, canvas, root):
        self.x = x
        self.y = y
        self.c = c  # c = 35
        self.i = i
        self.j = j
        self.canvas = canvas
        self.root = root
        self.body = self.canvas.create_oval(x*c, y*c, (x*c)+c, (y*c)+c, fill='yellow')

        self.xdir = 1
        self.ydir = 0

    def display(self):
        pass

    def update(self):
        # pps has to be divisible with c (35)
        xdir = self.xdir
        ydir = self.ydir
        if (self.x + xdir >= self.i) or (self.x + xdir < 0) or (self.y + ydir >= self.j) or (self.y + ydir < 0):
            self.xdir = 0
            self.ydir = 0
        else:
            pps = 4
            for f in range(self.c//pps):
                self.canvas.move(self.body, xdir*pps, ydir*pps)
                self.canvas.update()
            self.x += xdir
            self.y += ydir
        print('pacman x', self.x)
        print('pacman y', self.y)

    def up(self, event):

        self.xdir = 0
        self.ydir = -1
        print('up')

    def down(self, event):
        self.xdir = 0
        self.ydir = 1
        print('down')

    def left(self, event):
        self.xdir = -1
        self.ydir = 0
        print('left')

    def right(self, event):
        self.xdir = 1
        self.ydir = 0
        print('right')
