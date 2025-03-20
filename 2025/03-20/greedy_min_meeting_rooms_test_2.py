import heapq  # 우선순위 큐 사용을 위한 heapq 모듈

def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x:x[0])

    ongoing_end = []
    for s,e in meetings:
        if ongoing_end and ongoing_end[0] <= s : # 지금 시작시간이 전끝나는시간보다 크거나 같으면
            heapq.heappop(ongoing_end)
        heapq.heappush(ongoing_end, e)
        print(s,e)



    return len(ongoing_end)  # 임시값

# 테스트 코드
def test_min_meeting_rooms():
    # 예시 테스트 케이스
    meetings = [(0, 30), (5, 10), (15, 20)]
    result = min_meeting_rooms(meetings)
    assert result == 2, f"1Expected 2, but got {result}"

    meetings = [(7, 10), (2, 4)]
    result = min_meeting_rooms(meetings)
    assert result == 1, f"2Expected 1, but got {result}"

    meetings = [(1, 5), (2, 6), (3, 7), (4, 8)]
    result = min_meeting_rooms(meetings)
    assert result == 4, f"Expected 4, but got {result}"

    meetings = [(1, 2), (2, 3), (3, 4), (4, 5)]
    result = min_meeting_rooms(meetings)
    assert result == 1, f"Expected 1, but got {result}"

    print("🎉 모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_min_meeting_rooms()
