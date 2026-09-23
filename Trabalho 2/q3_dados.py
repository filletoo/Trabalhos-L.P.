from random import *

def lancar_dados(vezes=1):
    jogadas = []
    for _ in range(vezes):
        valor1 = randint(1, 6)
        valor2 = randint(1, 6)
        jogadas.append((valor1, valor2))

    return jogadas

def soma_jogadas(jogadas):
    somas = []
    for jogada in jogadas:
        soma = jogada[0] + jogada[1]
        somas.append(soma)

    return somas

def pegar_frequencias(somas_jogadas):
    frequencias = {}
    for s in somas_jogadas:
        frequencias[s] = frequencias.get(s, 0) + 1

    return frequencias

def somas_mais_frequentes(somas_jogadas):
    #fazer frequencias
    frequencias = pegar_frequencias(somas_jogadas)

    maior_frequencia = 0
    mais_frequentes = []

    for i in frequencias:
        if frequencias[i] > maior_frequencia:
            maior_frequencia = frequencias[i]

    for j in frequencias:
        if frequencias[j] == maior_frequencia:
            mais_frequentes.append(j)

    return mais_frequentes

def media_somas(somas_jogadas):
    soma = 0
    for s in somas_jogadas:
        soma += s

    media = soma/100

    return media

if __name__ == '__main__':
    jogadas = lancar_dados(vezes=100)
    somas_jogadas = soma_jogadas(jogadas)

    media = media_somas(somas_jogadas)
    frequencias = pegar_frequencias(somas_jogadas)
    mais_frequentes = somas_mais_frequentes(somas_jogadas)

    print("------------------------------------------------------------")
    print("Somas:")
    for i in range(len(somas_jogadas)):
        print(f"- Jogada {i + 1}: {somas_jogadas[i]}")

    print("\nAparições:")
    for i in range(2, 13):
        print(f"- {i}: {frequencias.get(i, 0)} vez(es)")

    print(f"\nMédia das somas: {media:.2f}")

    print(f"Somas mais frequentes (frequencia: {frequencias[mais_frequentes[0]]}): ", end="")
    for i in range(len(mais_frequentes)):
        if i != len(mais_frequentes) - 1:
            print(f"{mais_frequentes[i]}", end=", ")
        else:
            print(mais_frequentes[i])

    print("------------------------------------------------------------")