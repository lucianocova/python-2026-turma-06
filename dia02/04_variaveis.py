# %%
teo = "Teodoro Calvo"

print(teo)

teo = "Teodoro"

print(teo)

teo = 33

print(teo)

# %%

nome = "Teo"
sobrenome = "Calvo"
salario = 1_549
altura = 1.82
idade = 33

mensagem = f"""
Olá, {nome} {sobrenome}. Legal que você tem {idade} anos!

Você me parece mais alto que {altura} m.

Dá para beber muita cerveja para quem ganha R$ {salario}
"""

print(mensagem)

# %%

mensagem = "Olá, {nome} {sobrenome}.\nLegal que você tem {idade} anos!\nVocê me parece mais alto que {altura} m.\nDá para beber muita cerveja para quem ganha R$ {salario}".format(nome=nome, sobrenome=sobrenome, idade=idade, altura=altura, salario=salario)

print(mensagem)

# %%

