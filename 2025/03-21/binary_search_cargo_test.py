# 파일명: binary_search_cargo_test.py
"""
📝 문제 설명
무게를 재는 저울이 하나 있다. 여러 개의 짐을 나눠서 배에 실어야 하는데,
각 짐의 무게는 배열 weights에 주어진다.
하나의 배는 한 번에 최대 k개의 짐만 실을 수 있고,
짐을 실었을 때 총 무게의 최댓값을 최소화하고 싶다.

이때 가능한 최솟값을 찾아라.

weights: 짐들의 무게 배열 (1 ≤ len(weights) ≤ 10^4)
k: 한 배에 실을 수 있는 최대 짐 개수 (1 ≤ k ≤ len(weights))
"""


def min_max_weight(weights, k):  # 최댓 값을 최소화
    # weights.sort(key=lambda x: x, reverse=True)  # 무게를 오름차순
    left = max(weights)  # 가장 무거운 짐 하나 (무조건 실어야 함)
    right = sum(weights)  # 전체 짐을 한 배에 다 실었을 때 총 합

    def can_divide(weights, k, max_limit):  # 특정 최대 무게 mid로 나눌수있는지 판별하는 함수 만들기
        # k : 최대 짐 개수

        count = 1  # 필요한 배의 수
        total = 0  # 현재 배의 무게 합
        for w in weights:
            if w > max_limit:  # 이 조건을 추가!
                return False  # mid로는 절대 안됨

            if total + w > max_limit:
                count += 1
                total = w  # 다음 배로 넘김
            else:
                total += w
        return count <= k

    answer = right

    while left <= right:
        mid = (left + right) // 2
        if can_divide(weights, k, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


def test_min_max_weight():
    tests = [
        {"index": 1, "weights": [3, 1, 4, 3, 2], "k": 3, "want": 5},
        {"index": 2, "weights": [5, 5, 5, 5], "k": 2, "want": 10},
        {"index": 3, "weights": [1, 2, 3, 4, 5], "k": 3, "want": 6},
        {"index": 4, "weights": [10, 20, 30], "k": 1, "want": 60},
        {"index": 5, "weights": [7, 2, 5, 10, 8], "k": 2, "want": 18},
        {"index": 6, "weights": [1, 1, 1, 1, 1, 1], "k": 2, "want": 3},
        {"index": 7, "weights": [10, 10, 10, 10], "k": 4, "want": 10},
        {"index": 8, "weights": [10, 20, 30, 40, 50], "k": 5, "want": 50},
        {"index": 9, "weights": [10, 10, 10, 10], "k": 1, "want": 40},
        {"index": 10, "weights": [2, 2, 2, 2, 2], "k": 2, "want": 6},
    ]

    for test in tests:
        got = min_max_weight(test["weights"], test["k"])
        if got != test["want"]:
            print(f"❌ 실패: 테스트 {test['index']} - got {got}, expected {test['want']}")
        else:
            print(f"✅ 성공: 테스트 {test['index']} - got {got}")


# ✅ 테스트 실행
test_min_max_weight()
