def solution(n, k):
    total_amount = (12000 * n) + (2000 * k)
    service = int(n/10)
    if service > 0:
        total_amount -= (2000 * service)
        return total_amount
    else:
        return total_amount

