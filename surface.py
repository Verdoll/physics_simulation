import pygame

class Surface:
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_pixels(self):
        result = []
        for x in range(self.x, self.x + self.width + 1):
            for y in range(self.y, self.y + self.height + 1):
                result.append((x, y))
        return result

    def draw_surface(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, self.width, self.height))