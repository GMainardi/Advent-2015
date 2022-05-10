input = [line for line in open('input.txt', 'r')]

input = [c for c in input[0]]

floor = 0

for e in input:
    if e == '(':
        floor += 1
    if e == ')':
        floor -= 1

print(floor)