def lerN():
    while True:
        n = input("Indique a ordem da matriz: ")
        if not n.isdigit() or int(n) <= 0:
            print("Digite um valor inteiro positivo")
            continue
        n = int(n)
        break
    return n

def lerNumeros(n, i):
    valido = False
    while not valido:
        numeros = input(f"Digite os valores da linha {i + 1}: ").split()
        if len(numeros) < n: 
            print("A quantidade de números da linha deve ser", n)
            continue
        valido = True
        for i in range(len(numeros)):
            try:
                numeros[i] = int(numeros[i])
            except:
                print("Digite apenas números inteiros")
                valido = False
                break
    return numeros

def lerMatriz(n):
    matriz = []
    for i in range(n):
        linha = lerNumeros(n, i)
        matriz.append(linha)

    return matriz

def exibir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:2d}", end=" ")
        print()

def soma_linha(matriz, linha):
    soma = 0
    for coluna in range(len(matriz)):
        soma += matriz[linha][coluna]

    return soma

def soma_coluna(matriz, coluna):
    soma = 0
    for linha in range(len(matriz)): 
        soma += matriz[linha][coluna]

    return soma

def soma_diagonal(matriz, principal=True):
    n = len(matriz)
    if principal:
        linha = 0
        coluna = 0
        somaDigPrincipal = 0
        while linha < n and coluna < n:
            somaDigPrincipal += matriz[linha][coluna]
            linha += 1
            coluna += 1
        return somaDigPrincipal

    else:
        linha = 0
        coluna = n - 1
        somaDigSecundaria = 0
        while linha < n and coluna >= 0:
            somaDigSecundaria += matriz[linha][coluna]
            linha += 1
            coluna -= 1
        return somaDigSecundaria

def iguais(somas):
    igual = True
    for i in somas:
        if i != somas[0]:
            igual = False
            break
    return igual

if __name__=="__main__":
    n = lerN()
    matriz = lerMatriz(n)
    somas = []

    print("\nMatriz:")
    exibir_matriz(matriz)
    print()

    #soma das linhas
    for linha in range(n):
        soma = soma_linha(matriz, linha)
        print(f"Soma da linha {linha + 1}: {soma}")
        somas.append(soma)

    #soma das colunas
    for coluna in range(n):
        soma = soma_coluna(matriz, coluna)
        print(f"Soma da coluna {coluna + 1}: {soma}")
        somas.append(soma)

    #soma das diagonais
    somaDigPrincipal = soma_diagonal(matriz, principal=True)
    print(f"Soma da diagonal principal: {somaDigPrincipal}")
    somas.append(somaDigPrincipal)

    somaDigSecundaria = soma_diagonal(matriz, principal=False)
    print(f"Soma da diagonal secundária: {somaDigSecundaria}")
    somas.append(somaDigSecundaria)

    #é quadrado mágico
    quadMagic = iguais(somas)
    if quadMagic:
        print("\nA matriz é um quadrado mágico")
    else:
        print("\nA matriz não é um quadrado mágico")
    