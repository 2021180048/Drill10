from pico2d import load_image
import game_world

class Ball:
    image = None
    degree = 0
    radian = 0
    def __init__(self, x, y, velocity):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        # self.image.draw(self.x, self.y)
        if self.velocity > 0:
            self.image.clip_composite_draw(0, 0, 21, 21, -self.radian, '', self.x, self.y)
        if self.velocity < 0:
            self.image.clip_composite_draw(0, 0, 21, 21, self.radian, '', self.x, self.y)

    def update(self):
        self.degree = (self.degree + 20) % 360
        
        self.radian = self.degree * 3.141592 / 180
        self.x += self.velocity

        if self.x < 50 or self.x > 800 - 50:
            game_world.remove_object(self)
