#Condicional If Elif Else - Curso de Python #11
clima = "sol"
dinheiro = 299
lugar = ""

if clima == "sol" or (dinheiro >= 300 and dinheiro <= 500):
    lugar = "Clube"
else:
    lugar = "Cinema"
print ("Vou ao " + lugar)

#AND = 
# V com V = V
# V com F = F
# F com V = F
# F com F = F

#OR = 
# V com V = V
# V com F = V
# F com V = V
# F com F = F