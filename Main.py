from SpriteGroup import *
from mute import *
from pause import *
import pygame.event
from Explosion import *
from Visualization import *
pygame.init()
pygame.mixer.music.load(os.path.join("sounds", "01_Opening.mp3"))  #açılış müziği
pygame.mixer.music.play(-1, 0.0)
bg = (0, 0, 0)
level = 1#easy mode
level2 = 2#hard mode
empty = pygame.Surface([20, 20])
empty.fill(bg)
clock = pygame.time.Clock() # oyun zamanını tutuyor
clock_tick=20 #oyunun hızı
tickCounter=0
running= True #loop boolean değeri
###########

########
background = pygame.Surface(size) #background
background.fill(bg)
screen.blit(background, (0, 0))  # ekrana background ekleme
game_mode='menu'

#FONTS
over_font = pygame.font.SysFont("comicsansms", 40)
label_font = pygame.font.SysFont("comicsans", 30)
start_font = pygame.font.SysFont("comicsansms", 40)


menu_options=1
graphics=0


############GAME MAPS-----------
game_map = []
game_map_hard = []
game_map_normal = []
empty = pygame.Surface([20, 20])
empty.fill(bg)

def setup_game_map():
    global game_map
    global game_map_normal
    global game_map_hard
    game_map = []
    game_map_normal = []
    game_map_hard = []


    for x in range(40):
        arrayOfZeros = [0]*30
        game_map.append(arrayOfZeros)
        game_map_hard.append(arrayOfZeros)
        game_map_normal.append(arrayOfZeros)
    for x in range (30):
        randomX=random.randint(0,29)
        randomY=random.randint(0,27)
        game_map[randomX][randomY] = 1
        game_map_hard[randomX][randomY] = 1
        game_map_normal[randomX][randomY] = 1

def draw_game_map():
        for column in range(30):
            for row in range(40):
                spot = game_map[row][column]
                if spot == 1:  #ilk hali
                    screen.blit(empty,[column*20, row*20])
                    screen.blit(mushroom_image, [column*20, row*20])  # mantarın foto boyutu 20x20
                if spot == 2:  #ikinci hali
                    screen.blit(empty,[column*20, row*20])
                    screen.blit(mushroom_image2, [column*20, row*20])
                if spot == 3:
                    screen.blit(empty,[column*20, row*20])
                    screen.blit(mushroom_image3, [column*20, row*20])
                if spot == 4:
                    screen.blit(empty,[column*20, row*20])
                    game_map[row][column] = 0

def draw_map_normal():
    for column in range(30):
        for row in range(40):
            spot = game_map_normal[row][column]
            if spot == 1:  # ilk hali
                screen.blit(empty, [column * 20, row * 20])
                screen.blit(mushroom_image, [column * 20, row * 20])  # mantarın foto boyutu 20x20
            if spot == 2:  # ikinci hali
                screen.blit(empty, [column * 20, row * 20])
                screen.blit(mushroom_image2, [column * 20, row * 20])
            if spot == 3:
                screen.blit(empty, [column * 20, row * 20])
                screen.blit(mushroom_image3, [column * 20, row * 20])
            if spot == 4:
                screen.blit(empty, [column * 20, row * 20])
                game_map_normal[row][column] = 0

def draw_hard_map():
    for column in range(30):
        for row in range(40):
            spot = game_map_hard[row][column]
            if spot == 1:  # ilk hali
                screen.blit(empty, [column * 20, row * 20])
                screen.blit(mushroom_hard_img, [column * 20, row * 20])  # mantarın foto boyutu 20x20
            if spot == 2:  # ikinci hali
                screen.blit(empty, [column * 20, row * 20])
                screen.blit(mushroom_hard_img2, [column * 20, row * 20])
            if spot == 3:
                screen.blit(empty, [column * 20, row * 20])
                screen.blit(mushroom_hard_img3, [column * 20, row * 20])
            if spot == 4:
                screen.blit(empty, [column * 20, row * 20])
                game_map_hard[row][column] = 0

setup_game_map()

while running:
    clock.tick(clock_tick)
    tickCounter+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
           running=False

