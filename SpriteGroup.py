###############
from Player import *
from Player2 import *
from Fire import *
from Spider import *
from Spider2 import *
from Flea2 import *
from Centipede import *
from Centipede2 import *
from Scorpion import *

###TÜM SPRITELAR YARATILDI###
player = Player(300, 650)  # playerın ekrandaki yeri
player2 = Player2(300, 650)
fire = Fire()
flea2 = Flea2()
fireGroup = pygame.sprite.Group()
fireGroup.add(fire)

allsprites = pygame.sprite.Group()
allsprites.add(player)
allsprites.add(fireGroup)

allsprites_hard = pygame.sprite.Group()
allsprites_hard.add(player2)
allsprites_hard.add(fireGroup)
allsprites_hard.add(flea2)

allsprites_normal = pygame.sprite.Group()
allsprites_normal.add(player)
allsprites_normal.add(fireGroup)

boom = pygame.sprite.Group()

scorpions = pygame.sprite.Group()
for m in range(1):
    scorpion = Scorpion(20 * m, -20)
    scorpions.add(scorpion)
#hard level için tekrar akrep yarattım çünkü leveller arası geçiş yapıldığında akrep olduğu yerden devam ediyordu
scorpions_hard = pygame.sprite.Group()
for m in range(1):
    scorpion_ = Scorpion(20 * m, -20)
    scorpions_hard.add(scorpion_)

centipedes = pygame.sprite.Group() #easy
for m in range(12): # centinin uzunluğu 12
    centipede = Centipede(20*m, -20)
    centipedes.add(centipede)

centipedes_hard = pygame.sprite.Group() #hard
for m in range(12):
    centipede2 = Centipede2(20 * m, -20)
    centipedes_hard.add(centipede2)


spider = Spider()
spider2 = Spider2()
allsprites.add(spider)
allsprites.add(centipedes)
allsprites.add(boom)

allsprites_normal.add(spider)
allsprites_normal.add(scorpions)
allsprites_normal.add(boom)
allsprites_normal.add(centipedes)

allsprites_hard.add(spider2)
allsprites_hard.add(centipedes_hard)
allsprites_hard.add(boom)
allsprites_hard.add(scorpions_hard)
