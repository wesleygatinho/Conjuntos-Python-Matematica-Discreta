import random

def obter_conjunto_usuario():
    """
    Solicita ao usuário um conjunto de números inteiros.
    Valida se a entrada possui entre 4 e 8 elementos distintos.
    """
    while True:
        try:
            entrada = input("Digite entre 4 e 8 números inteiros (separados por espaço): ")
            # Converte a entrada em uma lista de inteiros e depois em um set para remover duplicatas
            numeros = set(int(x) for x in entrada.split())
            
            # Validação do tamanho do conjunto (4 a 8 elementos)
            if 4 <= len(numeros) <= 8:
                return numeros
            else:
                print(f"Erro: Você digitou {len(numeros)} elementos únicos. O conjunto deve ter entre 4 e 8.")
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros válidos.")

def gerar_conjunto_aleatorio():
    """
    Gera um conjunto aleatório com tamanho entre 4 e 8 elementos.
    Os números sorteados variam de 1 a 20 (Universo).
    """
    tamanho = random.randint(4, 8)
    # random.sample garante que não haja números repetidos na escolha
    # Considerando um universo de números entre 1 e 20
    dados = random.sample(range(1, 21), tamanho)
    return set(dados)

def realizar_operacoes(conjunto_a, conjunto_b):
    """
    Realiza as operações de União, Interseção e Diferença.
    Exibe os resultados formatados na tela.
    """
    # Operações de Conjuntos
    uniao = conjunto_a | conjunto_b          # A U B
    intersecao = conjunto_a & conjunto_b     # A ∩ B
    diferenca_a_b = conjunto_a - conjunto_b  # A - B
    diferenca_b_a = conjunto_b - conjunto_a  # B - A
    
    print("\n" + "="*40)
    print("RESULTADOS DAS OPERAÇÕES")
    print("="*40)
    
    # Exibição dos Conjuntos de Entrada
    print(f"Conjunto A (Usuário): {conjunto_a}")
    print(f"Conjunto B (Aleatório): {conjunto_b}")
    print("-" * 40)
    
    # Exibição das Operações
    print(f"União (A U B):       {uniao}")
    print(f"Interseção (A ∩ B):  {intersecao}")
    print(f"Diferença (A - B):   {diferenca_a_b}")
    print(f"Diferença (B - A):   {diferenca_b_a}")
    
    print("-" * 40)
    # Exibição da Cardinalidade (Tamanho)
    print(f"Cardinalidade |A|:     {len(conjunto_a)}")
    print(f"Cardinalidade |B|:     {len(conjunto_b)}")
    print(f"Cardinalidade |A U B|: {len(uniao)}")
    print("="*40)

def main():
    """
    Função principal que orquestra a execução do programa.
    """
    print("--- Atividade Prática: Teoria dos Conjuntos ---\n")
    
    # 1. Obter conjunto do usuário
    conjunto_a = obter_conjunto_usuario()
    
    # 2. Gerar conjunto aleatório
    conjunto_b = gerar_conjunto_aleatorio()
    
    # 3. Realizar cálculos e mostrar resultados
    realizar_operacoes(conjunto_a, conjunto_b)

if __name__ == "__main__":
    main()