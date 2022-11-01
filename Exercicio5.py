#5) Escreva uma função que:
#a) Receba uma frase como parâmetro.
#b) Retorne uma nova frase com cada palavra com as letras invertidas.

def primeiro_nome(nome):
    return nome

def inverter(texto):
    return texto[::-1]

name = input("Digite o primeiro nome: ")
print("O nome digitado é {} ".format(primeiro_nome(name)))


algumacoisa = input("Digite uma palavra para ser invertida: ")
print(inverter(algumacoisa))