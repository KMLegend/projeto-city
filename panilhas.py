import pandas as pd
import os

storage = 'C:\\Users\\kevin.maykel\\Documents\\Meus Projetos\\projeto-city\\storage'
lista_arquivos = os.listdir(storage)

caminho = "C:\\Users\\kevin.maykel\\Documents\\Meus Projetos\\projeto-city\\storage\\Piloto - Tabela - " # Caminho para as tabelas.


def qual_tabela(): # Função que opera as tabelas individualmente.
    
    for tabelas in lista_arquivos: # Para tabelas na lista de arquivos do Storage.
        quebra = tabelas.split("Piloto - Tabela - ") # Quebra uniformemente os nomes de tabela.
        
        for nome in quebra: # Para nome de tabelas que foi quebrada.
            if nome[0:] == "Atmos.xlsx": # if de operação das tabelas individualmente.
                df = pd.read_excel(caminho + nome, sheet_name="Tabelas")
                print(df)
                
            
                
    
# Piloto - Tabela - Atmos.xlsx    
qual_tabela()
