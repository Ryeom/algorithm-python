def max_meetings(meetings):
    meetings.sort(key=lambda x: x[1])
    print(meetings)

    count = 0
    prev_end = 0
    for start, end in meetings:
        if prev_end <= start:
            count += 1
            prev_end = end

    return count


def test_max_meetings():
    tests = [
        {"index": 1, "meetings": [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)], "want": 3},
        {"index": 2, "meetings": [(1, 2), (2, 3), (3, 4), (4, 5)], "want": 4},
        {"index": 3, "meetings": [(1, 10), (2, 3), (3, 4), (4, 5)], "want": 3},
        {"index": 4, "meetings": [(1, 5), (2, 6), (3, 7), (4, 8)], "want": 1},
        {"index": 5, "meetings": [(0, 30), (5, 10), (15, 20)], "want": 2},
    ]

    for t in tests:
        got = max_meetings(t["meetings"])
        if got != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - max_meetings({t['meetings']}) = {got}; expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")


if __name__ == "__main__":
    test_max_meetings()
