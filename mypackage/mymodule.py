"""
 author: EdwinB12
email: w.edwin.brown@outlook.com
license: MIT 
"""

import numpy as np
import matplotlib.pyplot as plt


def get_randnum():
    return np.random.uniform()


def plot_normal_distribution(**kwargs):
    distribution = np.sort(np.random.normal(**kwargs))
    plt.scatter(distribution, np.arange(len(distribution)))
