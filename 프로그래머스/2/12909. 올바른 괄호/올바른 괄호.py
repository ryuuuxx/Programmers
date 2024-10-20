def solution(s):
    stack = []  #스택 - 선입후출, 괄호 짝맞추기에 딱
    for char in s:
        if char == '(':  # 먼저 여는 괄호 스택에 추가
            stack.append(char)
        elif char == ')':  # 닫는 괄호로 짝맞추기
            if stack: 
                stack.pop() # 여는 괄호 존재시 제거(짝이 맞으므로)
            else: 
                return False
    return len(stack) == 0  # 괄호가 다 짝이 맞으면 stack은 비어있고 True
