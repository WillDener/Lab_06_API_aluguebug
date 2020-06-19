import requests
import json


def aluguel(valor, dia):
    r = requests.get(
        'https://aluguebug.herokuapp.com/calc?dados={"valor_nominal":'+str(valor)+',"dia":'+str(dia)+'}')
    return json.loads(r.json())


print('Willian Dener da Silva Pinto \nAplicacao em esta consumindo a API Web \nhttps://aluguebug.herokuapp.com/calc?dados')
print(aluguel(350.0, 16))
