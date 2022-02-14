def print_caminho(caminho):
    print(' --> '.join(map(lambda cidade: cidade.nome, caminho.cidades)))