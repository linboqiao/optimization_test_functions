from utils.visualizer import Visualizer

visualizer = Visualizer(function_name="StyblinskiTang",
                        n_points=100,
                        dimension=2,
                        x_limits=(-5, 5),
                        y_limits=(-5, 5))
visualizer.plot()
