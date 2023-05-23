with open('Daten') as d:
    with open('zwischenschritt', 'w') as z:
        for x in d:
            menge = int(x) // 3 - 2
            z.write(str(menge) + '\n')
s = open('zwischenschritt', 'r')
su = s.read().split('\n')
su.pop()
summ = [int(string) for string in su]
summe1 = sum(summ)
print(summe1)
s.close()
with open('zwischenschritt') as d:
    with open('zwischenschritt2', 'w') as z:
        for x in d:
            if int(x) > 5:
             menge = int(x) // 3 - 2
             z.write(str(menge) + '\n')
s = open('zwischenschritt2', 'r')
su = s.read().split('\n')
su.pop()
summ = [int(string) for string in su]
summe2 = sum(summ)
with open('zwischenschritt2') as d:
    with open('zwischenschritt3', 'w') as z:
        for x in d:
            if int(x) > 5:
             menge = int(x) // 3 - 2
             z.write(str(menge) + '\n')
s = open('zwischenschritt3', 'r')
su = s.read().split('\n')
su.pop()
summ = [int(string) for string in su]
summe3 = sum(summ)
with open('zwischenschritt3') as d:
    with open('zwischenschritt4', 'w') as z:
        for x in d:
            if int(x) > 5:
             menge = int(x) // 3 - 2
             z.write(str(menge) + '\n')
s = open('zwischenschritt4', 'r')
su = s.read().split('\n')
su.pop()
summ = [int(string) for string in su]
summe4 = sum(summ)
with open('zwischenschritt4') as d:
    with open('zwischenschritt5', 'w') as z:
        for x in d:
            if int(x) > 5:
             menge = int(x) // 3 - 2
             z.write(str(menge) + '\n')
s = open('zwischenschritt5', 'r')
su = s.read().split('\n')
su.pop()
summ = [int(string) for string in su]
summe5 = sum(summ)
with open('zwischenschritt5') as d:
    with open('zwischenschritt6', 'w') as z:
        for x in d:
            if int(x) > 5:
             menge = int(x) // 3 - 2
             z.write(str(menge) + '\n')
s = open('zwischenschritt6', 'r')
su = s.read().split('\n')
su.pop()
summ = [int(string) for string in su]
summe6 = sum(summ)
with open('zwischenschritt6') as d:
    with open('zwischenschritt7', 'w') as z:
        for x in d:
            if int(x) > 5:
             menge = int(x) // 3 - 2
             z.write(str(menge) + '\n')
s = open('zwischenschritt7', 'r')
su = s.read().split('\n')
su.pop()
summ = [int(string) for string in su]
summe7 = sum(summ)
with open('zwischenschritt7') as d:
    with open('zwischenschritt8', 'w') as z:
        for x in d:
            if int(x) > 5:
             menge = int(x) // 3 - 2
             z.write(str(menge) + '\n')
s = open('zwischenschritt8', 'r')
su = s.read().split('\n')
su.pop()
summ = [int(string) for string in su]
summe8 = sum(summ)
with open('zwischenschritt8') as d:
    with open('zwischenschritt9', 'w') as z:
        for x in d:
            if int(x) > 5:
             menge = int(x) // 3 - 2
             z.write(str(menge) + '\n')
s = open('zwischenschritt9', 'r')
su = s.read().split('\n')
su.pop()
summ = [int(string) for string in su]
summe9 = sum(summ)
ges = summe1 + summe2 + summe3 + summe4 + summe5 + summe6 + summe7 + summe8 + summe9
print(ges)
s.close
# alles = 0
# fuel = 0
# with open('fuel', 'w') as m:
#  for x in summ:
#     if x > 0:
#      fuel = 0 + fuel
#      y = x // 3 - 2
#      while y > 5:
#       alles = y // 3 - 2
#       fuel = fuel + alles
#       y = alles
#     m.write(str(fuel) + '\n')
# s = open('fuel', 'r')
# su = s.read().split('\n')
# su.pop()
# summ = [int(string) for string in su]
# summe = sum(summ)
# print(summe + summe1)
# s.close()