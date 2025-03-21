import heapq


def min_meeting_rooms(meetings):
    meetings = sorted(meetings,key=lambda x:x[0])
    prev_end = []
    for s,e in meetings:
        if prev_end and prev_end[0]<=s: #시작시간이 앞시간끝나는 시간보다 클때
            heapq.heappop(prev_end)
        heapq.heappush(prev_end,e)
    return len(prev_end)

def test_min_meeting_rooms():
    tests = [
        {"index": 1, "meetings": [(0, 30), (5, 10), (15, 20)], "want": 2},
        {"index": 2, "meetings": [(7, 10), (2, 4)], "want": 1},
        {"index": 3, "meetings": [(1, 5), (2, 6), (3, 7), (4, 8)], "want": 4},
        {"index": 4, "meetings": [(6, 7), (2, 4), (8, 12)], "want": 1},
        {"index": 5, "meetings": [(1, 10), (2, 5), (6, 9), (8, 15)], "want": 3},
    ]

    for test in tests:
        got = min_meeting_rooms(test["meetings"])
        if got != test["want"]:
            print(f"❌ 실패: 테스트 {test['index']} - got {got}, expected {test['want']}")
        else:
            print(f"✅ 성공: 테스트 {test['index']} - got {got}")

# ✅ 테스트 실행
test_min_meeting_rooms()
