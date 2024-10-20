def solution(s):
    # 공백으로 문자열 구분
    s = s.split()
    s_list = []
    for i in s:
        if i == 'Z':
            # Z일 경우 직전 숫자 제거
            # 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제(pop)
            s_list.pop()
        else:
            # Z가 아닐 경우 i에 해당되는 숫자 리스트 마지막에 추가(append)
            s_list.append(int(i))
    return sum(s_list)