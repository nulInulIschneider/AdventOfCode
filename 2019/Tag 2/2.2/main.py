comp = open('Input', 'r')
for line in comp:
    uter = []
    for element in line[0:].split(','):
        uter.append(element)
uter = [int(i) for i in uter]
copylist = open('Input', 'r')
for line in copylist:
    freshlist = []
    for element in line[0:].split(','):
        freshlist.append(element)
freshlist = [int(i) for i in freshlist]
a = 0
noun = uter[1]
verb = uter[2]
done = False
for noun in range(100):
  for verb in range(100):
    uter[2] = verb
    uter[1] = noun
    a = 0
    while a < len(uter):
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
    if uter [0] == 19690720:
        done = True
        print(uter[0])
        print(uter[1])
        print(uter[2])
        Answer = (100 * noun) + verb
        print(Answer)
    uter = [n for n in freshlist]
    if done:
        break
  if done:
    break
