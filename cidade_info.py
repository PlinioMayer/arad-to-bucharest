from typing import List

class Rota:
    distancia: int

    def __init__(self, cidade, distancia: int):
        self.cidade = cidade
        self.distancia = distancia

class Cidade:
    nome: str
    distancia_bucharest: int
    rotas: List[Rota]

    def __init__(self, nome: str, distancia_bucharest: int):
        self.nome = nome
        self.distancia_bucharest = distancia_bucharest


class Caminho:
    cidades: List[Cidade]
    distancia: int

    def __init__(self, cidades: List[Cidade], distancia: int = 0):
        self.cidades = cidades
        self.distancia = distancia


arad: Cidade = Cidade(
    'Arad',
    366
)

bucharest: Cidade = Cidade(
    'Bucharest',
    0
)

craiova: Cidade = Cidade(
    'Craiova',
    160
)

dobreta: Cidade = Cidade(
    'Dobreta',
    242
)

eforie: Cidade = Cidade(
    'Eforie',
    161
)

fagaras: Cidade = Cidade(
    'Fagaras',
    178
)

giurgiu: Cidade = Cidade(
    'Giurgiu',
    77
)

hirsova: Cidade = Cidade(
    'Hirsova',
    151
)

iasi: Cidade = Cidade(
    'Iasi',
    226
)

lugoj: Cidade = Cidade(
    'Lugoj',
    244
)

mehadia: Cidade = Cidade(
    'Mehadia',
    241
)

neamt: Cidade = Cidade(
    'Neamt',
    234
)

oradea: Cidade = Cidade(
    'Oradea',
    380
)

pitesti: Cidade = Cidade(
    'Pitesti',
    98
)

rimnicu_vilcea = Cidade(
    'Rimnicu Viclea',
    193
)

sibiu = Cidade(
    'Sibiu',
    253
)

timisoara = Cidade(
    'Timisoara',
    329
)

urzicene = Cidade(
    'Urzicene',
    80
)

vaslui = Cidade(
    'vaslui',
    199
)

zerind: Cidade = Cidade(
    'Zerind',
    374
)

arad.rotas = [
    Rota(zerind, 75),
    Rota(timisoara, 118),
    Rota(sibiu, 140)
]

bucharest.rotas = [
    Rota(pitesti, 101),
    Rota(urzicene, 85),
    Rota(giurgiu, 90),
    Rota(fagaras, 211)
]

craiova.rotas = [
    Rota(dobreta, 120),
    Rota(rimnicu_vilcea, 146),
    Rota(pitesti, 138)
]

dobreta.rotas = [
    Rota(mehadia, 75),
    Rota(craiova, 120)
]

eforie.rotas = [
    Rota(hirsova, 86)
]

fagaras.rotas = [
    Rota(sibiu, 99),
    Rota(bucharest, 211)
]

giurgiu.rotas = [
    Rota(bucharest, 90)
]

hirsova.rotas = [
    Rota(urzicene, 98),
    Rota(eforie, 86)
]

iasi.rotas = [
    Rota(neamt, 87),
    Rota(vaslui, 92)
]

lugoj.rotas = [
    Rota(timisoara, 111),
    Rota(mehadia, 70)
]

mehadia.rotas = [
    Rota(lugoj, 70),
    Rota(dobreta, 75)
]

neamt.rotas = [
    Rota(iasi, 87)
]

oradea.rotas = [
    Rota(zerind, 71),
    Rota(sibiu, 151)
]

pitesti.rotas = [
    Rota(rimnicu_vilcea, 97),
    Rota(craiova, 138),
    Rota(bucharest, 101)
]

rimnicu_vilcea.rotas = [
    Rota(sibiu, 80),
    Rota(craiova, 146),
    Rota(pitesti, 97)
]

sibiu.rotas = [
    Rota(arad, 140),
    Rota(oradea, 151),
    Rota(fagaras, 99),
    Rota(rimnicu_vilcea, 80)
]

timisoara.rotas = [
    Rota(arad, 118),
    Rota(lugoj,111)
]

urzicene.rotas = [
    Rota(bucharest, 85),
    Rota(vaslui, 142),
    Rota(hirsova, 98)
]

vaslui.rotas = [
    Rota(iasi, 92),
    Rota(urzicene, 142)
]

zerind.rotas = [
    Rota(arad, 75),
    Rota(oradea, 71)
]

cidades: List[Cidade] = [
    arad,
    bucharest,
    craiova,
    dobreta,
    eforie,
    fagaras,
    giurgiu,
    hirsova,
    iasi,
    lugoj,
    mehadia,
    neamt,
    oradea,
    pitesti,
    rimnicu_vilcea,
    sibiu,
    timisoara,
    urzicene,
    vaslui
]