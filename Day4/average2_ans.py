"""average2_ans.py

    Read the numbers and find the count, sum, lowest, highest, mean and median. Sort the list without list.sort().

"""

__author__ = "maydee"


numbers = []
total = 0
lowest = None
highest = None

while True:
    try:
        line = input("enter a number or Enter to finish: ")
        if not line:
            break
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

print("numbers:", numbers)
if numbers:
    for i in range(len(numbers) - 1, 1, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j + 1], numbers[j] = numbers[j], numbers[j + 1]
    if len(numbers) % 2 != 0:
        median = numbers[len(numbers)//2]
    else:
        median = (numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1]) / 2
    print("count =", len(numbers), "sum =", total,
          "lowest =", lowest, "highest =", highest,
          "mean =", total / len(numbers), "median =", median)