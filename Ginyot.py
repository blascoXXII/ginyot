import random

#Dictionario con las puntuaciones de cada carta

puntuaciones={}
puntuaciones[1]=12
puntuaciones[2]=0
puntuaciones[3]=10
puntuaciones[4]=0
puntuaciones[5]=0
puntuaciones[6]=0
puntuaciones[7]=0
puntuaciones[10]=3
puntuaciones[11]=2
puntuaciones[12]=4


def creardiccionario(jugadores):
    
    """
    Description: Esta funcion crea un diccionario con la información de cada jugador
    
    Argumentos: jugadores - Lista de strings con el nombre de los jugadores (generalmente 2 o 4)
    
    Output: Diccionario con el nombre de los jugadores como clave y una lista como valor. Los elementos de
            la lista seran una lista de tuplas (string, int) (que representa la mano (cartas que dispone el
            jugador)), un int que representa los puntos acumulados, un int que representa el número de turno,
            un string que indica el equipo (el 1r y 3r jugador seran un equipo y el 2n y 4o otro)
    
    """
    
    d={}
    
    i=1
    
    for jugador in jugadores:
        d[jugador]=[[],0,i,i%2]
        i+=1
        
    return d

def crearbaraja(palos=["oros","bastos","copas","espadas"]):
    
    """
    Description: Esta funcion crea una nueva baraja con los palos especipicados
    
    Argumentos: palos - Lista de string con los palos de la baraja (habitualmente oros, bastos, copas y espadas)
    
    Output: baraja - Lista de tuplas (string, int) con la nueva baraja de cartas.
    """
    
    baraja = []
    
    for i in palos:
        
        for num in range(1,13):
            
            if num != 0 or num!= 8 or num!=9:
                baraja.append((i,num))
        
    ultima=baraja.pop(random.randint(0,len(baraja)-1))
    baraja.append(ultima)
    return baraja


def repartircarta(baraja):
    """
    Description: Esta funcion escoje una carta aleatoria de la baraja especificada.
    
    Argumentos: baraja - Lista de tuplas (strin, int) con la baraja de cartas de la partida.
    
    Output: baraja - Lista de tuplas (string, int) con la baraja de cartas restantes
            carta - Tupla (string, int) correspondiente a la carta repartida
    """
    
    if len(baraja) == 0:
        return ""
    
    carta = baraja.pop(random.randint(0,len(baraja)-2))
    
    return (baraja, carta)


def primerreparto(d, baraja):
    """
    Description: Esta funcio reparte las manos iniciales a todos los jugadores
    
    Argumentos: d - Diccionario con la información de todos los jugadores
                baraja, Lista de tuplas (string, int) con la baraja de cartas de la partida.
                
    Output: d - Diccionario con la información de los jugadores actualizada
            baraja - Lista de tuplas (string, int) con las cartas restantes
    """
    
    for i in range(6):
        for jugador in d:
            baraja, carta = repartircarta(baraja)
            d[jugador][0].append(carta)
            
    return (d, baraja)
            

def tirarcarta(mano):
    """
    Description: Esta funcion escoge la carta a jugar dada una mano
    
    Argumentos: mano - Lista de tuplas (string, int) con la mano de un jugador (conjunto de cartas de las que
                        dispone)
    Output: mano - Lista de tuplas (string, int) con la mano actualizada
            carta - Tupla (string, int) con la carta a jugar
    """
    
    carta = mano.pop(random.randint(0,len(mano)-1))
    
    print ("Se juega la carta", carta)

    return (mano, carta)


def tirada(d):
    """
    Description: Esta funcion genera la tirada de todos los jugadores
    
    Argumentos: d - Diccionario con la información de todos los jugadores
    
    Output: d- Diccionario con la información de todos los jugadores actualizada
            tirada - Diccionario con el nombre de jugador como clave y la tupla (string, int) como valor
    """
    
    tirada={}
    
    for jugador in d:
        d[jugador][0], tirada[jugador] = tirarcarta(d[jugador][0])
        
     
    return (d, tirada)


    
def test():
    
    d= creardiccionario(["a","b","c","d"])
    baraja = crearbaraja()
    d, baraja = primerreparto(d, baraja)
    
    d,mesa = tirada(d)
    
    return mesa