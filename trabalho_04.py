import numpy as np

####################################################### CLASSE ITEM

class Objeto:
    def __init__(self, peso, valor, razao):
        self.peso = peso
        self.valor = valor
        self.razao = razao

####################################################### PROGRAMAÇÃO DINÂMICA

def mochila_dinamica(objetos, capacidade_max):
    """Resolve o problema da mochila usando programação dinâmica.
    
    Args:
        objetos (list): Lista de objetos Objeto.
        capacidade_max (int): Capacidade máxima da mochila.
    
    Returns:
        tuple: Valor total, Itens selecionados.
    """
    solucao_dinamica = []
    valor_total_dinamica = 0
    tabela = np.zeros((len(objetos) + 1, capacidade_max + 1))
    
    for i in range(1, len(objetos) + 1):
        for j in range(1, capacidade_max + 1):
            if objetos[i - 1].peso <= j:
                tabela[i, j] = max(tabela[i - 1, j], tabela[i - 1, j - objetos[i - 1].peso] + objetos[i - 1].valor)
            else:
                tabela[i, j] = tabela[i - 1, j]

    valor_total_dinamica = tabela[len(objetos), capacidade_max]
    
    # Traçar a solução
    i, j = len(objetos), capacidade_max
    while i > 0 and j > 0:
        if tabela[i, j] != tabela[i - 1, j]:
            solucao_dinamica.append(i - 1)
            j -= objetos[i - 1].peso
        i -= 1
    
    solucao_dinamica.reverse()
    return valor_total_dinamica, solucao_dinamica

####################################################### ALGORITMO GULOSO

def mochila_gulosa(objetos, capacidade_max):
    """Resolve o problema da mochila usando um algoritmo guloso.
    
    Args:
        objetos (list): Lista de objetos Objeto.
        capacidade_max (int): Capacidade máxima da mochila.
    
    Returns:
        tuple: Valor total, Itens selecionados.
    """
    solucao_gulosa = []
    peso_atual = 0
    valor_total_gulosa = 0
    
    objetos_ordenados = sorted(objetos, key=lambda x: (x.razao, -x.peso), reverse=True)
    #s
    for objeto in objetos_ordenados:
        if peso_atual + objeto.peso <= capacidade_max:
            solucao_gulosa.append(objeto)
            peso_atual += objeto.peso
            valor_total_gulosa += objeto.valor
    
    solucao_indices = [objetos.index(obj) for obj in solucao_gulosa]
    return valor_total_gulosa, solucao_indices

####################################################### FUNÇÃO PRINCIPAL

def main():
    """Função principal para executar a lógica do programa."""
    objetos = []
    
    entrada = input().split()
    capacidade_maxima = int(entrada[0])
    quantidade_itens = int(entrada[1])
    
    for _ in range(quantidade_itens):
        dados = input().split()
        peso = int(dados[0])
        valor = int(dados[1])
        razao = valor / peso
        objetos.append(Objeto(peso, valor, razao))
    
    valor_dinamica, solucao_dinamica = mochila_dinamica(objetos, capacidade_maxima)
    valor_gulosa, solucao_gulosa = mochila_gulosa(objetos, capacidade_maxima)
    porcentagem = (100 * valor_gulosa) / valor_dinamica
    
    print(" ".join(map(str, solucao_dinamica)))
    print(" ".join(map(str, solucao_gulosa)))
    print(int(valor_dinamica), valor_gulosa)
    print("{:.2f}".format(porcentagem))

####################################################### EXECUÇÃO

if __name__ == "__main__":
    main()
