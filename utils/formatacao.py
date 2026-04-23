import re
import unicodedata

def limpar_nome_arquivo(nome):
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
    nome = re.sub(r'[<>:"/\\|?*]', '', nome)
    return nome.replace(' ', '_')[:50]