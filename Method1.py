"""
描述：计算AUC的方法1，即计算正样本的预测概率大于负样本的预测概率的个数
作者：王佳秋
日期：2020年5月29日
"""

import numpy as np
from sklearn.metrics import roc_auc_score as roc_auc_score2


def roc_auc_score1(true, scores):
    """计算AUC的方法1"""
    count = 0  # 计数器
    data = list(zip(true, scores))
    print("data: ", data)
    positives = list(filter(lambda x: x[0] == 1, data))
    negatives = list(filter(lambda x: x[0] == 0, data))
    print("positives: ", positives)
    print("negatives: ", negatives)

    for positive in positives:
        for negative in negatives:
            if positive[1] > negative[1]:
                count += 1
            elif positive[1] == negative[1]:
                count += 0.5

    return count / (len(positives) * len(negatives))


if __name__ == "__main__":
    print("Hello World Python from WJQ!")
    y_true = np.array([0, 0, 1, 1])  # array函数将队列转换成数组
    print("y_true:", type(y_true))
    y_scores = np.array([0.1, 0.4, 0.35, 0.8])
    print("方法注释：", roc_auc_score1.__doc__)
    auc_score = roc_auc_score1(y_true, y_scores)
    print("通过方法1计算得到的模型AUC值：", auc_score)

    """sklearn库中提供了计算工具，只需提供真实值和预测值即可"""
    y_true2 = np.array([0, 0, 1, 1])
    y_scores2 = np.array([0.1, 0.4, 0.35, 0.8])
    auc_score = roc_auc_score2(y_true, y_scores)
    print("通过方法2计算得到的模型AUC值：", auc_score)
