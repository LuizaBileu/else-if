# numero = int(input("Digite um número inteiro: "))
# if numero >= 0:
#     print("Número positivo ou zero.")
# else:
#     print("Número negativo.")


senha = input("Digite a senha: ")

if senha == "1234":
    print("Acesso permitido.")
else:
    print("Acesso negado.")



# if numero % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")



# nota = float(input("Digite a nota do aluno (de 0 a 10): "))
# if 0 <= nota <= 10:

#     if nota >= 6:
#         print("Aprovado!")
#     else:
#         print("Reprovado!")
# else:
#     print("Nota inválida! Digite um valor entre 0 e 10.")


nota = input("Digite a sua nota:")

if nota >= 8:
    print("nota exelente")

elif nota >6 and nota <= 7:
    print("na media")
elif nota <=5:
    print("recuperaçao")
else:
    print("nenhuma das opcoes")

