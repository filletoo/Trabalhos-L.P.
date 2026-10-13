import random
import os
import sys

'''Retorna se uma string é vazia (não tem nada ou
é só espaços em branco)'''
def str_vazia(texto: str):
    return texto == '' or texto.isspace()

'''Exceção para caso nenhuma palavra tenha sido encontrada no arquivo'''
class ZeroPalavrasEncontradas(Exception):
    def __init__(self, arquivo):
        super().__init__(f"Nenhuma palavra pôde ser encontrada em '{arquivo}'")

'''Exceção para caso a escolha do usuário seja inválida
(digitou um número ou mais de uma letra, por exemplo)'''
class EscolhaInvalida(Exception):
    def __init__(self, escolha):
            super().__init__(f"'{escolha}' não é uma escolha válida")

'''Exceçao para caso seja tentada uma letra ja tentada anteriormente'''
class LetraJaTentada(Exception):
    def __init__(self, letra):
            super().__init__(f"'{letra}' já foi tentada anteriormente")

'''Exceção para caso seja tentada uma nova letra
depois do jogo já ter acabado. Apenas por boa prática,
já que não é possível isso acontecer no main por conta
da opção de tentar de novo'''
class JogoJaAcabou(Exception):
    def __init__(self):
            super().__init__(f"O jogo já terminou")

