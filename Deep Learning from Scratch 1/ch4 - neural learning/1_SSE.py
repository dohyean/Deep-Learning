"""
오차제곱합(sum of squares for error, SSE)
"""

import numpy as np

def sum_squares_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)

def main():
    t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

    y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
    print(sum_squares_error(np.array(y1), np.array(t)))

    y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
    print(sum_squares_error(np.array(y2), np.array(t)))

if __name__ == "__main__":
    main()