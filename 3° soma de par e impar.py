i = 0
soma_par = 0
soma_impar = 0

while(i <= 100):
    if i % 2 == 0:
        print(f"{i} Par")
        soma_par += i
    else:
        print(f"{i} Impar")
        soma_impar += i

    i+=1

print("Encerrou")
print(f"Soma dos pares: {soma_par} e a soma dos impares: {soma_impar}")