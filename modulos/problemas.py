def calc_problemas(problema, problemas):
    from modulos.ost import OST
    import pygame
    pygame.mixer.init()
    if problema > problemas:
        if problema == 1:
            pygame.mixer.music.load(OST["primeiro_panico"])
            pygame.mixer.music.play(loops=-1)
        elif problema == 2:
            pygame.mixer.music.load(OST["segundo_panico"])
            pygame.mixer.music.play(loops=-1)
        problemas += problema
    return problemas
