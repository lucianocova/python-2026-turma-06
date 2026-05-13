# %%
# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

escolha = input("""Escolha entre:
    1 - água mineral natural (R$1,50)
    2 - água mineral com gás (R$2,50)
""")

if escolha == "1":
    print("Total a pagar: R$1.50")

elif escolha == "2":
    print("Total a pagar: R$2.50")

else:
    print("Entre com uma opçao válida!")

# valor = 0
# if escolha == "1":
#     valor += 1.5

# elif escolha == "2":
#     valor = valor + 2.5


# if valor == 0:
#     print("Entre com um valor válido!")

# else:
#     print(f"Total a pagar: R${valor}")
