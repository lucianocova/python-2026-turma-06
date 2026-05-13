# %%
# Faça um programa que receba um número inteiro e
#  calcule sua raiz quadrada e exiba o resultado.

numero = input("Entre com um número: ")

numero = float(numero)

raiz = numero ** 0.5

msg = f"A raiz de {numero} é {raiz}"
print(msg)