"""Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10."""

bacteria_a = 4
bacteria_b = 10
dias = 0   

while bacteria_a <= bacteria_b:
    bacteria_a += bacteria_a * 0.03
    bacteria_b += bacteria_b * 0.015
    dias += 1

print(f"Levará {dias} dias para a colônia de bactérias A ultrapassar ou igualar a colônia de bactérias B.")