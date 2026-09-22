def lerMatricula():
    while True:
        matri = input("Matrícula do aluno: ")
        if not matri.isnumeric():
            print("Matrícula deve conter apenas números")
        else: break
    return matri

def lerNome():
    while True:
        nome = input("Nome do aluno: ").lower()
        if not nome.isalpha():
            print("Nome deve conter apenas letras")
        else: break
    return nome

def lerTelefone():
    while True:
        telefone  = input("Telefone do aluno: ")
        if not telefone.isnumeric():
            print("Telfeone deve conter apenas números")
        else: break
    return telefone

def cadastrar_aluno(alunos):
    matricula = lerMatricula()
    nome  = lerNome()
    telefone  = lerTelefone()
    curso  = input("Curso do aluno: ").lower()
    if matricula not in alunos:
        alunos[matricula] = {"nome": "", "telefone": "", "curso": ""}
        alunos[matricula]["nome"] = nome
        alunos[matricula]["telefone"] = telefone
        alunos[matricula]["curso"] = curso
        return True
    else:
        return False

def buscar_aluno(alunos):
    matricula = lerMatricula()
    if matricula in alunos:
        print("--------------------------------------")
        print(f"- Nome: {alunos[matricula]['nome']}")
        print(f"- Telefone: {alunos[matricula]['telefone']}")
        print(f"- Curso: {alunos[matricula]['curso']}")
        return True
    else:
        return False

def listar_alunos(alunos):
    if len(alunos) == 0:
        return False
    else:
        for matri in alunos:
            print("--------------------------------------")
            print(f"Matrícula: {matri}")
            print(f"- Nome: {alunos[matri]['nome']}")
            print(f"- Telefone: {alunos[matri]['telefone']}")
            print(f"- Curso: {alunos[matri]['curso']}")
        return True

def remover_aluno(alunos):
    matricula = lerMatricula()
    if matricula in alunos:
        alunos.pop(matricula)
        return True
    else:
        return False

def alterar_aluno(alunos):
    matricula = lerMatricula()
    
    if matricula in alunos:
        novoNome = lerNome()
        novoTelefone  = lerTelefone()
        novoCurso  = input("Curso do aluno: ").lower()
        alunos[matricula]["nome"] = novoNome
        alunos[matricula]["telefone"] = novoTelefone
        alunos[matricula]["curso"] = novoCurso
        return True
    else:
        return False

if __name__ == "__main__":
    menu = '''--------------------------------------
1. Cadastrar aluno 
2. Buscar aluno por matrícula 
3. Listar todos os alunos 
4. Remover aluno 
5. Encerrar
6. Alterar dados de um aluno
--------------------------------------
Opção: '''

    alunos = {}
    while True:
        opcao = input(menu)

        if opcao == '1':
            if cadastrar_aluno(alunos):
                print("Cadastro realizado com sucesso")
            else:
                print("Matricula ja cadastrado")

        elif opcao == "2":
            if not buscar_aluno(alunos):
                print("Matrícula não encontrada")

        elif opcao == "3":
            if not listar_alunos(alunos):
                print("Não há alunos cadastrados")

        elif opcao == "4":
            if remover_aluno(alunos):
                print("Aluno removido")
            else:
                print("Matrícula não cadastrada")

        elif opcao == "5":
            break

        elif opcao == "6":
            if alterar_aluno(alunos):
                print("Dados do aluno alterados com sucesso")
            else:
                print("Matrícula não cadastrada")

        else:
            print("Escolha uma opção válida")