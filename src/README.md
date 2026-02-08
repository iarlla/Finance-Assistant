# 🚀 Nexus Z: Mentor FinTech para a Geração Z em TI

O **Nexus Z** é um assistente financeiro e de carreira desenvolvido para ajudar jovens profissionais de tecnologia (Engenheiros de Software, POs e Analistas) a navegarem na complexa transição entre CLT e PJ, com foco no mercado de Brasília-DF e no objetivo de longo prazo da casa própria.

## 🎯 O Problema que Resolvemos

Muitos profissionais juniores aceitam propostas PJ que, após impostos e custos operacionais, resultam em um **"bug de liquidez"** (ganham nominalmente mais, mas têm menos poder de compra real que um CLT). O Nexus Z utiliza o **Gemini 1.5 Pro** e lógica tributária real para "debugar" essas ofertas.

## 🛠️ Stack Tecnológica

* **Inteligência Artificial:** Google Gemini 1.5 Pro (via Google AI Studio).
* **Interface:** Streamlit (Python-based UI).
* **Processamento de Dados:** Pandas & JSON.
* **Gestão de Ambiente:** Python Venv (PEP 668 compliant).

## 📂 Estrutura do Projeto

```text
Finance-Assistant/
├── data/                       # Base de Conhecimento (RAG Local)
│   ├── certificacoes_ti.json   # Roadmap e custos de certificações
│   ├── vagas_df_market.json    # Inteligência salarial de Brasília
│   ├── tabelas_tributarias.csv # Alíquotas 2026 (Simples, IRRF, INSS)
│   └── fluxo_caixa_usuario.csv # Perfil financeiro do usuário
├── src/                        # Código Fonte
│   ├── app.py                  # Aplicação Principal e UI
│   ├── agente.py               # Integração com a LLM Gemini
│   ├── calculadora.py          # Engine de lógica tributária (Fator R)
│   └── utils.py                # Utilitários de carga de dados
├── .env.example                # Template de chaves de API
└── .gitignore                  # Proteção de segredos e ambientes

```

## ⚙️ Lógica de Negócio (O "Pulo do Gato")

### 1. Simulação CLT vs PJ

O sistema não faz apenas uma subtração simples. Ele calcula o **Poder de Compra Real** da CLT, provisionando:

* 
* 
* 

### 2. Otimização via Fator R

O assistente orienta o usuário sobre a migração do **Anexo V (15,5%)** para o **Anexo III (6%)** do Simples Nacional, validando se o Pró-labore atinge os **28%** necessários do faturamento.

## 🚀 Como Executar

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/finance-assistant.git
cd finance-assistant

```


2. **Configure o Ambiente Virtual:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
pip install -r requirements.txt

```


3. **Configure suas chaves:**
* Crie um arquivo `.env` na raiz.
* Adicione sua `GEMINI_API_KEY` obtida no [Google AI Studio](https://aistudio.google.com/).


4. **Inicie a aplicação:**
```bash
streamlit run src/app.py

```



## 📈 Roadmap Futuro

* [ ] **Integração de PDFs:** Leitura automática de editais de certificação.
* [ ] **Visão Computacional:** Upload de contracheques para análise automática.
* [ ] **Multi-City:** Expansão da base de dados salariais para SP, BH e Remoto Internacional.

---

**Desenvolvido por Iarla – Engenheira de Software** 🚀
