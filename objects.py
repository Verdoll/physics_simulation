import pygame

class Object:
    def __init__(self, x, y, width, height, weight, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.weight = weight
        self.color = color
        self.negative_speed_x = 0
        self.down_speed_y = 0
        self.positive_speed_x = 0
        self.up_speed_y = 0

    def tick(self, speed_x = 0, speed_y = 0):
        moving_y = -self.up_speed_y + self.down_speed_y
        self.x += -self.negative_speed_x + speed_x + self.positive_speed_x
        self.y += moving_y

    def gravity(self):
        if self.up_speed_y > 0:
            self.up_speed_y -= 1
        else:
            self.down_speed_y += 1

    def crash_with_floor(self):
        if self.down_speed_y > 0:
            self.up_speed_y += self.down_speed_y // 2
            self.down_speed_y = 0


    def draw_object(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    #brainfuck func
    def get_pixels(self):
        result = []
        for x in range(self.x, self.x + self.width + 1):
            for y in range(self.y, self.y + self.height + 1):
                result.append((x, y))
        return result