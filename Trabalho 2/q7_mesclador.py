def ler_nomes(arquivo):
    nomes = []
    try: 
        with open(arquivo, mode="r") as f:
            linha = "ç"
            while linha != "":
                linha = f.readline()
                if linha == "": break

                if not linha.isspace():
                    nomes.append(remover_espacos_extremidades(linha))

    except FileNotFoundError:
        return False

    return nomes

def escreverNomes(arquivo, lista):
    with open(arquivo, mode="w") as f:
        for n in lista:
            f.write(n + '\n')

def remover_espacos_extremidades(nome):
    nome = nome.split()
    nome_sem_espaco = ""
    for i in range(len(nome)):
        if i != len(nome) - 1:
            nome_sem_espaco += nome[i] + " "
        else:
            nome_sem_espaco += nome[i]

    return nome_sem_espaco

def remover_duplicatas_e_ordenar(nomes_a, nomes_b):
    lista_final = set()
    for n in nomes_a:
        lista_final.add(n)

    for n in nomes_b:
        lista_final.add(n) 

    lista_final = list(lista_final)
    lista_final.sort()

    return lista_final

if __name__ == "__main__":
    nomes_a = ler_nomes("lista_a.txt")
    nomes_b = ler_nomes("lista_b.txt")

    if (type(nomes_a) == bool and not nomes_a) or (type(nomes_b) == bool and not nomes_b):
        print("Não foi possível encontrar algum ou ambos os arquivos")
    else:
        lista_final = remover_duplicatas_e_ordenar(nomes_a, nomes_b)
        
        escreverNomes("lista_final.txt", lista_final)

        print("--------------------------------------------------------------------------")
        print(f'Quantidade de nomes no arquivo "lista_a.txt": {len(nomes_a)}')
        print(f'Quantidade de nomes no arquivo "lista_b.txt": {len(nomes_b)}')
        print(f'Quantidade de nomes distintos na lista final : {len(lista_final)}')
        print("--------------------------------------------------------------------------")