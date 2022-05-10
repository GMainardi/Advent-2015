import enum


input = [line for line in open('input.txt', 'r')]

input = [c for c in input[0]]

floor = 0

for i, e in enumerate(input):
    if e == '(':
        floor += 1
    elif e == ')':
        floor -= 1
    if floor == -1:
        print(i+1)
        break
