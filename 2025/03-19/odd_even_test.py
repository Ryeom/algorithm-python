

def separate_odd_even(numbers):
    odd = []
    even = []
    for n in numbers:
        if n%2 ==0:
            even.append(n)
        else:
            odd.append(n)


    return odd, even  # 임시값


def test_separate_odd_even():
    tests = [
        {
            'index': 1,
            'numbers': [1, 2, 3, 4, 5, 6],
            'want_odd': [1, 3, 5],
            'want_even': [2, 4, 6]
        },
        {
            'index': 2,
            'numbers': [10, 15, 20, 25, 30],
            'want_odd': [15, 25],
            'want_even': [10, 20, 30]
        }
    ]

    for tt in tests:
        got_odd, got_even = separate_odd_even(tt['numbers'])
        if got_odd != tt['want_odd'] or got_even != tt['want_even']:
            print(
                f"❌ 실패: 테스트 {tt['index']} - separate_odd_even({tt['numbers']}) = {got_odd}, {got_even}; want {tt['want_odd']}, {tt['want_even']}")
        else:
            print(f"✅ 성공: 테스트 {tt['index']} - got = {got_odd}, {got_even}")


test_separate_odd_even()
