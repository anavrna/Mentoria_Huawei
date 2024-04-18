def conversao():
    temp_f = float(input("Digite a temperatura em graus Fahrenheit: "))
    temp_c = 5 * ((temp_f-32)/9)
    return temp_c
converter = conversao()
print(f"A temperatura em graus Celsius é: {converter}")