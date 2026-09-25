import pygame

class Object:
    def __init__(self, x, y, width, height, weight, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.weight = weight
        self.color = color
        self.speed_x = 0
        self.speed_y = 0

    def tick(self, speed_x = 0, speed_y = 0):
        self.x += self.speed_x + speed_x
        self.y += self.speed_y + speed_y

    def gravity(self):
        self.speed_y += 5

    def draw_object(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))