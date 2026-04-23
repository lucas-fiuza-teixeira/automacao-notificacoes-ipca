import pandas as pd
import os

from config import ARQUIVO_EXCEL, TEMPLATE_WORD, PASTA_SAIDA
from generators.notificacao_generator import gerar_notificacao

os.makedirs(PASTA_SAIDA, exist_ok=True)

df = pd.read_excel(ARQUIVO_EXCEL)
grupos = df.groupby(['razao_social', 'cnpj', 'numero_contrato', 'email'])

total_global = 0
memoria_total = []

for dados_cliente, grupo in grupos:
    total, memoria = gerar_notificacao(
        grupo,
        dados_cliente,
        TEMPLATE_WORD,
        PASTA_SAIDA
    )

    total_global += total
    memoria_total.extend(memoria)

# exporta memória
pd.DataFrame(memoria_total).to_excel("memoria_calculo.xlsx", index=False)

print("\n=======================")
print(f"TOTAL GLOBAL: R$ {total_global:.2f}")
