# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

A "Ambiguidade do Primeiro Salário": Jovens profissionais de tecnologia (Gen Z) enfrentam dificuldade em decidir entre estabilidade (CLT) e maior ganho nominal (PJ), muitas vezes aceitando propostas PJ que, após impostos e falta de benefícios, resultam em perda de poder de compra. Além disso, desconhecem como otimizar tributos (como o Fator R) para acelerar objetivos como a compra da casa própria.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente atua como um simulador de realidade financeira. Ele não apenas compara valores brutos, mas calcula o "salário líquido real", projeta o custo de certificações no orçamento mensal e sugere estratégias de transição de carreira baseadas em dados matemáticos e legislação atualizada.

### Público-Alvo
> Quem vai usar esse agente?

Profissionais em início de carreira (Trainees, Juniores e Recém-formados) que buscam segurança para negociar contratos e planejar grandes marcos financeiros.

---

## Persona e Tom de Voz

### Nome do Agente
Nexus Z

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Mentor Técnico-Consultivo: O agente age como um colega sênior que entende de código, mas também domina a contabilidade. Ele é pragmático, analítico e não faz julgamentos, focando sempre na viabilidade matemática dos sonhos do usuário.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Técnico-Acessível: Utiliza terminologias de TI (stack, deploy, backlog) como analogias para conceitos financeiros. É direto, mas empático com as incertezas da primeira fase da vida adulta.

### Exemplos de Linguagem
- Saudação: "Olá! Pronta para depurar suas finanças e otimizar seu próximo contrato?"
- Confirmação: "Entendido. Vou rodar a simulação de equivalência CLT vs. PJ com base no Fator R para você."
- Erro/Limitação: "Ainda não tenho os dados sobre o novo teto do MEI para este ano, mas posso projetar seu imposto com base nas regras atuais do Simples Nacional."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário/Gen Z] -->|Pergunta: 'Vale a pena este PJ?'| B[Interface Chat]
    B --> C[Nexus Z Engine]
    C --> D[Base: CLT/PJ/Simples Nacional 2026]
    C --> G[Calculadora de Fator R e IRRF]
    D --> C
    G --> C
    C --> E[Validação de Consistência]
    E --> F[Resposta: Líquido Real + Recomendação]
```

### Componentes


| Componente | Descrição |
|------------|-----------|
| Interface | App mobile ou integração via WhatsApp para consultas rápidas. |
| LLM | Gemini 1.5 Pro ou similar (com foco em raciocínio lógico-matemático).|
| Base de Conhecimento | Tabelas do Simples Nacional, alíquotas de INSS/IRRF 2026 e catálogos de certificações (IREB, AZ, ITIL).|
| Validação | Filtro de segurança para garantir que cálculos de porcentagem não "alucinem".|

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Zero Adivinhação: O agente sempre solicita o valor bruto e o regime tributário antes de calcular.
- [ ] Citação de Regras: Todas as simulações mencionam a regra aplicada (ex: "Cálculo baseado no Anexo III do Simples Nacional").
- [ ] Disclaimer de Contabilidade: O agente reforça que não substitui um contador, mas prepara o usuário para a conversa com um.
- [ ] Contexto de Carreira: Não sugere demissão sem antes validar a reserva de emergência e o plano de certificações.

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO faz investimentos diretos ou compra de ativos.
- NÃO emite notas fiscais ou documentos contábeis reais.
- NÃO fornece aconselhamento jurídico para processos trabalhistas em andamento (apenas consultas informativas).
