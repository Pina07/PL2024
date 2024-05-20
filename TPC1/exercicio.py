import os
import sys

#dic = _id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado


file_path = 'emd.csv'  #colocar o path do ficheiro csv aqui


# FAz parse do ficheiro csv e devolve um dicionario com os dados
def parse_csv(file_path):
    dicionario = {}
    with open(file_path, 'r') as file:
        linhas = file.readlines()
        linhas.pop(0)
        linhas = [linha.strip() for linha in linhas]
        
        for linha in linhas:
            linha = linha.split(',')
            dicionario[linha[0]] = (linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7], linha[8], linha[9], linha[10], linha[11], linha[12])
    return dicionario


#Devolve as modalidades presentes no csv
def get_sports(dicionario):
    modalidade = set()
    for id in dicionario:
        modalidade.add(dicionario[id][7])
    return sorted(list(modalidade))




#Devolve a percentagem de atletas aptos e inaptos
def get_aptitude_percentages(dicionario):
    aptos = 0
    inaptos = 0
    for id in dicionario:
        if dicionario[id][11] == 'true':
            aptos += 1
        else:
            inaptos += 1
    total = aptos + inaptos
    return (aptos/total)*100, (inaptos/total)*100




#Devolve a distribuição por idades
def get_age_distribution(dicionario):
    distribution = {}
    for id in dicionario:
        age = int(dicionario[id][4])
        age_range = f'{age//5*5}-{age//5*5+4}'
        if age_range in distribution:
            distribution[age_range] += 1
        else:
            distribution[age_range] = 1
    return distribution


dicionario = parse_csv(file_path)
print("As Modalidades sao: ", get_sports(dicionario), "\n")
print("A percentagem de ateltas aptos e inaptos é respetivamente: ", get_aptitude_percentages(dicionario), "\n")
print("A distribuição por idades é .", get_age_distribution(dicionario), "\n")








