import pandas as pd
import os

storage = 'C:\\Users\\kevin.maykel\\Documents\\Meus Projetos\\Python\\projeto-city\\storage'
lista_arquivos = os.listdir(storage)

lista_arquivos = [i.split('Piloto - Tabela - ', 2) for i in lista_arquivos]


print(list(filter(lambda x: x[0].lower() in 'a', lista_arquivos)))

"""
def qual_tabela():
    print("1")
    for tabelas in lista_arquivos:
        #print("2")
        if lista_arquivos[0] == ['', 'Azure  .xlsx']:
            print("3")
            print("tabelas")

qual_tabela()


nomeTabela = "Piloto - Tabela - " + tabela + ".xlsx"

df = pd.read_excel("storage\\{nomeTabela}")

"""