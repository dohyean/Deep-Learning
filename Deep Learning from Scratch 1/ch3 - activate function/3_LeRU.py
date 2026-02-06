import numpy as np
import matplotlib.pylab as plt

def leru(x):
    """
    0 이하의 데이터는 모두 0으로 표시, 이외에는 동일 값으로 반환
    """
    return np.maximum(0, x)

def main():
    """
    -5.0 ~ 5.0까지 x축을 기준으로 0.1씩 이동하면서 leru 실행
    """
    x = np.arange(-5.0, 5.0, 0.1)
    y = leru(x)
    plt.plot(x, y)
    plt.ylim(-1.0, 5.9)
    plt.show()

if __name__ == "__main__":
    main()