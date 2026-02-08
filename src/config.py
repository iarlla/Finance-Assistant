import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do Agente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4-turbo-preview"  # Ou gpt-3.5-turbo para economia

# Regras de Negócio (Base de Conhecimento Mockada)
TRIBUTACAO_2026 = {
    "simples_nacional_minimo": 0.06,
    "fator_r_limite": 0.28,
    "inss_pro_labore": 0.11
}
