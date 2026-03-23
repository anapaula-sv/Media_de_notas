# media de notas

nota1 = float(input("digite a sua primeira nota: "))
while nota1 < 0 or nota1 > 10: #faz a validação da nota, para garantir que o usuário digite uma nota entre 0 e 10
    print("nota inválida, por favor digite uma nota entre 0 e 10.")
    nota1 = float(input("digite a sua primeira nota: "))

nota2 = float(input("Digite a sua segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("nota inválida, por favor digite uma nota entre 0 e 10.")
    nota2 = float(input("Digite a sua segunda nota: "))

nota3 = float(input("Digite a sua terceira nota: "))
while nota3 < 0 or nota3 > 10:
    print("nota inválida, por favor digite uma nota entre 0 e 10.")
    nota3 = float(input("Digite a sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3 #faz o cálculo da média das notas
print(f"a sua média é: {media:.2f}") #exibe a média com duas casas decimais
if media >= 7:
    print("parabéns, você foi aprovado!")
else:
    print("infelizmente, você foi reprovado.")
