# Calculadora, recebe problemas e return resultados verticais 
# recebe na varável problems
# restorna na variável arranged_problems
# exemplo de entrada de problema: ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

problems = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]

def arithmetic_arranger(problems, status = False):

    #itialize variables
    numbers1 = []
    oper = []
    numbers2 = []

    if len(problems) > 5:
        return "Error: Too many problems."

    #loops trough values and Checks for errors
    for i in problems :
        problem = i.split()

        numbers1.append(problem[0])

        if problem[1] != "+" and problem[1] != "-":
            return "Error: Operator must be '+' or '-'."

        oper.append(problem[1])

        numbers2.append(problem[2])

        #Checks if the input are only numbers
        if not (problem[0].isdigit() and problem[2].isdigit()):
            return "Error: Numbers must only contain digits."

        #Checks lenght of given numbers 
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

    arranged_problems = ""

    #initialize rows 
    topRow = ""
    bottomRow = ""
    separator = ""
    totalLen = [0] * len(problems)
    resultsFormat = "\n"

    #Figures out the amount of spaces in top and bottom row by the lenght of the numbers 
    for i in range(len(problems)):
        if len(numbers1[i]) > len(numbers2[i]):
            totalLen[i] = len(numbers1[i]) + 2 
        
        else:
            totalLen[i] = len(numbers2[i]) + 2

        if i != 0 :

            topRow += "    "
            bottomRow += "    "
            separator += "    "

        #writes top row
        topRow += " " * (totalLen[i] - len(numbers1[i]))
        topRow += numbers1[i]

        #writes bottom row
        bottomRow += oper[i] + ( " " * (totalLen[i] - len(numbers2[i]) - 1))
        bottomRow += numbers2[i]
        
        #writes separator
        separator += "-" * totalLen[i]


    arranged_problems = "{}\n{}\n{}" .format(topRow, bottomRow, separator)
    
    #Calculates the results
    if status == True :
        
        for i in range(len(problems)):
            
            if oper[i] == "+":
                result = int(numbers1[i]) + int(numbers2[i])
            
            elif oper[i] == "-":
                result = int(numbers1[i]) - int(numbers2[i])

            result = str(result)

            totalSpace = totalLen[i]
            if i != 0 : totalSpace += 4

            resultsFormat += result.rjust(totalSpace)

        arranged_problems += resultsFormat
    return arranged_problems

print(arithmetic_arranger(problems, True))