def min_boats(people, limit):
    people.sort(key=lambda x: x)
    print(people)
    count = 0  # 보트의 개수
    left = 0
    right = len(people) - 1

    while left <= right:
        if people[right] + people[left] <= limit:  # 제일 작은것과 제일큰거 합친게 가능
            count += 1
            left += 1
            right -= 1
        else:  # 제일큰거 하나만 태움
            count += 1
            right -= 1

    return count


def test_min_boats():
    tests = [
        {"index": 1, "people": [70, 50, 80, 50], "limit": 100, "want": 3},
        {"index": 2, "people": [40, 40, 40, 40], "limit": 80, "want": 2},
        {"index": 3, "people": [60, 80, 60], "limit": 120, "want": 2},
        {"index": 4, "people": [100, 100, 100], "limit": 100, "want": 3},
        {"index": 5, "people": [30, 40, 60, 70], "limit": 100, "want": 2},
    ]

    for t in tests:
        got = min_boats(t["people"], t["limit"])
        if got != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - min_boats({t['people']}, {t['limit']}) = {got}; expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")


if __name__ == "__main__":
    test_min_boats()
