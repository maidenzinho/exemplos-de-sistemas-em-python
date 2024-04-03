tentativas = 0

while (tentativas < 3):
  user = input("Digite o usuário: ")
  passwd = input("Digite a senha: ")

  if (user == "admin" and passwd == "admin"):
    print("Seja bem vindo!")
    break
  else:
    print("Senha incorreta!")

    tentativas += 1
    print(f"Tentativas restantes: {tentativas}")
