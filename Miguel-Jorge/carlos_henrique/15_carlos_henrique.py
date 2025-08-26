true = True
false = False

out = true and true
out1 = true and false
out2 = false and true
out3 = false and false

print('\n',4*' ', 'AND truth table\n',4*' ',15*'-')

print(29*'-')
print(f'| true   AND  true  | {out}  |')
print(29*'-')
print(f'| true   AND  false | {out1} |')
print(29*'-')
print(f'| false  AND  true  | {out2} |')
print(29*'-')
print(f'| false  AND  false | {out3} |')
print(29*'-')

