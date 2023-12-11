# r[0] = {sucess/danger}

r = []
rSafe = ["success", "INCÊNDIO NÃO DETECTADO"]
rNoSafe = ["danger", "INCÊNDIO DETECTADO!"]

safe = False

if safe:
    r = rSafe
else:
    r = rNoSafe

fResult = ["nivel1", "detectada"]
tResult = ["nivel3", "48°C"]
uResult = ["nivel2", "15% (baixa)"]