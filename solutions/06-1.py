with open("inputs/06-input.txt") as f:
    lines = f.read().splitlines()

dp = 0
size = 130
gp = tuple()
direction = "up"

for i in range(size):
    if "^" in lines[i]:
        j = lines[i].index("^")
        gp = (i,j)


def find_next_position():
    global gp
    global direction
    print(gp)
    if direction == "up":
        next = lines[gp[0] + 1][gp[1]]
    if direction == "right":
        next = lines[gp[0]][gp[1] + 1]
    if direction == "down":
        next = lines[gp[0] - 1][gp[1]]
    if direction == "left":
        next = lines[gp[0] + 1][gp[1] - 1]

    if next == "#":
        changedir()
    

    if direction == "up":
        gp =  (gp[0] + 1, gp[1])
    if direction == "right":
        gp =  (gp[0] + 1, gp[1])
    if direction == "down":
        gp =  (gp[0] + 1, gp[1])
    if direction == "left":
        gp =  (gp[0] + 1, gp[1])

def changedir():
    global direction
    if direction == "up":
        direction = "right"
    if direction == "right":
        direction = "down"

    if direction == "down":
        direction = "left"

    if direction == "left":
        direction = "up"

# print(lines[gp[0]][gp[1]])

while True:
    if gp[0] > 130 or gp[1] > 130:
        break

    current = lines[gp[0]][gp[1]]

    if current != "0":
        dp += 1
    
    lines[gp[0]] = lines[gp[0]][:gp[1]] + "0" + lines[gp[0]][gp[1] + 1:]
    print(gp)
    find_next_position()

print(dp)