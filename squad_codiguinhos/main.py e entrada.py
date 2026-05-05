from motor_outliers import calcular_metricas
from auditoria_viz import exibir_relatorio

notas_brutas = [100.0, -50.0, 100.0, 2000.0, 5000.0, 0]
notas_fiscais = []

for nota in notas_brutas:
    if nota > 0:
        notas_fiscais.append(nota)

print(f"Notas processadas: {notas_fiscais}")
print("-" * 30)


media, variancia, qtd = calcular_metricas(notas_fiscais)
print(f"Média calculada: {media:.2f}")

