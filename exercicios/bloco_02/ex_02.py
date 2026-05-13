# %%

# Faça um programa que de bom dia, pergunta o nome da pessoa
#  e responde que é um prazer conhecer ela, citando o nome da pessoa.

nome = input("Olá, bom dia! Entre com o seu nome: ")

# print("Nome original:", nome)

nome = nome.title().strip(" ")

# print("Nome formatado:", nome)

print("Que bom te conhecer, ", nome, ". Boas vindas!!", sep="")
print(f"Que bom te conhecer, {nome}. Boas vindas!!")