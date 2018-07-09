
PIEZAS = {
    'O':[
        '0000\n0110\n0110\n0000',
    ],

    'S':[
        '0000\n0022\n0220\n0000',
        '0000\n0200\n0220\n0020',
    ],

    'Z':[
        '0000\n3300\n0330\n0000',
        '0000\n0030\n0330\n0300',
    ],

    'I':[
        '0400\n0400\n0400\n0400',
        '0000\n4444\n0000\n0000',
    ],

    'J':[
        '0000\n5000\n5550\n0000',
        '0000\n0550\n0500\n0500',
        '0000\n0000\n5550\n0050',
        '0000\n0050\n0050\n0550',
    ],

    'L':[
        '0000\n0060\n6660\n0000',
        '0000\n0060\n0060\n0660',
        '0000\n0000\n6660\n6000',
        '0000\n0660\n0060\n0060',
    ],

    'T':[
        '0000\n0700\n7770\n0000',
        '0000\n0700\n0770\n0700',
        '0000\n0000\n7770\n0700',
        '0000\n0070\n0770\n0070',
    ]}
#for k, v in PIEZAS.items():
    #print(k)
    #for p in v:
        #print(p, '\n')

COLORES = {
    0: (0, 0, 0),
    1: (255, 255, 0),
    2: (0, 255, 0),
    3: (255, 0, 0),
    4: (0, 255, 255),
    5: (0, 0, 255),
    6: (255, 127, 0),
    7: (255, 0, 255),
    8: (127, 255, 0),
    9: (255, 255, 255),
}
        
for name, rotations in PIEZAS.items():
    PIEZAS[name] = [[[int(i) for i in p] for p in r.splitlines()]
                    for r in rotations]

TAMAÑO_VENTANA=640, 480
DIM_TABLERO=10,20
BORDE_TABLERO=4
TAMAÑO_BLOQUE=20,20

TAMAÑO_TABLERO=tuple([DIM_TABLERO[i]*TAMAÑO_BLOQUE[i] for i in range(2)])
TAMAÑO_TABBORDE=tuple([DIM_TABLERO[i]*TAMAÑO_BLOQUE[i]+BORDE_TABLERO*2 for i in range(2)])

MARGEN=tuple([TAMAÑO_VENTANA[i]-TAMAÑO_TABLERO[i]-BORDE_TABLERO*2 for i in range(2)])
START_TABLERO=int(MARGEN[0]/2),MARGEN[1]+2*BORDE_TABLERO
START_TABBORDE=int(MARGEN[0]/2)-BORDE_TABLERO,MARGEN[1]+BORDE_TABLERO

CENTRO_VENTANA=tuple([TAMAÑO_VENTANA[i]/2 for i in range(2)])
POS=CENTRO_VENTANA[0],CENTRO_VENTANA[1]+100
POSICION_MARCADOR=TAMAÑO_VENTANA[0]-START_TABBORDE[0]/2,120
POSICION_PIEZAS=POSICION_MARCADOR[0],150
POSICION_LINEAS=POSICION_MARCADOR[0],180
POSICION_TETRIS=POSICION_MARCADOR[0],210
POSICION_NIVEL=POSICION_MARCADOR[0],240

GRAVEDAD=0.35
