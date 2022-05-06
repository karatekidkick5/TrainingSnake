import pygame 
import time 
import math 


Track = pygame.image.load("C:\\Users\\9396238\\OneDrive\\Final Project\\racetrack1.png")
Track = pygame.transform.scale(Track, (1000, 1000))
Blue_Car = pygame.image.load("C:\\Users\\9396238\OneDrive\\Final Project\\pixel_racecar_blue.png")

WIDTH, HEIGHT = Track.get_width(), Track.get_height()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Racing Game')

FPS = 60 
'''
class Car: 
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG 
        self.max_vel = max_vel 
        self.vel = 0 
        self.rotation_vel = rotation_vel
        self.angle = 0 
        self.x, self.y = self.START_POS
        self.acceleration = .1 
    
    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        rotated_image = pygame.transform.rotate(self.img, self.angle)
        rotated_image.get_rect(center = self.img.get_rect(center = (self.x, self.y)))


    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()


class PlayerCar(Car):
    IMG = Blue_Car
    START_POS = (180, 200)

'''
def draw(win):
    
    win.blit()

    
    pygame.display.update()


run = True
clock = pygame.time.Clock()
images = [(Track, (0, 0))]
#player_car = PlayerCar(4, 4)

while run:
    clock.tick(FPS)

    WINDOW.blit(Track, (0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False
'''
    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()

    if not moved:
        player_car.reduce_speed()
'''

pygame.quit()