'''Classe que irá gerenciar o jogo'''
class JogoForca:
    '''Muitos atributos e métodos são privados para evitar que,
    por exemplo, o usuário da classe mude a palavra secreta no 
    meio do jogo e provoque um comportamento inesperado'''

    '''Estagios da forca, atributo de classe. Público para que 
    possam ser personalizaveis os estágios'''
    ESTAGIOS_FORCA = [
    """
    +---+
    |   |
        |
        |
        |
        |
=========""",
    """
    +---+
    |   |
    O   |
        |
        |
        |
=========""",
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
=========""", 
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========""",
    """
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
=========""",
    """
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
=========""",
    """
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
=========""",
    ]

    '''Variantes de algumas letras, como as acentuadas, para deixar o jogo mais
    flexível, permitindo o uso de palavras com elas mas sem exigir do jogador que
    as digite especificamente'''
    __letras_correspondentes = {
        'a': "aàáãâä",
        'e': "eèéêë",
        'i': "iìíîï",
        'o': "oòóõôö",
        'u': "uùúûü",
        'c': "cç"
    }
    
    def __init__(self, arquivo_palavras: str):
        self.__palavras = self.carregar_palavras(arquivo_palavras)

        self.__vidas = len(JogoForca.ESTAGIOS_FORCA) - 1
        self.__letras_erradas = []
        self.__letras_tentadas = set()

        self.__palavra_secreta = ""
        self.__palavra_oculta = []
        self.__escolher_palavra()

    '''Carregar o arquivo de palavras'''
    def carregar_palavras(self, arquivo: str):
        palavras = []
        
        with open(arquivo, mode='r', encoding='utf-8') as f:
            while True:
                palavra = f.readline()
                '''Checar se chegou no final do arquivo'''
                if palavra == '':
                    break
                
                '''Checar se a linha é vazia e passar para a próxima caso sim'''
                if str_vazia(palavra):
                    continue

                '''Verifica se há pelo menos uma letra na palavra,
                passar para a próxima linha caso não'''
                tem_letra = False
                for c in palavra:
                    if c.isalpha():
                        tem_letra = True
                        break

                if not tem_letra:
                    continue

                '''Remover espaços em branco e converter para minúsculas'''
                palavra = palavra.strip().lower()

                palavras.append(palavra)

        if len(palavras) == 0:
            raise ZeroPalavrasEncontradas(arquivo)
        
        return palavras

    '''Escolher a palavra do jogo'''
    def __escolher_palavra(self):
        '''Escolhe uma palavra aleatória dentre as do arquivo'''
        self.__palavra_secreta = random.choice(self.__palavras)
        '''Cria-se, primeiramente, a palavra oculta como sendo completamente oculta'''
        self.__palavra_oculta = ['_']*len(self.__palavra_secreta)

        '''Revelar os caracteres especiais, ou seja, os que não são letras,
        como espaços, hífens e números'''
        for i in range(len(self.__palavra_secreta)):
            if not (self.__palavra_secreta[i].isalpha()):
                self.__palavra_oculta[i] = self.__palavra_secreta[i]

    '''Limpa a tela, adequando o comando com base no sistema operacional:
    'cls' caso seja Windows, 'clear' caso seja Mac ou Linux'''
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    '''Exibir o jogo'''
    def exibir_estado(self):
        '''Limpar a tela'''
        self.limpar_tela()

        '''Mostrar o estágio da forca, baseado na quantidade de erros'''
        estagio = JogoForca.ESTAGIOS_FORCA[len(self.__letras_erradas)]
        print(estagio)

        '''Mostrar a palavra oculta'''
        print(f"Palavra: ", end="")
        for c in self.__palavra_oculta:
            print(c, end=" ")

        '''Vidas restantes'''
        print(f"\nVidas restantes: {self.__vidas}")

        '''Letras que já foram escolhidas mas estavam erradas'''
        print(f"Letras erradas: ", end="")
        for i in range(len(self.__letras_erradas)):
            print(self.__letras_erradas[i], end="")
            if i != len(self.__letras_erradas) - 1:
                print(",", end="")

        print()

        '''Checar e imprimir a condição do jogo, ou seja, se o jogador ganhou, perdeu
        ou ainda nenhum dos dois (jogo continua)'''
        condicao = self.checar_condicao()
        if condicao == -1:
            print("\nVocê perdeu!")
            print(f"A palavra era: {self.__palavra_secreta}")

        elif condicao == 1:
            print("\nParabéns!")
            print("Você ganhou!")

    '''Valida a escolha, permitindo apenas letras únicas'''
    def validar_input(self, escolha: str):
        '''Remove espaços extras no inicio e fim'''
        escolha = escolha.strip().lower()

        '''Retorna falso se não for uma letra ou tiver mais de um caractere'''
        if not escolha.isalpha() or len(escolha) != 1:
            return False

        return True

    '''Analisa e processa uma nova escolha de letra'''
    def atualizar_jogo(self, escolha: str):
        '''Não testa uma escolha nova caso o jogo ja tenha acabado'''
        if self.checar_condicao() != 0:
            raise JogoJaAcabou

        '''Remove espaços extras no inicio e fim e transforma em minúsculo'''
        escolha = escolha.strip().lower()

        '''Caso a escolha não seja válida, joga a exceção correspondente
        para que o usuário da classe decida como lidar com isso'''
        if self.validar_input(escolha):

            '''Caso a letra digitada seja uma variação de alguma outra, transforma nessa
            versão padrão, para facilitar a validação e processamento da entrada'''
            for letra, correspondentes in self.__letras_correspondentes.items():
                if escolha in correspondentes:
                    escolha = letra

            '''Se a letra ja foi tentada, joga a exceção correspondente,
            para que o usuário da classe decida como lidar com isso'''
            if not (escolha in self.__letras_tentadas):
                existe = False

                '''Testa se a escolha é igual a cada letra da palavra secreta, revelando
                também as variantes (com acentos)'''
                for i in range(len(self.__palavra_secreta)):
                    '''Revela a letra se a escolha for igual o caractere da palavra secreta
                    ou se esse caractere está na lista de variantes da escolha'''
                    if (escolha == self.__palavra_secreta[i]) or (self.__palavra_secreta[i] in self.__letras_correspondentes.get(escolha, "")):
                        self.__palavra_oculta[i] = self.__palavra_secreta[i]
                        existe = True

                '''Caso a escolha não exista na palavra secreta, diminui a vida e a adiciona
                nas letras erradas'''
                if not existe:
                    self.__vidas -= 1
                    self.__letras_erradas.append(escolha)

                '''Adiciona a escolha nas letras ja tentadas'''
                self.__letras_tentadas.add(escolha)
            else:
                raise LetraJaTentada(escolha)
        else:
            raise EscolhaInvalida(escolha)

    '''Checa a condição atual do jogo 
    [vitória (1), derrota (-1) ou ainda nenhum dos dois (0)]'''
    def checar_condicao(self):
        if self.__vidas <= 0:
            '''Caso não tenha vida, retorna derrota'''
            return -1

        elif not ('_' in self.__palavra_oculta):
            '''Caso tenha vida e não exista mais letra para se revelar,
            retorna vitória'''
            return 1

        else:
            '''Retorna que o jogo deve continuar'''
            return 0

    '''Reseta o jogo, para que o usuário da classe não precise instanciar
    um novo objeto'''
    def resetar(self):
        self.__vidas = len(JogoForca.ESTAGIOS_FORCA) - 1

        self.__escolher_palavra()
        self.__letras_erradas = []
        self.__letras_tentadas = set()

    '''Métodos get para permitir ao usuário acessar os
    atributos diretamente sem poder alterá-los'''
    def getPalavras(self):
        return self.__palavras

    def getVidas(self):
        return self.__vidas

    def getLetrasErradas(self):
        return self.__letras_erradas

    def getLetrasTentadas(self):
        return self.__letras_tentadas

    def getPalavraSecreta(self):
        return self.__palavra_secreta

    def getPalavraOculta(self):
        return self.__palavra_oculta

