import pygame
from pygame import *
from datetime import datetime

pygame.init() # Inicializador

larg = 624
altr = 112

tela = pygame.display.set_mode((larg, altr))
tempo = pygame.time.Clock()
executa = True
fonte = pygame.font.SysFont("vivaldi", 30, False, False)

pygame.display.set_caption("São quantos duodécimos de qual hora??")

def geraDuodecimos():
    agora = datetime.now()
    horas = int(agora.strftime("%H"))
    minutos = int(agora.strftime("%M"))

    duodecimos = minutos // 5

    horasDict = {
        1: "primeira", 2: "segunda", 3: "terceira",
        4: "quarta", 5: "quinta", 6: "sexta",
        7: "sétima", 8: "oitava", 9: "nona",
        10: "décima", 11: "undécima", 12: "duodécima"
    }

    horaConvert = 0

    if horas <= 6:
        horaConvert = horas + 6
    elif horas >= 7 and horas <= 18:
        horaConvert = horas - 6
    else:
        horaConvert = horas - 18

    def ciclo(hora):
        if horas >= 7 and horas <= 18:
            return f"{hora} (diurna)"
        else:
            return f"{hora} noturna"

    hora = ciclo(horasDict[horaConvert])

    if duodecimos < 2:
        if duodecimos == 0:
            return f"É a hora {hora}"
        else:
            return f"É 1 duodécimo da hora {hora}"
    else:
        return f"São {duodecimos} duodécimos da hora {hora}"
    

while executa:
    tempo.tick(1000)
    tela.fill((12, 12, 12))
    mensagem = geraDuodecimos()
    textFormat = fonte.render(mensagem, True, (244, 244, 244))
    centro = textFormat.get_rect(center=(larg // 2, altr // 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executa = False

    tela.blit(textFormat, (centro))
    pygame.display.update()

pygame.quit()