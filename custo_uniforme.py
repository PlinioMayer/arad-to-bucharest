from typing import Optional, List
from cidade_info import *
from util import *

def buscar_menor_caminho(caminho_atual: Caminho, caminhos: List[Caminho] = [], melhor_caminho: Caminho = None):
    novo_melhor_caminho = melhor_caminho

    menor_caminho: Caminho = None
    menor_caminho_index: int = -1

    for caminho_index, caminho in enumerate(caminhos):
        if not menor_caminho:
            menor_caminho = caminho
            menor_caminho_index = caminho_index
            continue

        if caminho.distancia < menor_caminho.distancia:
            menor_caminho = caminho
            menor_caminho_index = caminho_index

    for rota in caminho_atual.cidades[-1].rotas:
        if rota.cidade in caminho_atual.cidades:
            continue

        if rota.cidade is bucharest:
            caminho_atual.cidades.append(bucharest)
            caminho_atual.distancia += rota.distancia

            if not novo_melhor_caminho:
                novo_melhor_caminho = caminho_atual
            elif caminho_atual.distancia < novo_melhor_caminho.distancia:
                novo_melhor_caminho = caminho_atual

            continue
        
        novo_caminho = Caminho(caminho_atual.cidades.copy(), caminho_atual.distancia)

        novo_caminho.cidades.append(rota.cidade)
        novo_caminho.distancia += rota.distancia

        adicionar = True

        if novo_melhor_caminho and novo_caminho.distancia > novo_melhor_caminho.distancia:
            adicionar = False
        else:
            for caminho in caminhos:
                if novo_caminho.cidades[-1] is caminho.cidades[-1] and novo_caminho.distancia > caminho.distancia:
                    adicionar = False

        if adicionar:
            caminhos.append(novo_caminho)
            if menor_caminho:
                if novo_caminho.distancia < menor_caminho.distancia:
                    menor_caminho = novo_caminho
                    menor_caminho_index += 1
            else:
                menor_caminho = novo_caminho
                menor_caminho_index += 1


    if len(caminhos):
        del caminhos[menor_caminho_index]
        return buscar_menor_caminho(menor_caminho, caminhos, novo_melhor_caminho)
    else:
        return novo_melhor_caminho

def main():
    menor_caminho = buscar_menor_caminho(Caminho([arad]))
    print_caminho(menor_caminho)
    print('Distância:', menor_caminho.distancia)

    
if __name__ == '__main__':
    main()