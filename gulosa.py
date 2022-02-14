from cidade_info import *
from util import *

def buscar_menor_caminho(caminho_atual: Caminho):
    menor_rota: Rota = None
    for rota in caminho_atual.cidades[-1].rotas:
        if rota.cidade is bucharest:
            caminho_atual.cidades.append(bucharest)
            caminho_atual.distancia += rota.distancia

            return caminho_atual

        if not menor_rota:
            menor_rota = rota
            continue

        if rota.cidade.distancia_bucharest < menor_rota.cidade.distancia_bucharest:
            menor_rota = rota

    caminho_atual.cidades.append(menor_rota.cidade)
    caminho_atual.distancia += menor_rota.cidade.distancia_bucharest

    return buscar_menor_caminho(caminho_atual)

def main():
    menor_caminho = buscar_menor_caminho(Caminho([arad]))
    print_caminho(menor_caminho)


if __name__ == '__main__':
    main()