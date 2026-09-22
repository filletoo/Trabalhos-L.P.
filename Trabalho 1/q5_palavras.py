def remover_pontuacao(texto):
    pontuacao = ",.!?:;()—"
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

if __name__ == "__main__":
    texto = input("Texto: ")
    #1 - remover pontuacao
    texto = remover_pontuacao(texto)
    #2 - deixar tudo minusculo
    texto = texto.lower()
    #3 - separar as palavras
    texto = texto.split()
    #4 - frequencias
    freq = frequencias(texto)

    print("\nTotal de palavras no texto:", len(texto))
    print("Total de palavras distintas:", len(freq))

    pal_mais_freq = mais_frequentes(freq, quant=1)
    print(f"\nPalavra(s) mais frequente(s):")
    for frequencia in pal_mais_freq:
        print(f"Frequencia: {frequencia}")
        for palavra in pal_mais_freq[frequencia]: 
            print(f"- {palavra}")

    pal_mais_freq10 = mais_frequentes(freq, quant=10)
    print("\n10 Palavras mais frequentes: ")
    ranking = 1
    for frequencia in pal_mais_freq10:
        print(f"#{ranking}: (frequencia {frequencia})")
        for palavra in pal_mais_freq10[frequencia]: 
            print(f"- {palavra}")
        ranking += 1