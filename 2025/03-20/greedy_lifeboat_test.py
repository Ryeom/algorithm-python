import heapq


def min_boats(people, limit):
    people.sort()  # 몸무게 기준으로 정렬
    i, j = 0, len(people) - 1  # 투 포인터 (가벼운 사람, 무거운 사람)
    count = 0

    while i <= j:
        # TODO: 가장 가벼운 사람과 가장 무거운 사람이 함께 탈 수 있는지 체크
        if people[i] + people[j] > limit:
            count +=1
            j-=1
        elif people[i] + people[j] <= limit:
            count +=1
            j-=1
            i+=1



    return count

# 테스트 코드
def test_min_boats():
    # 예시 테스트 케이스
    people = [70, 50, 80, 50]
    limit = 100
    result = min_boats(people, limit)
    assert result == 3, f"Expected 3, but got {result}"

    people = [100, 200, 150, 80]
    limit = 200
    result = min_boats(people, limit)
    assert result == 3, f"Expected 3, but got {result}"

    people = [40, 50, 60, 90]
    limit = 100
    result = min_boats(people, limit)
    assert result == 3, f"Expected 3, but got {result}"

    people = [70, 80, 50]
    limit = 100
    result = min_boats(people, limit)
    assert result == 3, f"Expected 3, but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_min_boats()
