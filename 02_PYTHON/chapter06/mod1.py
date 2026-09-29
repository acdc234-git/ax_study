def add(num1, num2):
    return num1 + num2

def minus(num1,num2):
    return num1-num2

VERSION = "1.0.0"


if __name__ == '__main__': # 터미널에서 파이썬을 실행하면
    print('모듈명:', __name__)

    result = add(10,20)
    print("결과: ", result)
