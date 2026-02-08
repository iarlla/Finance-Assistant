import google.generativeai as genai
import config

# Configuração do modelo
genai.configure(api_key=config.GEMINI_API_KEY)

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
    """Envia o histórico para o Gemini e retorna a resposta."""
    try:
        # Inicializa o modelo
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            system_instruction=SYSTEM_PROMPT
        )
        
        # Converte o histórico para o formato do Gemini
        # O Streamlit guarda as mensagens, aqui nós as enviamos para o chat do Gemini
        chat = model.start_chat(history=[])
        
        # O Gemini lida melhor com o envio da última mensagem em um chat ativo
        ultima_mensagem = mensagens[-1]["content"]
        response = chat.send_message(ultima_mensagem)
        
        return response.text
    except Exception as e:
        return f"Erro no Kernel (Gemini Stack Trace): {str(e)}"