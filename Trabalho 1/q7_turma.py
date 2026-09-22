def cadastrar_alunos():
    alunos = {}
    while True:
        nome = input("\nNome do aluno: ").lower()
        if nome == "0":
            break

        if nome in alunos:
            while True:
                opcao = input("Aluno já cadastrado. Deseja mudar as notas dele? (s/n): ").lower()
                if opcao not in "sn":
                    print("Escolha uma opção válida")
                    continue
                break
            if opcao == "n":
                continue    
                    
        alunos[nome] = []
        i = 0
        while i < 3: 
            nota = input(f"Digite a nota {i + 1} do aluno: ")
            try:
                nota = float(nota)
                if nota >= 0 and nota <= 10:
                    alunos[nome].append(nota)
                    i += 1
                else:
                    print("A nota deve estar entre 0 e 10")
            except:
                print("A nota deve ser um número real")
        
    return alunos

def registrar_situacao_alunos(alunos, medias):
    alunos = dict(sorted(alunos.items(), key=lambda x: sum(x[1]), reverse=True))
    aprovados = 0
    for nome in alunos:
        soma = 0
        print(f"Aluno {nome}:")
        for i in range(3):
            soma += alunos[nome][i]
            print(f"- Nota {i + 1}: {alunos[nome][i]}")

        media = soma/3
        medias.append(media)
        print(f"- Media: {media:.2f}")
        print("- Situação: ", end="")
        if media >= 7:
            print("Aluno aprovado")
            aprovados += 1
        elif media >= 4:
            print("Aluno de recuperação")
        else:
            print("Aluno reprovado")
        print("-----------------------------------------")

    return aprovados

if __name__ == "__main__":
    medias = []
    print("Digite '0' para parar os cadastros")
    alunos = cadastrar_alunos()
    print()

    if len(alunos) > 0:
        aprovados = registrar_situacao_alunos(alunos, medias)
        
        media_geral = sum(medias)/len(medias)
        maior_media = max(medias)
        menor_media = min(medias)
        percentual_aprov = aprovados/len(alunos)*100

        print(f"- Média geral da turma: {media_geral:.2f}")
        print(f"- Maior média da turma: {maior_media:.2f}")
        print(f"- Menor média da turma: {menor_media:.2f}")
        print(f"- Percentual de alunos aprovados da turma: %{percentual_aprov:.2f}")
    else:
        print("Nenhum aluno foi cadastrado")
