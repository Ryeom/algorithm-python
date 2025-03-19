def extract_numbers(s):
    res = []
    for n in s:
        if n.isdigit():
            res.append(int(n))
    return res  # 임시값
#  return [int(c) for c in s if c.isdigit()]

# 테스트
def test_extract_numbers():
    s = "abc123def456"
    result = extract_numbers(s)
    assert result == [1, 2, 3, 4, 5, 6], f"Expected [1, 2, 3, 4, 5, 6], but got {result}"

    s = "no numbers here"
    result = extract_numbers(s)
    assert result == [], f"Expected [], but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_extract_numbers()
