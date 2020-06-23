
import pygame.event
import os
import pygame

bg = (0, 0, 0)  #background rengi
size = [600, 700]  # genişlik, yükseklik
screen = pygame.display.set_mode(size)  #ekran oluşturma
pygame.display.set_caption("Centipede")  #title

#BACKGROUND-----------------------
background = pygame.Surface(size)
background.fill(bg)
screen.blit(background, (0, 0))  # ekrana background ekleme

#MUSHROOMS FOTOLARI-----------------------
mushroom_image = pygame.image.load(os.path.join("images", "mush1.png"))  # mantarın hareketleri eklendi
mushroom_image2 = pygame.image.load(os.path.join("images", "mush2.png"))
mushroom_image3 = pygame.image.load(os.path.join("images", "mush3.png"))

mushroom_hard_img = pygame.image.load(os.path.join("images", "lvl2_mushroom1.png"))  # mantarın hareketleri eklendi
mushroom_hard_img2 = pygame.image.load(os.path.join("images", "lvl2_mushroom2.png"))
mushroom_hard_img3 = pygame.image.load(os.path.join("images", "lvl2_mushroom3.png"))

mushroom_image.set_colorkey((0,0,0))
mushroom_image2.set_colorkey((0,0,0))
mushroom_image3.set_colorkey((0,0,0))

mushroom_hard_img.set_colorkey((0,0,0))
mushroom_hard_img2.set_colorkey((0,0,0))
mushroom_hard_img3.set_colorkey((0,0,0))

#MENUDEKİ FOTOLAR-----------------------
menu_header=[]
menu_header.append(pygame.image.load(os.path.join("images", "logo_1.png")))
menu_header.append(pygame.image.load(os.path.join("images", "logo_2.png")))
menu_hard=[]
menu_hard.append(pygame.image.load(os.path.join("images", "hard-1.png")))
menu_hard.append(pygame.image.load(os.path.join("images", "hard-2.png")))
menu_handbook=[]
menu_handbook.append(pygame.image.load(os.path.join("images", "handbook-1.png")))
menu_handbook.append(pygame.image.load(os.path.join("images", "handbook-2.png")))
menu_easy=[]
menu_easy.append(pygame.image.load(os.path.join("images", "easy_1.png")))
menu_easy.append(pygame.image.load(os.path.join("images", "easy_2.png")))
menu_normal=[]
menu_normal.append(pygame.image.load(os.path.join("images", "normal-2.png")))
menu_normal.append(pygame.image.load(os.path.join("images", "normal-1.png")))
menu_quit=[]
menu_quit.append(pygame.image.load(os.path.join("images", "exit-1.png")))
menu_quit.append(pygame.image.load(os.path.join("images", "exit-2.png")))
menu_mute=[]
menu_mute.append(pygame.image.load(os.path.join("images", "mute.png")))

menu_footer=pygame.image.load(os.path.join("images", "footer_black.png"))
#HANDBOOK FOTOLAR-----------------------
handbook_space=[]
for i in range(0,6):
    handbook_space.append(pygame.image.load(os.path.join("images", "sp-%d.png" % i)))
handbook_up=[]
for i in range(1,5):
    handbook_up.append(pygame.image.load(os.path.join("images", "yon-%d.png" % i)))
handbook_shroom=[]
for i in range(1,6):
    handbook_shroom.append(pygame.image.load(os.path.join("images", "b2-%d.png" % i)))
handbook_flea=[]
for i in range(1,5):
    handbook_flea.append(pygame.image.load(os.path.join("images", "flea-%d.png" % i)))
handbook_spider=[]
for i in range(1,10):
    handbook_spider.append(pygame.image.load(os.path.join("images", "spider-%d.png" % i)))
handbook_centipede=[]
for i in range(1,5):
    handbook_centipede.append(pygame.image.load(os.path.join("images", "centi-%d.png" % i)))
handbook_footer=[]
for i in range(1, 3):
    handbook_footer.append(pygame.image.load(os.path.join("images", "esc_%d.png" % i)))


