import sys
import numpy as np

def AND_simple(x1, x2) -> int:
    """
    구현은 간단하지만, 
    θ가 조건문에서 하드코딩이 되어서 학습에서 유용하게 사용할 수 없음
    → 편향이 명시적으로 들어나지 않음
    y = { 0  ( x1*w1 + x2*w2 ≤ θ )
        { 1  ( w1*w1 + w2*w2 > θ )
    """
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = (x1 * w1) + (x2 * w2)
    if tmp <= theta:
        return 0
    else:
        return 1
    
def AND(x1, x2) -> int:
    """
    AND_simple에서 편향이 명시적으로 들어나지 않은 현상을 해결한 코드
    θ를 b로 표현함으로써 가중치로써 동일한 취급이 가능해 수학적으로 분리가 가능해짐
    b = -θ
    y = { 0  ( b + x1*w1 + x2*w2 ≤ 0 )
        { 1  ( b + w1*w1 + w2*w2 > 0 )    
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2) -> int:
    """
    NAND는 AND의 가중치가 반대로 변경된 형태
    """
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2) -> int:
    """
    OR은 AND에서 b만 변경
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def main():
    argv = sys.argv

    match argv[1]:
        case '0':
            # AND_simple 예시
            print(f"AND_simple(0, 0) = {AND_simple(0, 0)}")
            print(f"AND_simple(1, 0) = {AND_simple(1, 0)}")
            print(f"AND_simple(0, 1) = {AND_simple(0, 1)}")
            print(f"AND_simple(1, 1) = {AND_simple(1, 1)}")
        case '1':
            # AND 예시
            print(f"AND(0, 0) = {AND(0, 0)}")
            print(f"AND(1, 0) = {AND(1, 0)}")
            print(f"AND(0, 1) = {AND(0, 1)}")
            print(f"AND(1, 1) = {AND(1, 1)}")
        case '2':
            # NAND 예시
            print(f"NAND(0, 0) = {NAND(0, 0)}")
            print(f"NAND(1, 0) = {NAND(1, 0)}")
            print(f"NAND(0, 1) = {NAND(0, 1)}")
            print(f"NAND(1, 1) = {NAND(1, 1)}")
        case '3':
            # OR 예시
            print(f"OR(0, 0) = {OR(0, 0)}")
            print(f"OR(1, 0) = {OR(1, 0)}")
            print(f"OR(0, 1) = {OR(0, 1)}")
            print(f"OR(1, 1) = {OR(1, 1)}")
        case _:
            print("잘못된 입력입니다.")

# main
if __name__ == '__main__':
    main()
