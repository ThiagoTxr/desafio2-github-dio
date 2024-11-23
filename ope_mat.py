num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja realizar: (+, -, *, /)")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    if num2 == 0:
        print("Não se divide por zero")
    else:
        print(num1 / num2)
else:
    print("Operação inválida")