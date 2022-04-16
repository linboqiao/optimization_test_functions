
from math import pi
from math import sqrt

from landscapes.single_objective import ackley
from landscapes.single_objective import ackley_n2
from landscapes.single_objective import adjiman
from landscapes.single_objective import amgm
from landscapes.single_objective import bartels_conn
from landscapes.single_objective import beale
from landscapes.single_objective import bent_cigar
from landscapes.single_objective import bird
from landscapes.single_objective import bohachevsky_n1
from landscapes.single_objective import bohachevsky_n2
from landscapes.single_objective import bohachevsky_n3
from landscapes.single_objective import booth
from landscapes.single_objective import branin
from landscapes.single_objective import brent
from landscapes.single_objective import brown
from landscapes.single_objective import bukin_n6
from landscapes.single_objective import camel_hump_3
from landscapes.single_objective import camel_hump_6
from landscapes.single_objective import carrom_table
from landscapes.single_objective import chichinadze
from landscapes.single_objective import chung_reynolds
from landscapes.single_objective import colville
from landscapes.single_objective import cosine_mixture
from landscapes.single_objective import cross_in_tray
from landscapes.single_objective import csendes
from landscapes.single_objective import cube
from landscapes.single_objective import damavandi
from landscapes.single_objective import deckkers_aarts
from landscapes.single_objective import dixon_price
from landscapes.single_objective import drop_wave
from landscapes.single_objective import easom
from landscapes.single_objective import eggholder
from landscapes.single_objective import exponential
from landscapes.single_objective import freudenstein_roth
from landscapes.single_objective import goldstein_price
from landscapes.single_objective import griewank
from landscapes.single_objective import himmelblau
from landscapes.single_objective import holder_table
from landscapes.single_objective import hosaki
from landscapes.single_objective import keane
from landscapes.single_objective import levi_n13
from landscapes.single_objective import leon
from landscapes.single_objective import matyas
from landscapes.single_objective import michalewicz
from landscapes.single_objective import mccormick
from landscapes.single_objective import parsopoulos
from landscapes.single_objective import pen_holder
from landscapes.single_objective import plateau
from landscapes.single_objective import qing
from landscapes.single_objective import quartic
from landscapes.single_objective import rastrigin
from landscapes.single_objective import rotated_hyper_ellipsoid
from landscapes.single_objective import rosenbrock
from landscapes.single_objective import salomon
from landscapes.single_objective import schaffer_n2
from landscapes.single_objective import schaffer_n4
from landscapes.single_objective import schwefel
from landscapes.single_objective import sphere
from landscapes.single_objective import step
from landscapes.single_objective import styblinski_tang
from landscapes.single_objective import sum_of_different_powers
from landscapes.single_objective import sum_of_squares
from landscapes.single_objective import trid
from landscapes.single_objective import tripod
from landscapes.single_objective import wolfe
from landscapes.single_objective import zakharov


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


#要绘制函数图像
def f(x, y):
   return np.sin(np.sqrt(x ** 2 + y ** 2))
#准备x,y数据
x = np.linspace(-6, 0.1, 30)
y = np.linspace(-6, 0.1, 30)
#生成x、y网格化数据
X, Y = np.meshgrid(x, y)
#准备z值
#Z = f(X, Y)
Z = adjiman([X,Y])
#绘制图像
fig = plt.figure()
ax = plt.axes(projection='3d')
#调用绘制线框图的函数plot_wireframe()
#ax.plot_wireframe(X, Y, Z, color='red')
ax.plot_surface(X, Y, Z,cmap='viridis', edgecolor='none')
ax.set_title('Surface plot')
# 调整视角
ax.view_init(elev=45,    # 仰角
             azim=45    # 方位角
            )
plt.show()