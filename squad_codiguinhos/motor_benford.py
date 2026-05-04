def calcular_limite(media, variancia):
    desvio_padrao = variancia ** 0.5
    limite_seguranca = media + (3 * desvio_padrao)
    return limite_seguranca