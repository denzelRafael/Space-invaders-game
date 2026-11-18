class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, dt, direction, WIDTH):
        if direction == "right":
            self.x += self.speed * dt
            self.x = min(self.x, WIDTH - 50)  # Ensure the player doesn't go out of the screen
        
        if direction == "left":
            self.x -= self.speed * dt
            self.x = max(self.x, 0)  # Ensure the player doesn't go out of the screen
        