# 중위 -> 후위
def infix_(s):
    result = []
    stack = []
    priority = {'+': 1, '*': 2}

    for i in s:
        if i.isdigit():
            result.append(i)
        else:
            if not stack:
                stack.append(i)
            elif i =='*' or i == '+':
                while stack and priority[i]<=priority[stack[-1]]:
                    result.append(stack.pop())
                stack.append(i)
    while stack:
        result.append(stack.pop())
    return result

for test in range(10):
    num = int(input())
    s = input()
    post = infix_(s)        # 후위계산식

    cal = []
    for i in post:
        if i.isdigit():
            cal.append(int(i))
        elif i == '+':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(int(num1)+int(num2))
        elif i == '*':
            num1 = cal.pop()
            num2 = cal.pop()
            cal.append(int(num1)*int(num2))
    print(f'#{test+1}',end=' ')
    print(*cal)

