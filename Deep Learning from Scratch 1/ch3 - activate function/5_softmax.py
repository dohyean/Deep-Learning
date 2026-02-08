"""
softmax 함수
softmax를 구현할 때에는 결함이 있음 → 오버플로우에 의한 결함
지수 함수(exponential function)를 사용하기 때문에 큰 값이 자주 등장
"""
import numpy as np

def softmax_can_overflow(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def main():
    a = np.array([0.3, 2.9, 4.0])
    y = softmax(a)
    print(y)
    print(np.sum(y))

if __name__ == "__main__":
    main()