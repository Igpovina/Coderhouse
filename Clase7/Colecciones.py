"""
Transforma el texto en:

Gordon lanzó su curva...
- Strawberry ha fallado por un pie! -gritó Joe Castiglione.
- Dos pies le corrigió Troop.
- Strawberry menea la cabeza como disgustado… -agrega el comentarista.

Lo único prohibido es modificar directamente el texto
"""


cadena:str = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"
texto:list = cadena.split("&")
for i,j in enumerate(texto):
    texto[i] = j.capitalize()
    if (i==0):
        texto[i] = j.capitalize() + "..."
    else:
        texto[i] = "- " + texto[i] + "."
cadena = "\n".join(texto)
print(cadena)