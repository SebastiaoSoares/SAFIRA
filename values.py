# r[0] = {sucess/danger}

r = []
rSafe = ["success", "INCÊNDIO NÃO DETECTADO"]
rNoSafe = ["danger", "INCÊNDIO DETECTADO!"]

safe = True

if safe:
    r = rSafe
else:
    r = rNoSafe

fResult = ["nivel1", "não detectada"]
tResult = ["nivel3", "48°C"]
uResult = ["nivel2", "15% (baixa)"]