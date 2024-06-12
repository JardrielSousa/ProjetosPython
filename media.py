print("====================")
nome = input("fale seu nome:")
nota1 = float(input("nota 1:"))
nota2 = float(input("nota 2:"))
nota3 = float(input("nota 3:"))

faltas = float(input("número de faltas:"))

media = (nota1+nota2+nota3)/3;

print("====================")
print("nome:"+nome)
print("====================")
if(media>6 and faltas<25):
   print("Você está aprovado")
else:
   print("Você está reprovado")