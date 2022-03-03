salario = input()
percentualAumento = input()
SalarioFloat = float(salario)
percentualAumentoFloat = float(percentualAumento)
aumento = SalarioFloat * (1+(percentualAumentoFloat/100))
print('Seu salario teve aumento de ' + str(percentualAumentoFloat) + ' %, passando de R$ ' + str(SalarioFloat) + ' para R$ ' + str(aumento))

