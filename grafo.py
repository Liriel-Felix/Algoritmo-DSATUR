import re

class Grafo:
    def __init__(self):
        self.adjacencia = {}
        self.direcionado = False
    
    def adicionar_vertice(self, v):
        if v not in self.adjacencia:
            self.adjacencia[v] = []
    
    def adicionar_aresta(self, v1, v2, direcionado=False):
        """Adiciona aresta, tratando como não-direcionada por padrão"""
        self.adicionar_vertice(v1)
        self.adicionar_vertice(v2)
        
        if v2 not in self.adjacencia[v1]:
            self.adjacencia[v1].append(v2)
        
        if not direcionado and v1 not in self.adjacencia[v2]:
            self.adjacencia[v2].append(v1)
    
    def vertices(self):
        return list(self.adjacencia.keys())
    
    def vizinhos(self, v):
        return self.adjacencia.get(v, [])
    
    def grau(self, v):
        return len(self.vizinhos(v))
    
    def numero_vertices(self):
        return len(self.adjacencia)
    
    def numero_arestas(self):
        if self.direcionado:
            total = sum(len(vizinhos) for vizinhos in self.adjacencia.values())
            return total
        else:
            total = sum(len(vizinhos) for vizinhos in self.adjacencia.values())
            return total // 2
    
    def tem_aresta(self, v1, v2):
        return v2 in self.adjacencia.get(v1, [])


def carregar_grafo_gv(caminho_arquivo):
    """
    Carrega grafo de arquivo .gv (GraphViz DOT format)
    Suporta grafos não-direcionados (graph) e direcionados (digraph)
    """
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    # Detecta se é grafo direcionado
    direcionado = 'digraph' in conteudo[:20]
    
    # Remove comentários
    conteudo = re.sub(r'//.*', '', conteudo)
    
    grafo = Grafo()
    grafo.direcionado = direcionado
    
    # Extrair arestas
    if direcionado:
        # Padrão para arestas direcionadas: A -> B
        padrao = r'(\w+)\s*->\s*(\w+)'
    else:
        # Padrão para arestas não-direcionadas: A -- B
        padrao = r'(\w+)\s*--\s*(\w+)'
    
    arestas = re.findall(padrao, conteudo)
    
    # Extrair vértices isolados (declarados sozinhos)
    vertices_isolados = re.findall(r'^\s*(\w+)\s*;', conteudo, re.MULTILINE)
    
    # Adicionar todas as arestas
    for v1, v2 in arestas:
        grafo.adicionar_aresta(v1, v2, direcionado)
    
    # Adicionar vértices isolados
    for v in vertices_isolados:
        grafo.adicionar_vertice(v)
    
    return grafo


def criar_grafo_professor():
    """Cria o grafo específico do professor (fallback se arquivo .gv não existir)"""
    grafo = Grafo()
    
    arestas = [
        ("1", "2"), ("1", "4"), ("1", "5"),
        ("2", "3"), ("2", "4"), ("2", "5"), ("2", "6"), ("2", "10"),
        ("3", "5"), ("3", "6"), ("3", "10"),
        ("4", "5"), ("4", "7"), ("4", "8"),
        ("5", "6"), ("5", "9"), ("5", "10"),
        ("6", "10"), ("6", "11"), ("6", "14"),
        ("7", "8"),
        ("8", "13"),
        ("9", "10"),
        ("10", "14"),
        ("11", "14"), ("11", "17"), ("11", "20"),
        ("12", "13"), ("12", "16"), ("12", "20"),
        ("13", "14"),
        ("14", "17"), ("14", "20"),
        ("15", "16"), ("15", "18"),
        ("16", "18"),
        ("18", "19"),
        ("17", "20"), ("17", "14"), ("17", "11")
    ]
    
    for v1, v2 in arestas:
        grafo.adicionar_aresta(v1, v2)
    
    return grafo