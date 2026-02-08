from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

SYSTEM_PROMPT = """
Você é o Nexus Z, mentor financeiro para a Geração Z de TI.
Use analogias de engenharia de software (debug, deploy, backlog).
REGRAS:
1. CLT vs PJ: Sempre calcule o 'Líquido Real'.
2. MEI: Proibido para engenharia de software.
3. Fator R: Use a regra de 28% para baixar imposto para 6%.
4. Tom de voz: Técnico, direto e educativo.
"""

def responder_nexus_z(mensagens):
    """Envia o histórico para a LLM e retorna a resposta do Nexus Z."""
    try:
        response = client.chat.completions.create(
            model=config.MODEL_NAME,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + mensagens,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro no sistema (Stack Trace): {str(e)}"
