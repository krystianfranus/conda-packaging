from my_package import inc
import numpy as np


def main():
    print('Fancy calculations ...')
    rnd_arr = np.random.uniform(size=(5,))
    print(f'Random numbers: {inc(rnd_arr)}')
