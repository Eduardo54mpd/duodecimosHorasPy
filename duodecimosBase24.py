from datetime import datetime

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
elif 7 <= horas <= 18:
    horaConvert = horas - 6
else:
    horaConvert = horas - 18

def ciclo (hora):
    if 7 <= horas <= 18:
        return f"{hora} (diurna)"
    else:
        return f"{hora} noturna"

hora = ciclo(horasDict[horaConvert])

if duodecimos < 2:
    if duodecimos == 0:
        print(f"É a hora {hora}")
    else:
        print(f"É 1 duodécimo da hora {hora}")
else:
    print(f"São {duodecimos} duodécimos da hora {hora}")