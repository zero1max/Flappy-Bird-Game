import random
import time

import pygame

pygame.init()
screen_width = 600
screen_height = 800
size = (screen_width , screen_height)
win = pygame.display.set_mode(size)
pygame.display.set_caption('Bird game')

time_ = pygame.time.Clock()
def music():

    file = ['./sunkenland.mp3']
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(random.choice(file))
    pygame.mixer.music.play()

class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text, pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show1(self):
        win.blit(button1.surface, (self.x, self.y))
    def show2(self):
        win.blit(button2.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if button1.rect.collidepoint(x, y):
                    mainloop()
                if button2.rect.collidepoint(x, y):
                    pygame.quit()


button1 = Button(
    "Start",
    (450, 650),
    font=40,
    bg="green",
    feedback="You clicked me")

button2 = Button(
    'Quit',
    (250 , 650),
    font = 40,
    bg = 'red'
)
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

        if self.rect.top >= screen_height:
            self.game_over = -1


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

        else:
            font = pygame.font.Font('freesansbold.ttf', 60)

            text = font.render('Game over', True, 'red')

            textRect = text.get_rect()


            textRect.center = (screen_width // 2, screen_height // 2)
            win.blit(text, textRect)
            button1.show1()
            button2.show2()





        win.blit(self.bird_list[self.index] , self.rect)


class Backround:
    def __init__(self, x, y):

        self.tosiq_rect1 = pygame.Rect(x, y, 50, 100)
        self.tosiq_rect2 = pygame.Rect(600, 800-100, 50, 100)


        self.speed = 5
        self.walk_time = 40
        self.counter = 0
        self.game_over = 1
        self.score = 0
        self.height_score = 0

    def move_bg(self):
        _ = [200, 240 , 250]
        height1 = random.choice(_)
        height2 = random.choice(_)
        if self.game_over == 1:

            if self.tosiq_rect1.colliderect(bird.rect) or self.tosiq_rect2.colliderect(bird.rect):
                self.game_over = -1
            self.tosiq_rect2.x -= self.speed
            self.tosiq_rect1.x -= self.speed

            if self.tosiq_rect1.x + self.tosiq_rect1.width < 0:
                self.tosiq_rect1.x = 600
                self.tosiq_rect1.height = height1
                if self.game_over == 1 and bird.game_over == 1:
                    self.score += 10
            if self.tosiq_rect2.x + self.tosiq_rect2.width < 0:
                self.tosiq_rect2.x = 600
                self.tosiq_rect2.height = height2
                self.tosiq_rect2.y = 800 - height2
        else:

            font = pygame.font.Font('freesansbold.ttf', 60)


            text = font.render('Game over', True, 'red')


            textRect = text.get_rect()


            textRect.center = (screen_width // 2, screen_height // 2)
            win.blit(text, textRect)
            button1.show1()
            button2.show2()


        pygame.draw.rect(win, 'green', self.tosiq_rect1)
        pygame.draw.rect(win, 'green', self.tosiq_rect2)




img_load = pygame.image.load('./sky.jpg')
img = pygame.transform.scale(img_load , (600 , 800))


def score():
    font = pygame.font.Font('freesansbold.ttf', 30)

    text = font.render(f'Score : {bg.score}', True, 'red')
    # text.set_alpha(0)

    textRect = text.get_rect()

    textRect.center = (screen_width - 100, 50)
    win.blit(text, textRect)

def hight_score():
    font = pygame.font.Font('freesansbold.ttf', 30)

    text = font.render(f'Hight Score : {bg.height_score}', True, 'red')
    # text.set_alpha(0)

    textRect = text.get_rect()

    textRect.center = (screen_width - 450, 50)
    win.blit(text, textRect)
    if bg.score > bg.height_score:
        bg.height_score += 10

def mainloop():
    global bird, bg
    music()
    bird = Player(50, 400)
    bg = Backround(600, 0)
    running = True
    while running:
        time_.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button1.click(event)
            button2.click(event)




        win.blit(img , img.get_rect())
        bg.move_bg()
        bird.update()
        score()
        hight_score()    
        pygame.display.update()
    pygame.quit()

mainloop()