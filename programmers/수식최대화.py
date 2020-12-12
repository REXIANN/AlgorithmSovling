from itertools import permutations

# define calc function
def calc(array, operand):
    stack = []
    array = array[::-1]
    #print('calc', array, operand)
    while array:
        elem = array.pop()
        if elem == operand:
            first_num = stack.pop()
            second_num = array.pop()
            result = eval(str(first_num) + operand + str(second_num))
            stack.append(result)
        else:
            stack.append(elem)
    return stack[::-1]


def solution(expression):
    answer = []
    head, tail = 0, 0
    while head < len(expression):
        if expression[head] in "+-*":
            answer.append(int(expression[tail: head]))
            answer.append(expression[head])
            head, tail = head + 1, head + 1
        else:
            head += 1
    answer.append(int(expression[tail:head]))
    #print('sol', answer)

    max_value = 0
    for permutation in permutations('+-*'):
        array = answer[:]
        for operand in permutation:
            array = calc(array, operand)

        value = abs(array[0])    
        max_value = value if value > max_value else max_value
    return max_value


expression = "100-200*300-500+20"
print(solution(expression))