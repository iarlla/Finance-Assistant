import pandas as pd

def calcular_irrf(salario_base, tabela_irrf):
    """Calcula o IRRF com base nas faixas de 2026."""
    for _, faixa in tabela_irrf.iterrows():
        if salario_base <= faixa['faixa_fim']:
            return (salario_base * faixa['aliquota']) - faixa['deducao']
    return 0

def simular_clt(salario_bruto, tabela_taxas):
    """Calcula o líquido real da CLT com rigor matemático."""
    inss_teto = tabela_taxas[tabela_taxas['categoria'] == 'INSS_TETO_2026'].iloc[0]
    irrf_table = tabela_taxas[tabela_taxas['categoria'] == 'IRRF_MENSAL_2026']
    
    inss = min(salario_bruto * inss_teto['aliquota'], inss_teto['deducao'])
    irrf = calcular_irrf(salario_bruto - inss, irrf_table)
    
    liquido_mensal = salario_bruto - inss - irrf
    
    # Benefícios Reais (Provisão mensal):
    fgts = salario_bruto * 0.08
    decimo_terceiro = salario_bruto / 12
    ferias_mais_terco = (salario_bruto * 1.33) / 12 # Salário + 1/3 dividido por 12 meses
    
    total_real_clt = liquido_mensal + fgts + decimo_terceiro + ferias_mais_terco
    
    return round(liquido_mensal, 2), round(total_real_clt, 2)

def simular_pj_fator_r(faturamento, custo_contador=150.0, pro_labore_percent=0.28):
    """Calcula o líquido PJ subtraindo custos operacionais fixos."""
    pro_labore = faturamento * pro_labore_percent
    aliquota = 0.06 if pro_labore_percent >= 0.28 else 0.155
    
    imposto_das = faturamento * aliquota
    inss_pro_labore = pro_labore * 0.11 # Alíquota padrão sobre pró-labore
    
    # O líquido real PJ deve considerar o contador, que é obrigatório para ME
    liquido_real = faturamento - imposto_das - inss_pro_labore - custo_contador
    
    return round(liquido_real, 2), aliquota * 100