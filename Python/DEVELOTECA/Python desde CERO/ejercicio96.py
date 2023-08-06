# Modulo json para convertir datos

import json # notacion de objetos de llaves script (servicios api, etc)

datos='{"nombre":"Oscar", "Edad":38, "Ciudad":"Mexico"}'

lecturaDatos = json.loads(datos)

print(lecturaDatos["edad"])





