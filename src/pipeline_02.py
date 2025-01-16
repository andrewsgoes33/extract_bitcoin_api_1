import requests
from tinydb import TinyDB
from datetime import datetime

def extract_dados_bitcoin():
    """Obtem o JSON dos dados do Bitcoin da Coinbase pela API"""
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    return resposta.json()

def tratar_dados_bitcoin(dados_json):
    """Transforma os dados brutos da APi, renomeia as colunas e adiciona timestamp"""
    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    dados_tratados = {
        "valor" : valor,
        "criptomoeda" : criptomoeda,
        "moeda" : moeda,
        "timestamp" : timestamp
    }
    
    return dados_tratados

def salvar_dados_tinydb(dados, db_name="bitcoin_dados.json"):
    """Salva os dados em um banco NoSQL usando TinyDB."""
    db = TinyDB(db_name)
    db.insert(dados)
    print('Dados salvos no TinyDB!')
    
if __name__ == "__main__":
    "Extração e tratamento dos dados"
    dados_json = extract_dados_bitcoin()
    dados_tratados = tratar_dados_bitcoin(dados_json)
    
    #Mostra os dados tratados
    print("Dados Tratados:")
    print(dados_tratados)
    
    #Salvar no TinyDB
    salvar_dados_tinydb(dados_tratados)