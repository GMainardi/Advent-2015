input = [list(map(lambda x : int(x), line.split('x'))) for line in open('input.txt', 'r')]

total = 0

for prism in input:
    l, w, h = prism
    
    lower = min(prism)
    mid = sum(prism) - lower - max(prism)

    total += 2*lower + 2*mid + l*w*h

print(total)