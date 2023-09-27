def arithmetic_arranger(problems, show_answers=False):
    result = ""
    try:
        check_for_errors(problems)
        lines = []
        lines.append(write_first_line(problems))
        lines.append(write_second_line(problems))
        lines.append(write_third_line(problems))
        if show_answers == True:
            answers = calculate_answers(problems)
            lines.append(write_fouth_line(problems,answers))
        result = "\n".join(lines)
    except Exception as e:
        result = str(e)
    return result

def check_for_errors(problems):
    if len(problems) > 5:
        raise Exception("Error: Too many problems.")
    for problem in problems:
        operands = problem.split()
        if not operands[0].isnumeric() or not operands[2].isnumeric():
            raise Exception("Error: Numbers must only contain digits.")
        if len(operands[0]) > 4 or len(operands[2]) > 4:
            raise Exception("Error: Numbers cannot be more than four digits.")
        if operands[1] not in ["+", "-"]:
            raise Exception("Error: Operator must be '+' or '-'.")

def calculate_answers(problems):
    answers = []
    for problem in problems:
        operands = problem.split()
        if operands[1] == "+":
            answer = int(operands[0]) + int(operands[2])
        elif operands[1] == "-":
            answer = int(operands[0]) - int(operands[2])
        answers.append(str(answer))
    return answers

def write_first_line(problems):
    first_line = ""
    for i,problem in enumerate(problems):
        if i != 0:
            first_line += " "*4
        operands = problem.split()
        column_width = max(len(operands[0]), len(operands[2])) + 2
        first_line += " "*(column_width-len(operands[0])) + operands[0]
    return first_line

def write_second_line(problems):
    second_line = ""
    for i,problem in enumerate(problems):
        if i != 0:
            second_line += " "*4
        operands = problem.split()
        column_width = max(len(operands[0]), len(operands[2])) + 2
        second_line += operands[1]+" "*(column_width-len(operands[2])-len(operands[1])) + operands[2]
    return second_line

def write_third_line(problems):
    third_line = ""
    for i,problem in enumerate(problems):
        if i != 0:
            third_line += " "*4
        operands = problem.split()
        column_width = max(len(operands[0]), len(operands[2])) + 2
        third_line += "-"*column_width
    return third_line

def write_fouth_line(problems,answers):
    fourt_line = ""
    for i,problem in enumerate(problems):
        if i != 0:
            fourt_line += " "*4
        operands = problem.split()
        column_width = max(len(operands[0]), len(operands[2])) + 2
        fourt_line += " "*(column_width-len(answers[i])) + answers[i]
    return fourt_line