import pygame
import os


class Player(pygame.sprite.Sprite):
    gif = []
    gifDelay = 0
    gifCounter = 0

    def __init__(self, X, Y):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 3
        self.lives_normal = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.imgSize = (24, 22)
        self.currentScore = 0
        self.currentScore_normal = 0
        self.image = pygame.image.load(os.path.join("images", "pl.png"))
        self.gif.append(pygame.image.load(os.path.join("images", "pl.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "pl1.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "pl.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "pl1.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "pl.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "pl1.png")))

        for i in range(6): #gif olması için
            self.gif[i].set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y

    def hide(self): #sprite a çarptığında kaybolması için mainde çağrılan fonksiyon
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (600 / 2, 700 + 200)

    def update(self, keys):
        # eğer player gizliyse tekrar gözüksün diye
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = 600 / 2 #tekrar gözükeceği yer için genişliğin yarısı
            self.rect.bottom = 700 - 10 #height için aynı şey

        self.gifDelay += 1

        if(self.gifDelay%4==0):
            self.image=self.gif[self.gifCounter]
            self.gifCounter+=1
            self.gifDelay=0
            if self.gifCounter==6:
                self.gifCounter=0
        ###PLAYERIN SINIRLARI###
        if keys[pygame.K_UP]:
            if self.rect.y<=600:
                self.rect.y=500 #playerın üst sınırı
            else:
                self.rect.y-=20
        if keys[pygame.K_DOWN]:
            if self.rect.y>=680:
                self.rect.y=680
            else:
                self.rect.y+=20
        if keys[pygame.K_LEFT]:
            if self.rect.x<=0:  #sol sınırı
                self.rect.x=0
            else:
                self.rect.x-=20
        if keys[pygame.K_RIGHT]:
            if self.rect.x>=580:
                self.rect.x=580 #sağ sınır
            else:
                self.rect.x+=20

