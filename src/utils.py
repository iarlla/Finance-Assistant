import json
import os

def carregar_dados_json(caminho_arquivo):
    """Lê arquivos JSON da pasta data de forma segura."""
    if not os.path.exists(caminho_arquivo):
        return None
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def buscar_vagas_df():
    return carregar_dados_json("data/vagas_df_market.json")

def buscar_certificacoes():
    return carregar_dados_json("data/certificacoes_ti.json")