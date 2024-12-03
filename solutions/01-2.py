with open("inputs/01-input.txt") as f:
    lines = f.read().splitlines()

left = []
right = []
total = 0

for line in lines:
    a = int(line[0:8])
    b = int(line[8:14])

    left.append(a)
    right.append(b)

left = sorted(left)
right = sorted(right)

for a in left:
    for b in right:
        if a == b:
            total += a
        
        if a > b:
            continue

print(total)