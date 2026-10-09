# Implementação do Jogo da Forca em Python

![Exemplo de Telas](https://github.com/ufpi-lp/lp2026-1/blob/main/forca.png)

## Objetivo da atividade

Nesta atividade, você deverá implementar um **jogo da forca em modo terminal** utilizando a linguagem Python.

O objetivo é praticar conceitos fundamentais de programação, como:

* leitura de arquivos;
* listas, conjuntos e strings;
* estruturas condicionais;
* estruturas de repetição;
* funções;
* tratamento de exceções;
* organização de código;
* interação com o usuário via terminal.

Ao final da atividade, o programa deverá permitir que o usuário jogue uma partida completa de forca, tentando adivinhar uma palavra secreta escolhida aleatoriamente a partir de um arquivo de palavras.

## Parte 1 — Preparação do projeto

### 1. Crie a pasta do projeto

Crie uma pasta chamada, por exemplo:

```text
jogo_forca
```

Dentro dessa pasta, você deverá criar pelo menos dois arquivos:

```text
forca.py
palavras.txt
```

O arquivo `foca.py` conterá o código principal do jogo.

O arquivo `palavras.txt` conterá a lista de palavras que poderão ser sorteadas pelo jogo.

### 2. Crie o arquivo de palavras

No arquivo `palavras.txt`, escreva uma palavra por linha.

Exemplo:

```text
python
algoritmo
terminal
programacao
computador
variavel
funcao
lista
```

Instruções:

1. Escreva pelo menos 10 palavras no arquivo.
2. Use inicialmente palavras sem espaço.
3. Dê preferência a palavras sem acento na primeira versão.
4. Salve o arquivo na mesma pasta do arquivo `foca.py`.

## Parte 2 — Estrutura inicial do programa

### 3. Importe os módulos necessários

No início do arquivo Python, importe os módulos que serão necessários para:

1. escolher palavras aleatoriamente;
2. limpar a tela do terminal;
3. encerrar o programa em caso de erro ou interrupção.

Pense em quais módulos da biblioteca padrão do Python podem ser usados para essas tarefas.

### 4. Defina a arte ASCII da forca

Crie uma estrutura de dados para armazenar os diferentes estágios visuais da forca.

Instruções:

1. Use uma lista para armazenar os desenhos da forca.
2. Cada posição da lista deve representar uma quantidade de erros.
3. O primeiro desenho deve representar a forca vazia.
4. O último desenho deve representar o jogador sem vidas restantes.
5. Use strings multilinha para representar os desenhos.

Exemplo conceitual:

```text
Estágio 0 → nenhum erro
Estágio 1 → cabeça
Estágio 2 → cabeça e tronco
Estágio 3 → cabeça, tronco e um braço
...
Estágio final → boneco completo
```

Observação: tente montar sua própria representação usando caracteres ASCII como `+`, `-`, `|`, `/`, `\`, `O` e `=`.

Exemplo: 

```bash
FORCA_ART = [
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
    ..., 
    ...,
    ]
```

## Parte 3 — Leitura do arquivo de palavras

### 5. Crie uma função para carregar palavras

Crie uma função chamada, por exemplo:

```text
carregar_palavras
```

Essa função deverá receber como parâmetro o nome do arquivo de palavras.

Ela deverá:

1. abrir o arquivo;
2. ler todas as linhas;
3. remover espaços em branco antes e depois de cada palavra;
4. converter as palavras para letras minúsculas;
5. ignorar linhas vazias;
6. retornar uma lista com as palavras válidas.

### 6. Trate possíveis erros na leitura

A função de carregamento deve lidar com situações problemáticas.

Considere os seguintes casos:

1. O arquivo `palavras.txt` não existe.
2. O arquivo existe, mas está vazio.
3. O arquivo contém apenas linhas em branco.
4. Ocorre algum erro inesperado durante a leitura.

Instruções:

* Use `try/except`.
* Exiba uma mensagem amigável para o usuário.
* Encerre o programa se não houver palavras válidas para jogar.

## Parte 4 — Inicialização do jogo

### 7. Sorteie a palavra secreta

Depois de carregar a lista de palavras, escolha uma palavra aleatória para ser a palavra secreta.

Instruções:

1. Use uma função apropriada do módulo de aleatoriedade.
2. Armazene a palavra escolhida em uma variável.
3. A palavra deve permanecer escondida do jogador durante a partida.

### 8. Crie a palavra oculta

Crie uma representação da palavra secreta usando underscores `_`.

Exemplo:

```text
Palavra secreta: algoritmo
Palavra oculta: _ _ _ _ _ _ _ _ _
```

Instruções:

1. A quantidade de underscores deve ser igual ao número de letras da palavra secreta.
2. Use uma lista para representar a palavra oculta.
3. Cada posição da lista deve corresponder a uma letra da palavra secreta.


### 9. Crie as variáveis de controle do jogo

Crie variáveis para controlar o estado da partida.

Você deverá controlar:

1. quantidade de vidas restantes;
2. letras erradas;
3. letras já digitadas;
4. palavra oculta;
5. palavra secreta.

Sugestão:

* Use uma lista para armazenar letras erradas.
* Use um conjunto para armazenar letras já digitadas.
* Use um número inteiro para representar as vidas.

## Parte 5 — Exibição do estado do jogo

### 10. Crie uma função para exibir o estado atual

Crie uma função responsável por mostrar na tela:

1. o desenho atual da forca;
2. a palavra oculta;
3. a quantidade de vidas restantes;
4. as letras erradas;
5. uma mensagem final, quando necessário.

Essa função deve ser chamada a cada rodada do jogo.

### 11. Limpe a tela antes de exibir o estado

Antes de mostrar o estado atualizado do jogo, limpe o terminal.

Instruções:

1. Verifique se o sistema operacional é Windows, Linux ou macOS.
2. Use o comando adequado para limpar a tela.
3. Faça isso dentro da função de exibição.

### 12. Exiba a palavra oculta de forma legível

A palavra oculta deve aparecer com espaços entre os caracteres.

Exemplo:

```text
Palavra: a _ _ o _ i _ _ o
```

Instruções:

1. Use a lista que representa a palavra oculta.
2. Transforme essa lista em uma string formatada.
3. Não mostre diretamente a palavra secreta durante a partida.


## Parte 6 — Entrada do usuário

### 13. Solicite uma letra ao jogador

Dentro do loop principal do jogo, peça ao usuário que digite uma letra.

Exemplo de mensagem:

```text
Digite uma letra:
```

Instruções:

1. Leia a entrada usando `input`.
2. Remova espaços antes e depois da entrada.
3. Converta a entrada para letra minúscula.


### 14. Valide a entrada do jogador

Antes de processar a tentativa, verifique se a entrada é válida.

A entrada deve obedecer às seguintes regras:

1. Deve conter apenas um caractere.
2. Deve ser uma letra.
3. Não pode ter sido digitada anteriormente.

Se a entrada for inválida:

1. mostre uma mensagem de aviso;
2. não remova vidas;
3. peça para o jogador tentar novamente.

### 15. Controle letras repetidas

O jogo não deve penalizar o jogador por digitar uma letra já usada.

Instruções:

1. Antes de processar a tentativa, verifique se a letra já está no conjunto de letras digitadas.
2. Se já estiver, informe ao jogador.
3. Solicite uma nova tentativa.
4. Se ainda não estiver, adicione a letra ao conjunto de letras digitadas.

## Parte 7 — Processamento da tentativa

### 16. Crie uma função para processar a letra digitada

Crie uma função responsável por atualizar o estado do jogo após cada tentativa.

Essa função deverá receber:

1. a letra digitada;
2. a palavra secreta;
3. a palavra oculta;
4. a lista de letras erradas;
5. a quantidade de vidas.

Ela deverá retornar o estado atualizado.

### 17. Caso a letra esteja correta

Se a letra digitada existir na palavra secreta:

1. percorra a palavra secreta posição por posição;
2. identifique todas as posições onde a letra aparece;
3. atualize a palavra oculta nessas posições;
4. não diminua a quantidade de vidas.

Exemplo:

```text
Palavra secreta: algoritmo
Letra digitada: o
Palavra oculta: _ _ _ o _ _ _ _ o
```

### 18. Caso a letra esteja errada

Se a letra digitada não existir na palavra secreta:

1. adicione a letra à lista de letras erradas;
2. diminua uma vida;
3. atualize o desenho da forca na próxima exibição.

Exemplo:

```text
Letras erradas: e, u
Vidas restantes: 4
```

## Parte 8 — Loop principal do jogo

## 19. Crie o loop da partida

O jogo deve continuar enquanto:

1. o jogador ainda tiver vidas;
2. a palavra ainda não tiver sido completamente descoberta.

Pense em uma condição lógica que combine essas duas regras.

### 20. Dentro do loop principal

A cada rodada, o programa deve executar a seguinte sequência:

1. limpar a tela;
2. exibir o estado atual da forca;
3. mostrar a palavra oculta;
4. mostrar vidas restantes;
5. mostrar letras erradas;
6. pedir uma letra;
7. validar a entrada;
8. processar a tentativa;
9. atualizar o estado do jogo.

## Parte 9 — Vitória ou derrota

### 21. Verifique se o jogador venceu

O jogador vence quando não houver mais underscores na palavra oculta.

Exemplo:

```text
Palavra: a l g o r i t m o
Parabéns! Você acertou a palavra!
```

Instruções:

1. Após o fim do loop, verifique se a palavra oculta foi completamente revelada.
2. Exiba uma mensagem de vitória.
3. Mostre o estado final do jogo.


### 22. Verifique se o jogador perdeu

O jogador perde quando as vidas chegam a zero antes de completar a palavra.

Instruções:

1. Exiba uma mensagem de derrota.
2. Mostre a palavra secreta.
3. Mostre o desenho final da forca.

Exemplo:

```text
Game Over!
A palavra era: ALGORITMO
```

## Parte 10 — Tratamento de interrupções

### 23. Trate interrupções do usuário

O programa deve lidar com interrupções como:

1. `Ctrl+C`;
2. finalização inesperada da entrada.

Instruções:

1. Use tratamento de exceções.
2. Exiba uma mensagem amigável.
3. Encerre o programa de forma controlada.

## Parte 11 — Organização do código

### 24. Crie uma função principal

Organize o fluxo principal do jogo dentro de uma função chamada, por exemplo:

```text
main
```

Essa função deverá controlar:

1. carregamento das palavras;
2. escolha da palavra secreta;
3. inicialização das variáveis;
4. execução do loop principal;
5. exibição do resultado final.

### 25. Use a estrutura padrão de execução

No final do arquivo, use a estrutura padrão do Python para executar o programa somente quando ele for executado diretamente.

Instruções:

1. Pesquise o significado de:

```text
if __name__ == "__main__":
```

2. Explique, em comentário no próprio código, por que essa estrutura é útil.


## Parte 12 — Testes manuais

### 26. Teste o jogo com entradas válidas

Execute o jogo e teste:

1. letras corretas;
2. letras erradas;
3. vitória;
4. derrota.

Anote se o comportamento está correto.

## 27. Teste o jogo com entradas inválidas

Teste situações como:

```text
ab
1
@
espaço em branco
letra repetida
```

O programa deve avisar o usuário e não deve descontar vidas nesses casos.

### 28. Teste problemas no arquivo de palavras

Faça testes com:

1. arquivo inexistente;
2. arquivo vazio;
3. arquivo com linhas em branco;
4. arquivo com palavras válidas.

Observe se o programa trata os erros corretamente.

# Critérios de avaliação

O exercício será avaliado considerando:

| Critério               | Descrição                                        |
| ---------------------- | ------------------------------------------------ |
| Funcionamento geral    | O jogo permite uma partida completa              |
| Leitura de arquivo     | As palavras são carregadas corretamente          |
| Sorteio da palavra     | A palavra secreta é escolhida aleatoriamente     |
| Validação de entrada   | O programa rejeita entradas inválidas            |
| Controle de vidas      | As vidas diminuem apenas em erros válidos        |
| Letras repetidas       | O programa identifica letras já digitadas        |
| Atualização da palavra | Letras corretas aparecem nas posições corretas   |
| Condição de vitória    | O jogo reconhece quando a palavra foi descoberta |
| Condição de derrota    | O jogo reconhece quando as vidas acabam          |
| Organização            | O código está dividido em funções                |
| Clareza                | O código é legível e bem comentado               |

# Entrega

O aluno deverá entregar um arquivo .zip contendo, pelo menos, os dois arquivos abaixo:
```text
forca.py
palavras.txt
```
