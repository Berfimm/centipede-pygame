import pygame,random,os

class Explosion(pygame.sprite.Sprite):
    gifDelay=0
    gifCounter=0
    gif=[]
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.imgSize=(20,20)
        self.image=pygame.image.load(os.path.join("images", "expo1.png"))
        self.gif.append(pygame.image.load(os.path.join("images", "expo1.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "expo2.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "expo3.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "expo4.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "expo5.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "expo6.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "expo5.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "expo4.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "expo3.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "expo2.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "expo1.png")))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        for i in range(11): #11 foto ekledim hareketli gif gibi gözüksün diye
            self.gif[i].set_colorkey((0,0,0))
    def update(self):
        #Gif
        self.gifDelay+=1
        if(self.gifDelay%1==0):
            self.image=self.gif[self.gifCounter]
            self.gifCounter+=1
            self.gifDelay=0
            if self.gifCounter==11:
                self.kill()
