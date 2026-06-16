idade_usuario = input("Por favor, insira sua idade: ")

print("Que tal praticar um pouco de matemática básica? Vamos lá!")
num1 = int(input("Por favor, digite o primeiro número que vamos utilizar: "))
num2 = int(input("Agora digite o segundo: "))

soma = num1 + num2
print("A soma dos números escolhidos é igual a", soma,".")

multip = num1 * num2
print("Multiplicando os números escolhidos temos o resultado de", multip,".")

divisao1 = num1 / 2
divisao2 = num2 / 2
print("Se dividirmos ambos os números escolhidos por 2, o resultado, respectivamente será", divisao1, "e", divisao2,".")

potencia1 = num1 ** 2
potencia2 = num2 ** 2
print("Ambos os números escolhidos elevados a 2, é igual a", potencia1, "e", potencia2,"respectivamente.")

print("Agora, seja bem-vindo(a) à nossa calculadora!")

print("Escolha qual das operações você deseja realizar:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")

opcao = input("Digite o número da operação escolhida: ")

if opcao == "1":
  resultado = num1 + num2
  print("Resultado:", resultado)
elif opcao == "2":
  resultado = num1 - num2
  print("Resultado:", resultado)
elif opcao == "3":
  resultado = num1 * num2
  print("Resultado:", resultado)
elif opcao == "4":
  if num2 == 0:
    print("A divisão por zero não é possível.")
  else:
    print("Resultado:", num1 / num2)
else:
  print("Até logo. Encerramos por aqui.")

