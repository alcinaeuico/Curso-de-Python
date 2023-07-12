salário=float(input("informe o seu salário"))
if salário<128000:
    percentagem=0.2
    aumento=salário*percentagem
    novo_salario=salário+aumento
elif(salário>=128000 and salário<=500000):
     percentagem=0.15
     aumento=salário*percentagem
     novo_salario=salário+aumento
elif(salário>=500000 and salário<=1000000):
     percentagem=0.1
     aumento=salário*percentagem
     novo_salario=salário+aumento
else:
    percentagem=0.5
    aumento=salário*percentagem
    novo_salario=salário+aumento
print("salário antes do reajuste:",salário)
print("percentagem:",percentagem)
print("aumento a ser aplicado:",aumento)
print("novo salári:",novo_salario)
              
