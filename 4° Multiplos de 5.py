i = 0
soma_par = 0
soma_impar = 0
soma_cinco = 0

while(i <= 100):
    #Par ou impar
    if i % 2 == 0:
        print(f"{i} Par")
        soma_par += i
    else:
        print(f"{i} Impar")
        soma_impar += i

    if i % 5 == 0:
        print(f"{i} é multiplo de 5")
        soma_cinco += i

    i+=1

print("Encerrou")
print(f"Soma dos pares: {soma_par}, soma dos impares: {soma_impar} e os multiplos de 5: {soma_cinco}")