input = [list(map(lambda x : int(x), line.split('x'))) for line in open('input.txt', 'r')]

total = 0

for prism in input:
    l, w, h = prism

    lower = min(prism)
    mid = sum(prism) - lower - max(prism)

    total += 2*l*w + 2*w*h + 2*h*l + lower*mid

print(total)