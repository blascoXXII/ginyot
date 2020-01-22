import random
import operator

#Dictionario con las puntuaciones de cada carta

puntuaciones={}
puntuaciones[1]=11
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
            
            if num!= 8 and num!=9:
                baraja.append((i,num))
        
    ultima=baraja.pop(random.randint(0,len(baraja)-1))
    baraja.append(ultima)
    
    print("Vamos de: ",ultima[0])
    
    return baraja, ultima[0]


def repartircarta(baraja):
    """
    Description: Esta funcion escoje una carta aleatoria de la baraja especificada.
    
    Argumentos: baraja - Lista de tuplas (strin, int) con la baraja de cartas de la partida.
    
    Output: baraja - Lista de tuplas (string, int) con la baraja de cartas restantes
            carta - Tupla (string, int) correspondiente a la carta repartida
    """
    if len(baraja) == 0:
        return ""
    elif len(baraja)==1:
        carta = baraja.pop(0)
    else:
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
            

def tirarcarta(mano, decision):
    """
    Description: Esta funcion escoge la carta a jugar dada una mano
    
    Argumentos: mano - Lista de tuplas (string, int) con la mano de un jugador (conjunto de cartas de las que
                        dispone)
                decision - Booleana que indica si la jugada se escoge o se realiza aleatoria
                
    Output: mano - Lista de tuplas (string, int) con la mano actualizada
            carta - Tupla (string, int) con la carta a jugar
    """
    if decision:
        
        print("******** Tu mano es: *********")
        print(mano)
        eleccion = input("Escoje que carta quieres jugar: ")
        carta = mano.pop(int(eleccion))
    else:
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
    
    primerpalo=""
    
    
    for i in range(1,5):
        
        for jugador in d:
            if d[jugador][2]==i:
                print("Tira el jugador: ",jugador, " en el turno ", d[jugador][2])
                d[jugador][0], tirada[jugador] = tirarcarta(d[jugador][0],jugador=="a")
                
                if primerpalo=="":
                    primerpalo=tirada[jugador][0]
     
    return (d, tirada,primerpalo)

def ganadortirada(puntuaciones,triunfo,tirada, primerpalo):
    
    """
    Description:
    
    """
    puntos={}
    
    for jugador in tirada:
                
        puntuacion = tirada[jugador][1]+puntuaciones[tirada[jugador][1]]**2
        
        if tirada[jugador][0]==triunfo:
            puntuacion += 1000
        elif tirada[jugador][0]==primerpalo:
            puntuacion += 200
            
        puntos[jugador]=puntuacion
        
    ganador = max(puntos.items(), key=operator.itemgetter(1))[0]
    
    return ganador


def cantar(d, triunfo, cantados, ganador):
    
    """Description: Esta funcion revisa si alguno de los jugadores puede cantar.
    
        Argumentos: d - Diccionario con la información de los jugadores durante la partida
                    triunfo - String que indica el triunfo de la partida
                    cantados - Lista de string que indica los palos que ya se han cantado
                    ganador - String que indica el jugador que ha ganado la ronda
                    
        Output:     d- Diccionario actualizado con la información de los jugadores durante la partida
                    cantados - Lista de strings con los palos que ya se han cantado actualizada
    """
    equipoganador=d[ganador][3]
    
    for jugador in d:
        
        if d[jugador][3]==equipoganador:
            
            for card in d[jugador][0]:
                
                if (card[1]==10 or card[1]==12) and (not card[0] in cantados):
                    
                    for card2 in d[jugador][0][d[jugador][0].index(card)+1:len(d[jugador][0])]:
                        
                        if (card2[1]==10 or card2[1]==12) and card2[0]==card[0]:
                            
                            if card2[0]==triunfo:
                                print(jugador, " canta las cuarenta")
                                d[jugador][1]+=40
                            else:
                                print(jugador," canta las veinte de ", card2[0])
                            
                            cantados.append(card2[0])
                            
    return (d,cantados)
            

