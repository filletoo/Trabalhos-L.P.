def lerSaque():
    while True:
        saque = input("Informe o valor do saque: ")
        try:
            saque = int(saque)
        except:
            print("Digite um valor inteiro de saque")
            continue
        
        if saque > 1000:
            print("O saque máximo permitido é de R$1000,00")
            continue
        elif saque <= 0:
            print("O valor do saque deve ser um número inteiro positivo")
            continue
        break
    return saque

def minCedulas(saque, cedulas):
    min = []
    for i in range(len(cedulas)):
        quant_cedula = saque // cedulas[i]
        saque %= cedulas[i]
        min.append(quant_cedula)
        i += 1

    return min

if __name__ == "__main__":
    cedulas = [200, 100, 50, 20, 10, 5, 2, 1]
    saque = lerSaque()
    quantCedulas = minCedulas(saque, cedulas)

    for i in range(len(cedulas)):
        print(f"Quantidade de cédulas {cedulas[i]}: {quantCedulas[i]}")