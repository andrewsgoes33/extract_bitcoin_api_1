import requests
from tinydb import TinyDB
from datetime import datetime

def extrair_dados_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    return resposta.json()

def tratar_dados_bitcoin(dados_json):
    valor = dados_json['data']['amount']
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    dados_tratados = {
        'valor' : valor,
        'criptomoeda' : criptomoeda,
        'moeda' : moeda,
        'timestamp' : timestamp
        }
    
    return dados_tratados

def salvar_dados_tinydb(dados, db_name='bitcoin_teste_1.json'):
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos no TinyDB!")
    
    
    
if __name__ == '__main__':
    dados_json = extrair_dados_bitcoin()
    dados_tratados = tratar_dados_bitcoin(dados_json)
    print("Resultado final dos dados tratados:")
    print(dados_tratados)
    salvar_dados_tinydb(dados_tratados)