# Recap of all the lectures in Variables

# I needed to convert the money I have in different currencies to dollars
# I have pesos, soles and reais
pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

dollar_pesos = pesos / 19.63
dollar_soles = soles / 3.68
dollar_reais = reais / 5.68

total_dollars = dollar_pesos + dollar_soles + dollar_reais

print(total_dollars)