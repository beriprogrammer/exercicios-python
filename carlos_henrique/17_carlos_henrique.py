true = True
false = False

out = (true ^ true)
out1 = (true ^ false)
out2 = (false ^ true)
out3 = (false ^ false)

print('\n',6*' ', 'XOR truth table')

print(32*'-')
print(f'|    A    |    B   |  XOR(A,B) |')
print(32*'-')
print(f'|  true   |  true  |   {out}   |')
print(32*'-')
print(f'|  true   |  false |   {out1}    |')
print(32*'-')
print(f'|  false  |  true  |   {out2}    |')
print(32*'-')
print(f'|  false  |  false |   {out3}   |')
print(32*'-')

