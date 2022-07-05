import os
from banco import Banco
from flask import Flask


def buscarAcessoIP():
    ipInterno = '172.31.39.225'
    ipExterno = '152.67.49.7'
    hostname = os.environ.get('HOSTNAME')
    ehServidor = 'ALFA' in hostname.upper() if hostname else False
    return ipInterno if ehServidor else ipExterno

ipAcesso = buscarAcessoIP()
at_alfa = Banco(ipAcesso, 'at_alfa')


def buscarDados():
    sql = "SELECT * FROM edi002 limit 5"
    dados = at_alfa.selecionar(sql)
    return dados

app = Flask(__name__)

@app.route("/")
def hello_world():
    dados = buscarDados()
    listaCNPJ = []

    for dado in dados:
        listaCNPJ.append(dado['cli004_cnpj'])

    resposta = f"<pre>{listaCNPJ}</pre>"
    return resposta

# if __name__ == '__main__':
#     selecionaBanco = buscarDados()
#     print(selecionaBanco[0]['cli004_cnpj'])
#     for selecionaUm in selecionaBanco:
#         print(selecionaUm['cli004_cnpj'])
