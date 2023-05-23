import copy

cal = open('calories', 'r')

count = 1
calories_per_elf = {}

for line in cal:
    if line != '\n':
        if count in calories_per_elf:
            calories_per_elf[count].append(int(line))
        else:
            calories_per_elf[count] = [int(line)]
        # print(calories_per_elf[count])
    else:
        count += 1
sum_calories_per_elf = dict([(key, sum(values)) for key, values in calories_per_elf.items()])
# print(sum_calories_per_elf)
max_key = max(sum_calories_per_elf, key=sum_calories_per_elf.get)
print(sum_calories_per_elf[max_key])

# Teil 2

calories_part_two = copy.deepcopy(sum_calories_per_elf)
top_three_elves = []
while len(top_three_elves) < 3:
    max_calories = max(calories_part_two, key=calories_part_two.get)
    top_three_elves.append(calories_part_two[max_calories])
    calories_part_two[max_calories] = 0
print(top_three_elves)

sum_top_three_elves = 0
for element in range(0, len(top_three_elves)):
    sum_top_three_elves = sum_top_three_elves + top_three_elves[element]
print(sum_top_three_elves)
print("test")
