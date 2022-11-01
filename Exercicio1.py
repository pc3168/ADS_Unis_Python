#Faça um programa que leia a idade de uma pessoa expressa
# em dias e mostre-a expressa em anos, meses e dias.
from datetime import date, datetime

dataHoje = date.today();
data_em_texto = input('Digite uma data de nascimento no formato dd-MM-yyyy: ')
data = datetime.strptime(data_em_texto, '%d-%m-%Y').date()
dataFormatada = data.strftime('%d-%m-%Y')

# Calculo da quantidade de dias
dias = abs((dataHoje - data).days)

# Calculo da quantidade de anos
anos = dias // 365

# Calculo da quantidade de meses
meses = dias // 30

print("data digitada: {} ".format(dataFormatada))
print("data de hoje: {} ".format(dataHoje))
print("sua idade é {} ano(s) ".format(anos))
print("sua idade é {} mes(es) ".format(meses))
print("sua idade é {} dia(s) ".format(dias))


