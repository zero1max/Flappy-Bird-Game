import random
import time

import pygame

pygame.init()
screen_width = 800
screen_height = 700
size = (screen_width , screen_height)
win = pygame.display.set_mode(size)
pygame.display.set_caption('Bird game')
sky = pygame.image.load('./sky.jpg')

time_ = pygame.time.Clock()


class Player:
    def __init__(self , x , y):
        self.bird_list = []

        for i in range(14):
            img = pygame.image.load(f'./img/bird_{i}.png')
            self.image = pygame.transform.scale(img , (100 , 100))
            self.bird_list.append(self.image)

        self.index = 0
        self.rect = self.bird_list[self.index].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.jump_num = 0
        self.walk_time = 5
        self.game_over = 1

    def update(self):
        self.counter += 1

        if self.game_over == 1:
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] == True:
                self.jump_num = -10

            self.jump_num += 1

            if self.walk_time < self.counter:
                self.counter = 0
                self.index += 1
                if self.index >= 14:
                    self.index = 0

            if self.rect.colliderect(bg.tosiq_rect1) or self.rect.colliderect(bg.tosiq_rect2):
                self.game_over = -1

            self.rect.y += self.jump_num

        win.blit(self.bird_list[self.index] , self.rect)

    
class Backround:
    def __init__(self, x, y):

        self.tosiq_rect1 = pygame.Rect(x, y, 50, 100)
        self.tosiq_rect2 = pygame.Rect(x, 700-100, 50, 100)


        self.speed = 5
        self.walk_time = 40
        self.counter = 0
        self.game_over = 1

    def move_bg(self):
        _ = [200, 300 , 250]
        height1 = random.choice(_)
        height2 = random.choice(_)
        if self.game_over == 1:

            if self.tosiq_rect1.colliderect(bird.rect) or self.tosiq_rect2.colliderect(bird.rect):
                self.game_over = -1
            self.tosiq_rect2.x -= self.speed
            self.tosiq_rect1.x -= self.speed

            if self.tosiq_rect1.x + self.tosiq_rect1.width < 0:
                self.tosiq_rect1.x = 800
                self.tosiq_rect1.height = height1
            if self.tosiq_rect2.x + self.tosiq_rect2.width < 0:
                self.tosiq_rect2.x = 800
                self.tosiq_rect2.height = height2
                self.tosiq_rect2.y = 700 - height2
        else:
            font = pygame.font.Font('freesansbold.ttf', 60)


            text = font.render('Game over', True, 'red', 'white')


            textRect = text.get_rect()


            textRect.center = (screen_width // 2, screen_height // 2)
            win.blit(text, textRect)

            


        pygame.draw.rect(win, 'green', self.tosiq_rect1)
        pygame.draw.rect(win, 'green', self.tosiq_rect2)






bird = Player(50 , 400)
bg = Backround(800   , 0)
running = True
while running:
    time_.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    
    win.blit(sky, (0, 0))
    bird.update()
    bg.move_bg()
    
    pygame.display.update()