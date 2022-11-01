#3) Faça um programa que leia 3 números inteiros e mostre o menor deles.

a = int(input('Digite um número para a: '))
b = int(input('Digite um número para b: '))
c = int(input('Digite um número para c: '))

if a <= b and a <= c:
    print("o valor menor é {} ".format(a))
elif b <= a and b <= c:
    print("o valor menor é {} ".format(b))
else:
    print("o valor menor é {} ".format(c))