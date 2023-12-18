# r[0] = {sucess/danger}

r = []
rSafe = ["success", "INCÊNDIO NÃO DETECTADO", "green", "não detectada"]
rNoSafe = ["danger", "INCÊNDIO DETECTADO!", "red","detectada"]

safe = True

if safe:
    r = rSafe
else:
    r = rNoSafe
