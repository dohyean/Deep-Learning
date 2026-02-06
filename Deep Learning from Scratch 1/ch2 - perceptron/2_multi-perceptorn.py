from perceptron import AND, NAND, OR
import sys

def XOR(x1, x2):
    """
    기본적으로 XOR을 구현하기 위해서는 AND, NAND, OR 3가지를 활용할 수 있음
    XOR = (NAND ∩ OR)
    이런 구조를 다층 퍼셉트론이라고 명칭함
    """
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)

def main():
    argv = sys.argv

    match argv[1]:
        case '0':
            # XOR 예시
            print(f"XOR(0, 0) = {XOR(0, 0)}")
            print(f"XOR(1, 0) = {XOR(1, 0)}")
            print(f"XOR(0, 1) = {XOR(0, 1)}")
            print(f"XOR(1, 1) = {XOR(1, 1)}")
        case _:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()