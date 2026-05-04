import motor_outliers
import motor_benford
import auditoria_viz

notas_brutas = [100.0, -50.0, 100.0, 2000.0, 0]
notas_fiscais = []

for nota in notas_brutas:
    if nota > 0:
        notas_fiscais.append(nota)


media, variancia, qtd = motor_outliers.calcular_metricas(notas_fiscais)

limite = motor_benford.calcular_limite(media, variancia)

auditoria_viz.exibir_relatorio(notas_fiscais, limite)