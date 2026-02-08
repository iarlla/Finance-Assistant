# Base de Conhecimento

## Dados Utilizados

O Nexus Z utiliza uma base híbrida que cruza dados do mercado de tecnologia com a legislação fiscal brasileira de 2026.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `certificacoes_ti.json` | JSON | Tabela de preços (USD/BRL) e pré-requisitos das certificações (IREB, AZ, ITIL). |
| `tabelas_tributarias_2026.csv` | CSV | Alíquotas atualizadas do Simples Nacional, faixas de IRRF e teto do INSS. |
| `vagas_df_market.json` | JSON | Médias salariais (CLT/PJ) específicas para Brasília para cargos de Dev e PO. |
| `fluxo_caixa_usuario.csv` | CSV | Registro de ganhos atuais (2 salários mínimos) e gastos fixos para cálculo de poupança. |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Para garantir a precisão do aconselhamento, os dados mockados foram expandidos com:Conversão Cambial Dinâmica: Preços de certificações internacionais são atualizados com o câmbio projetado para 2026.Regra do Fator R: Implementação lógica da fórmula $$Folha\ de\ Pagamento \div Faturamento \geq 0,28$$ para validar a migração de alíquotas (Anexo V para Anexo III).Custo de Oportunidade: Inclusão de cálculos de FGTS e 13º projetados para garantir que a comparação PJ não seja ilusória.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos de legislação e mercado são carregados como uma Base de Conhecimento Vetorial (RAG). Já os dados sensíveis do usuário (transações e salário) são injetados na sessão via Personal Context para manter a privacidade e volatilidade.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

O agente utiliza um System Prompt que define as regras de negócio (ex: "Nunca sugira MEI para Engenheiros"). Os dados de mercado entram como contexto de suporte para fundamentar a resposta, enquanto os dados do usuário servem de variáveis para as fórmulas financeiras.

---

## Exemplo de Contexto Montado

> O agente processa o contexto desta forma antes de gerar a resposta:

```
[CONTEXTO DO USUÁRIO]
- Cargo Atual: CLT (2 salários mínimos ~ R$ 3.242,00)
- Objetivo: Analista de Requisitos / Cloud
- Localização: Brasília-DF
- Meta: Entrada de imóvel em 3 anos

[DADOS DE REFERÊNCIA]
- Proposta Recebida: R$ 3.500,00 PJ (GS3 Tecnologia)
- Custo Certificação CPRE-FL: R$ 1.300,00
- Regra Fiscal: Profissão intelectual (Vedado MEI)

[ANÁLISE NEXUS Z]
- Break-even CLT vs PJ para este usuário: R$ 5.200,00
- Status da Proposta: "High Risk / Low Return"
```
