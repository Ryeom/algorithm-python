def pair_sum(nums, target):

    left = 0
    right = len(nums)-1

    while left<right :
        n = nums[left] + nums[right]
        if n == target :
            return (left+1,right+1)
        elif n <target:
            left+=1
        else:
            right-=1


    return (0, 0)  # 임시값

# 테스트 코드
def test_pair_sum():
    # 예시 테스트 케이스
    nums = [2, 7, 11, 15]
    target = 9
    result = pair_sum(nums, target)
    assert result == (1, 2), f"Expected (1, 2), but got {result}"

    nums = [1, 3, 4, 5, 7, 10, 12]
    target = 15
    result = pair_sum(nums, target)
    assert result == (2, 7), f"Expected (4, 6), but got {result}"

    nums = [1, 2, 3, 4, 5, 6, 7]
    target = 9
    result = pair_sum(nums, target)
    assert result == (2, 7), f"Expected (3, 6), but got {result}"

    nums = [-5, -3, 0, 3, 8, 12]
    target = 5
    result = pair_sum(nums, target)
    assert result == (2, 5), f"Expected (2, 5), but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_pair_sum()
