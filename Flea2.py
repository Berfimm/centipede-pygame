import pygame, random, os


class Flea2(pygame.sprite.Sprite):
    drop = 0
    ax = 0
    ay = 0
    isActive = False
    gifDelay = 0
    gifCounter = 0
    gif = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgSize = (20, 20) #fotolar 20x20
        self.image = pygame.image.load(os.path.join("images", "lvl2_flea1.png"))
        self.gif.append(pygame.image.load(os.path.join("images", "lvl2_flea1.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "lvl2_flea2.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "lvl2_flea3.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "lvl2_flea4.png")))
        transparent = self.image.get_at((1, 1))
        self.image.set_colorkey(transparent)
        self.rect = self.image.get_rect()
        self.rect.y = -20
        self.ax = self.rect.x
        self.ay = self.rect.y
        for i in range(4):
            self.gif[i].set_colorkey((0, 0, 0))

    def update(self):
        if (self.isActive):
            self.gifDelay += 1
            if (self.gifDelay % 4 == 0): #gif kısmı
                self.image = self.gif[self.gifCounter]
                self.gifCounter += 1
                self.gifDelay = 0
                if self.gifCounter == 4:
                    self.gifCounter = 0
            rnd = random.randint(1, 5)
            if (rnd == 1 and self.rect.y % 20 == 0):
                self.drop = 1
                self.ax = self.rect.x
                self.ay = self.rect.y
            self.rect.y += 10
            if (self.rect.y >= 780):
                self.drop = 0
                self.deactivate()

    def activate(self):
        self.isActive = True
        startpos = random.randint(0, 29)
        self.rect.x = startpos * 20

    def deactivate(self):
        self.rect.y = -40
        self.isActive = False

