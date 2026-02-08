import pandas as pd

def calcular_irrf(salario_base, tabela_irrf):
    """Calcula o IRRF com base nas faixas de 2026."""
    for _, faixa in tabela_irrf.iterrows():
        if salario_base <= faixa['faixa_fim']:
            return (salario_base * faixa['aliquota']) - faixa['deducao']
    return 0

def simular_clt(salario_bruto, tabela_taxas):
    """Calcula o líquido real da CLT incluindo benefícios."""
    # Projeção simplificada de 2026
    inss_teto = tabela_taxas[tabela_taxas['categoria'] == 'INSS_TETO_2026'].iloc[0]
    irrf_table = tabela_taxas[tabela_taxas['categoria'] == 'IRRF_MENSAL_2026']
    
    inss = min(salario_bruto * inss_teto['aliquota'], inss_teto['deducao'])
    irrf = calcular_irrf(salario_bruto - inss, irrf_table)
    
    liquido_mensal = salario_bruto - inss - irrf
    # Benefícios invisíveis (Provisão de 13º e FGTS)
    beneficios = (salario_bruto * 0.08) + (salario_bruto / 12) 
    
    return round(liquido_mensal, 2), round(liquido_mensal + beneficios, 2)

def simular_pj_fator_r(faturamento, pro_labore_percent=0.28):
    """Calcula imposto PJ com base na regra do Fator R."""
    pro_labore = faturamento * pro_labore_percent
    # Se Pro-labore >= 28%, Anexo III (6%), senão Anexo V (15.5%)
    aliquota = 0.06 if pro_labore_percent >= 0.28 else 0.155
    
    imposto_das = faturamento * aliquota
    inss_pro_labore = pro_labore * 0.11 # Simplificado
    
    liquido = faturamento - imposto_das - inss_pro_labore
    return round(liquido, 2), aliquota * 100