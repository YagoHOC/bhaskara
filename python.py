import math

valorA = input('Qual o valor A?')
valorB = input('Qual o valor B?')
valorC = input('Qual o valor C?')
xis = valorB*(-1)+math.sqrt(valorB*valorB - 4*valorA*valorC)

valorA*(xis*xis)+valorB*xis+valorC == 0
