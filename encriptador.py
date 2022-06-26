# clave de encriptacion en json
clave_de_encriptacion = {
        'a': '?',
        'b': '-',
        'c': '~',
        'd': 'Ŋ',
        'e': '{',
        'f': '*',
        'g': '_',
        'h': '%',
        'i': 'j',
        'j': 'k',
        'k': ')',
        'l': 'm',
        'm': 'n',
        'n': '9',
        'o': 'p',
        'p': 'q',
        'q': '1',
        'r': 's',
        's': 't',
        't': 'u',
        'u': 'v',
        'v': 'w',
        'w': 'x',
        'x': 'y',
        'y': 'z',
        'z': 'a',

        '1': '!',
        '2': ']',
        '3': '&',
        '4': '$',
        '5': '#',
        '6': '^',
        '7': '@',
        '8': 'ñ',
        '9': '+',
        '0': ':'

    }

clave_inversa_de_encriptacion = {}
for key, value in clave_de_encriptacion.items():
    clave_inversa_de_encriptacion[value] = key

def encriptador(palabra):
    nueva_palabra = ''
    for letra in palabra:
        nueva_palabra += clave_de_encriptacion[letra]

    return nueva_palabra

def desencriptar(palabra):
    palabra_desencriptada = ''
    for letra in palabra:
        palabra_desencriptada += clave_inversa_de_encriptacion[letra]

    return palabra_desencriptada

if __name__ == '__main__':
    # Script2.py executed as script
    # do something
    clave = encriptador('maritimo')

    print(clave)
    print(desencriptar(clave))
    
    print(desencriptar("n?sjujnp"))
