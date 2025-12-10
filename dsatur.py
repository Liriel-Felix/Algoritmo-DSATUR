from grafo import Grafo

def dsatur(grafo):
    """
    Implementação do algoritmo DSATUR para coloração de grafos
    """
    V = grafo.vertices()
    
    # Estruturas de dados
    C = {v: 0 for v in V}  # 0 = sem cor
    grau_saturacao = {v: 0 for v in V}
    grau = {v: grafo.grau(v) for v in V}
    U = set(V)  # Vértices não coloridos
    
    while U:
        # 1. Selecionar vértice com maior grau de saturação
        u = _selecionar_vertice(U, grau_saturacao, grau)
        
        # 2. Encontrar menor cor disponível
        cor = _encontrar_cor_disponivel(u, grafo, C)
        
        # 3. Colorir vértice
        C[u] = cor
        U.remove(u)
        
        # 4. Atualizar graus de saturação dos vizinhos
        _atualizar_saturacao(u, cor, grafo, C, grau_saturacao, U)
    
    return C


def _selecionar_vertice(U, grau_saturacao, grau):
    """Seleciona vértice com maior saturação, desempata por maior grau"""
    melhor_v = None
    max_sat = -1
    max_grau = -1
    
    for v in U:
        sat = grau_saturacao[v]
        g = grau[v]
        
        if sat > max_sat or (sat == max_sat and g > max_grau):
            melhor_v = v
            max_sat = sat
            max_grau = g
    
    return melhor_v


def _encontrar_cor_disponivel(vertice, grafo, coloracao):
    """Encontra a menor cor não usada pelos vizinhos"""
    vizinhos = grafo.vizinhos(vertice)
    cores_vizinhos = {coloracao[v] for v in vizinhos if coloracao[v] != 0}
    
    cor = 1
    while cor in cores_vizinhos:
        cor += 1
    return cor


def _atualizar_saturacao(vertice, cor, grafo, coloracao, grau_saturacao, U):
    """Atualiza grau de saturação dos vizinhos não coloridos"""
    for vizinho in grafo.vizinhos(vertice):
        if vizinho in U:
            # Verificar se esta cor é nova para o vizinho
            vizinhos_do_vizinho = grafo.vizinhos(vizinho)
            cores_existentes = {
                coloracao[v] for v in vizinhos_do_vizinho 
                if coloracao[v] != 0
            }
            
            if cor not in cores_existentes:
                grau_saturacao[vizinho] += 1