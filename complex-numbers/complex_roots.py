import matplotlib.pyplot as plt
import numpy as np
from pathvalidate import sanitize_filepath
from utils import ensure_dir

def plot_roots(N: list, Z: list):
    """
    Give this function a list N of the nth roots you want to compute,
    and a list Z of the complex numbers z = (x, y) of which you want to compute
    the nth roots, then this function will make plots for each z and save them
    """
    ensure_dir(f'plots/N={N[-1]}/somepath.someextension')

    for z in Z:
        x, y = z
        X = []
        Y = []
        magnitude = np.sqrt(x ** 2 + y **2)
        angle = np.arctan2(y, x) + 2 * np.pi
        padding = magnitude * 0.05
        for n in N:


            root_magnitude = magnitude ** (1 / n)
            roots  = []
            for i in range(1, n + 1):
                root_angle = angle * i / n
                root_x = root_magnitude * np.cos(root_angle)
                root_y = root_magnitude * np.sin(root_angle)
                root = (root_x, root_y)
                roots.append(root)
            X.extend([root[0] for root in roots])
            Y.extend([root[1] for root in roots])
        plt.scatter(x=X, y=Y)
        plt.xlim([-magnitude - padding, magnitude + padding])
        plt.ylim([-magnitude - padding, magnitude + padding])
        plt.xlabel("Real part")
        plt.ylabel("Imaginary part")

        title = f'z={x} + {y}i, N={N[-1]}'
        plt.title(title)
        filename = sanitize_filepath(f'plots/N={N[-1]}/{title}.png')
        plt.savefig(filename)
        plt.cla()