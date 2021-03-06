import pygame,os


class Centipede(pygame.sprite.Sprite):
    gifDelay=0
    gifCounter=0
    gif=[]

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.imgSize = (20, 20) #foto boyutları 20x20
        self.image = pygame.image.load(os.path.join("images", "centi2.png"))
        self.gif.append(pygame.image.load(os.path.join("images", "centi2.png")))
        self.gif.append(pygame.image.load(os.path.join("images", "centi3.png")))
        transparent=self.image.get_at((1,1))
        self.image.set_colorkey(transparent)
        for i in range(2): #gif oluşturma
            self.gif[i].set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.left_right=1
        self.up_down=1
        self.vertical_move=0
    def update(self):
        #Gif
        self.gifDelay+=1
        if(self.gifDelay%4==0):
            self.image=self.gif[self.gifCounter]
            self.gifCounter+=1
            self.gifDelay=0
            if self.gifCounter==2:
                self.gifCounter=0
        #soldan sağa hareketi
        if self.vertical_move>0:
            self.vertical_move-=1

        if(self.left_right==1 and self.vertical_move==0):
            self.rect.x+=20 #20 olmasının centinin 20x20 olması 20 birimlik hareket tanımlandı
            #sağ kısım
            if(self.rect.x>580):
                self.rect.x-=20 #sağ sınırı
                self.collide()
                self.vertical_move-=1
                if(self.rect.y>=680): #ne kadar uzunluktan sonra yukarı çıkacağı height 700dü
                    self.up_down=0
                    self.rect.x-=20
                if self.rect.y <0: #en üste çıktıktan sonra geri dönmesi için
                    self.up_down=1
                    self.rect.x +=20

        elif(self.left_right==0 and self.vertical_move==0):
            self.rect.x-=20
            #left wall
            if(self.rect.x<0): ##sol sınırı
                self.rect.x+=20
                self.collide()
                self.vertical_move-=1
                #en alt sınır
                if(self.rect.y>=680):
                    self.up_down=0
                if self.rect.y <0: #en üste çıktıktan sonra geri dönmesi için
                    self.up_down=1
                    self.rect.x +=20
    def collide(self):
        self.vertical_move=2
        if(self.left_right==1):
            self.left_right=0
            if(self.up_down==1):
                self.rect.y+=20
            else:
                self.rect.y-=20
        elif(self.left_right==0):
            self.left_right=1
            if(self.up_down==1):
                self.rect.y+=20
            else:
                self.rect.y-=20
