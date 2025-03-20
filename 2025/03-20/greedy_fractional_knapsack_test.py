def fractional_knapsack(items, capacity):
    # 1️⃣ 가치 대비 무게 비율이 높은 순으로 정렬
    items = sorted(items, key=lambda x: x[0] / x[1], reverse=True)

    result_value = 0.0  # 배낭에 담긴 총 가치
    remaining_capacity = capacity  # ✅ 배낭의 남은 용량

    print(f"초기 상태: {items}, capacity={capacity}")

    for value, weight in items:
        print(f"현재 물건: (가치={value}, 무게={weight}), 남은 용량={remaining_capacity}")

        if weight <= remaining_capacity:
            # 2️⃣ 전체 아이템을 배낭에 넣을 수 있는 경우
            remaining_capacity -= weight
            result_value += value
            print(f"✔ 전체 담기: 현재 가치={result_value}, 남은 용량={remaining_capacity}")
        else:
            # 3️⃣ 일부만 담아야 하는 경우 (Fractional)
            result_value += (value / weight) * remaining_capacity  # ✅ 일부 담기
            print(f"⚠ 부분 담기: 추가된 가치={(value / weight) * remaining_capacity}, 총 가치={result_value}")
            break  # ✅ 배낭이 꽉 찼으므로 종료

    print(f"최종 가치: {result_value}")
    return result_value  # 배낭의 총 가치 반환



def test_fractional_knapsack():
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50
    result = fractional_knapsack(items, capacity)
    assert abs(result - 240.0) < 1e-6, f"Expected 240.0, but got {result}"

    items = [(500, 30), (200, 10), (300, 20)]
    capacity = 50
    result = fractional_knapsack(items, capacity)
    assert abs(result - 850.0) < 1e-6, f"Expected 800.0, but got {result}"

    items = [(100, 10), (150, 20), (200, 30)]
    capacity = 25
    result = fractional_knapsack(items, capacity)
    assert abs(result - 212.5) < 1e-6, f"Expected 212.5, but got {result}"

    items = [(40, 5), (100, 20), (50, 10)]
    capacity = 20
    result = fractional_knapsack(items, capacity)
    assert abs(result - 115.0) < 1e-6, f"Expected 90.0, but got {result}"

    print("🎉 모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_fractional_knapsack()
