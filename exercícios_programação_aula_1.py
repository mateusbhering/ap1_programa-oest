"""Exercícios programação aula 1

**Exercício 00**

Faça um Programa que peça dois números inteiros e um número real. Calcule e mostre:

a) o produto do dobro do primeiro com metade do segundo.

b) a soma do triplo do primeiro com o terceiro.

c) o terceiro elevado ao cubo.
"""

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = float(input("Terceiro número: "))
#letra a
a = (num1 * 2) * (num2/2)
print("Resultado da letra A:", a)
#letra b
b = (num1 * 3) + num3
print("Resultado da letra B:", b)
#letra c
c = num3**3
print("Resultado da letra C:", c)

"""**Exercício 1**

Crie um programa que receba as notas da AP1, AP2 e AC e informe a soma e a média das variáveis.

"""

ap1 = float(input("Nota da AP1: "))
ap2 = float(input("Nota da AP2: "))
ac = float(input("Nota da AC: "))
#soma das variaveis
soma = ap1 + ap2 + ac
#media das variaveis
media = (ap1+ap2+ac)/3
#print de tudo
print("A soma é:",soma)
print("A média das notas é:",media)

"""**Exercício 3**

Faça um programa que leia o salário bruto de uma pessoa em um determinado mês. Calcule e mostre o seu salário líquido no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato. A saída do programa deve escrever o seguinte texto:

print("(+) Salário Bruto: R$",sbruto)

print("(-) IR (11%): R$",ir)

print("(-) INSS (8%): R$",inss)

print("(-) Sindicato ( 5%): R$",sindi)

print("(-) Total Desconto : R$",totdesc)

print("(=) Salário Liquido: R$",sliq)

"""

salario_bruto = float(input("Salário Bruto: "))
ir = salario_bruto * 11/100
inss = salario_bruto * 8/100
sindi = salario_bruto * 5/100
totdesc = (ir + inss + sindi)
sliq = salario_bruto - totdesc
print("Salário bruto:",salario_bruto)
print("Imposto de renda:",ir)
print("Sindicato:",sindi)
print("Desconto total:",totdesc)
print("Salário Liquido:",sliq)

"""**Exercício 4**

Faça um programa que receba o raio, calcule e mostre:

a) o comprimento de uma esfera; sabe-se que C = 2*Pi*R;

b) a área de uma esfera; sabe-se que A = Pi*Rˆ2;

c) o volume de uma esfera; sabe-se que V = 3⁄4*Pi*Rˆ3.

Obs: Considere Pi = 3.14

"""

r = float(input("Raio: "))
pi = 3.14
#comprimento
c = 2*pi*r
print("Comprimento:",c)
#area
a = pi*r**2
print("Área:",a)
#volume
v = 3/4*pi*r**3
print("Volume:",v)

"""**Exercício 5**

Faça um programa que receba uma temperatura em Celsius, calcule e mostre essa temperatura em Fahrenheit. 

Sabe-se que F = C*9/5 + 32.
"""

c = float(input("Temperatura em celsius: "))
f = c * 9/5 + 32
print("F", f)