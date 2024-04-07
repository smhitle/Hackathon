import pygame

RED = (255, 0, 0)


class ghost:
    def __init__(self, x, y, speed, radius, walls, screen, cell_size, gw, gh):
        self.x = x
        self.y = y
        self.xdir = 0
        self.ydir = 0
        self.modes = ['scatter', 'chase', 'frightened']
        self.color = RED
        self.speed = speed
        self.radius = radius
        self.walls = walls
        self.screen = screen
        self.cell_size = cell_size
        self.gw = gw
        self.gh = gh
        self.cx = (self.x * cell_size) + radius
        self.cy = (self.y * cell_size) + radius
        self.txdir = 0
        self.tydir = 0
        self.inmotion = False

    def update(self):
        if self.inmotion:
            self.cx += self.txdir * self.speed
            self.cy += self.tydir * self.speed
            pygame.draw.circle(self.screen, RED, (self.cx, self.cy), self.radius)
            # checking if motion from one square to other is over
            if (self.cx == ((self.x + self.txdir) * self.cell_size) + self.radius) and (
                    self.cy == ((self.y + self.tydir) * self.cell_size) + self.radius):
                self.x += self.txdir
                self.y += self.tydir
                # wrapping around grid edges
                self.x %= self.gw
                self.y %= self.gh
                self.cx = (self.x * self.cell_size) + self.radius
                self.cy = (self.y * self.cell_size) + self.radius
                if (self.xdir != 0) or (self.ydir != 0):
                    self.txdir = self.xdir
                    self.tydir = self.ydir
                else:
                    self.inmotion = False
        else:
            pygame.draw.circle(self.screen, RED, (self.cx, self.cy), self.radius)