def main():
    arquivo_palavras = "palavras.txt"

    '''Tratamento para caso o arquivo não exista ou não tenha palavras, fechando o programa 
    em ambos os casos. Feito com tratamento de exceção para que o usuário da classe tenha 
    liberdade de decisão sobre o que fazer'''
    try:
        Forca = JogoForca(arquivo_palavras)

    except FileNotFoundError:
        print(f"'{arquivo_palavras}' não pode ser encontrado")
        sys.exit()

    except ZeroPalavrasEncontradas:
        print(f"Nenhuma palavra pôde ser encontrada em '{arquivo_palavras}'")
        sys.exit()

    except:
        '''Caso default para quando algo inesperado ocorrer'''
        print("Um erro inesperado ocorreu")
        sys.exit()

    '''Loop do jogo'''
    mensagem = ""
    while True:
        '''Checa para ver se o jogo já acabou e se deve continuar'''
        condicao = Forca.checar_condicao()
  
        if condicao != 0:
            Forca.exibir_estado()

            '''Pergunta se um novo jogo deve ser iniciado'''
            while True:
                continuar = input("\nDeseja tentar de novo? (s/n): ").strip().lower()
                if continuar not in ['s', 'n']:
                    print("Escolha uma opção válida")
                else:
                    break
            if continuar == 'n':
                break
            else:
                Forca.resetar()
                continue

        '''Exibe a forca junto com uma mensagem ao usuário, 
        que depende de seu input anterior'''
        Forca.exibir_estado()

        if mensagem:
            print('\n' + mensagem)

        try:
            letra = input("\nDigite uma letra: ")
            Forca.atualizar_jogo(letra)
            mensagem = ""

        except KeyboardInterrupt, EOFError:
            '''Caso o usuário digite algo inválido, como Ctrl+C'''
            mensagem = "Digite uma entrada válida"

        except EscolhaInvalida:
            '''Caso o usuário digite algo inválido, como mais de uma letra ou um número'''
            mensagem = "Escolha inválida"

        except LetraJaTentada:
            '''Caso o usuário digite algo que já foi tentado'''
            mensagem = "Essa letra já foi tentada antes"

        except:
            '''Caso default para quando algo inesperado ocorrer'''
            print("Um erro inesperado ocorreu")
            sys.exit()

'''__name__ usado para que o main só execute quando esse arquivo
for executado diretamente, ou seja, essa parte funciona como um teste
da implementação da classe e não executará quando esse arquivo for
importado como módulo'''
if __name__ == '__main__':
    main()