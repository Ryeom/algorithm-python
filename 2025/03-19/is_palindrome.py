def is_palindrome(s):
    return s==s[::-1]

# 테스트
def test_is_palindrome():
    s = "madam"
    result = is_palindrome(s)
    assert result == True, f"Expected True, but got {result}"

    s = "hello"
    result = is_palindrome(s)
    assert result == False, f"Expected False, but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_is_palindrome()
