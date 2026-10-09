import random
import os
import sys

def str_vazia(texto: str):
    return texto == '' or texto.isspace()

class ZeroPalavrasEncontradas(Exception):
    def __init__(self, arquivo):
        super().__init__(f"Nenhuma palavra pôde ser encontrada em '{arquivo}'")

class EscolhaInvalida(Exception):
    def __init__(self, letra):
            super().__init__(f"'{letra}' não é uma escolha válida'")

class LetraJaTentada(Exception):
    def __init__(self, letra):
            super().__init__(f"'{letra}' já foi tentada anteriormente")

class JogoForca:
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

    letras_correspondentes = {
        'a': "àáãâä",
        'e': "èéêë",
        'i': "ìíîï",
        'o': "òóõôö",
        'u': "ùúûü",
        'c': "ç"
    }
    
    def __init__(self, arquivo_palavras: str):
        self.palavras = self.carregar_palavras(arquivo_palavras)

        self.vidas = len(JogoForca.ESTAGIOS_FORCA) - 1
        self.letras_erradas = []
        self.letras_tentadas = set()

        self.palavra_secreta = ""
        self.palavra_oculta = []
        self.escolher_palavra()

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

                '''Remover espaços em branco e converter para minúsculas'''
                palavra = palavra.strip().lower()

                palavras.append(palavra)

        if len(palavras) == 0:
            raise ZeroPalavrasEncontradas(arquivo)
        
        return palavras

    def escolher_palavra(self):
        self.palavra_secreta = random.choice(self.palavras)
        self.palavra_oculta = ['_']*len(self.palavra_secreta)

        for i in range(len(self.palavra_secreta)):
            if not (self.palavra_secreta[i].isalpha()):
                self.palavra_oculta[i] = self.palavra_secreta[i]
    
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def exibir_estado(self):
        self.limpar_tela()

        estagio = JogoForca.ESTAGIOS_FORCA[len(self.letras_erradas)]
        print(estagio)
        print(f"Palavra: ", end="")
        for c in self.palavra_oculta:
            print(c, end=" ")

        print(f"\nVidas restantes: {self.vidas}")

        print(f"Letras erradas: ", end="")
        for i in range(len(self.letras_erradas)):
            print(self.letras_erradas[i], end="")
            if i != len(self.letras_erradas) - 1:
                print(",", end="")

        print()

        condicao = self.checar_condicao()
        if condicao == -1:
            print("\nVocê perdeu!")
            print(f"A palavra era: {self.palavra_secreta}")

        elif condicao == 1:
            print("\nParabéns!")
            print("Você ganhou!")

    def validar_input(self, escolha: str):
        escolha = escolha.strip().lower()

        if len(escolha) != 1 or not escolha.isalpha():
            return False

        return True

    def nova_escolha(self, escolha: str):
        escolha = escolha.strip().lower()
        for letra, correspondentes in self.letras_correspondentes.items():
            if escolha in correspondentes:
                escolha = letra
        
        if self.validar_input(escolha):
            if not (escolha in self.letras_tentadas):
                existe = False
                
                for i in range(len(self.palavra_secreta)):
                    if (escolha == self.palavra_secreta[i].lower()) or (self.palavra_secreta[i].lower() in self.letras_correspondentes.get(escolha, "")):
                        self.palavra_oculta[i] = self.palavra_secreta[i]
                        existe = True

                if not existe:
                    self.vidas -= 1
                    self.letras_erradas.append(escolha)

                self.letras_tentadas.add(escolha)
            else:
                raise LetraJaTentada(escolha)
        else:
            raise EscolhaInvalida(escolha)
        
    def checar_condicao(self):
        if self.vidas == 0:
            return -1

        elif not ('_' in self.palavra_oculta):
            return 1

        else:
            return 0

    def resetar(self):
        self.vidas = len(JogoForca.ESTAGIOS_FORCA) - 1

        self.escolher_palavra()
        self.letras_erradas = []
        self.letras_tentadas = set()

def main():
    arquivo_palavras = "palavras.txt"

    '''Tratamento para caso o arquivo não exista ou não tenha palavras.
    Feito no main para que o usuário da classe tenha liberdade de decisão
    sobre o que fazer'''
    try:
        Forca = JogoForca(arquivo_palavras)

    except FileNotFoundError:
        print(f"'{arquivo_palavras}' não pode ser encontrado")
        sys.exit()

    except ZeroPalavrasEncontradas:
        print(f"Nenhuma palavra pôde ser encontrada em '{arquivo_palavras}'")
        sys.exit()

    except:
        print("Um erro inesperado ocorreu")
        sys.exit()

    mensagem = ""
    while True:
        Forca.exibir_estado()

        if mensagem != "":
            print('\n' + mensagem)

        try:
            letra = input("\nDigite uma letra: ")
            Forca.nova_escolha(letra)
            mensagem = ""

            condicao = Forca.checar_condicao()    
            if condicao != 0:
                Forca.exibir_estado()
                while True:
                    continuar = input("\nDeseja tentar de novo? (s/n): ").lower()
                    if continuar not in ['s', 'n']:
                        print("Escolha uma opção válida")
                    else:
                        break
                if continuar == 'n':
                    break
                else:
                    Forca.resetar()
        
        except KeyboardInterrupt:
            mensagem = "Digite uma entrada válida"

        except EscolhaInvalida:
            mensagem = "Escolha inválida"

        except LetraJaTentada:
            mensagem = "Essa letra já foi tentada antes"

        except:
            print("Um erro inesperado ocorreu")
            sys.exit()
        
if __name__ == '__main__':
    main()