# TODO entender como isso funciona

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro: # cada linha é uma lista de strings
        print(" | ".join(linha)) # a função join concatena os elementos da lista em apenas uma string
        print("-" * 10)


# Função para verificar se houve vitória
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Verificar colunas
    for col in range(3):
        if tabuleiro[0][col] == jogador and tabuleiro[1][col] == jogador and tabuleiro[2][col] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False


# Função para verificar se o tabuleiro está cheio
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True


# Função principal do jogo
def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Posição já ocupada, tente novamente.")
            continue

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"


# Iniciar o jogo
jogo_da_velha()
