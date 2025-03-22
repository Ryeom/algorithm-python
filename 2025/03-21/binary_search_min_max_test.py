# houses: 각 집의 좌표 (정렬되지 않음)
# c: 설치할 공유기 개수
"""
📘 문제 설명: 공유기 설치
N개의 집이 수직선 위에 존재할 때, 집에 공유기 C개를 설치하려고 한다.
가장 인접한 두 공유기 사이의 거리를 최대로 하여 설치하되, C개의 공유기를 모두 설치할 수 있는 가장 큰 거리를 구하시오.
-> 가능한 띄엄띄엄 공유기를 설치해라
"""


def max_min_distance(houses, c):
    houses.sort()

    def can_install(distance):
        count = 1
        last_pose = houses[0]
        print(f"\n✅ 거리 기준: {distance}")
        print(f"처음 설치: 집 위치 {last_pose} (count = {count})")

        for i in range(1, len(houses)):
            print(f"last_pose {last_pose} houses[i] {houses[i]} houses[i] - last_pose = {houses[i] - last_pose} → 집 위치 {houses[i]} 확인 중... ", end="")
            if houses[i] - last_pose >= distance:
                count += 1
                last_pose = houses[i]
                print(f"공유기 설치! (count = {count})")
            else:
                print("너무 가까워서 설치 X")

        print(f"총 설치된 공유기 개수: {count} (필요: {c})")
        return count >= c

    left = 1
    right = houses[-1] - houses[0]
    answer = 0

    print(f"\n🏠 집 위치들: {houses}")
    print(f"🔍 공유기 {c}대 설치 시작!\n")

    while left <= right:
        mid = (left + right) // 2
        if can_install(mid):
            answer = mid
            print(f"➡ 가능: 거리 {mid} → 더 넓은 거리 시도 (left={mid + 1})")
            left = mid + 1
        else:
            print(f"❌ 불가능: 거리 {mid} → 더 좁은 거리 시도 (right={mid - 1})")
            right = mid - 1

    print(f"\n✅ 최적 최소 거리 = {answer}")
    return answer


def test_max_min_distance():
    tests = [
        {"index": 1, "houses": [1, 2, 8, 4, 9], "c": 3, "want": 3},
        {"index": 2, "houses": [1, 2, 4, 8, 9], "c": 3, "want": 3},
        {"index": 3, "houses": [1, 3, 6, 10, 15], "c": 3, "want": 7},
        {"index": 4, "houses": [5, 17, 100, 111], "c": 2, "want": 106},
        {"index": 5, "houses": [1, 2, 3, 4, 5], "c": 2, "want": 4},
    ]

    for t in tests:
        result = max_min_distance(t["houses"], t["c"])
        if result != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - got {result}, expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got {result}")


if __name__ == "__main__":
    test_max_min_distance()
