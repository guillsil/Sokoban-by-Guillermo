import gamelib
from soko import *
from pila import Pila
ACCIONES = [OESTE, NORTE, SUR, ESTE]

def juego_mostrar(grilla):
    """En la función juego_mostrar tenemos que utilizar las funciones de Gamelib para dibujar el tablero
    ¡No es necesario dibujar nada muy sofisticado! Debería ser suficiente con usar las funciones
    draw_text y draw_rectangle/draw_line y gamelib.draw_image."""
    tamanio = dimencion_grilla(grilla)
    for i in range(tamanio[COL]):
        for j in range(tamanio[FIL]):
            if hay_pared(grilla, i, j):
                gamelib.draw_image("img/ground.gif", TAMANIO_CELDA * i, TAMANIO_CELDA* j)
                gamelib.draw_image("img/wall.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
            elif hay_caja(grilla, i, j):
                gamelib.draw_image("img/ground.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
                gamelib.draw_image("img/box.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
            elif hay_objetivo(grilla, i, j):
                gamelib.draw_image("img/ground.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
                gamelib.draw_image("img/goal.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
                if hay_jugador(grilla, i, j):
                    gamelib.draw_image("img/player.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
            elif hay_jugador(grilla, i, j):
                gamelib.draw_image("img/ground.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
                gamelib.draw_image("img/player.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)
            else:
                gamelib.draw_image("img/ground.gif",TAMANIO_CELDA*i,TAMANIO_CELDA*j)

def hallar_max_columnas(desc):
    """Devuelve el largo del string más largo, si el string no tiene una Pared, Caja, Jugador
    o Objetivo, se ignora y se sigue buscando"""
    max_col = 0
    for i in range(len(desc)):
        if desc[i] != "":
            if desc[i][0] in OBJETOS_DEL_JUEGO:
                if len(desc[i]) > max_col:
                    max_col = len(desc[i])
    return max_col

def completar_grilla(desc):
    """Devuelve una lista de string complentando los espacios en blanco del final de cada
     string, teniendo en cuenta la cantidad de columnas maxima, también saca el nombre del nivel si lo continene y
     lo devuelve como string"""
    nombre = ""
    max_col = hallar_max_columnas(desc)
    for i in range(len(desc)):
        while len(desc[i]) < max_col:
            desc[i] += " "
    return desc
def obtener_nivel(archivo_nivel):
    """Lee el archivo de niveles y devuelve una lista con los niveles donde cada nivel es una lista de strings"""
    try:
        niveles = []
        with open(archivo_nivel) as archivo:
            desc = []
            for linea in archivo:
                if linea == "\n":
                    niveles.append(completar_grilla(desc))
                    desc = []
                else:
                    if  not linea.startswith("Level ") and not linea.startswith("'"):
                        desc.append(linea.rstrip())
            niveles.append(completar_grilla(desc))
        return niveles
    except FileNotFoundError:
        raise FileNotFoundError("El archivo de niveles no existe")

def convertir_inmutable(grilla):
    """Recibe una grilla y devuelve una tupla con las tuplas de cada fila"""
    grilla_inmutable = []
    for fila in grilla:
        grilla_inmutable.append(tuple(fila))
    return tuple(grilla_inmutable)
def buscar_solucion(estado_inicial):
    """Busca una solucion al nivel utilizando backtracking, si encuentra una solucion devuelve un conjunto de acciones
    que resuelven el nivel, de lo contrario devuelve None"""
    visitados = set()
    return backtrack(estado_inicial, visitados)
def backtrack(estado, visitados):
    """Algoritmo de backtracking para resolver el nivel"""
    visitados.add(convertir_inmutable(estado))
    if juego_ganado(estado):
        return True, Pila()
    for accion in ACCIONES:
        nuevo_estado = mover(estado, accion)
        if convertir_inmutable(nuevo_estado) in visitados:
            continue
        solucion_encontrada, acciones = backtrack(nuevo_estado, visitados)
        if solucion_encontrada:
            acciones.apilar(accion)
            return True,  acciones
    return False, None
def ejecutar_movimiento(juego, accion):
    """Ejecuta el Movimiento presionado por la tecla y apila, desapila los estados para poder deshacer y rehacer"""
    juego["anteriores"].apilar(juego["grilla"])
    juego["grilla"] = mover(juego["grilla"], accion)
    juego["siguientes"] = Pila()
    juego["movimientos_solucion"] = Pila()

def actualizar_pilas_nivel(juego, nivel):
    """Actualiza las pilas de estados del juego"""
    juego["siguientes"] = Pila()
    juego["anteriores"] = Pila()
    juego["movimientos_solucion"] = Pila()
    juego["grilla"] = crear_grilla(juego["niveles"][nivel])

def actualizar_estado(juego):
    """Actualiza el estado del juego, según la `tecla` presionada.
    Devuelve el nuevo estado del juego.
    """
    if juego["tecla"] in juego["teclas_validas"]:
        if juego["teclas_validas"][juego["tecla"]]  == "OESTE":
            ejecutar_movimiento(juego, ACCIONES[0])
        elif juego["teclas_validas"][juego["tecla"]] == "ESTE":
            ejecutar_movimiento(juego, ACCIONES[3])
        elif juego["teclas_validas"][juego["tecla"]] == "NORTE":
            ejecutar_movimiento(juego, ACCIONES[1])
        elif juego["teclas_validas"][juego["tecla"]] == "SUR":
            ejecutar_movimiento(juego, ACCIONES[2])
        elif juego["teclas_validas"][juego["tecla"]] == "REINICIAR":
            actualizar_pilas_nivel(juego, juego["nivel"])
        elif juego["teclas_validas"][juego["tecla"]] == "NEXT_LEVEL":
            if juego["nivel"] < len(juego["niveles"]) - 1:
                juego["nivel"] += 1
                actualizar_pilas_nivel(juego, juego["nivel"])
        elif juego["teclas_validas"][juego["tecla"]] == "PREV_LEVEL":
            if juego["nivel"] > 0:
                juego["nivel"] -= 1
                actualizar_pilas_nivel(juego, juego["nivel"])
        elif juego["teclas_validas"][juego["tecla"]] == "DESHACER":
            if not juego["anteriores"].esta_vacia():
                juego["siguientes"].apilar(juego["grilla"])
                juego["grilla"] = juego["anteriores"].desapilar()
        elif juego["teclas_validas"][juego["tecla"]] == "REHACER":
            if not juego["siguientes"].esta_vacia():
                juego["anteriores"].apilar(juego["grilla"])
                juego["grilla"] = juego["siguientes"].desapilar()
        elif juego["teclas_validas"][juego["tecla"]] == "PISTA":
            if not juego["movimientos_solucion"].esta_vacia():
                juego["anteriores"].apilar(juego["grilla"])
                juego["grilla"] = mover(juego["grilla"], juego["movimientos_solucion"].desapilar())
            else:
                juego["movimientos_solucion"] = buscar_solucion(juego["grilla"])[1]

def cargar_teclas(archivo):
    """Recibe un archivo de teclas donde cada linea tiene la siguiente forma <Tecla> = <Accion>, se debera delvolver un
    diccionario con la TECLA como clave y la ACCION como valor"""
    try:
        teclas = {}
        with open(archivo) as archivo:
            for linea in archivo:
                linea = linea.strip().split(" = ")
                if linea[0] == "":
                    continue
                teclas[linea[0]] = linea[1]
        return teclas
    except FileNotFoundError:
        raise FileNotFoundError("El archivo de teclas no existe")

def main():
    # Inicializar el estado del juego
    control_juego = {}
    control_juego["niveles"] = obtener_nivel("niveles.txt")
    control_juego["teclas_validas"] = cargar_teclas("teclas.txt")
    control_juego["siguientes"] = Pila()
    control_juego["anteriores"] = Pila()
    control_juego["movimientos_solucion"] = Pila()
    control_juego["nivel"] = 0
    control_juego["grilla"] = crear_grilla(control_juego["niveles"][control_juego["nivel"]])

    while gamelib.is_alive():

        tamanio = dimencion_grilla(control_juego["grilla"])
        gamelib.resize(tamanio[COL] * TAMANIO_CELDA, tamanio[FIL] * TAMANIO_CELDA)

        gamelib.draw_begin()
        # Dibujar la pantalla
        juego_mostrar(control_juego["grilla"])
        gamelib.draw_end()

        gamelib.title("Sokoban++ - Nivel {}".format(control_juego["nivel"] + 1))

        ev = gamelib.wait(gamelib.EventType.KeyPress)
        if not ev:
            break
        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break
        # Actualizar el estado del juego, según la `tecla` presionada
        tecla = ev.key
        control_juego["tecla"] = tecla
        actualizar_estado(control_juego)

        # Verificar si el jugador ganó o perdió
        if juego_ganado(control_juego["grilla"]):
            control_juego["nivel"] += 1
            actualizar_pilas_nivel(control_juego, control_juego["nivel"])

        if control_juego["nivel"] > len(control_juego["niveles"]) - 1:
            gamelib.say("GANASTE")
            break
gamelib.init(main)