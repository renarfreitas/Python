#Strings P2 - Curso de Python #07
#texto = "Curso de Python"
#palavra = "python"
#res = palavra.upper() in texto.upper()
#res = palavra not in texto

#print(res)
#curso = "Curso de Python"
#canal = "CFB Cursos"

#res = curso + " do canal "+ canal

#print(res)
cidade = "Salvador"
dia = 27
mes = "Fevereiro"
ano = 2021
canal = "CFB Cursos"
data = "{}, {} de {} de {} \n \"{}\""

#\' \"" \n \r \t \b
print(cidade + ", " + str(dia) + " de " + mes + " de " +str(ano))
print(data.format (cidade, dia, mes, ano, canal))