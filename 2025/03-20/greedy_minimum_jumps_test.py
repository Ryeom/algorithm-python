def min_jumps(nums):
    if len(nums) ==0 :
        return 0
    count =0 #점프횟수
    cur = 0
    maxReach = nums[0]  # 현재 점프에서 도달할 수 있는 최대 인덱스
    step = nums[0]  # 현재 점프에서 남은 이동 가능 횟수

    for i in range(1,len(nums)):
        if i==len(nums) -1:
            return count+1
        maxReach = max(maxReach,i+nums[i]) # 최대 도달 가능 위치 업데이트
        # 이동할 수 있는 남은 스텝 감소
        step -= 1

        # 스텝이 0이 되면 점프해야 함
        if step == 0:
            count += 1
            step = maxReach - i  # 새로운 점프의 이동 가능 횟수 업데이트

    return count  # 임시값

# 테스트 코드
def test_min_jumps():
    # 예시 테스트 케이스
    nums = [2, 3, 1, 1, 4]
    result = min_jumps(nums)
    assert result == 2, f"Expected 2, but got {result}"

    nums = [2, 3, 0, 1, 4]
    result = min_jumps(nums)
    assert result == 2, f"Expected 2, but got {result}"

    nums = [1, 1, 1, 1, 1]
    result = min_jumps(nums)
    assert result == 4, f"Expected 4, but got {result}"

    nums = [10, 1, 1, 1, 1]
    result = min_jumps(nums)
    assert result == 1, f"Expected 1, but got {result}"

    print("모든 테스트 케이스가 통과했습니다!")

# 테스트 실행
test_min_jumps()
