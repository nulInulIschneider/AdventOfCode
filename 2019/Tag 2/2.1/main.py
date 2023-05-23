comp = open('Input', 'r')
for line in comp:
    uter = []
    for element in line[0:].split(','):
        uter.append(element)
uter = [int(i) for i in uter]
uter[1] = 12
uter[2] = 2
a = 0

while True:
    opcode = uter[a]
    if opcode == 1:
        d = uter[a + 1]
        e = uter[a + 2]
        b = uter[d] + uter[e]
        c = uter[a + 3]
        uter[c] = b
        a += 4
    if opcode == 2:
        d = uter[a + 1]
        e = uter[a + 2]
        b = uter[d] * uter[e]
        c = uter[a + 3]
        uter[c] = b
        a += 4
    if opcode == 99:
        break
print(uter[0])
comp.close()
comp = open('Input', 'r')
for line in comp:
    uter = []
    for element in line[0:].split(','):
        uter.append(element)
uter = [int(i) for i in uter]
uter[1] = 12
uter[2] = 2
a = 0
while True:
    opcode = uter[a]
    if opcode == 1:
        d = uter[a + 1]
        e = uter[a + 2]
        b = uter[d] + uter[e]
        c = uter[a + 3]
        uter[c] = b
        a += 4
    if opcode == 2:
        d = uter[a + 1]
        e = uter[a + 2]
        b = uter[d] * uter[e]
        c = uter[a + 3]
        uter[c] = b
        a += 4
    if opcode == 99:
        break
    if uter[0] == 19690720:
        break
    #a += 1
print(uter[0])
print(d)
print(e)

