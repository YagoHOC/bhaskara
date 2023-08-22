# ax2 + bx + c = 0

valorA = int(input('Qual o valor A?'))
valorB = int(input('Qual o valor B?'))
valorC = int(input('Qual o valor C?'))

valorX = ((valorB * -1) + (valorB**2 - 4 * valorA * valorC) ** (1/2)) / (2 * valorA)
valorX2 = ((valorB * -1) + (valorB**2 - 4 * valorA * valorC) ** (1/2)) / (2*valorA)

print('O valor x1 é '+str(valorX))
print('O valor x2 é '+str(valorX2))

