import re

'''Remove os espaços no inicio e no fim de uma string,
para que a leitura de inputs seja mais flexível'''
def remover_espacos(texto: str):
    return texto.strip()

'''Indica se a string é vazia, ou seja, se não tem elementos
ou é só espaços em branco'''
def str_vazia(texto):
    return texto == '' or texto.isspace()

'''Checa se a agenda está vazia'''
def agenda_vazia(agenda):
    return len(agenda) == 0

'''Pega uma linha do arquivo csv e retorna uma lista 
já com os campos separados'''
def pegar_linha_csv(arquivo):
    return arquivo.readline().strip('\n').split(',')

'''Carregamento e salvamento do arquivo .csv'''
def carregar_csv(arquivo):
    agenda = {}
    cabecalho = ['nome', 'telefones', 'rua', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado']

    '''Checa se o arquivo .csv existe primeiramente,
    retornando uma agenda vazia caso não'''
    try:
        with open(arquivo, 'r') as f:
            '''Checa se o cabeçalho existe igual ao esperado.
            Retorna uma agenda vazia caso não'''
            cabecalho_arquivo = pegar_linha_csv(f)

            if cabecalho_arquivo != cabecalho:
                print(f"{arquivo} não contém um cabeçalho ou sua formatação não está como esperada,\numa agenda vazia será criada e poderá sobrescrever o arquivo")
                return agenda

            '''Lê linha por linha, separando os campos e salvando na agenda'''
            while True:
                linha = f.readline()
                '''Checa se não há mais nada para ler'''
                if linha == '':
                    break

                '''Separa os campos e salva no dicionário'''
                linha = linha.strip('\n').split(',')
                '''Se a linha não tem todos os campos, ignora e passa para a próxima
                (linha vazia, por exemplo)'''
                if len(linha) != 9:
                    continue

                nome = linha[0]
                agenda[nome] = {}

                telefones = linha[1].split('|')
                agenda[nome]['telefones'] = telefones

                agenda[nome]['endereco'] = {}
                agenda[nome]['endereco']['rua'] = linha[2]
                agenda[nome]['endereco']['numero'] = linha[3]
                agenda[nome]['endereco']['complemento'] = linha[4]
                agenda[nome]['endereco']['bairro'] = linha[5]
                agenda[nome]['endereco']['cep'] = linha[6]
                agenda[nome]['endereco']['cidade'] = linha[7]
                agenda[nome]['endereco']['estado'] = linha[8]

    except FileNotFoundError:
        print(f"{arquivo} não encontrado, uma agenda vazia será criada")
    
    return agenda

def salvar_csv(agenda, arquivo):
    cabecalho = ['nome', 'telefones', 'rua', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado']

    '''Como a aplicação lê e escreve do mesmo arquivo, o salvamento salva a agenda do zero,
    para evitar repetições de contatos'''
    with open(arquivo, mode='w') as f:
        '''Escreve o cabeçalho'''
        for i in range(len(cabecalho)):
            f.write(cabecalho[i])
            if i != len(cabecalho) - 1:
                f.write(',')

        '''Guarda os campos de cada contato numa lista, depois 
        escreve eles separados por vírgula no .csv'''
        for nome in agenda:
            linha = []
            linha.append(nome)

            telefones = agenda[nome]['telefones']
            campo_tel = ""
            for i in range(len(telefones)):
                if i != len(telefones) - 1:
                    campo_tel += telefones[i] + '|'
                else:
                    campo_tel += telefones[i]
            linha.append(campo_tel)

            endereco = agenda[nome]['endereco']

            linha.append(endereco['rua'])
            linha.append(endereco['numero'])
            linha.append(endereco['complemento'])
            linha.append(endereco['bairro'])
            linha.append(endereco['cep'])
            linha.append(endereco['cidade'])
            linha.append(endereco['estado'])

            f.write('\n')
            for i in range(len(linha)):
                f.write(linha[i])
                if i != len(linha) - 1:
                    f.write(',')

'''Verifica se o CEP tem o formato adequado, em que 'd' representa
onde deve haver um número'''
def validar_cep(cep, formato):
    if len(cep) != len(formato):
        return False

    for i in range(len(formato)):
        if (formato[i] == 'd') and (not cep[i].isnumeric()):
            return False
        elif formato[i] == '-' and cep[i] != '-':
            return False

    return True

'''Funções de ler as entradas do usuário, com um parâmetro que determina
se elas devem aceitar entradas vazias, para casos como o da edição de contatos'''
def ler_cep(permitir_vazio=False):
    formato = 'ddddd-ddd'
    while True:
        cep = remover_espacos(input(f"*CEP ({formato}): "))
        '''Permite uma entrada vazia caso o parâmetro em questão seja True'''
        if str_vazia(cep) and permitir_vazio:
            break
        
        if validar_cep(cep, formato):
            break
        else:
            print("Formato do CEP inválido.")

    return cep

'''O parâmetro 'quant', quando igual a -1, indica que deve ser perguntado
ao usuário quantos telefones ele deseja adicionar. Quando igual qualquer outro valor,
indica que dever ser lidos aquela quantidade de telefones. Usado no processo de editar contato
para editar apenas os contatos já existentes'''
def ler_telefones(permitir_vazio=False, quant=-1):
    telefones = []
    if quant == -1:
        while True:
            n = input("Quantos telefones deseja adicionar?: ")
            try:
                n = int(n)
                if n <= 0:
                    print("Digite um número inteiro maior que 0")
                else:
                    break
            except ValueError:
                print("Digite um número inteiro")

    else:
        n = quant

    for i in range(n):
        while True:
            tel = remover_espacos(input(f"Telefone {i + 1}*: "))
            if str_vazia(tel) and not permitir_vazio:
                print("Campo não deve ser vazio")
            else:
                break
        telefones.append(tel)

    return telefones

'''Além da validação padrão, valida se é numérico'''
def ler_numero(permitir_vazio=False):
    while True:
        numero = remover_espacos(input("*Numero: "))
        if str_vazia(numero) and not permitir_vazio:
            print("Número não pode ser vazio")
        
        elif not permitir_vazio and not numero.isnumeric():
            print("O campo deve ser um número positivo")
        else:
            break

    return numero

'''Lê uma entrada mais geral, sem condições ou 
tratamentos diferentes, como o CEP e os telefones'''
def ler_input_geral(msg, permitir_vazio=False):
    while True:
        campo = remover_espacos(input(msg))
        if str_vazia(campo) and not permitir_vazio:
            print("Campo não pode ser vazio")
        else:
            break

    return campo

'''Lê o endereço utilizando as funções acima'''
def ler_endereco(permitir_vazio=False):
    endereco = {}
    rua = ler_input_geral("*Rua: ", permitir_vazio)
    numero = ler_numero(permitir_vazio)
    complemento = ler_input_geral("Complemento: ", True)
    bairro = ler_input_geral("*Bairro: ", permitir_vazio)
    cep = ler_cep(permitir_vazio)
    cidade = ler_input_geral("*Cidade: ", permitir_vazio)
    estado = ler_input_geral("*Estado/UF: ", permitir_vazio).upper()

    endereco['rua'] = rua
    endereco['numero'] = numero
    endereco['complemento'] = complemento
    endereco['bairro'] = bairro
    endereco['cep'] = cep
    endereco['cidade'] = cidade
    endereco['estado'] = estado

    return endereco

'''Realiza o cadastro de um novo contato, utilizando as funções
anteriores. Retorna se o cadastro deu certo ou não
(quando o nome já está cadastrado)'''
def cadastro(agenda):
    nome = ler_input_geral("*Nome: ")
    if nome in agenda:
        return False
    
    telefones = ler_telefones()
    endereco = ler_endereco()

    agenda[nome] = {}
    agenda[nome]['telefones'] = telefones
    agenda[nome]['endereco'] = endereco
    return True

'''Exibe um único contato'''
def exibir_contato(nome, agenda):
    contato = agenda[nome]
    print(f"--Nome: {nome}")

    print("--Telefones: ")
    for i in range(len(contato['telefones'])):
        print(f"  -Telefone {i + 1}: {contato['telefones'][i]}")

    endereco = contato['endereco']
    print("--Endereco: ")
    print(f"  -Rua: {endereco['rua']}")
    print(f"  -Número: {endereco['numero']}")
    print(f"  -Complemento: {endereco['complemento']}")
    print(f"  -Bairro: {endereco['bairro']}")
    print(f"  -CEP: {endereco['cep']}")
    print(f"  -Cidade: {endereco['cidade']}")
    print(f"  -Estado: {endereco['estado']}")

'''Exibe todos os contatos, chamando
a função 'exibir_contato' para todos eles'''
def exibir_todos_contatos(agenda):
    for nome in agenda:
        exibir_contato(nome, agenda)
        print()

'''Busca contatos na agenda com um certo nome, sem precisar ser o nome completo
e sendo case-insenstive. Retorna um dicionário com os contatos encontrados'''
def buscar_nome(nome, agenda):
    contatos_buscados = {}
    for n in agenda:
        if nome in n.lower():
            contatos_buscados[n] = agenda[n]
    
    return contatos_buscados

'''Busca contatos na agenda com um certo telefone.
Retorna um dicionário com os contatos encontrados'''
def buscar_telefone(tel, agenda):
    contatos_buscados = {}
    for nome in agenda:
        if tel in agenda[nome]['telefones']:
            contatos_buscados[nome] = agenda[nome]
    
    return contatos_buscados

'''Realiza a edição de contatos, utilizando o parâmetro 'permitir_vazio'
das funções de leitura de entrada para que o usuário possa deixar o campo em branco'''
def editar_contato(nome, agenda):
    '''Novo nome, aceita que seja o mesmo também, não aceita um que já exista'''
    while True:
        novo_nome = remover_espacos(ler_input_geral("*Nome: ", permitir_vazio=True))
        if novo_nome not in agenda or novo_nome == nome:
            break
        else:
            print("Um contato com esse nome já existe")
    
    novos_tel = ler_telefones(permitir_vazio=True, quant=len(agenda[nome]['telefones']))
    novo_endereco = ler_endereco(permitir_vazio=True)

    for i in range(len(novos_tel)):
        if not str_vazia(novos_tel[i]):
             agenda[nome]['telefones'][i] = novos_tel[i]

    for chave in novo_endereco:
        if not str_vazia(novo_endereco[chave]):
            agenda[nome]['endereco'][chave] = novo_endereco[chave]

    '''Caso seja editado o nome, cria-se uma nova chave com o mesmo valor da anterior
    e deleta-se a anterior'''
    if not str_vazia(novo_nome):
        agenda[novo_nome] = agenda.pop(nome)

if __name__ == '__main__':
    arquivo_csv = "agenda_contatos.csv"

    menu = '''-------------------------------------
1 - Cadastrar contato
2 - Listar contatos
3 - Busca parcial por nome
4 - Busca parcial por telefone
5 - Editar contato
6 - Remover contato
7 - Salvar contatos
8 - Sair
-------------------------------------
Opção: '''

    '''Carrega a agenda num dicionário a partir do arquivo csv'''
    agenda = carregar_csv(arquivo_csv)

    while True:
        opcao = input(menu)
        print()
        
        if opcao == '1':
            '''Realiza o cadastro e indica se o nome já está cadastrado'''
            
            print("'*' indica um campo obrigatório")
            if cadastro(agenda):
                print("Cadastro realizado")
            else:
                print("Nome já cadastrado")

        elif opcao == '2':
            '''Exibe todos os contatos, exceto quando não há nenhum na agenda'''
            
            if agenda_vazia(agenda):
                print("A agenda está vazia")
            else:
                exibir_todos_contatos(agenda)

        elif opcao == '3':
            '''Busca um nome quando a agenda não está vazia'''
            
            if agenda_vazia(agenda):
                print("A agenda está vazia")
            else:
                nome = remover_espacos(input("Nome buscado: ").lower())
                nomes_buscados = buscar_nome(nome, agenda)

                if len(nomes_buscados) == 0:
                    print("Ninguém com este nome foi encontrado na lista de contatos")
                else:
                    print(f"\n{len(nomes_buscados)} Contato(s) encontrados")
                    exibir_todos_contatos(nomes_buscados)

        elif opcao == '4':
            '''Busca um telefone quando a agenda não está vazia'''
            
            if agenda_vazia(agenda):
                print("A agenda está vazia")
            else:
                tel = remover_espacos(input("Telefone buscado: ").lower())
                tel_buscados = buscar_telefone(tel, agenda)

                if len(tel_buscados) == 0:
                    print("Ninguém com este telefone foi encontrado na lista de contatos")
                else:
                    print(f"\n{len(tel_buscados)} Contato(s) encontrados")
                    exibir_todos_contatos(tel_buscados)

        elif opcao == '5':
            '''Edita um contato quando a agenda não está vazia e caso exista'''
            
            if agenda_vazia(agenda):
                print("A agenda está vazia")
            else:
                print("Deixe o campo vazio para não alterar o valor original")
                nome = input("Nome do contato: ")
                if nome in agenda:
                    editar_contato(nome, agenda)
                else:
                    print("Contato não encontrado")

        elif opcao == '6':
            '''Remove um contato quando a agenda não está vazia e caso exista'''
            
            if agenda_vazia(agenda):
                print("A agenda está vazia")
            else:
                nome = input("Nome do contato que deseja remover: ")
                if nome in agenda:
                    while True:
                        escolha = input("Tem certeza que deseja realizar a remoção?(s/n): ").lower()
                        if escolha in ['s', 'n']:
                            break
                        else:
                            print("Escolha uma opção válida")

                    if escolha == 's':
                        agenda.pop(nome)
                        print("Contato excluído com sucesso")
                else:
                    print("Contato não encontrado")

        elif opcao == '7':
            '''Salva a agenda em csv'''
            salvar_csv(agenda, arquivo_csv)
            print("Agenda salva")

        elif opcao == '8':
            break

        else:
            print("Escolha uma opção válida")

    '''Salva a agenda em csv quando o programa termina'''
    salvar_csv(agenda, arquivo_csv)
    print("Agenda salva")