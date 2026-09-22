def filtrar_linhas(arquivo, palavra_chave):
    linhas_filtradas = []
    with open(arquivo, mode="r") as f:
        linha = "a"
        while linha != "":
            linha = f.readline()
            if linha == "": break
            
            for palavra in linha.split():
                if palavra_chave.lower() == palavra.lower():
                    linhas_filtradas.append(linha) 
                    break

    return linhas_filtradas

def gravar_linhas(arquivo, linhas, palavra_chave=""):
     with open(arquivo, mode="w") as f:
        if len(linhas) == 0:
            f.write(f'Nenhuma linha foi encontrada a qual continha a palavra-chave "{palavra_chave}".')
        else:
            for l in linhas_filtradas:
                f.write(l)
    
if __name__ == '__main__':
    palavra_chave = input("Indique uma palavra chave: ")

    linhas_filtradas = filtrar_linhas("frases.txt", palavra_chave)

    gravar_linhas("resultado_busca.txt", linhas_filtradas, palavra_chave)

    print(f"{len(linhas_filtradas)} linhas encontradas")