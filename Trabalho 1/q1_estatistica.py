def lerDados():
    valido = False
    while not valido:
        dados = input("Digite a sequência de numeros inteiros:\n").split()
        if len(dados) == 0: 
            print("Sequencia não pode ser vazia")
            continue
        valido = True
        for i in range(len(dados)):
            try:
                dados[i] = int(dados[i])
                print(dados[i])
            except:
                print(f"Sequencia invalida, pois há um elemento que não é um inteiro")
                valido = False
                break
    return dados

def maiorMenor(dados):
    maior = dados[0]
    menor = dados[0]
    for i in dados:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i

    return maior, menor

def quantParImp(dados):
    par = 0
    impar = 0
    for i in dados:
        if i % 2 == 0:
            par += 1
        else:
            impar += 1

    return par, impar

if __name__ == "__main__":
    dados = lerDados()

    quant_elem = len(dados)
    maior, menor = maiorMenor(dados)
    soma = sum(dados)
    media = soma/quant_elem
    quant_par, quant_imp = quantParImp(dados)
    quant_distintos = len(set(dados))

    print("----------------------------------------------")
    print(f"Quantidade de elementos:", quant_elem)
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Soma dos valores: {soma}")
    print(f"Media aritmetica: {media:.2f}")
    print(f"Quantidade de numeros pares: {quant_par}")
    print(f"Quantidade de numeros impares: {quant_imp}")
    print(f"Quantidade de valores distintos: {quant_distintos}")
    print("----------------------------------------------")

    

