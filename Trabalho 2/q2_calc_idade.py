from datetime import *

def lerData():
    while True:
        nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        data_nascimento = nascimento.split('/')
        if len(data_nascimento) != 3:
            print("Data inválida")
            continue
    
        try:
            data = date(int(data_nascimento[2]), int(data_nascimento[1]), int(data_nascimento[0]))
            if data > date.today():
                print("Data inválida")
            else:
                break
        except ValueError:
            print("Data inválida")

    return data

def ajustar_data_bissexta(data, ano):
    eh_bissexto = (data.year % 100 == 0 and data.year % 400 == 0) or (data.year % 4 == 0 and not data.year % 100 == 0)
    if eh_bissexto and data.day == 29 and data.month == 2:
        data = date(ano, 3, 1)
    else:
        data = date(ano, data.month, data.day)

    return data

def calc_idade(data_nascimento):
    aniversario = ajustar_data_bissexta(data_nascimento, date.today().year)
    idade = date.today().year - data_nascimento.year

    if aniversario > date.today():
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
    prox = ajustar_data_bissexta(data_nascimento, data_nascimento.year + idade + 1)

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