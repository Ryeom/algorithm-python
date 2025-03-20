import heapq


def min_meeting_rooms(meetings):
    if not meetings:
        return 0

    meetings.sort(key=lambda x:x[0])
    min_heap = []
    for s, e in meetings:
        if min_heap and min_heap[0] <= s:
            heapq.heappop(min_heap)

        heapq.heappush(min_heap,e)

    return  len(min_heap) # 임시값

# 테스트 코드
def test_min_meeting_rooms():
    # 예시 테스트 케이스
    meetings = [(0, 30), (5, 10), (15, 20)]
    result = min_meeting_rooms(meetings)
    assert result == 2, f"Expected 2, but got {result}"

    meetings = [(7, 10), (2, 4)]
    result = min_meeting_rooms(meetings)
    assert result == 1, f"Expected 1, but got {result}"

    meetings = [(1, 5), (2, 6), (3, 7), (4, 8)]
    result = min_meeting_rooms(meetings)
    assert result == 4, f"Expected 4, but got {result}"

    meetings = [(1, 3), (3, 5), (5, 7), (7, 9)]
    result = min_meeting_rooms(meetings)
    assert result == 1, f"Expected 1, but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_min_meeting_rooms()
