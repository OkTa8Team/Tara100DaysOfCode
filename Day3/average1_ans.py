"""average1_ans.py

    Takes the numbers from user, counts mean, highest, lowest and mean. Displays it.
    
"""

__author__ = "maydee"

numbers = []
total = 0
lowest = None
highest = None
count = 0
while True:
    try:
        line = input("enter a number or Enter to finish: ")
        if not line:
            break
        number = int(line)
        numbers.append(number)
        count += 1
        total += number
        if highest is None or number > highest:
            highest = number
        if lowest is None or number < lowest:
            lowest = number
    except ValueError as err:
        print(err)
print("numbers:", numbers)
print("count =", count, "sum =", total, "lowest =", lowest, "highest =", highest, "mean =", total/count)
