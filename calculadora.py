idade_usuario = input("Por favor, insira sua idade: ")

print("Agora sim, seja bem-vindo(a) à nossa calculadora!")

print("Que tal praticar um pouco de matemática básica? Vamos lá!")

while True:
  print("Escolha qual das operações você deseja realizar:")
  print("\n=== MENU ===")
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Potenciação")
  print("5 - Divisão")
  print("6 - Sair")

  opcao = input("Digite o número da operação escolhida: ")

  if opcao == "6":
    print("Até logo! Encerramos por aqui.")
    break

  if opcao not in ["1", "2", "3", "4", "5"]:
    print("Opção inválida!")
    continue

  try:
    num1 = int(input("Por favor, digite o primeiro número que vamos utilizar: "))
    num2 = int(input("Agora digite o segundo: "))
  except ValueError:
    print("Por favor, digite apenas números!")
    continue

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

   while True:
     continuar = input("Deseja realizar outra operação? (s/n): ").lower()

     if continuar in ["s", "n"]:
       break
     print("Resposta inválida!")

   if continuar == "n":
     print("Até logo!")
     break
