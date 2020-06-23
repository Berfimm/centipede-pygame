import pygame

muted = False
def muted():
    muted = False
    if muted:
        muted = False
        pass
    else:
        pygame.mixer.music.set_volume(0)
        muted = True


unmuted = False
def unmuted():
    unmuted = False
    if unmuted:
        unmuted = False
        pass
    else:
        pygame.mixer.music.set_volume(80)
        unmuted = True

