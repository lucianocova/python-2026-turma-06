# %%

nome = input("Entre com o seu nome: ")
print(nome)

# %%

idade = input("Entre com a sua idade: ")
print(idade, type(idade))

idade = int(idade)
print(idade, type(idade))

# %%

diff = 75 - idade
print(f"{nome}, faltam {diff} anos para você chegar em 75 anos.")