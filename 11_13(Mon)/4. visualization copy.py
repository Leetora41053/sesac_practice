import matplotlib.pyplot as plt
import numpy as np

def f1(x): return 2 *x**2
def f2(x): return 1/8 *x**2
def f3(x): return 1/6 *x**2

def df_dx1(x): return 4*x
def df_dx2(x): return 1/4*x
def df_dx3(x): return 1/3*x

x1, x2, x3 = 3
ITERATIONS = 30 #총 20번의 update를 할 것

x_track1, y_track1 = [x1], [f1(x)]
x_track2, y_track2 = [x2], [f2(x)]
x_track3, y_track3 = [x3], [f3(x)] #업데이트되는 x,y를 저장하기 위한 list
#NOTE: 초깃값을 먼저 저장해둬야 한다

for iter in range(ITERATIONS):
	dy_dx1 = df_dx1(x1)
	dy_dx2 = df_dx2(x2)
	dy_dx3 = df_dx3(x3)
	x1 = x1 - dy_dx1
	x2 = x2 - dy_dx2
	x3 = x3 - dy_dx3
	
	x_track1.append(x1)
	x_track2.append(x2)
	x_track3.append(x3)

	y_track1.append(f1(x1))
	y_track2.append(f2(x2))
	y_track3.append(f3(x3))

fig, axes = plt.subplots(3,1, figsize = (10, 10))

function_x = np.linspace(-5, 5, 100)
function_y1 = f1(function_x)
function_y2 = f2(function_x)
function_y3 = f3(function_x)

axes[0].plot(function_x, function_y1, 'r')
axes[0].scatter(x_track1, y_track1, c=range(ITERATIONS+1), cmap='rainbow')

axes[1].plot(function_x, function_y2, 'g')
axes[1].scatter(x_track2, y_track2, c=range(ITERATIONS+1), cmap='rainbow')

axes[2].plot(function_x, function_y3, 'b')
axes[2].scatter(x_track3, y_track3,c=range(ITERATIONS+1), cmap='rainbow')



# axes[1].plot(x_track, marker='o')
# axes[1].set_xlabel("Iteration", fontsize=15)
# axes[1].set_ylabel("x", fontsize=15)
fig.tight_layout()

plt.show()


#20번의 update를 통해 초기 x는 0.0346으로 update되어 x* = 0에 가까워짐