true = True
false = False

out = true ^ true
out1 = true ^ false
out2 = false ^ true
out3 = false ^ false

print('\n',4*' ', 'XOR truth table\n',4*' ',15*'-')

print(29*'-')
print(f'| true   XOR  true  | {out} |')
print(29*'-')
print(f'| true   XOR  false | {out1}  |')
print(29*'-')
print(f'| false  XOR  true  | {out2}  |')
print(29*'-')
print(f'| false  XOR  false | {out3} |')
print(29*'-')

