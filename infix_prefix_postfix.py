def priority(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/' or op == '%':
        return 2
    elif op == '^':
        return 3
    else:
        return 0


def infix_to_prefix(exp):
    exp = exp[::-1]
    stack = []
    pre_Exp = ""
    i = 0
    while i in range(0, len(exp)):
        if exp[i].isalpha():
            pre_Exp += exp[i]
        elif exp[i] == ')' or exp[i] == ']' or exp[i] == '}':
            stack.append(exp[i])
        elif exp[i] == '(' or exp[i] == '[' or exp[i] == '{':
            if exp[i] == '(':
                while stack[-1] != ')':
                    pre_Exp += stack.pop()
                stack.pop()
            if exp[i] == '[':
                while stack[-1] != ']':
                    pre_Exp += stack.pop()
                stack.pop()
            if exp[i] == '{':
                while stack[-1] != '}':
                    pre_Exp += stack.pop()
                stack.pop()
        else:
            if len(stack) == 0:
                stack.append(exp[i])
            else:
                if priority(exp[i]) >= priority(stack[-1]):
                    stack.extend(exp[i])
                elif priority(exp[i]) < priority(stack[-1]):
                    pre_Exp += stack.pop()
                    pos = len(stack) - 1
                    while pos >= 0 and priority(stack[pos]) > priority(exp[i]):
                        pre_Exp += stack.pop()
                        pos -= 1
                        if pos < 0:
                            break
                    stack.extend(exp[i])
        i += 1
    while len(stack) != 0:
        pre_Exp += stack.pop()
    return pre_Exp[::-1]

def infix_to_postfix(exp):
    stack = []
    post_Exp = ""
    i = 0
    while i in range(0, len(exp)):
        if exp[i].isalpha():
            post_Exp += exp[i]
        elif exp[i] == '(' or exp[i] == '[' or exp[i] == '{':
            stack.append(exp[i])
        elif exp[i] == ')' or exp[i] == ']' or exp[i] == '}':
            if exp[i] == ')':
                while stack[-1] != '(':
                    post_Exp += stack.pop()
                stack.pop()
            if exp[i] == ']':
                while stack[-1] != '[':
                    post_Exp += stack.pop()
                stack.pop()
            if exp[i] == '}':
                while stack[-1] != '{':
                    post_Exp += stack.pop()
                stack.pop()
        else:
            if len(stack) == 0:
                stack.append(exp[i])
            else:
                if priority(exp[i]) > priority(stack[-1]):
                    stack.extend(exp[i])
                elif priority(exp[i]) <= priority(stack[-1]):
                    post_Exp += stack.pop()
                    pos = len(stack) - 1
                    while pos >= 0 and priority(stack[pos]) == priority(exp[i]):
                        post_Exp += stack.pop()
                        pos -= 1
                        if pos < 0:
                            break
                    stack.extend(exp[i])
        i += 1
    while len(stack) != 0:
        post_Exp += stack.pop()
    return post_Exp


if __name__ == '__main__':
    choice = input('Enter your choice: ')
    if choice == 'console':
        exp = input('Enter an infix expression: ')
        ask = input('Convert to prefix or postfix? ')
        if ask == 'prefix':
            infix_to_prefix(exp)
        elif ask == 'postfix':
            infix_to_postfix(exp)

    elif choice == 'file':
        path = input("Enter path of the file: ")
        with open('exp.txt', 'r') as f:
            exp = f.read()
        ask = input('Convert to prefix or postfix? ')
        if ask == 'prefix':
            infix_to_prefix(exp)
        elif ask == 'postfix':
            infix_to_postfix(exp)
    elif choice == 'exit':
        exit()