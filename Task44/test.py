import numpy as np
import pandas as pd


def testMainTask(lst) -> list:
    print("===================")
    print("this is  start test")

    np.random.shuffle(lst)

    data = pd.DataFrame({'whoAmI': lst})

    one_hot = pd.get_dummies(data['whoAmI'])

    data = pd.concat([data, one_hot], axis=1)
    data = data.drop('whoAmI', axis=1)

    return (data.head())
