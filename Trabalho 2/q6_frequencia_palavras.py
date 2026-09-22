def remover_pontuacao(texto):
    pontuacao = ",.!?:;()—-#"
    for p in pontuacao:
        texto = texto.replace(p, " ")

    return texto

def frequencias(texto):
    freq = {}
    for palavra in texto:
        freq[palavra] = freq.get(palavra, 0) + 1

    return freq

def mais_frequentes(freq, quant):
    top_freq = [] #maiores frequencias
    pal_mais_freq = {} #palavras mais frequentes
    for palavra in freq:
        top_freq.append(freq[palavra])

    top_freq.sort(reverse=True)
    top_freq = top_freq[0:quant]

    for palavra in freq:
        frequencia = freq[palavra]
        if frequencia in top_freq:
            if frequencia not in pal_mais_freq:
                pal_mais_freq[frequencia] = []
            pal_mais_freq[frequencia].append(palavra)

    pal_mais_freq = dict(sorted(pal_mais_freq.items(), key=lambda x: x[0], reverse=True))
    return pal_mais_freq

def lerLinhas(arquivo):
    linhas = []
    with open(arquivo, mode="r") as f:
        linha = "ç"
        while linha != "":
            linha = f.readline()
            if linha == "": break

            if not linha.isspace():
                linhas.append(remover_pontuacao(linha).lower())

    return linhas

if __name__ == '__main__':
    texto_linhas = lerLinhas("texto.txt")

    palavras = []
    for linha in texto_linhas:
        for palavra in linha.split():
            palavras.append(palavra)

    freq = frequencias(palavras)

    mais_freq = mais_frequentes(freq, 1)
    mais_freq_10 = mais_frequentes(freq, 10)

    with open("relatorio.txt", "w") as f:
        f.write(f"Total de linhas: {len(texto_linhas)}\n")
        f.write(f"\nTotal de palavras: {len(palavras)}\n")
        f.write(f"\nTotal de palavras distintas: {len(set(palavras))}\n")
        f.write(f"\nPalavras mais frequentes (frequencia {max(mais_freq)}):\n")

        for p in mais_freq:
            for i in mais_freq[p]:
                f.write(f"- {i}\n")

        k = 1
        f.write(f"\n10 Palavras mais frequentes:\n")
        for p in mais_freq_10:
            f.write(f"#{k} (frequencia {p}):\n")
            for i in mais_freq_10[p]:
                f.write(f"- {i}\n")

            k += 1