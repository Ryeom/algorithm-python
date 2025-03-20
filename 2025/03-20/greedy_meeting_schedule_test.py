def max_meetings(meetings):
    meetings.sort(key=lambda x: x[1])  # 끝나는 시간 기준 정렬

    count = 0
    prev_end = 0  # 마지막으로 선택된 회의 종료 시간
    selected_meetings = []  # 선택된 회의 리스트

    for start, end in meetings:
        if start >= prev_end:
            count += 1
            prev_end = end
            selected_meetings.append((start, end))

    print(f"선택된 회의: {selected_meetings}")
    return count


# 테스트 코드
def test_max_meetings():
    # 예시 테스트 케이스
    meetings = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    result = max_meetings(meetings)
    assert result == 3, f"Expected 4, but got {result}"

    meetings = [(1, 2), (2, 3), (3, 4), (4, 5)]
    result = max_meetings(meetings)
    assert result == 4, f"Expected 4, but got {result}"

    meetings = [(1, 10), (2, 3), (3, 4), (4, 5)]
    result = max_meetings(meetings)
    assert result == 3, f"Expected 3, but got {result}"

    meetings = [(1, 5), (2, 6), (3, 7), (4, 8)]
    result = max_meetings(meetings)
    assert result == 1, f"Expected 1, but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_max_meetings()
