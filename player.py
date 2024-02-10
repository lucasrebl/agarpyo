import pygame

BLUE = (0, 0, 255)

class Player:
    def __init__(self, width, height):
        self.color = BLUE
        self.speed = 100
        self.size = 40
        self.position = [width // 2, height // 2]
        self.direction = (0, 0)
        self.width = width
        self.height = height
        self.score = 0
        
    def handle_key_event(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            self.direction = (0, -1)
        elif keys[pygame.K_s]:
            self.direction = (0, 1)
        elif keys[pygame.K_q]:
            self.direction = (-1, 0)
        elif keys[pygame.K_d]:
            self.direction = (1, 0)
            
    def handle_mouse_event(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        diff_x = mouseX - self.width // 2
        diff_y = mouseY - self.height // 2
        max_diff = 5
        diff_x = max(-max_diff, min(diff_x, max_diff))
        diff_y = max(-max_diff, min(diff_y, max_diff))
        self.direction = (diff_x, diff_y)

    def move(self, elapsed_time):
        self.position[0] += self.direction[0] * self.speed * elapsed_time
        self.position[1] += self.direction[1] * self.speed * elapsed_time
        
    def teleport(self, width, height):
        if self.position[0] > width:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = width

        if self.position[1] > height:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = height

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.size)
        
    def reset(self, width, height):
        self.score = 0
        self.speed = 100
        self.size = 40
        self.position = [width // 2, height // 2]
        self.direction = (0, 0)