from motor_outliers import calcular_metricas
from motor_benford import calcular_limite
from auditoria_viz import exibir_relatorio

notas_brutas = [100.0, -50.0, 100.0, 2000.0, 5000.0, 0]
notas_fiscais = []

for nota in notas_brutas:
    if nota > 0:
        notas_fiscais.append(nota)

print(f"Notas processadas: {notas_fiscais}")
print("-" * 30)

# Aqui chamamos a função direto, sem o "motor_outliers." na frente
media, variancia, qtd = calcular_metricas(notas_fiscais)
print(f"Média calculada: {media:.2f}")

# Aqui a mesma coisa, sem o "motor_benford."
limite = calcular_limite(media, variancia)
print(f"Limite de segurança definido: {limite:.2f}")
print("-" * 30)

# E aqui sem o "auditoria_viz."
exibir_relatorio(notas_fiscais, limite)