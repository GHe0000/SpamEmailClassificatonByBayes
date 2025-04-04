import os
from itertools import islice
import numpy as np


# 读取数据集，各返回 N 个文件
def load_dataset(data_dir, n):
    X, y = [], []

    spam_dir = os.path.join(data_dir, 'spam')
    for filename in islice(os.listdir(spam_dir), n):
        with open(os.path.join(spam_dir, filename), 'r', encoding='utf-8') as f:
            words = f.read().split()
            if len(words) > 0:
                X.append(words)
                y.append("spam")

    ham_dir = os.path.join(data_dir, 'ham')
    for filename in islice(os.listdir(ham_dir), n):
        with open(os.path.join(ham_dir, filename), 'r', encoding='utf-8') as f:
            words = f.read().split()
            if len(words) > 0:
                X.append(words)
                y.append("ham")

    return X, np.array(y)


# 读取单个数据文件
def load_one_file(filename):
    X = []
    with open(filename, 'r', encoding='utf-8') as f:
        words = f.read().split()
        X.append(words)
    return X


def find_word_list(X, data_dir, n, label='spam'):
    dir = os.path.join(data_dir, label)
    for filename in islice(os.listdir(dir), n):
        with open(os.path.join(dir, filename), 'r', encoding='utf-8') as f:
            words = f.read().split()
            if(X == words):
                return os.path.join(dir, filename)
    return None
