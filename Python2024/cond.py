idade = 1
possui_carteira = True

if idade >= 18 and possui_carteira:
    print("Você pode dirigir!")
elif possui_carteira:
    print("Você apenas possui carteira")
else:
    print("Não pode dirigir!")

print("Fim do programa!")

a = [1,2,3,4,5,6]
b = 0

#Laço de repetição
for x in a:
    print(x)
    b = b+x
print(b)

for x in range(1,11,1):
    print(x)