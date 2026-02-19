"""
mini-batch
"""

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from pathlib import Path
import importlib.util

spec = importlib.util.spec_from_file_location(
    "load_mnist",
    Path(__file__).resolve().parent / "3_mnist.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
load_mnist = mod.load_mnist

def load_mnist_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
    print("=" * 10 + "load_mnist" + "=" * 10)
    print(x_train.shape)
    print(t_train.shape)
    
    return x_train, t_train

def mini_batch(x_train, t_train, batch_size):
    train_size = x_train.shape[0]
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    print("=" * 10 + "mini_batch" + "=" * 10)
    print(x_batch.shape)
    print(t_batch.shape)
    
    return x_batch, t_batch

def main():
    x_train, t_train = load_mnist_data()
    x_batch, t_batch = mini_batch(x_train, t_train, 10)

if __name__ == "__main__":
    main()