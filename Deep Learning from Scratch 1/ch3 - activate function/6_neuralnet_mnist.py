"""
손글씨 데이터를 순방향으로 예측
"""

import os, pickle, importlib.util
from pathlib import Path
import numpy as np

spec = importlib.util.spec_from_file_location(
    "load_mnist",
    Path(__file__).resolve().parent / "6_mnist.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
load_mnist = mod.load_mnist

spec = importlib.util.spec_from_file_location(
    "sigmoid_mod",
    Path(__file__).resolve().parent / "2_sigmoid.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
sigmoid = mod.sigmoid


def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    
    return x_test, t_test

def init_network():
    with open(os.path.dirname(__file__) + "/sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3

    y = a3
    return y

def main():
    x, t = get_data()
    network = init_network()

    accuracy_cnt = 0
    for i in range(len(x)):
        y = predict(network, x[i])
        p = np.argmax(y)
        if p == t[i]:
            accuracy_cnt += 1
    
    print("Accuracy: " + str(float(accuracy_cnt) / len(x)))

if __name__ == "__main__":
    main()