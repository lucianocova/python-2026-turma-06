# %%

print("True =", True)

print("False =", False)

print("True = ", "> 0")

print("True = bool(1) =", bool(1))
print("True = bool(2) =", bool(2))
print("True = bool(-1) =", bool(-1))
print("True = bool(-2) =", bool(-2))
print("True = bool('T') =", bool('T'))

# %%

print("False = bool(0) =", bool(0))
print("False = bool('') =", bool(''))
print("False = bool(None) =", bool(None))

# %%
# V   V   V
# 1 + 1 = 2

# V   F   V
# 1 + 0 = 1

# F   V   V
# 0 + 1 = 1

# F   F   F
# 0 + 0 = 0

print("True ou True =", "True or True =",  True or True)
print("True ou False =", "True or False =",  True or False)
print("False ou True =", "False or True =",  False or True)
print("False ou False =", "False or False =",  False or False)

# %%

# V   V   V
# 1 * 1 = 1

# V   F   F
# 1 * 0 = 0

# F   V   F
# 0 * 1 = 0

# F   F   F
# 0 * 0 = 0

print("True e True =", "True and True =",  True and True)
print("True e False =", "True and False =",  True and False)
print("False e True =", "False and True =",  False and True)
print("False e False =", "False and False =",  False and False)

# %%

print("not True = ", not True)
print("not False = ", not False)

# %%

# NAO CHUVA  E  (NAO TROVAO  OU DINHEIRO)

not True and (not True or True)
False and (False or True)
False and True
False