def verificar_coloracao(grafo, coloracao):
    """Verifica se a coloração é válida para grafo não-direcionado"""
    for v in grafo.vertices():
        cor_v = coloracao[v]
        for vizinho in grafo.vizinhos(v):
            if coloracao[vizinho] == cor_v:
                return False, f"Conflito na aresta {v}-{vizinho}: mesma cor {cor_v}"
    
    return True, "Coloração válida (nenhum par de vértices adjacentes tem a mesma cor)"


def analisar_grafo(grafo):
    """Exibe análise detalhada do grafo"""
    print(f"Tipo: {'Direcionado' if grafo.direcionado else 'Não-direcionado'}")
    print(f"Número de vértices: {grafo.numero_vertices()}")
    print(f"Número de arestas: {grafo.numero_arestas()}")
    
    print("\nGrau de cada vértice:")
    vertices_ordenados = sorted(grafo.vertices(), key=lambda x: (len(x), x))
    for v in vertices_ordenados:
        vizinhos = sorted(grafo.vizinhos(v), key=lambda x: (len(x), x))
        print(f"  Vértice {v:>3}: grau {grafo.grau(v):2} - vizinhos: {vizinhos}")
    
    # Estatísticas
    graus = [grafo.grau(v) for v in grafo.vertices()]
    if graus:
        print(f"\nGrau máximo: {max(graus)}")
        print(f"Grau mínimo: {min(graus)}")
        print(f"Grau médio: {sum(graus)/len(graus):.2f}")


def mostrar_coloracao(coloracao):
    """Exibe a coloração de forma organizada"""
    # Agrupar vértices por cor
    cores_vertices = {}
    for vertice, cor in coloracao.items():
        if cor not in cores_vertices:
            cores_vertices[cor] = []
        cores_vertices[cor].append(vertice)
    
    # Ordenar
    print("\n" + "="*50)
    print("COLORAÇÃO DSATUR - VÉRTICES AGRUPADOS POR COR")
    print("="*50)
    
    for cor in sorted(cores_vertices.keys()):
        vertices = sorted(cores_vertices[cor], key=lambda x: (len(x), x))
        print(f"Cor {cor:2}: {vertices}")
    
    return cores_vertices


def mostrar_estatisticas(cores_vertices, grafo):
    """Exibe estatísticas da coloração"""
    print("\n" + "="*50)
    print("ESTATÍSTICAS DA COLORAÇÃO")
    print("="*50)
    
    num_cores = len(cores_vertices)
    print(f"Número total de cores usadas: {num_cores}")
    
    # Limite inferior teórico (número cromático)
    grau_max = max(grafo.grau(v) for v in grafo.vertices())
    print(f"Limite inferior (grau máximo + 1): ≤ {grau_max + 1}")
    
    print("\nDistribuição de vértices por cor:")
    for cor in sorted(cores_vertices.keys()):
        num_vertices = len(cores_vertices[cor])
        percentual = (num_vertices / grafo.numero_vertices()) * 100
        print(f"  Cor {cor:2}: {num_vertices:2} vértices ({percentual:5.1f}%)")


def mostrar_visual(coloracao, largura=5):
    """Exibe representação visual com emojis"""
    cores_emoji = ["🔴", "🔵", "🟢", "🟡", "🟣", "🟠", "⚫", "⚪", "🟤", "🔶", "🔷"]
    
    print("\n" + "="*50)
    print("REPRESENTAÇÃO VISUAL (emoji por cor)")
    print("="*50)
    
    vertices = sorted(coloracao.keys(), key=lambda x: (len(x), x))
    
    for i, v in enumerate(vertices):
        cor_num = coloracao[v]
        idx = (cor_num - 1) % len(cores_emoji)
        print(f"{v:>3}{cores_emoji[idx]} ", end="")
        
        if (i + 1) % largura == 0:
            print()
    
    if len(vertices) % largura != 0:
        print()
    
    # Legenda
    print("\nLegenda:")
    cores_unicas = sorted(set(coloracao.values()))
    for cor in cores_unicas:
        idx = (cor - 1) % len(cores_emoji)
        print(f"  {cores_emoji[idx]} = Cor {cor}")