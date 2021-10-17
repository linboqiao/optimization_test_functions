import abc
from typing import Tuple
import numpy as np

from utils.exception import IncorrectDimensionError


class TestFunction(metaclass=abc.ABCMeta):

    def __init__(self, dimension: int):
        self.dimension = dimension

    @abc.abstractmethod
    def formula(self, point: np.ndarray) -> float:
        """
        The Test Fucntion's formula. This method
        must be implemented by all test functions.
        :param point: A point to be evaluated
        :return: The value of the function in the provided point
        """
        raise NotImplementedError

    def get_plot_data(self,
                      n_points: int,
                      x_limits: Tuple[float, float],
                      y_limits: Tuple[float, float]):

        """
        :param n_points: It refers to the number of points in the x and y axes. The total
        number of points in the surface will be the cartesian product (n * n)
        :param x_limits: A tuple containing max and min value in the x axis
        :param y_limits: A tuple containing max and min value in the y axis
        :return: A tuple containing x, y and z (as the evalutation of the cartesian product by self.formula)
        """

        if self.dimension != 2:
            raise IncorrectDimensionError("Only plots with dimension 2 are allowed")

        x = np.linspace(x_limits[0], x_limits[1], n_points)
        y = np.linspace(y_limits[0], y_limits[1], n_points)
        z = np.zeros(shape=(x.shape[0], y.shape[0]))

        for i, a1 in enumerate(x):
            for j, a2 in enumerate(y):
                point = np.array([a2, a1])
                z[i, j] = self.formula(point)

        return x, y, z
