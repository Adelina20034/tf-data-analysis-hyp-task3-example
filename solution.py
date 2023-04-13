import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 5127116142 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return ttest_ind(x, y, equal_var=False, alternative="less").pvalue > 0.07  # Ваш ответ, True или False
