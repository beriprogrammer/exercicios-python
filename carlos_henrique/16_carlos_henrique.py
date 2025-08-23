true = True
false = False

out = true or true
out1 = true or false
out2 = false or true
out3 = false or false

print('\n',6*' ', 'OR truth table')

print(32*'-')
print(f'|    A    |    B   |  A OR B   |')
print(32*'-')
print(f'|  true   |  true  |   {out}    |')
print(32*'-')
print(f'|  true   |  false |   {out1}    |')
print(32*'-')
print(f'|  false  |  true  |   {out2}    |')
print(32*'-')
print(f'|  false  |  false |   {out3}   |')
print(32*'-')

