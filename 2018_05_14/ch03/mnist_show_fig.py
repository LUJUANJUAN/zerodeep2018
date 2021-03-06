# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.pardir) #親ディレクターのファイルをインポートするための設定
import numpy as np
from dataset.mnist import load_mnist 
from PIL import Image #画像の表示にPILモジュールを使用

def img_show(img):
	pil_img = Image.fromarray(np.uint8(img))
	pil_img.show()

#インポートしたload_mnistによってMNISTデータセットの読み込みを行う

(x_train, t_train), (x_test, t_test) = \
	load_mnist(flatten = True, normalize = False)

img = x_train[0]
label = t_train[0]
print(label)

img = img.reshape(28, 28) #画像の表示には28×28のサイズに再変形
img_show(img)
