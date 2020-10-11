N = [n for n in range(1, 7)]
Z = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1), (0.78, 1.32)]

from complex_roots import plot_roots

plot_roots(N=N, Z=Z)