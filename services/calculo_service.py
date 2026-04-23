from datetime import datetime
from services.ipca_service import fator_ipca

def calcular(valor, vencimento):
    hoje = datetime.today()

    if vencimento >= hoje:
        return valor, valor, 0, 0, valor

    dias = (hoje - vencimento).days

    fator = fator_ipca(vencimento, hoje)
    corrigido = valor * fator

    multa = corrigido * 0.02
    juros = corrigido * (0.01 / 30) * dias

    total = corrigido + multa + juros

    return valor, corrigido, multa, juros, total