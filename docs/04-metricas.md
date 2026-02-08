# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do Nexus Z deve focar na precisão dos cálculos e na aderência às leis trabalhistas brasileiras de 2026. A avaliação pode ser feita de duas formas complementares:

1. Testes estruturados: Validação das fórmulas de equivalência CLT vs PJ e regras de Fator R.

2. Feedback real: Teste com outros profissionais de TI (Juniores e Trainees) para avaliar se a linguagem "tech" e os conselhos de carreira são úteis.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Precisão de Cálculo** | O agente calculou o "Líquido Real" corretamente? | Simular CLT de R$ 3.242 e validar se o total real bate com $S_{bruto} + 22.3\%$ (provisões). |
| **Segurança Fiscal** | O agente barrou a tentativa de ser MEI? | Perguntar "Posso ser PO como MEI?" e esperar um "Não" fundamentado. |
| **Conformidade (Fator R)** | A sugestão de Anexo III foi baseada nos 28%? | Testar se o agente sugere Pró-labore de R$ 2.800 para um faturamento de R$ 10.000. |
| **Coerência de Mercado** | Os salários sugeridos batem com Brasília? | Comparar a resposta do agente com os dados do vagas_df_market.json. |


> [!TIP]
> Peça para colegas de Engenharia de Software testarem o Nexus Z. Como eles entendem de lógica, serão os melhores para encontrar "edge cases" nos cálculos tributários. Lembre-os de que o contexto é o de um profissional Júnior em Brasília.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Equivalência CLT vs PJ
- **Pergunta:** "Ganho 3.242 CLT. Vale a pena aceitar 3.500 PJ?"
- **Resposta esperada:** Agente deve informar que o valor é insuficiente e sugerir algo próximo a R$ 5.200,00.
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Custo de Carreira
- **Pergunta:** "Quanto preciso guardar para tirar a CPRE-FL e a AZ-900?"
- **Resposta esperada:** Soma dos valores no certificacoes_ti.json (aprox. R$ 1.850,00).
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Como faço para trocar o óleo do carro?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Regra do Fator R
- **Pergunta:** "Como pago menos imposto ganhando 10k PJ?"
- **Resposta esperada:** Explicação sobre o Pró-labore de 28% para migrar para o Anexo III (6%).
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**
- A separação de conceitos entre Líquido Mensal e Poder de Compra Real (incluindo benefícios).
- A recusa imediata de enquadramento em MEI para atividades intelectuais.
- A linguagem alinhada com o público Gen Z/Tech de Brasília.

**O que pode melhorar:**
- Latência: O Gemini 1.5 Pro é potente, mas o tempo de resposta pode ser otimizado com streaming.
- RAG: Integrar a leitura direta do PDF do Simples Nacional para evitar atualizações manuais no CSV.

---

## Métricas Avançadas (Opcional)

Para o monitoramento do Nexus Z em produção, utilizaremos: 

- Latência de Inferência: Tempo entre o chat_input e a resposta final.
- Taxa de Acerto de Fórmulas: Validação via scripts de teste unitário comparando a saída da LLM com a calculadora.py.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
