import os
from datetime import datetime

def create_today_folder(base_path: str) -> None:
    # 현재 날짜 가져오기
    now = datetime.now()
    year = now.strftime("%Y")      # 연도 (YYYY)
    month_day = now.strftime("%m-%d")  # 월-일 (MM-DD)

    # 연도 폴더 경로
    year_path = os.path.join(base_path, year)
    # 오늘 날짜 폴더 경로
    today_path = os.path.join(year_path, month_day)

    # 연도 폴더가 없으면 생성
    if not os.path.exists(year_path):
        try:
            os.mkdir(year_path)
        except OSError as e:
            print(f"연도 폴더 생성 실패: {e}")
            return

    # 오늘 날짜 폴더가 없으면 생성
    if not os.path.exists(today_path):
        try:
            os.mkdir(today_path)
        except OSError as e:
            print(f"오늘 날짜 폴더 생성 실패: {e}")
            return

    print(f"폴더 생성 완료: {today_path}")

def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 F9을(를) 누릅니다.

# 예시로 현재 디렉토리에 폴더 생성
if __name__ == '__main__':
    print_hi('PyCharm')
    create_today_folder(".")
