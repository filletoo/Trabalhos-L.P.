def calcPontuacao(senha, min):
    pontuacao = 0
    tamMin = False
    letraMaius = False
    letraMinus = False
    digito = False
    especial = False

    if len(senha) >= min:
        tamMin = True
    for char in senha:
        if char.isupper():
            letraMaius = True
        elif char.islower():
            letraMinus = True
        elif char.isdigit():
            digito = True
        elif not char.isalnum():
            especial = True

    if tamMin: pontuacao += 1
    if letraMaius: pontuacao += 2
    if letraMinus: pontuacao += 2
    if digito: pontuacao += 3
    if especial: pontuacao += 4

    return pontuacao, tamMin, letraMaius, letraMinus, digito, especial

def exibir_criterios(pontuacao):
    print("\nCritérios atendidos: ")
    if pontuacao[1]:
        print(f"- Tamanho mínimo (6) atendido")
    if pontuacao[2]:
        print(f"- A senha possui letras maiúsculas")
    if pontuacao[3]:
        print(f"- A senha possui letras minúsculas")
    if pontuacao[4]:
        print(f"- A senha possui dígitos")
    if pontuacao[5]:
        print(f"- A senha possui caracteres especiais")
    
    print("\nCritérios não atendidos: ")
    if not pontuacao[1]:
        print(f"- Tamanho mínimo (6) não atendido")
    if not pontuacao[2]:
        print(f"- A senha não possui letras maiúsculas")
    if not pontuacao[3]:
        print(f"- A senha não possui letras minúsculas")
    if not pontuacao[4]:
        print(f"- A senha não possui dígitos")
    if not pontuacao[5]:
        print(f"- A senha não possui caracteres especiais")

if __name__=="__main__":
    senha = input("Digite a senha: ")
    pontuacao = calcPontuacao(senha, min=6)

    print(f"\nPontuação: {pontuacao[0]}")
    print("Classificação: ", end="")
    
    if pontuacao[0] >= 9:
        print("Senha forte")
    elif pontuacao[0] >= 5:
        print("Senha média")
    else:
        print("Senha fraca")
    
    exibir_criterios(pontuacao)
    

        