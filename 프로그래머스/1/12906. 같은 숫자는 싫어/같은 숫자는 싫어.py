def solution(arr):
    sorted_arr = [arr[0]]   # 기존 배열의 첫 번째 요소를 저장할 배열에 추가
    
    # 기존 배열의 두 번째 요소부터 비교하며 중복 값 제거
    for num in range(1, len(arr)):
        if arr[num] != arr[num - 1]:
            sorted_arr.append(arr[num]) # 직전의 숫자와 다르면 저장할 배열 끝에 추가
    return sorted_arr
