import pytest
import aluguel as z


def teste_menor_1_WDSP():
    valor = z.aluguel(350.0, -1)
    esperado = -1
    assert valor['valor_calculado'] == esperado


def teste_dia_1_WDSP():
    valor = z.aluguel(350.0, 1)
    valor_descontado = 350.0-(350.0*0.10)
    assert valor['valor_calculado'] == valor_descontado


def teste_dia_0_WDSP():
    valor = z.aluguel(350.0, 0)
    esperado = -1
    assert valor['valor_calculado'] == esperado


def teste_dia_6_WDSP():
    valor = z.aluguel(350.0, 6)
    valor_descontado = 350.0-(350.0*0.05)
    assert valor['valor_calculado'] == valor_descontado


def teste_dia_11_WDSP():
    valor = z.aluguel(350.0, 11)
    valor_descontado = 350.0-(350.0*0.0)
    assert valor['valor_calculado'] == valor_descontado


def teste_dia_15_WDSP():
    valor = z.aluguel(350.0, 15)
    valor_descontado = 350.0
    assert valor['valor_calculado'] == valor_descontado


def teste_dia_16_WDSP():
    valor_nominal = 350.0
    valor = z.aluguel(valor_nominal, 16)
    dia_juro = 16 - 15
    valor_descontado = 350.0+(350.0*0.02)+(350.0*(dia_juro/1000))
    assert valor['valor_calculado'] == valor_descontado


def teste_dia_30_WDSP():
    valor_nominal = 350.0
    valor = z.aluguel(valor_nominal, 30)
    dia_juro = 30 - 15
    valor_descontado = 350.0+(350.0*0.02)+(350.0*(dia_juro/1000))
    assert valor['valor_calculado'] == valor_descontado


def teste_maior_30_WDSP():
    valor_nominal = 350.0
    valor = z.aluguel(valor_nominal, 35)
    esperado = -1
    assert valor['valor_calculado'] == esperado

# Gerar relatório
# pytest testes.py --html=report.html
# Rodar testes
# pytest testes.py
