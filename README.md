# Geração Automatizada de Notificações com Correção por IPCA

Projeto desenvolvido para automatizar a geração de notificações financeiras com atualização monetária baseada no IPCA (IBGE), cálculo de juros e multa, e geração de documentos Word personalizados.

## Problema

O cliente precisava consolidar e atualizar valores financeiros em prazo exíguo, o que manualmente seria:

- Demorado
- Suscetível a erros
- Pouco escalável

## Solução

Desenvolvi uma automação em Python que:

- Lê dados de um arquivo Excel
- Aplica correção monetária com base no IPCA (via API do IBGE)
- Calcula multa e juros pro rata die
- Gera notificações personalizadas em Word
- Estrutura os dados de forma padronizada e auditável

## Tecnologias

- Python
- Pandas
- Requests
- python-docx
- API SIDRA (IBGE)

##  Destaques Técnicos

- Consulta única à API do IBGE (alta performance)
- Cálculo de IPCA mês a mês (aderente ao mercado)
- Arquitetura modular (services, generators, utils)
- Normalização de dados com `unicodedata`
- Geração automatizada de documentos Word

## Estrutura

- `services/` → regras de negócio e cálculos
- `generators/` → geração de documentos
- `utils/` → funções auxiliares
- `data/` → arquivos de entrada (anonimizados)
- `output/` → arquivos gerados

## Como executar

```bash
pip install -r requirements.txt
python -m main
