def solution(array, height):
    tall = 0
    
    for i in array:
        if (i - height) > 0:
            tall += 1
        else:
            pass
    return tall
    