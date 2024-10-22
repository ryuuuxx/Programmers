from collections import deque
def solution(card1, card2, goal):
    # 스택과 큐 준비
    stack = card1[::-1]  # card1의 요소를 스택으로 (역순으로 처리)
    queue = deque(card2)  # card2의 요소를 큐로
    addlist = []  # card1 + card2 리스트

    # goal 리스트에 맞게 스택과 큐의 요소를 순차적으로 꺼내기
    for target in goal:
        if stack and stack[-1] == target:
            addlist.append(stack.pop())  # 스택의 요소가 goal과 같으면 pop
        elif queue and queue[0] == target:
            addlist.append(queue.popleft())  # 큐의 요소가 goal과 같으면 popleft
        else:
            # 현재 스택이나 큐의 요소가 goal의 현재 요소와 다르면 실패
            return "No"

    # 모두 처리한 후에 goal과 비교
    if addlist == goal:
        return "Yes"