import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 50)


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)

    def change_text(self, text, bg="black"):
        """Change the text whe you click"""
        self.text = self.font.render(text, 10, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        screen.blit(button1.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")


def mainloop():
    """ The infinite loop where things happen """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            button1.click(event)
        button1.show()
        clock.tick(30)
        pygame.display.update()


button1 = Button(
    "Meni bos",
    (100, 100),
    font=50,
    bg="navy",
    feedback="Hello! My name is ZeRo_1_MaX")

mainloop()
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41
# 42
# 43
# 44
# 45
# 46
# 47
# 48
# 49
# 50
# 51
# 52
# 53
# 54
# 55
# 56
# 57
# 58
# 59
# 60
# import pygame
 
# pygame.init()
# screen = pygame.display.set_mode((500, 600))
# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 20)
 
 
# class Button:
#     """Create a button, then blit the surface in the while loop"""
 
#     def __init__(self, text,  pos, font, bg="black", feedback=""):
#         self.x, self.y = pos
#         self.font = pygame.font.SysFont("Arial", font)
#         if feedback == "":
#             self.feedback = "text"
#         else:
#             self.feedback = feedback
#         self.change_text(text, bg)
 
#     def change_text(self, text, bg="black"):
#         """Change the text whe you click"""
#         self.text = self.font.render(text, 1, pygame.Color("White"))
#         self.size = self.text.get_size()
#         self.surface = pygame.Surface(self.size)
#         self.surface.fill(bg)
#         self.surface.blit(self.text, (0, 0))
#         self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
#     def show(self):
#         screen.blit(button1.surface, (self.x, self.y))
 
#     def click(self, event):
#         x, y = pygame.mouse.get_pos()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if pygame.mouse.get_pressed()[0]:
#                 if self.rect.collidepoint(x, y):
#                     self.change_text(self.feedback, bg="red")
 
 
# def mainloop():
#     """ The infinite loop where things happen """
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             button1.click(event)
#         button1.show()
#         clock.tick(30)
#         pygame.display.update()
 
 
# button1 = Button(
#     "Click here",
#     (100, 100),
#     font=30,
#     bg="navy",
#     feedback="You clicked me")
 
# mainloop()