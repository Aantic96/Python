import re

def calculate(num1, operator, num2):
    num1 = int(num1)
    num2 = int(num2)
    if operator == "+":
        result = num1 + num2
    else:
        result = num1 - num2
    return str(result)


def arithmetic_arranger(list_problems, solution = False):
    temp_list = []

    #Filling the temp list
    for item in list_problems:
        problem = item.split(" ")

        result = calculate(problem[0], problem[1], problem[2])

        len1 = len(problem[0])
        len2 = len(problem[2])

        if len1 >= len2:
            problem[2] = problem[2].rjust(len1)
            result = result.rjust(len1 + 2)
        else:
            problem[0] = problem[0].rjust(len2)
            result = result.rjust(len2 + 2)

        problem.append(result)
        temp_list.append(problem)

    row1 = ""
    row2 = ""
    row3 = ""
    row4 = ""

    for item in temp_list:
        row1 += "  " + item[0] + "    "
        row2 += item[1] + " " +  item[2] + "    "
        row3 += "-" * (len(item[0]) + 2) + "    " 
        row4 += item[3] + "    "

    print(row1)
    print(row2)
    print(row3)

    if solution == True:
        print(row4)


arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)