frase = str(input("Digite uma frase: ")).strip().upper()
frase2 = frase.split()
junto = "".join(frase2)
inverso = ""
for c in range(len(junto) - 1,-1,-1):
    inverso += junto[c]
print("O inverso de {} fica {}".format(junto,inverso))
if inverso == junto:
    print("Ele é um palindromo")
else:
    print("Ele não é um palindromo")