def ronda(puntuaciones, d, triunfo, cantados, ncards):
    
    """Description: Esta funcion genera una ronda
        
        Argumentos: puntuaciones - Diccionario con los puntos que otorga cada carta
                    d - Diccionario con la información de los jugadores durante la partida
                    triunfo - String que indica el triunfo de la partida
                    ncards - Número de cartas en la mano de los jugadores
                    cantados - Lista de string que indica los palos que ya se han cantado
                    
        Output:     d- Diccionario actualizado con la información de los jugadores durante la partida
                    cantados - Lista de strings con los palos que ya se han cantado actualizada
    """
    d, mesa, primerpalo = tirada(d)
    
    ganador = ganadortirada(puntuaciones, triunfo, mesa, primerpalo)
    
    print("El ganador de la mano es: ", ganador)

    puntos=0
    for tir in mesa:
        puntos+=puntuaciones[mesa[tir][1]]
    
    if ncards==1:
        print("Ultima ronda")
        puntos+=10
    
    d[ganador][1]+=puntos
    
    
    #revisar cantos
    d, cantados = cantar(d,triunfo,cantados,ganador)
    
    #Reasignar turnos
    
    turnoanterior=d[ganador][2]
    turnosiguiente=1
    
    jugadoresasignados=[]
    
    while turnosiguiente<len(d)+1:
        
        for jugador in d:
            
            if (not jugador in jugadoresasignados) and d[jugador][2]==turnoanterior:
                d[jugador][2]=turnosiguiente
                if turnoanterior==len(d):
                    turnoanterior=1
                else:
                    turnoanterior+=1
                
                turnosiguiente+=1
                jugadoresasignados.append(jugador)
                break
    return (d, cantados)


def repartirtodos(d,baraja):
    """Description: Esta funcion reparte una carta a cada jugador.
    
        Argumentos: d - Diccionario con la información de los jugadores durante la partida.
                    baraja - Lista de tuplas (string, int) con las cartas de la baraja
        
        Output:     d - Diccionario actualizado con la información de los jugadores durante la partida.
                    baraja - Lista de tuplas (string, int) con las cartas de la baraja pendientes
    """
    if len(baraja)==0:
        return d,baraja
        
    i=1
    while i <= len(d):
        
        baraja, carta = repartircarta(baraja)
        
        for jugador in d:
            
            if d[jugador][2]==i:
                d[jugador][0].append(carta)
                i+=1
                break
    
    return (d,baraja)
    

def completa (puntuaciones,d):
    """Description: Esta funcion genera un juego completo
    
        Argumentos: puntuaciones - Diccionario con los puntos que otorga cada carta
                    d - Diccionario con la información de los jugadores durante la partida
                    
        Output:     d - Diccionario actualizado con la información de los jugadores durante la partida
    """
    pequipo1=0
    pequipo2=0
    
    while pequipo1<101 and pequipo2<101:
        
        print("_____________Nueva partida________________")
    
        baraja, triunfo = crearbaraja()
        
        d, baraja = primerreparto(d,baraja)
        
        ncards=6
        
        cantados=[]
        
        while ncards>0 and pequipo1<101 and pequipo2<101:
            
            print("")
            print("Nueva ronda")
            print("")
            
            d, cantados = ronda(puntuaciones,d,triunfo,cantados, ncards)
            d, baraja = repartirtodos(d,baraja)
            
            #conocer el número de cartas de un jugador (no importa cual):
            for jugador in d:
                ncards = len(d[jugador][0])
                if d[jugador][3]==1:
                    pequipo1+=d[jugador][2]
                else:
                    pequipo2+=d[jugador][2]
    
    
    if pequipo1>pequipo2:
        print("Gana el equipo 1")
    else:
        print("Gana el equipo 2")

    return d
    

def test():
    
    d= creardiccionario(["a","b","c","d"])
    
    d = completa(puntuaciones,d)
    
    return d


if __name__ == "__main__":
    d=test()