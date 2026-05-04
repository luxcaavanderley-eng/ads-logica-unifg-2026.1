def calcular_metricas(notas_fiscais):
    quantidade = len(notas_fiscais)
    soma = 0
    for n in notas_fiscais:
        soma += n
    media = soma / quantidade

    soma_quadrados = 0
    for n in notas_fiscais:
        soma_quadrados += (n - media) ** 2
    variancia = soma_quadrados / quantidade
    
    return media, variancia, quantidade