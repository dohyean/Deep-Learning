import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    """
    step_function과 차이점은 매끄러운 곡선으로 구성이 되어 있음
    비선형 함수
    """
    return 1 / (1 + np.exp(-x))

def main():
    """
    -5.0 ~ 5.0까지 x축을 기준으로 0.1씩 이동하면서 sigmoid 실행
    """
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()

if __name__ == "__main__":
    main()