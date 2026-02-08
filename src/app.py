import streamlit as st
import pandas as pd
from agente import responder_nexus_z
from calculadora import simular_clt, simular_pj_fator_r
from utils import buscar_vagas_df, buscar_certificacoes

st.set_page_config(page_title="Nexus Z - Inteligência Financeira", layout="wide")

# Carregamento de Dados das tabelas que criamos
tabelas = pd.read_csv("data/tabelas_tributarias_2026.csv")
vagas_data = buscar_vagas_df()
cert_data = buscar_certificacoes()

st.title("🚀 Nexus Z: Mentor de Carreira & Finanças")

# Criação das Abas
tab1, tab2, tab3 = st.tabs(["💬 Chat Nexus Z", "📊 Simulador CLT vs PJ", "🏢 Marketplace de Carreira"])

with tab1:
    st.subheader("Otimize sua Carreira")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ex: Vale a pena trocar minha CLT de 3k por PJ de 5k?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            response = responder_nexus_z(st.session_state.messages)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

with tab2:
    st.subheader("Calculadora de Equivalência Real")
    col1, col2 = st.columns(2)
    
    with col1:
        salario_clt = st.number_input("Salário CLT Bruto (R$)", value=3242.0)
        liqd_clt, real_clt = simular_clt(salario_clt, tabelas)
        st.metric("Poder de Compra Real (CLT)", f"R$ {real_clt}")
        st.caption("Inclui FGTS e Provisão de 13º")

    with col2:
        faturamento_pj = st.number_input("Faturamento PJ Oferecido (R$)", value=5500.0)
        liqd_pj, aliq = simular_pj_fator_r(faturamento_pj)
        st.metric("Líquido PJ (Anexo III)", f"R$ {liqd_pj}", f"-{aliq}% Imposto")
        st.caption("Considerando Fator R (28% Pró-labore)")

    # Gráfico de Comparação
    st.markdown("### Comparativo Visual")
    dados_grafico = pd.DataFrame({
        "Modelo": ["CLT (Poder Real)", "PJ (Líquido)"],
        "Valor (R$)": [real_clt, liqd_pj]
    })
    st.bar_chart(dados_grafico.set_index("Modelo"))

    if liqd_pj < real_clt:
        st.error("⚠️ Atenção: Esta proposta PJ tem um 'bug' de liquidez. O valor real da sua CLT é maior.")
    else:
        st.success("✅ Build Sucesso: Esta proposta PJ aumenta seu fluxo de caixa real.")

with tab3:
    st.subheader("Radar de Mercado: Brasília-DF")
    
    # Seção de Vagas
    if vagas_data:
        st.markdown("### 💰 Médias Salariais 2026")
        for cargo in vagas_data['cargos']:
            with st.expander(f"Ver salários para: {cargo['titulo']}"):
                df_vaga = pd.DataFrame(cargo['niveis']).T
                st.table(df_vaga[['clt_media', 'pj_media']])
    
    st.markdown("---")
    
    # Seção de Certificações
    if cert_data:
        st.markdown("### 🎓 Roadmap de Certificações")
        cols = st.columns(2)
        for i, cert in enumerate(cert_data['certificacoes']):
            with cols[i % 2]:
                st.info(f"**{cert['nome']}**\n\nInvestimento: R$ {cert['preco_brl_est']}\n\n*Nível: {cert['nivel']}*")