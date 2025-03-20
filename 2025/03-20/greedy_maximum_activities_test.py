def max_activities(activities):
    activities.sort(key=lambda x:x[1])

    prev_end = 0
    count = 0
    for s,e in activities:
        if s >=prev_end: # 시작시간이 전끝시간보다 크거나 같을때
            count+=1
            prev_end = e


    return count 

# 테스트 코드
def test_max_activities():
    # 예시 테스트 케이스
    activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    result = max_activities(activities)
    assert result == 3, f"1Expected 4, but got {result}"

    activities = [(1, 2), (2, 3), (3, 4), (4, 5)]
    result = max_activities(activities)
    assert result == 4, f"2Expected 4, but got {result}"

    activities = [(1, 10), (2, 3), (3, 4), (4, 5)]
    result = max_activities(activities)
    assert result == 3, f"Expected 3, but got {result}"

    activities = [(1, 5), (2, 6), (3, 7), (4, 8)]
    result = max_activities(activities)
    assert result == 1, f"Expected 1, but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_max_activities()
