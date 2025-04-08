# 그리디 - 정기권 도둑

# n : 버스 타는 횟수
# k : 버스 정기 요금 (버스를 탄 구간의 총 요금이 k원보다 크면 이득)
# fares : n개의 버스 요금
def min_total_cost_with_pass(n, k, fares):
    total = sum(fares)
    max_saved = 0
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += fares[right]

        # 구간합이 K보다 작거나 같을 때까지 확장 (절약 불가)
        while current_sum > k:
            saved = current_sum - k
            max_saved = max(max_saved, saved)
            current_sum -= fares[left]
            left += 1

    return total - max_saved


# 테스트
def test():
    tests = [
        ((7, 100, [20, 30, 50, 90, 10, 60, 30]), 200),
        ((4, 100, [10, 20, 30, 40]), 100),
        ((5, 50, [10, 20, 30, 40, 50]), 100),
        ((1, 10, [5]), 5),
        ((1, 10, [15]), 10),
        ((3, 30, [20, 20, 20]), 50),
        ((6, 70, [10, 20, 30, 40, 50, 60]), 140),
        ((10, 100, [1,2,3,4,5,6,7,8,9,10]), 45),
        ((10, 200, [1,1,1,1,1,1,1,1,1,1]), 10),
        ((5, 60, [60, 60, 60, 60, 60]), 180),
    ]
    for i, ((n, k, fares), expected) in enumerate(tests):
        result = min_total_cost_with_pass(n, k, fares)
        print(f"Test {i}: {'✅' if result == expected else '❌'} (Expected: {expected}, Got: {result})")

test()
