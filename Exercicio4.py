#4) Implementar uma função que retorne verdadeiro se o número for primo
#(falso caso contrário). Testar de 1 a 100.


def primo(n):
    mult = 0
    for i in range(2,n):
        if( n % i == 0):
            mult += 1
    if(mult == 0 and n != 1):
        print("{} É primo".format(n))

for i in range(101):
    primo(i+1)