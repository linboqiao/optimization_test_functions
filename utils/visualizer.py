from typing import Tuple
import plotly.graph_objects as go
import test_functions.functions as functions_factory


class Visualizer:
    """
    Visualizer class to plot the selected functions in Plotly
    """
    def __init__(self,
                 function_name: str,
                 n_points: int,
                 dimension: int,
                 x_limits: Tuple[float, float] = (-10., 10.),
                 y_limits: Tuple[float, float] = (-10., 10.)):
        """
        :param function_name: Function name to select among:
            - Rastrigin
            - Ackley,
            - Sphere
            - Rosenbrock
            - Beale
            - GoldsteinPrice
        :param n_points: It refers to the number of points in the x and y axes. The total
        number of points in the surface will be the cartesian product (n * n)
        :param dimension: Dimension
        :param x_limits: A tuple containing max and min value in the x axis
        :param y_limits: A tuple containing max and min value in the y axis
        """
        self.function_name = function_name
        self.n_points = n_points
        self.dimension = dimension
        self.x_limits = x_limits
        self.y_limits = y_limits

    def plot(self):
        function_class = getattr(functions_factory, self.function_name)(dimension=self.dimension)
        xyz = function_class.get_plot_data(self.n_points, self.x_limits, self.y_limits)

        fig = go.Figure(
            data=[go.Surface(
                x=xyz[0],
                y=xyz[1],
                z=xyz[2],
                colorscale="Rainbow",
                opacity=1,
                showscale=False)]
        )
        fig.show()



