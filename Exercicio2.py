#2) Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam
#ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso
#os valores formem um triângulo, calcular e escrever a área deste triângulo. Se
#não formam triângulo escrever os valores lidos. (Se a > b + c não formam
#triângulo algum, se a é o maior).

a = int(input('Digite um número para a: '))
b = int(input('Digite um número para b: '))
c = int(input('Digite um número para c: '))

if a + b > c and a + c > b and b + c > a :
    print("formam um triangulo: ")
    if a == b and a == c:
        print("Equilatero")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Escaleno")
else:
    print("os valores digitados não formam um triangulo. a , b e c : {}, {} e {}".format(a, b ,c ))