######INSTRUCTION######
    if game_mode=='handbook':
        pygame.display.set_caption("Centipede")
        if(tickCounter%10==0): #hızları
            graphics+=1
            #screen.blit(handbook_footer,(0,600))
            screen.blit(handbook_space[graphics%6],(0,0))
            screen.blit(handbook_up[graphics%4],(300,0))
            screen.blit(handbook_shroom[graphics%5],(0,200))
            screen.blit(handbook_flea[graphics%4],(300,200))
            screen.blit(handbook_spider[graphics%9],(0,400))
            screen.blit(handbook_centipede[graphics%4],(300,400))
            screen.blit(handbook_footer[graphics % 2], (0, 600))
        keys=pygame.key.get_pressed()
        if(keys[pygame.K_ESCAPE]):
            game_mode='menu'
            refresh=pygame.Surface([600,700])
            refresh.fill(bg)
            screen.blit(refresh,[0,0])
            menu_options=4
            graphics=0
    ##### MENU SELECTION KEYLERİ KONULDU ######
    if game_mode=='menu':
        pygame.display.set_caption("Centipede")
        keys=pygame.key.get_pressed()
        if(keys[pygame.K_DOWN] and menu_options<5): #key down
            menu_options+=1

        if(keys[pygame.K_UP] and menu_options>1): #key up
            menu_options-=1

        screen.blit(menu_header[tickCounter%2],(0,0)) #logo hareketi
        screen.blit(menu_footer,(0,625))
        # menu seçenekleri
        if menu_options==1:
            screen.blit(menu_easy[1],(0,200))
        else:
            screen.blit(menu_easy[0],(0,200))

        if menu_options==2:
            screen.blit(menu_normal[1],(0,335))
        else:
            screen.blit(menu_normal[0],(0,335))

        if menu_options==3:
            screen.blit(menu_hard[1],(0,420))
        else:
            screen.blit(menu_hard[0],(0,420))

        if menu_options==4:
            screen.blit(menu_handbook[1],(0,490))
        else:
            screen.blit(menu_handbook[0],(0,490))

        if menu_options==5:
            screen.blit(menu_quit[1],(0,575))
        else:
            screen.blit(menu_quit[0],(0,575))

        if menu_options==6:
            screen.blit(menu_mute[1],(0,650))
        else:
            screen.blit(menu_mute[0],(0,650))

        if(keys[pygame.K_RETURN]):
            refresh=pygame.Surface([600,700])
            refresh.fill(bg)
            screen.blit(refresh,[0,0])
            if menu_options==1:
                game_mode='easyLevel'
            elif menu_options==2:
                game_mode='normalLevel'
            elif menu_options==3:
                game_mode='hardLevel'
            elif menu_options==4:
                game_mode='handbook'
            elif menu_options==5:
                running=False

    elif game_mode=='gameover':
        ##### GAME OVER OLUNCA ÇIKAN YAZILARIN EKRANDAKİ YERİ AYARLANDI ##########
        text = over_font.render("GAME OVER!", True, (255,255,255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y-200])

        text = start_font.render("Hit Enter to Easy Mode", True, (255,255,255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        screen.blit(text, [text_x, text_y+30])

        text = start_font.render("Hit [Q] to Normal Mode", True, (255,255,255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        screen.blit(text, [text_x, text_y+90])

        text = start_font.render("Hit [W] to Hard Mode", True, (255,255,255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        screen.blit(text, [text_x, text_y+140])

        text = start_font.render("Hit [ESC] for Menu", True, (255,255,255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        screen.blit(text, [text_x, text_y+200])
        ########### OYUN BİTTİKTEN SONRAKİ SEÇENEKLER KONULDU############
        keys=pygame.key.get_pressed() ##oyun bittikten sonra seçenekler
        if(keys[pygame.K_RETURN]):
            game_mode='easyLevel'
            player.lives = 3
            player.currentScore = 0
            refresh=pygame.Surface([600,700])
            refresh.fill(bg)
            screen.blit(refresh,[0,0])
            centipedes=pygame.sprite.Group() ###kaldığı yerden devam etmesin centi baştan gelsin diye
            for m in range(12):
                centipede=Centipede(20*m,-20)
                centipedes.add(centipede)
                setup_game_map()
                allsprites.add(centipedes)
            allsprites = pygame.sprite.Group()
            allsprites.add(player)
            allsprites.add(fireGroup)
            allsprites.add(spider)
            allsprites.add(centipedes)
            allsprites.add(boom)
            spider.deactivate()
            fire.deactivate()
        #enterla yapamadım farklı key girmem gerekti
        if(keys[pygame.K_w]): #w basınca hard level - bu kısım oyun bittikten sonra yeniden başlatma kısmı
            game_mode='hardLevel'
            player2.lives = 3
            player2.currentScore_hard = 0
            refresh=pygame.Surface([600,700])
            refresh.fill(bg)
            screen.blit(refresh,[0,0])
            centipedes_hard=pygame.sprite.Group()
            for m in range(12): #centi baştan gelsin diye
                centipede2=Centipede2(20*m,-20)
                centipedes_hard.add(centipede2)
                setup_game_map()
                allsprites_hard.add(centipedes_hard)
            allsprites_hard=pygame.sprite.Group()
            allsprites_hard.add(player2)
            allsprites_hard.add(fireGroup)
            allsprites_hard.add(flea2)
            allsprites_hard.add(spider2)
            allsprites_hard.add(centipedes_hard)
            allsprites_hard.add(boom)
            spider2.deactivate()
            flea2.deactivate()
            fire.deactivate()
        if (keys[pygame.K_q]):  # q ya basınca normal level - bu kısım oyun bittikten sonra yeniden başlatma kısmı
            game_mode = 'normalLevel'
            player.lives_normal = 3
            player.currentScore_normal = 0
            refresh = pygame.Surface([600, 700])
            refresh.fill(bg)
            screen.blit(refresh, [0, 0])
            centipedes = pygame.sprite.Group()
            for m in range(12): #centi baştan
                centipede = Centipede(20 * m, -20)
                centipedes.add(centipede)
                setup_game_map()
                allsprites_normal.add(centipedes)
            for m in range(1): #akrep kaldığı yerden devam ediyordu baştan gelmesi içim
                scorpion = Scorpion(20 * m, -20)
                scorpions.add(scorpion)
                setup_game_map()
                allsprites_normal.add(scorpions)
            allsprites_normal = pygame.sprite.Group()
            allsprites_normal.add(player)
            allsprites_normal.add(fireGroup)
            allsprites_normal.add(spider)
            allsprites_normal.add(scorpions)
            allsprites_normal.add(centipedes)
            allsprites_normal.add(boom)
            spider.deactivate()
            fire.deactivate()
        if(keys[pygame.K_ESCAPE]):
            game_mode='menu'
            refresh=pygame.Surface([600,700])
            refresh.fill(bg)
            screen.blit(refresh,[0,0])
            centipedes=pygame.sprite.Group()
            for m in range(12):
                centipede=Centipede(20*m,-20)
                centipedes.add(centipede)
                setup_game_map()
                allsprites.add(centipedes)
            allsprites=pygame.sprite.Group()
            allsprites.add(player)
            allsprites.add(fireGroup)
            allsprites.add(spider)
            allsprites.add(centipedes)
            allsprites.add(boom)
            spider.deactivate()
            fire.deactivate()
            menu_options=1


    ########### EASY LEVEL ##############
    if game_mode=='easyLevel':
        shoot_x=int(fire.x/20)
        shoot_y=int(fire.y/20)
        #Fire
        keys=pygame.key.get_pressed()
        if(keys[pygame.K_SPACE] and fire.canFire):
            fire.activate(player.rect.x+8,player.rect.y+6)
            pygame.mixer.music.load(os.path.join("sounds", "laser_sound.mp3"))  #laser sesi eklendi
            pygame.mixer.music.play(0)
        for c in centipedes:
            if c.left_right==1 and c.rect.x<580:
                if game_map[int(c.rect.y/20)][int(c.rect.x/20)+1]:
                    c.collide()
            else:
                if game_map[int(c.rect.y/20)][int(c.rect.x/20)-1]:
                    c.collide()

            if c.rect.x==fire.rect.x-8 and c.rect.y==fire.rect.y-6:
                c.kill()
                game_map[shoot_y-1][shoot_x]=1
                player.currentScore+=10 #centi puan
                fire.deactivate()

        if game_map[shoot_y-1][shoot_x]>0:
            game_map[shoot_y-1][shoot_x]=game_map[shoot_y-1][shoot_x]+1
            player.currentScore+=3 #mantar
            fire.deactivate()

        # örümcek aktif
        if spider.isActive==False:
            rnd=random.randint(0,500/level)
            if rnd==0:
                spider.activate()

        if pygame.sprite.spritecollide(spider, fireGroup, False): # örümcek vurulduğunda
            bang=Explosion(spider.rect.x, spider.rect.y) # patlama efekti
            allsprites.add(bang)
            boom.add(bang)
            spider.deactivate()
            fire.deactivate()
            player.currentScore+=50 #spider puan

        if pygame.sprite.spritecollide(player, centipedes, False):  # centi çarptığında
            bang=Explosion(player.rect.x, player.rect.y)
            allsprites.add(bang)
            boom.add(bang)
            pygame.mixer.music.load(os.path.join("sounds", "col_sound.mp3"))  #game over sound
            pygame.mixer.music.play(0)
            player.hide() # çarpınca player kayboluyor bi süreliğine player classa bakın
            player.lives -= 1 #can azalıyor
            if player.lives == 0:
                game_mode = 'gameover' #sıfırlanınca oyun bitiyor

        if pygame.sprite.collide_rect(player,spider):
            bang=Explosion(player.rect.x,player.rect.y)
            allsprites.add(bang)
            boom.add(bang)
            pygame.mixer.music.load(os.path.join("sounds", "col_sound.mp3")) #game over sound
            pygame.mixer.music.play(0)
            player.hide() #yukardaki gibi ama centi için
            player.lives -= 1
            if player.lives == 0:
                game_mode = 'gameover'

        if(tickCounter%1==0): #playerın hızı
                player.update(keys)
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_ESCAPE]):
            game_mode = 'menu'
            refresh = pygame.Surface([600, 700])
            refresh.fill(bg)
            screen.blit(refresh, [0, 0])
            menu_options = 4

        #score ekrana yazıldı
        pygame.display.set_caption("Easy Mode")
        score_label = label_font.render(f"Score: {str(player.currentScore)}", 1, (0, 255, 153))
        screen.fill((0, 0, 0), rect=score_label.get_rect(topleft=(10, 10)))
        screen.blit(score_label, (10, 10))
        #lives ekrana yazıldı
        lives_label = label_font.render(f"Lives: {str(player.lives)}", 1, (0, 255, 153))
        screen.fill((0, 0, 0), rect=lives_label.get_rect(topleft=(600 - lives_label.get_width() - 10, 10)))
        screen.blit(lives_label, (600 - lives_label.get_width() - 10, 10))
        # spritelar ekrana yazdırılıyor
        allsprites.clear(screen, background)
        fire.update()
        spider.update()
        centipedes.update()
        boom.update()
        draw_game_map()
        allsprites.draw(screen)
#######END OF THE EASY LEVEL-------------------
#######NORMAL LEVEL----------------------------
    if game_mode == 'normalLevel':
        shoot_x = int(fire.x / 20)
        shoot_y = int(fire.y / 20)
        # Fire
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] and fire.canFire):
            fire.activate(player.rect.x + 8, player.rect.y + 6)
            pygame.mixer.music.load(os.path.join("sounds", "laser_sound.mp3"))  # laser sesi eklendi
            pygame.mixer.music.play(0)
        for c in centipedes:
            if c.left_right == 1 and c.rect.x < 580:
                if game_map_normal[int(c.rect.y / 20)][int(c.rect.x / 20) + 1]:
                    c.collide()
            else:
                if game_map_normal[int(c.rect.y / 20)][int(c.rect.x / 20) - 1]:
                    c.collide()

            if c.rect.x == fire.rect.x - 8 and c.rect.y == fire.rect.y - 6:
                c.kill()
                game_map_normal[shoot_y - 1][shoot_x] = 1
                player.currentScore_normal += 10  # centi puan
                fire.deactivate()
        for s in scorpions:  ##scorpion part
            if s.left_right == 1 and s.rect.x < 580:
                if game_map_normal[int(s.rect.y / 20)][int(s.rect.x / 20) + 1]:
                    s.collide()
            else:
                if game_map_normal[int(s.rect.y / 20)][int(s.rect.x / 20) - 1]:
                    s.collide()

            if s.rect.x == fire.rect.x - 8 and s.rect.y == fire.rect.y - 6:
                s.kill()
                game_map_normal[shoot_y - 1][shoot_x] = 1
                player.currentScore_normal += 20  # scorpion puan
                fire.deactivate()

        if game_map_normal[shoot_y - 1][shoot_x] > 0:
            game_map_normal[shoot_y - 1][shoot_x] = game_map[shoot_y - 1][shoot_x] + 1
            player.currentScore_normal += 3  # mantar
            fire.deactivate()

            # örümcek aktif
        if spider.isActive == False:
            rnd = random.randint(0, 500 / level)
            if rnd == 0:
                spider.activate()

        if pygame.sprite.spritecollide(spider, fireGroup, False):  # örümcek vurulduğunda
            bang = Explosion(spider.rect.x, spider.rect.y)  # patlama efekti
            allsprites_normal.add(bang)
            boom.add(bang)
            spider.deactivate()
            fire.deactivate()
            player.currentScore_normal += 50  # spider puan

        if pygame.sprite.spritecollide(player, centipedes, False):  # centi çarptığında
            bang = Explosion(player.rect.x, player.rect.y)
            allsprites_normal.add(bang)
            boom.add(bang)
            pygame.mixer.music.load(os.path.join("sounds", "col_sound.mp3"))  # game over sound
            pygame.mixer.music.play(0)
            player.hide()  # çarpınca player kayboluyor bi süreliğine player classa bakın
            player.lives_normal -= 1  # can azalıyor
            if player.lives_normal == 0:
                game_mode = 'gameover'  # sıfırlanınca oyun bitiyor

        if pygame.sprite.spritecollide(player, scorpions, False):  # akrep çarptığında
            bang = Explosion(player.rect.x, player.rect.y)
            allsprites_normal.add(bang)
            boom.add(bang)
            pygame.mixer.music.load(os.path.join("sounds", "col_sound.mp3"))  # game over sound
            pygame.mixer.music.play(0)
            player.hide()  # çarpınca player kayboluyor bi süreliğine player classa bakın
            player.lives_normal -= 1  # can azalıyor
            if player.lives_normal == 0:
                game_mode = 'gameover'  # sıfırlanınca oyun bitiyor

        if pygame.sprite.collide_rect(player, spider):
            bang = Explosion(player.rect.x, player.rect.y)
            allsprites_normal.add(bang)
            boom.add(bang)
            pygame.mixer.music.load(os.path.join("sounds", "col_sound.mp3"))  # game over sound
            pygame.mixer.music.play(0)
            player.hide()  # yukardaki gibi ama centi için
            player.lives_normal -= 1
            if player.lives_normal == 0:
                game_mode = 'gameover'

        if (tickCounter % 1 == 0):  # playerın hızı
            player.update(keys)

        if(tickCounter%6==0): #scorpion hızı
                scorpions.update()

        keys = pygame.key.get_pressed()

        if (keys[pygame.K_ESCAPE]): #esc ile menüye dönüş
            game_mode = 'menu'
            refresh = pygame.Surface([600, 700])
            refresh.fill(bg)
            screen.blit(refresh, [0, 0])
            menu_options = 3

        # score ekrana yazıldı
        pygame.display.set_caption("Normal Mode")
        score_label_norm = label_font.render(f"Score: {str(player.currentScore_normal)}", 1, (0, 255, 153))
        screen.fill((0, 0, 0), rect=score_label_norm.get_rect(topleft=(10, 10)))
        screen.blit(score_label_norm, (10, 10))
        # lives ekrana yazıldı
        lives_label_norm = label_font.render(f"Lives: {str(player.lives_normal)}", 1, (0, 255, 153))
        screen.fill((0, 0, 0), rect=lives_label_norm.get_rect(topleft=(600 - lives_label_norm.get_width() - 10, 10)))
        screen.blit(lives_label_norm, (600 - lives_label_norm.get_width() - 10, 10))
        # spritelar ekrana yazdırılıyor
        allsprites_normal.clear(screen, background)
        fire.update()
        spider.update()
        centipedes.update()
        scorpions.update()
        boom.update()
        draw_game_map()
        allsprites_normal.draw(screen)
    #####################END OF THE NORMAL LEVEL----------

        ###PAUSE
    if game_mode == 'easyLevel':
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_p]):
            game_mode = 'easyLevel'
            pause = True
            paused()

    if game_mode == 'normalLevel':
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_p]):
            game_mode = 'normalLevel'
            pause = True
            paused()

    if game_mode == 'hardLevel':
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_p]):
            game_mode = 'hardLevel'
            pause = True
            paused()

         ##MUTE
    if game_mode == 'menu'or game_mode =='easyLevel' or \
            game_mode=='hardLevel' or game_mode=='handbook' or game_mode=='normalLevel':
         keys = pygame.key.get_pressed()
         if (keys[pygame.K_m]):
             mute = True
             muted()

         ##UNMUTE
    if game_mode == 'menu'or game_mode =='easyLevel' or \
            game_mode=='hardLevel' or game_mode=='handbook' or game_mode=='normalLevel':
         keys = pygame.key.get_pressed()
         if (keys[pygame.K_n]):
             mute = False
             unmuted()

        ######################## HARD LEVEL######################
    if game_mode=='hardLevel':
        shoot_x=int(fire.x/20)
        shoot_y=int(fire.y/20)
        #Fire
        keys=pygame.key.get_pressed()
        if(keys[pygame.K_SPACE] and fire.canFire):
            fire.activate(player2.rect.x+8,player2.rect.y+6)
            pygame.mixer.music.load(os.path.join("sounds", "laser_sound.mp3"))  #laser sesi eklendi
            pygame.mixer.music.play(0)
        for c in centipedes_hard:
            if c.left_right==1 and c.rect.x<580:
                if game_map_hard[int(c.rect.y/20)][int(c.rect.x/20)+1]:
                    c.collide()
            else:
                if game_map_hard[int(c.rect.y/20)][int(c.rect.x/20)-1]:
                    c.collide()

            if c.rect.x==fire.rect.x-8 and c.rect.y==fire.rect.y-6:
                c.kill()
                game_map_hard[shoot_y-1][shoot_x]=1
                player2.currentScore_hard+=10 #centi vücudu
                fire.deactivate()

        if game_map_hard[shoot_y-1][shoot_x]>0:
            game_map_hard[shoot_y-1][shoot_x]=game_map_hard[shoot_y-1][shoot_x]+1
            player2.currentScore_hard+=3 #mantarın puanı 3
            fire.deactivate( )

        if spider2.isActive==False:
            rnd=random.randint(0,500/level2)
            if rnd==0:
                spider2.activate()

        if pygame.sprite.spritecollide(spider2,fireGroup,False):
            bang=Explosion(spider2.rect.x,spider2.rect.y)
            allsprites_hard.add(bang)
            boom.add(bang)
            spider2.deactivate()
            fire.deactivate()
            player2.currentScore_hard+=50 #spider puanı

        if flea2.isActive==False: #flea aktif
            rnd=random.randint(0,10/level2)
            if rnd==0:
                flea2.activate()
        else:
            if(flea2.drop):
                rnd=random.randint(1,5)

                if(rnd==1 and flea2.ay>0 and flea2.isActive):
                    game_map_hard[int(flea2.ay/20)+1][int(flea2.ax/20)]=1
                    flea2.drop=0
        for s in scorpions_hard:  ##scorpion part
            if s.left_right == 1 and s.rect.x < 580:
                if game_map_hard[int(s.rect.y / 20)][int(s.rect.x / 20) + 1]:
                    s.collide()
            else:
                if game_map_hard[int(s.rect.y / 20)][int(s.rect.x / 20) - 1]:
                    s.collide()

            if s.rect.x == fire.rect.x - 8 and s.rect.y == fire.rect.y - 6:
                s.kill()
                game_map_hard[shoot_y - 1][shoot_x] = 1
                player2.currentScore_hard += 20  # scorpion puan
                fire.deactivate()

        if pygame.sprite.spritecollide(flea2,fireGroup,False):# flea kısmı
            bang=Explosion(flea2.rect.x,flea2.rect.y) # patlama kısmı
            allsprites_hard.add(bang)
            boom.add(bang)
            flea2.deactivate()
            fire.deactivate()
            player2.currentScore_hard+=30 #pirenin puanı

        if pygame.sprite.spritecollide(player2, scorpions_hard, False):  # akrep çarptığında
            bang = Explosion(player2.rect.x, player2.rect.y)
            allsprites_hard.add(bang)
            boom.add(bang)
            pygame.mixer.music.load(os.path.join("sounds", "col_sound.mp3"))  # game over sound
            pygame.mixer.music.play(0)
            player2.hide()  # çarpınca player kayboluyor bi süreliğine player classa bakın
            player2.lives -= 1  # can azalıyor
            if player2.lives == 0:
                game_mode = 'gameover'  # sıfırlanınca oyun bitiyor

        if pygame.sprite.spritecollide(player2,centipedes_hard,False):
            bang=Explosion(player2.rect.x,player2.rect.y)
            allsprites_hard.add(bang)
            boom.add(bang)
            pygame.mixer.music.load(os.path.join("sounds", "col_sound.mp3"))  #game over sound
            pygame.mixer.music.play(0)
            player2.hide()
            player2.lives -= 1
            if player2.lives == 0:
                game_mode = 'gameover'

        if pygame.sprite.collide_rect(player2,spider2):
            bang=Explosion(player2.rect.x,player2.rect.y)
            allsprites_hard.add(bang)
            boom.add(bang)
            pygame.mixer.music.load(os.path.join("sounds", "col_sound.mp3")) #game over sound
            pygame.mixer.music.play(0)
            player2.hide()
            player2.lives -= 1
            if player2.lives == 0:
                game_mode = 'gameover'

        if pygame.sprite.collide_rect(player2,flea2): # fleaya çarpılırsa
            bang=Explosion(player2.rect.x,player2.rect.y)
            allsprites_hard.add(bang)
            boom.add(bang)
            pygame.mixer.music.load(os.path.join("sounds", "col_sound.mp3"))  #game over sound
            pygame.mixer.music.play(0)
            player2.hide()
            player2.lives -= 1
            if player2.lives == 0:
                game_mode = 'gameover'
        if(tickCounter%3==0): #hard level için oyuncu hızını yavaşlattım
                player2.update(keys)
        if(tickCounter%3==0):
                scorpions_hard.update()

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_ESCAPE]):
            game_mode = 'menu'
            refresh = pygame.Surface([600, 700])
            refresh.fill(bg)
            screen.blit(refresh, [0, 0])
            menu_options = 4
        #score ve live sayısının ekrana yazılması için easydeki aynı kodları ekledim
        pygame.display.set_caption("Hard Mode")
        score_label1= label_font.render(f"Score: {str(player2.currentScore_hard)}", 1, (255, 102, 153))
        screen.fill((0, 0, 0), rect=score_label1.get_rect(topleft=(10, 10)))
        screen.blit(score_label1, (10, 10))

        lvl2_lives_label = label_font.render(f"Lives: {str(player2.lives)}", 1, (255, 102, 153))
        screen.fill((0, 0, 0), rect=lvl2_lives_label.get_rect(topleft=(600 - lvl2_lives_label.get_width() - 10, 10)))
        screen.blit(lvl2_lives_label, (600 - lvl2_lives_label.get_width() - 10, 10))
        #tüm spritelar yazdırıldı
        allsprites_hard.clear(screen, background)
        fire.update()
        spider2.update()
        flea2.update()
        scorpions_hard.update()
        centipedes_hard.update()
        boom.update()
        draw_hard_map()
        allsprites_hard.draw(screen)
    pygame.display.flip()
pygame.quit()
