import plotly.graph_objects as go

from utils.surface_generator import SurfaceGenerator

test_function_names = ["Rastrigin", "Ackley", "Sphere", "Rosenbrock", "Beale", "GoldsteinPrice", "Booth", "Bukin",
                       "Matyas", "Levi", "Himmelblau", "ThreeHumpCamel", "Easom", "CrossInTray", "EggHolder",
                       "Holder", "McCormick", "SchafferN2", "SchafferN4", "StyblinskiTang"]

visible_list = [False]*len(test_function_names)

x_limits_list = [(-5.12, 5.12), (-5, 5), (-10, 10), (-10, 10), (-4.5, 4.5), (-2, 2), (-10, 10), (-15, -5),
                 (-10, 10), (-10, 10), (-5, 5), (-5, 5), (-100, 100), (-10, 10), (-512, 512), (-10, 10),
                 (-1.5, 4), (-100, 100), (-100, 100), (-5, 5)]

y_limits_list = [(-5.12, 5.12), (-5, 5), (-10, 10), (-10, 10), (-4.5, 4.5), (-2, 2), (-10, 10), (-3, 3),
                 (-10, 10), (-10, 10), (-5, 5), (-5, 5), (-100, 100), (-10, 10), (-512, 512), (-10, 10),
                 (-3, 4), (-100, 100), (-100, 100), (-5, 5)]


fig = go.Figure()
menus = []

for i in range(len(test_function_names)):
    surface = SurfaceGenerator(
        function_name=test_function_names[i],
        n_points=100,
        dimension=2,
        x_limits=x_limits_list[i],
        y_limits=y_limits_list[i]
    ).get()
    fig.add_trace(surface)

    visible_list_copy = visible_list.copy()
    visible_list_copy[i] = True

    menus.append({
        "label": test_function_names[i],
        "method": "update",
        "args": [
            {"visible": visible_list_copy},
        ]
    })

null_button = {
    "label": "None",
    "method": "update",
    "args": [
        {"visible": visible_list},
    ]
}

menus = [null_button] + menus

fig.update_layout(updatemenus=[
    dict(
        active=0,
        buttons=menus,
        x=0.3
    )
])

fig.show()
