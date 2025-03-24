# 활동 최대 가치 선택 문제 (Weighted Activity Selection)
import bisect
import heapq


def max_total_value(activities):
    activities.sort(key=lambda x: x[1])  # 종료시간 기준

    ends = [end for _, end, _ in activities]  # 종료시간 리스트
    n = len(activities)
    dp = [0] * n
    for i in range(n):
        start, end, value = activities[i]
        j = bisect.bisect_right(ends, start) - 1
        if j != -1:
            include_value = value + dp[j]
        else:
            include_value = value

        dp[i] = max(dp[i - 1], include_value) if i > 0 else include_value

    return dp[-1]


def test_max_total_value():
    tests = [
        {
            "index": 1,
            "activities": [(1, 3, 50), (2, 5, 20), (4, 6, 70), (6, 7, 60)],
            "want": 180,
        },
        {
            "index": 2,
            "activities": [(1, 2, 30), (2, 3, 40), (3, 4, 50), (4, 5, 60)],
            "want": 180,
        },
        {
            "index": 3,
            "activities": [(1, 4, 100), (2, 3, 50), (3, 5, 70)],
            "want": 120,
        },
        {
            "index": 4,
            "activities": [(1, 10, 500), (2, 3, 200), (4, 5, 200), (6, 7, 200)],
            "want": 600,
        },
        {
            "index": 5,
            "activities": [(1, 3, 100), (3, 5, 100), (5, 7, 100), (0, 10, 290)],
            "want": 300,
        },
    ]

    for t in tests:
        got = max_total_value(t["activities"])
        if got != t["want"]:
            print(f"❌ 실패: 테스트 {t['index']} - got {got}; expected {t['want']}")
        else:
            print(f"✅ 성공: 테스트 {t['index']} - got = {got}")


if __name__ == "__main__":
    test_max_total_value()
