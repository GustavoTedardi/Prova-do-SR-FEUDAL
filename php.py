num1 = float(input("digite o primero número"))
num2 = float(input("digite o segundo número"))

print("escolha a operação:")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")

op = int(input("digite o número da operação:"))

if op == 1:
    resultado = num1 + num2
    print("resultado", resultado)
elif op == 2:
    resultado = num1 - num2
    print("resultado:", resultado)
elif op == 3:
    resultado = num1 * num2
    print("resultado:", resultado)
else:
        print("opcão inválida")
        
       