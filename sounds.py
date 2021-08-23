import pygame.mixer
import threading

def play():
    pygame.mixer.init()
    pygame.mixer.music.load('./assets/sounds/lever.wav')
    pygame.mixer.music.play(loops=0)

def button():
    lolipop = threading.Thread(target=play)
    lolipop.start()