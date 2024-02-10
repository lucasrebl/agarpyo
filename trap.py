import pygame
import random

RED = (255, 0, 0)

class Trap:
    def __init__(self, width, height, difficulty):
        self.color = RED
        self.radius = random.randint(20, 75)
        self.difficulty = difficulty
        self.spawn_count = self.get_spawn_count(difficulty)
        self.positions = [[random.randint(0, width), random.randint(0, height)] for _ in range(self.spawn_count)]

    def get_spawn_count(self, difficulty):
        if difficulty == 'easy':
            return 2
        elif difficulty == 'medium':
            return 3
        elif difficulty == 'hard':
            return 4
        else:
            return 0

    def respawn(self, width, height):
        eaten_trap_index = random.randint(0, self.spawn_count - 1)
        self.positions[eaten_trap_index] = [random.randint(0, width), random.randint(0, height)]

    def render(self, screen):
        for position in self.positions:
            pygame.draw.circle(screen, self.color, (int(position[0]), int(position[1])), self.radius)
