import pygame, math, random
import os


class Spider2(pygame.sprite.Sprite):
    left_right = 1
    isActive = False
    gifDelay = 0
    gifCounter = 0
    gif = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgSize = (40, 20)
        self.image = pygame.image.load(os.path.join("images", "lvl2_spider1.png"))
        self.gif.append(pygame.image.load(os.path.join("images", "lvl2_spider1.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "lvl2_spider2.png")))
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.y = 550  # 700
        self.time = 0
        for i in range(2):
            self.gif[i].set_colorkey((0, 0, 0))
        start_position = random.randint(1, 2)
        if start_position == 1:
            self.rect.x = -40
            self.left_right = 1
        else:
            self.left_right = 0
            self.rect.x = 600

    def update(self):
        if (self.isActive):
            if (self.gifDelay % 8 == 0): #gif kısmı
                self.image = self.gif[self.gifCounter]
                self.gifCounter += 1
                self.gifDelay = 0
                if self.gifCounter == 2:
                    self.gifCounter = 0
            if self.time == 0:
                self.time = random.randint(5, 10)
                self.direction = random.randint(1, 4)
            # diagonal down
            if self.direction == 1:
                if self.left_right == 1:
                    self.rect.x = self.rect.x + 10
                else:
                    self.rect.x = self.rect.x - 10
                self.rect.y = self.rect.y + 5
            # diagonal up
            if self.direction == 2:
                if self.left_right == 1:
                    self.rect.x = self.rect.x + 10
                else:
                    self.rect.x = self.rect.x - 10
                self.rect.y = self.rect.y - 5
            # up
            if self.direction == 3:
                self.rect.y = self.rect.y - 5
            # down
            if self.direction == 4:
                self.rect.y = self.rect.y + 5
            if self.rect.y >= 620:  # spider sınırı
                if self.direction == 1:
                    self.direction = 2
                else:
                    self.direction = 3
            if self.rect.y <= 500:  # spider sınırı
                if self.direction == 2:
                    self.direction = 1
                else:
                    self.direction = 4
            if self.rect.x < -40 or self.rect.x > 600:  # 600
                self.deactivate()
            self.time -= 1

    def activate(self):
        self.isActive = True
        start_position = random.randint(1, 2)
        self.left_right = start_position
        if start_position == 1:
            self.rect.x = -40
            self.left_right = 1
        else:
            self.rect.x = 600

    def deactivate(self):
        self.rect.x = -40
        self.isActive = False


