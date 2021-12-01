""" Advent of Code 2021 """

file = open("AOC1", "r")
array = []
for line in file:
    num = int(line.rstrip())
    array.append(num)

first_tally = 0
second_tally = 0

for i in range(len(array) - 1):
    if (array[i] < array[i+1]):
        first_tally += 1

for j in range(len(array) - 3):
    if ((array[j] + array[j+1] + array[j+2]) < (array[j+1] + array[j+2] + array[j+3])):
        second_tally += 1

print(first_tally)
print(second_tally)