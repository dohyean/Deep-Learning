import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    """
    0, 1로 데이터를 반환함
    비선형 함수
    """
    return np.array(x > 0, dtype=int)

def main():
    """
    -5.0 ~ 5.0까지 x축을 기준으로 0.1씩 이동하면서 step_function 실행
    """
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()

if __name__ == "__main__":
    main()