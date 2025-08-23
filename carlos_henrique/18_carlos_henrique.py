true = True
false = False

out = not(true ^ true)
out1 = not(true ^ false)
out2 = not(false ^ true)
out3 = not(false ^ false)

print('\n',6*' ', 'NXOR truth table')

print(32*'-')
print(f'|    A    |    B   | XNOR(A,B) |')
print(32*'-')
print(f'|  true   |  true  |   {out}    |')
print(32*'-')
print(f'|  true   |  false |   {out1}   |')
print(32*'-')
print(f'|  false  |  true  |   {out2}   |')
print(32*'-')
print(f'|  false  |  false |   {out3}    |')
print(32*'-')

