def remover_espacos_extremidades(nome):
    nome = nome.split()
    nome_sem_espaco = ""
    for i in range(len(nome) - 1):
        nome_sem_espaco += nome[i] + " "

    nome_sem_espaco += nome[len(nome) - 1]
    return nome_sem_espaco

def cadastrarNomes():
    print('Digite "sair" quando terminar de digitar nomes')
    nomes = []

    while True:
        nome = input("Digite um nome: ")
        print(nome)
        if nome.lower() == "sair":
            break
        if nome != '':
            #ver se adiciona o removedor de espacos dps
            nomes.append(remover_espacos_extremidades(nome))

    #print(nomes)
    if len(nomes) == 0:
        return False
    else:
        with open("nomes.txt", mode="w") as f:
            for i in range(len(nomes)):
                if i != len(nomes) - 1:
                    f.write(nomes[i] + '\n')
                else:
                    f.write(nomes[i])
            
        return True

def maiores_nomes(nomes):
    pal_maior_tam = remover_espacos_extremidades(nomes[0]) #palavra de maior tamanho
    maiores = []

    for n in nomes:
        n = remover_espacos_extremidades(n)

        if len(n) > len(pal_maior_tam):
            pal_maior_tam = n

    for n in nomes:
        n = remover_espacos_extremidades(n)

        if len(n) == len(pal_maior_tam):
            maiores.append(n)
        
    return maiores

if cadastrarNomes():
    with open("nomes.txt", mode="r") as f:
        nomes = f.read()

    nomes = nomes.split('\n')

    maiores = maiores_nomes(nomes)

    print("Nomes cadastrados:")
    for n in nomes:
        print(f"- {n}")

    print(f"\nQuantidade de nomes: {len(nomes)}")
    print(f"\nMaiores nomes (tamanho {len(maiores[0])}):")
    for n in maiores:
        print(f"- {n}")
    
else:
    print("Nenhum nome foi cadastrado.")   

print()