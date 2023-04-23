"""Exercícios programação aula 2

**Exercício 05.**

Implemente um código em Python que receba todas as notas de um aluno, bem como suas faltas. O programa deve avaliar se o aluno foi aprovado, reprovado ou se terá que fazer AS. Em caso de AS, receber o valor da nota da prova, fazer a substituição da mesma em relação a menor nota (ap1 ou ap2) e reavaliar se o aluno foi aprovado ou reprovado.
"""

faltas = float(input("Faltas: "))
ap1 = float(input("Nota AP1: "))
ap2 = float(input("Nota AP2: "))
ac = float(input("Nota AC: "))

soma = ap1 + ap2 + ac
if faltas > 25:
    print("Aluno reprovado por falta")

elif faltas <= 25 and soma >= 70:
    print("Aluno aprovado")

elif faltas <= 25 and 30 > soma:
    print("Aluno reprovado por nota")

elif faltas <= 25 and 30 <= soma < 70:
    print("Aluno de AS")
    nota_as = float(input("Nota AS: "))
    if ap1 < ap2:
        menorap = ap1
    else:
        menorap = ap2
    notafinal = soma - menorap + nota_as
    if notafinal >= 70:
        print("Aluno aprovado pela AS")
    else:
        print("Aluno reprovado após AS")

ap1 = float(input("ap1:"))
ap2 = float(input("ap2:"))
ac = float(input("ac:"))
faltas = float(input("faltas:"))
nota = ap1 + ap2 + ac

if faltas > 25:
    print("reprovado")
if nota < 30:
    print("reprovado")
if faltas <= 25 and nota >= 70:
    print("aprovado")
if faltas <= 25 and 70 > nota >= 30:
    print("fazer as!")
    nota_as = float(input("as:"))
    if ap1 > ap2:
        menorap = ap2
    else:
        menorap = ap1
    notaf = nota + nota_as - menorap
    if notaf >= 70:
        print("aprovado")
    else:
        print("reprovado")

"""**Exercício 06.**

Usando **estruturas condicionais simples**, faça um programa que mostre o menu de opções a seguir, receba a opção do usuário e os dados necessários para executar cada operação.

Menu de opções:
1. Multiplicar dois números 

2. Dividir dois números 

Digite a opção desejada:
"""

num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
opcao = str(input("Opção: digite 'multi' para multiplicar e 'dividir' para divisão: "))
if opcao == "multi":
    print("Resultado:",num1*num2)
if opcao == "dividir":
    print("Resultado:",num1/num2)