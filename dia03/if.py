# %%

print("1 == 1 =", 1==1)
print("1 == 2 =", 1==2)
print("1 >= 1 =", 1>=1)
print("1 > 1 =", 1>1)
print("1 != 1 =", 1!=1)

# %%

idade = 89

if idade < 18:
    print("Vá para casa beber leite!")

elif idade < 70:
    print("Oh!!")
    print("Você pode se embriagar!")

else:
    print("Cuidade com seus remédios")


print("Fim!")
# %%

idade = 71

if 12 <= idade < 18:
    print("Vá para casa beber leite!")

elif idade >= 18 and idade <= 40:  # 18 <= idade <= 40
    print("Oh!!")
    print("Você pode se embriagar!")

elif 40 < idade < 70: # idade < 70 and idade > 40
    print("Pega leve!")

elif idade >= 70:
    print("Cuidade com seus remédios")

else:
    print("Nem era para vc estar na rua")

# %%
