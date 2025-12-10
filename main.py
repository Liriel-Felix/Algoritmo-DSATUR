#!/usr/bin/env python3
"""
Implementação do algoritmo DSATUR para coloração de grafos
Trabalho de Grafos - Docente: Bruno Motta
"""

import sys
import os
from grafo import carregar_grafo_gv, criar_grafo_professor
from dsatur import dsatur
from utils import (verificar_coloracao, analisar_grafo, 
                   mostrar_coloracao, mostrar_estatisticas, 
                   mostrar_visual)


def main():
    print("=" * 60)
    print("ALGORITMO DSATUR - COLORAÇÃO DE GRAFOS")
    print("=" * 60)
    
    # Determina qual arquivo usar
    if len(sys.argv) > 1:
        arquivo_gv = sys.argv[1]
        if not os.path.exists(arquivo_gv):
            # Tentar na pasta data/
            arquivo_gv = os.path.join("data", sys.argv[1])
    else:
        # Arquivo padrão
        arquivo_gv = os.path.join("data", "grafo_professor.gv")
    
    # Carregar grafo
    if os.path.exists(arquivo_gv):
        print(f"\nCarregando grafo do arquivo: {arquivo_gv}")
        try:
            grafo = carregar_grafo_gv(arquivo_gv)
            print(f"[OK] Grafo carregado com sucesso")
            print("\n")
        except Exception as e:
            print(f" Erro ao carregar arquivo .gv: {e}")
            print("Usando grafo padrão do professor...")
            print("\n")
            grafo = criar_grafo_professor()
    else:
        print(f"\n[ERRO]  Arquivo não encontrado: {arquivo_gv}")
        print("Usando grafo padrão do professor...")
        grafo = criar_grafo_professor()
    
    # 1. Análise do grafo
    print("ANÁLISE DO GRAFO")
    analisar_grafo(grafo)
    
    # 2. Executar DSATUR
    print("\n")
    print("EXECUTANDO ALGORITMO DSATUR")
    print("Critério: maior grau de saturação → maior grau")
    coloracao = dsatur(grafo)
    
    # 3. Mostrar resultados
    cores_vertices = mostrar_coloracao(coloracao)
    mostrar_estatisticas(cores_vertices, grafo)
    
    # 4. Validar
    print("\n")
    valido, mensagem = verificar_coloracao(grafo, coloracao)
    if valido:
        print(f"✓ {mensagem}")
        print("\n")
    else:
        print(f"✗ {mensagem}")
        print("\n[ERRO]  A coloração NÃO é válida!")
        print("\n")
    
    # 5. Visualização (opcional)
    print("VISUALIZAÇÃO")
    mostrar_visual(coloracao)
    print("\n")
    print("EXECUÇÃO CONCLUÍDA")
    
    # Salvar resultados em arquivo
    salvar_resultados(grafo, coloracao, arquivo_gv)


def salvar_resultados(grafo, coloracao, arquivo_origem):
    """Salva os resultados em um arquivo de texto"""
    arquivo_saida = "resultado_coloracao.txt"
    
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("RESULTADOS DA COLORAÇÃO DSATUR\n")
        f.write("=" * 60 + "\n\n")
        
        f.write(f"Grafo de entrada: {arquivo_origem}\n")
        f.write(f"Número de vértices: {grafo.numero_vertices()}\n")
        f.write(f"Número de arestas: {grafo.numero_arestas()}\n\n")
        
        f.write("COLORAÇÃO:\n")
        f.write("-" * 40 + "\n")
        
        # Agrupar por cor
        cores_vertices = {}
        for v, cor in coloracao.items():
            if cor not in cores_vertices:
                cores_vertices[cor] = []
            cores_vertices[cor].append(v)
        
        for cor in sorted(cores_vertices.keys()):
            vertices = sorted(cores_vertices[cor], key=lambda x: (len(x), x))
            f.write(f"Cor {cor:2}: {vertices}\n")
        
        f.write(f"\nTotal de cores utilizadas: {len(cores_vertices)}\n")
        
        # Validação
        valido, mensagem = verificar_coloracao(grafo, coloracao)
        f.write(f"\nValidação: {mensagem}\n")
    
    print(f"\n Resultados salvos em: {arquivo_saida}")


if __name__ == "__main__":
    main()