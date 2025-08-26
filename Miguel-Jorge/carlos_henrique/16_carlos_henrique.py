true = True
false = False

out = true or true
out1 = true or false
out2 = false or true
out3 = false or false

print('\n',4*' ', 'OR truth table\n',4*' ',14*'-')

print(28*'-')
print(f'| true   OR  true  | {out}  |')
print(28*'-')
print(f'| true   OR  false | {out1}  |')
print(28*'-')
print(f'| false  OR  true  | {out2}  |')
print(28*'-')
print(f'| false  OR  false | {out3} |')
print(28*'-')

