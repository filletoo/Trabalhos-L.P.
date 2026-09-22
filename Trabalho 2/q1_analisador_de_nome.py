def remover_espacos_extremidades(nome):
    nome = nome.split()
    nome_sem_espaco = ""
    for i in range(len(nome) - 1):
        nome_sem_espaco += nome[i] + " "

    nome_sem_espaco += nome[len(nome) - 1]
    return nome_sem_espaco

def contar_char_sem_espaco(nome):
    quant = 0
    for i in nome:
        if i != " ": quant += 1

    return quant

if __name__ == "__main__":
    nome = input("Digite seu nome completo:\n")
    nome_separado = nome.split()
    nome = remover_espacos_extremidades(nome)
    quant_char = contar_char_sem_espaco(nome)
    quant_pal = len(nome_separado)
    
    print("------------------------------------------------------------")
    print(f"- Nome sem espaços extras: {nome}")
    print(f"- Nome em letras maiúsculas: {nome.upper()}")
    print(f"- Nome em letras minúsculas: {nome.lower()}")
    print(f"- Quantidade de caracteres, desconsiderando espaços: {quant_char}")
    print(f"- Quantidade de palavras no nome: {quant_pal}")
    print(f"- Primeiro nome: {nome_separado[0]}")
    print(f"- Último nome: {nome_separado[-1]}")
    print("------------------------------------------------------------")