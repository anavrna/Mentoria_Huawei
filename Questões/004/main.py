area = float(input("Digite a área, em metros quadrados, que deseja pintar: "))
l_necessarios = (area/3)
latas = round(l_necessarios/18, 0)
p_total = round(latas * 80, 2)

print(f"A quantidade de latas necessárias é: {latas}")
print(f"O valor total é: R${p_total}")