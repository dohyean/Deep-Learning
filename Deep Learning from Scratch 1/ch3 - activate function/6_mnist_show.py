"""
손글씨 데이터(mnist)를 직접 이미지로 출력해 확인
"""

import numpy as np
from pathlib import Path
from PIL import Image
import importlib.util

spec = importlib.util.spec_from_file_location(
    "load_mnist",
    Path(__file__).resolve().parent / "6_mnist.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
load_mnist = mod.load_mnist

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


def main():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten = True, normalize=False)

    img = x_train[0]
    label = t_train[0]
    print(label)

    print(img.shape)
    img = img.reshape(28, 28)
    print(img.shape)

    img_show(img)

if __name__ == "__main__":
    main()