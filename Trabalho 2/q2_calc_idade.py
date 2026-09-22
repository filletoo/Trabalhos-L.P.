from datetime import *

def lerData():
    while True:
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")

        data_nascimento = nascimento.split('/')

        try:
            data = date(int(data_nascimento[2]), int(data_nascimento[1]), int(data_nascimento[0]))
            if data > date.today():
                print("Data de nascimento inválida")
            else:
                break
        except ValueError:
            print("Data inválida")

    return data

def calc_idade(data_nascimento):
    aniver = date(date.today().year, data_nascimento.month, data_nascimento.day)
    idade = (date.today() - data_nascimento).days//365

    if aniver > date.today():
        idade -= 1

    return idade

def dia_da_semana(dia):
    if dia == 0:
        return "Segunda-feira"
    elif dia == 1:
        return "Terça-feira"
    elif dia == 2:
        return "Quarta-feira"
    elif dia == 3:
        return "Quinta-feira"
    elif dia == 4:
        return "Sexta-feira"
    elif dia == 5:
        return "Sábado"
    elif dia == 6:
        return "Domingo"
    else:
        return None

def mes_do_ano(mes):
    if mes == 1:
        return "Janeiro"
    elif mes == 2:
        return "Fevereiro"
    elif mes == 3:
        return "Março"
    elif mes == 4:
        return "Abril"
    elif mes == 5:
        return "Maio"
    elif mes == 6:
        return "Junho"
    elif mes == 7:
        return "Julho"
    elif mes == 8:
        return "Agosto"
    elif mes == 9:
        return "Setembro"
    elif mes == 10:
        return "Outubro"
    elif mes == 11:
        return "Novembro"
    elif mes == 12:
        return "Dezembro"
    else:
        return None

def prox_niver(data_nascimento):
    idade = calc_idade(data_nascimento)
    prox = date(data_nascimento.year + idade + 1, data_nascimento.month, data_nascimento.day)

    return prox

if __name__ == '__main__':
    data_nascimento = lerData()
    idade = calc_idade(data_nascimento)
    prox_aniversario = prox_niver(data_nascimento)

    print("------------------------------------------------------------")
    print(f"Idade atual: {idade}") #idade
    print(f"Mês de nascimento: {mes_do_ano(data_nascimento.month)}")
    print(f"Dia da semana em que nasceu: {dia_da_semana(data_nascimento.weekday())}")
    print(f"Dias para o próximo aniversário: {(prox_aniversario - date.today()).days}")
    print("------------------------------------------------------------")