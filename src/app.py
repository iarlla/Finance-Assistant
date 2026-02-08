import streamlit as st
from agente import responder_nexus_z

st.set_page_config(page_title="Nexus Z - Seu Mentor FinTech", page_icon="🚀")

st.title("🚀 Nexus Z: Mentor de Carreira & Finanças")
st.markdown("---")

# Inicializa o histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do Usuário
if prompt := st.chat_input("Diga sua dúvida (ex: Vale a pena 4k PJ?)"):
    # Adiciona mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera resposta do Nexus Z
    with st.chat_message("assistant"):
        with st.spinner("Rodando debug financeiro..."):
            full_response = responder_nexus_z(st.session_state.messages)
            st.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar com Informações Úteis
st.sidebar.header("Dashboard de Contexto")
st.sidebar.info("""
**Status do Perfil:**
- Formação: Engenharia de Software
- Localização: Brasília-DF
- Foco: Analista de Requisitos / Cloud
""")
