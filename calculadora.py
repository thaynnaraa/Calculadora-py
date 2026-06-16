idade_usuario = input("Por favor, insira sua idade: ")

print("Agora, seja bem-vindo(a) à nossa calculadora!")

print("Que tal praticar um pouco de matemática básica? Vamos lá!")

print("Escolha qual das operações você deseja realizar:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Potenciação")
print("5 - Divisão")
print("6 - Sair")

opcao = input("Digite o número da operação escolhida: ")

num1 = int(input("Por favor, digite o primeiro número que vamos utilizar: "))
num2 = int(input("Agora digite o segundo: "))

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
  resultado = num1 ** num2
  print("Resultado:", resultado)
elif opcao == "5":
  if num2 == 0:
     print("A divisão por zero não é possível.")
  else:
     resultado = num1 / num2
     print("Resultado:", resultado)
elif opcao == "6":
  print("Até logo. Encerramos por aqui.")

else:
  print("Opção inválida!") 
