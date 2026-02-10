import random
from typing import Set, List, Tuple

# =========================
# Definição do Universo
# =========================
U_MIN = 1
U_MAX = 20  # Universo de 1 a 20


def universo() -> Set[int]:
    return set(range(U_MIN, U_MAX + 1))


# =========================
# Entrada e Parsing
# =========================
def tokenizar_entrada(entrada: str) -> List[str]:
    """
    Quebra a entrada em tokens aceitando espaço e vírgula.
    Trata entradas vazias ou só separadores.
    """
    entrada = entrada.strip()
    if not entrada:
        return []

    entrada = entrada.replace(",", " ")
    tokens = [t.strip() for t in entrada.split() if t.strip() != ""]
    return tokens


def parse_conjunto_numeros(tokens: List[str]) -> Tuple[Set[int], List[str]]:
    """
    Converte tokens em inteiros.

    Retorna:
      conjunto válido
      lista de inválidos
    """
    numeros: Set[int] = set()
    invalidos: List[str] = []

    for t in tokens:
        try:
            n = int(t)
            numeros.add(n)
        except ValueError:
            invalidos.append(t)

    return numeros, invalidos


def ler_conjunto_usuario(nome: str) -> Set[int]:
    """
    Lê conjunto com validações completas.
    """
    U = universo()

    print("\n--- Inserção do Conjunto ---")
    print(f"Digite os elementos do conjunto {nome}.")
    print("Regras:")
    print(f"- Apenas números entre {U_MIN} e {U_MAX}")
    print("- Digite de 4 a 8 valores")
    print("- Repetidos serão removidos\n")

    while True:
        entrada = input("Digite os números separados por espaço ou vírgula:\n> ")

        tokens = tokenizar_entrada(entrada)

        # Entrada vazia
        if len(tokens) == 0:
            print("Erro: entrada vazia.")
            continue

        # Quantidade digitada
        if len(tokens) > 8:
            print(f"Erro: você digitou {len(tokens)} valores. Máximo = 8.")
            continue

        if len(tokens) < 4:
            print(f"Erro: você digitou {len(tokens)} valores. Mínimo = 4.")
            continue

        conjunto, invalidos = parse_conjunto_numeros(tokens)

        # Não inteiros
        if invalidos:
            print(f"Erro: valores inválidos: {invalidos}")
            continue

        # Fora do universo
        if not conjunto.issubset(U):
            fora = sorted(conjunto - U)
            print(f"Erro: fora do intervalo permitido: {fora}")
            continue

        # Duplicatas
        if len(tokens) != len(conjunto):
            repetidos = len(tokens) - len(conjunto)
            print(f"Aviso: {repetidos} valor(es) repetido(s) removido(s).")

        # Cardinalidade final
        if 4 <= len(conjunto) <= 8:
            return conjunto
        else:
            print(
                f"Erro: após remover duplicatas, restaram {len(conjunto)} elementos."
            )


# =========================
# Geração automática
# =========================
def gerar_conjunto_aleatorio() -> Set[int]:
    U = list(universo())
    tamanho = random.randint(4, 8)
    return set(random.sample(U, tamanho))


# =========================
# Formatação
# =========================
def formatar_conjunto(S: Set[int]) -> str:
    return "{" + ", ".join(map(str, sorted(S))) + "}"


# =========================
# Operações
# =========================
def relatorio_operacoes(A: Set[int], B: Set[int]):

    U = universo()

    uniao = A | B
    intersecao = A & B
    diferenca_a_b = A - B
    diferenca_b_a = B - A
    diferenca_simetrica = A ^ B
    complemento_a = U - A
    complemento_b = U - B

    print("\n" + "=" * 60)
    print("RELATÓRIO DAS OPERAÇÕES DE CONJUNTOS")
    print("=" * 60)

    print(f"Universo U = {U_MIN}..{U_MAX}")
    print(f"U = {formatar_conjunto(U)}\n")

    print("Conjuntos:")
    print(f"A = {formatar_conjunto(A)}  |A| = {len(A)}")
    print(f"B = {formatar_conjunto(B)}  |B| = {len(B)} (gerado automaticamente)")

    print("\nOperações:")

    print(f"A ∪ B = {formatar_conjunto(uniao)}")
    print(f"|A ∪ B| = {len(uniao)}")

    print(f"\nA ∩ B = {formatar_conjunto(intersecao)}")
    print(f"|A ∩ B| = {len(intersecao)}")

    print(f"\nA - B = {formatar_conjunto(diferenca_a_b)}")
    print(f"B - A = {formatar_conjunto(diferenca_b_a)}")

    print(f"\nA Δ B = {formatar_conjunto(diferenca_simetrica)}")

    print("\nComplementos:")
    print(f"Ā = {formatar_conjunto(complemento_a)}")
    print(f"Ḃ = {formatar_conjunto(complemento_b)}")

    print("=" * 60)


# =========================
# Menu final
# =========================
def menu_repeticao() -> bool:
    """
    Retorna True se quiser rodar novamente.
    """
    while True:
        print("\nDeseja executar novamente?")
        print("1 - Sim")
        print("2 - Não (Sair)")

        opcao = input("> ")

        if opcao == "1":
            return True
        elif opcao == "2":
            print("\nEncerrando o programa...")
            return False
        else:
            print("Opção inválida. Digite 1 ou 2.")


# =========================
# Programa principal
# =========================
def executar_programa():

    print("\n=== Programa de Operações com Conjuntos ===")

    conjunto_a = ler_conjunto_usuario("A")
    conjunto_b = gerar_conjunto_aleatorio()

    relatorio_operacoes(conjunto_a, conjunto_b)


def main():

    while True:
        executar_programa()

        if not menu_repeticao():
            break


# =========================
# Execução
# =========================
if __name__ == "__main__":
    main()
