import requests
from datetime import datetime

# cache global em memória
_ipca_cache = None

def carregar_ipca():
    global _ipca_cache

    if _ipca_cache is not None:
        return _ipca_cache

    url = "https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/63/p/last%20120"

    response = requests.get(url, timeout=10)
    dados = response.json()[1:]

    ipca = {}

    for item in dados:
        periodo = item.get("D3C")  # YYYYMM
        valor = item.get("V")

        if not periodo or valor in ("...", "-", "", None):
            continue

        try:
            valor = float(valor.replace(",", "."))
            ano = int(periodo[:4])
            mes = int(periodo[4:])
            ipca[(ano, mes)] = valor
        except:
            continue

    _ipca_cache = ipca
    return _ipca_cache


def fator_ipca(inicio, fim):
    ipca_mensal = carregar_ipca()
    hoje = datetime.today()

    # início → próximo mês cheio
    if inicio.day > 1:
        mes = inicio.month + 1
        ano = inicio.year
        if mes > 12:
            mes = 1
            ano += 1
    else:
        mes = inicio.month
        ano = inicio.year

    # fim → último mês fechado
    if hoje.day < 28:
        mes_fim = hoje.month - 1
        ano_fim = hoje.year
        if mes_fim == 0:
            mes_fim = 12
            ano_fim -= 1
    else:
        mes_fim = hoje.month
        ano_fim = hoje.year

    fator = 1

    while (ano, mes) <= (ano_fim, mes_fim):
        variacao = ipca_mensal.get((ano, mes), 0)
        fator *= (1 + variacao / 100)

        mes += 1
        if mes > 12:
            mes = 1
            ano += 1

    return fator