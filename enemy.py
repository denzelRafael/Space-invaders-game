class Enemy:
    def __init__(self, x, y, speed, alive=True):
        self.x = x
        self.y = y
        self.speed = speed
        self.alive = alive

    def move(self, dt):
        self.x += self.speed * dt
        


    