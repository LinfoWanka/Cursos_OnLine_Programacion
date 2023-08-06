# Modulo json de JSON a String

import json

datosJSON={"nombre":"Oscar", "Edad":38, "Ciudad":"Mexico"}

datosJSONString=json.dumps(datosJSON)
print(datosJSONString)

