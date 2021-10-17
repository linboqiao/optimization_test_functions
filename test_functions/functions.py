from test_functions.base import *
from typing import Union


class Rastrigin(TestFunction):
    """
    Class that implements the Rastrigin Test Function
    """
    def formula(self, point: np.ndarray) -> float:
        return 10*self.dimension + np.sum(np.square(point) - 10*np.cos(2*np.pi*point))


class Ackley(TestFunction):
    """
    Class that implements the Ackley Test Function
    """
    def formula(self, point: np.ndarray) -> float:
        return -20*np.exp(-0.2 * np.sqrt(0.5 * np.sum(np.square(point)))) - \
               np.exp(0.5 * np.sum(np.cos(2*np.pi*point))) + np.e + 20


class Sphere(TestFunction):
    """
    Class that implements the Sphere function
    """
    def formula(self, point: np.ndarray) -> float:
        return 1. * np.sum(np.square(point))


class Rosenbrock(TestFunction):
    """
    Class that implements the Rosenbrock function
    """
    def formula(self, point: np.ndarray) -> float:
        formula_value = 0.0
        for i in range(len(point) - 1):
            formula_value += 100*(point[i + 1] - point[i]**2)**2 + (1 - point[i])**2
        return formula_value


class Beale(TestFunction):
    """
    Class that implements the Beale function
    """
    def formula(self, point: np.ndarray) -> Union[float, IncorrectDimensionError]:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return (1.5 - point[0] + point[0]*point[1])**2 + \
               (2.25 - point[0] + point[0] * (point[1]**2)) ** 2 + \
               (2.625 - point[0] + point[0] * (point[1]**3)) ** 2


class GoldsteinPrice(TestFunction):
    """
    Class that implements the Goldstein-Price function
    """
    def formula(self, point: np.ndarray) -> Union[float, IncorrectDimensionError]:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return (1 + ((point[0] + point[1] + 1) ** 2) *
                (19 - 14 * point[0] + 3 * (point[0] ** 2) - 14 * point[1] + 6 * point[0] * point[1] + 3 *
                 (point[1] ** 2))) * \
               (30 + ((2 * point[0] - 3 * point[1]) ** 2) *
                (18 - 32 * point[0] + 12 * (point[0] ** 2) + 38 * point[1] - 36 * point[0] * point[1] + 27 *
                 (point[1] ** 2)))


class Booth(TestFunction):
    """
    Class that implements the Booth function
    """
    def formula(self, point: np.ndarray) -> float:
        return (point[0] + 2*point[1] - 7)**2 + (2*point[0] + point[1] - 5)**2


class Bukin(TestFunction):
    """
    Class that implements the Bukin function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return 100*np.sqrt(np.abs(point[1] - 0.01*(point[0]**2))) + 0.01*np.abs(point[0] + 10)


class Matyas(TestFunction):
    """
    Class that implements the Matyas function
    """
    def formula(self, point: np.ndarray) -> float:
        return 0.26*(point[0]**2 + point[1]**2) - 0.48*point[0]*point[1]


class Levi(TestFunction):
    """
    Class that implements the Levi function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return (np.sin(3*np.pi*point[0]))**2 + ((point[0] - 1)**2)*(1 + (np.sin(3*np.pi*point[1]))**2) + \
               ((point[1] - 1)**2)*(1 + (np.sin(2*np.pi*point[1]))**2)


class Himmelblau(TestFunction):
    """
    Class that implements the Himmelblau function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return (point[0]**2 + point[1] - 11)**2 + (point[0] + point[1]**2 - 7)**2


class ThreeHumpCamel(TestFunction):
    """
    Class that implements the ThreeHumpCamel function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return 2*(point[0]**2) - 1.05*(point[0]**4) + (1/6.)*(point[0]**6) + point[0]*point[1] + point[1]**2


class Easom(TestFunction):
    """
    Class that implements the Easom function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return -np.cos(point[0])*np.cos(point[1])*np.exp(-((point[0] - np.pi)**2 + (point[1] - np.pi)**2))


class CrossInTray(TestFunction):
    """
    Class that implements the CrossInTray function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return -0.0001*(np.abs(np.sin(point[0])*np.sin(point[1])*np.exp(np.abs(
            100 - (np.sqrt(point[0]**2 + point[1]**2) / np.pi)))) + 1)**0.1


class EggHolder(TestFunction):
    """
    Class that implements the EggHolder function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return -(point[1] + 47)*np.sin(np.sqrt(np.abs(point[0]/2. + (point[1] + 47)))) - \
            point[0]*np.sin(np.sqrt(np.abs(point[0] - (point[1] + 47))))


class Holder(TestFunction):
    """
    Class that implements the Holder function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return - np.abs(np.sin(point[0])*np.cos(point[1])*np.exp(np.abs(1. - (np.sqrt(point[0]**2 + point[1]**2)/np.pi))))


class McCormick(TestFunction):
    """
    Class that implements the McCormick function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return np.sin(point[0] + point[1]) + (point[0] - point[1])**2 - 1.5*point[0] + 2.5*point[1] + 1


class SchafferN2(TestFunction):
    """
    Class that implements the SchafferN2 function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return 0.5 + ((np.sin(point[0]**2 + point[1]**2))**2 - 0.5) / (1 + 0.001*(point[0]**2 + point[1]**2))**2


class SchafferN4(TestFunction):
    """
    Class that implements the SchafferN4 function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return 0.5 + ((np.cos(np.abs(point[0]**2 + point[1]**2)))**2 - 0.5) / (1 + 0.001*(point[0]**2 + point[1]**2))**2


class StyblinskiTang(TestFunction):
    """
    Class that implements the StyblinskiTang function
    """
    def formula(self, point: np.ndarray) -> float:
        if self.dimension != 2:
            raise IncorrectDimensionError("This function is only allowed for 2 dimensions")
        return 0.5*np.sum(point**4 - 16*point**2 + 5*point)

