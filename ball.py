from pico2d import load_image
import game_world

class Ball:
    image = None
    degree = 0
    radian = 0
    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        # self.image.draw(self.x, self.y)
        self.image.clip_composite_draw(0, 0, 21, 21, self.radian, '', self.x, self.y)

    def update(self):
        self.degree = (self.degree + 10) % 360
        self.radian = self.degree * 180 / 3.141592
        self.x += self.velocity

        if self.x < 50 or self.x > 800 - 50:
            game_world.remove_object(self)
