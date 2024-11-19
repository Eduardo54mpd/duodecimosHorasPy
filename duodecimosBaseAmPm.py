from datetime import datetime

agora = datetime.now()

horas = int(agora.strftime("%I")) # Horas de 1 a 12
minutos = int(agora.strftime("%M"))
ampm = agora.strftime("%p") # Ciclo AM/PM

horaConvert = 0
duodecimos = minutos // 5

if horas < 7:
    horaConvert = horas + 6
else:
    horaConvert = horas - 6

horasDict = {
    1: 'primeira', 2: 'segunda', 3: 'terceira',
    4: 'quarta', 5: 'quinta', 6: 'sexta',
    7: 'sétima', 8: 'oitava', 9: 'nona',
    10: 'décima', 11: 'undécima', 12: 'duodécima'
}

def ciclo(hora):
    if (
        (7 <= horas <= 11) and (ampm == "AM") or # Valor de horas entre 7 AM e 11 AM
        (horas == 12 and ampm == "PM") or # 12 PM (uma vez que 12 AM seria à meia-noite)
        (1 <= horas <= 5 and ampm == "PM") # Valor de horas entre 1 PM e 5 PM
        ):
        return f'{hora} (diurna)'
    else:
        return f'{hora} noturna'

hora = ciclo(horasDict[horaConvert])

if duodecimos < 2:
    if duodecimos == 0:
        print(f"É a hora {hora}")
    else:
        print(f"É 1 duodécimo da hora {hora}")
else:
    print(f"São {duodecimos} duodécimos da hora {hora}")