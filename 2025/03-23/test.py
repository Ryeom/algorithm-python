"""
파이썬 문법
https://github.com/VSFe/Algorithm_Study/blob/main/Concept/Prev/vol.2/00_Special/Pythonic_Code_For_Coding_Test.md
"""

a = 5
for i in range(1, 2):
    for j in range(1, 5):
        a -= 1
        print(a)
        if a == 1:
            print("에이는 1이다")
            break

    else:
        print("어떨때 나오는건데 ")
# Some Code...
