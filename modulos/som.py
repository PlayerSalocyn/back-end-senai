########################################
                #SOM
########################################
import pygame
pygame.mixer.init()
sons = {
"notificação_1" : pygame.mixer.Sound('Sound/notificação1.mp3'),
"notificação_2" : pygame.mixer.Sound('Sound/notificação2.mp3'),
"notificação_3" : pygame.mixer.Sound('Sound/notificação3.mp3'),
"Aviso" : pygame.mixer.Sound('Sound/Aviso_perigo.mp3'),
"Alarme1" : pygame.mixer.Sound('Sound/Alarme1.mp3'),
"Alarme2": pygame.mixer.Sound('Sound/Alarme2.mp3'),
"Alarme3" : pygame.mixer.Sound('Sound/Alarme3.mp3'),
"Alarme_Final" : pygame.mixer.Sound('Sound/Alarme_final.mp3'),
"Erro" : pygame.mixer.Sound('Sound/Erro.mp3'),
"Grande_erro" : pygame.mixer.Sound('Sound/Grande_erro.mp3')
}