# Lab_06_API_aluguebug

Tarefa de testes de análise de valor limite e partições de equivalência

## Ambiente
- Python 3.6
- Pip 20.1.1

## Requisitos
- Request
- Pytest
- Pytest-html

## Execução da aplicação

Após clonar o projeto e ter entrado no diretório:
```
pip install -r requeriments.txt
```
Execute após baixar as dependências o arquivo aluguel.py no terminal:
```
python aluguel.py
```
Execute os testes com o comando:
```
pytest testes.py
```
Gere o relatório de testes com o comando:
```
pytest testes.py --html=report.html
```
