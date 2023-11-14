def f(x1, x2): return x1**2 + x2**2
def df_dx1(x1): return 2*x1
def df_dx2(x2): return 2*x2

ITERATIONS = 50
x1, x2 = 3, 3

# for iter in range(ITERATIONS):
# 	dy_dx1 = df_dx1(x1)
# 	dy_dx2 = df_dx2(x2)
# 	x1 = x1 - 0.03*dy_dx1
# 	x2 = x2 - 0.03*dy_dx2
cnt = 0
while True:
	if x1 < 0.0001:
		break
	cnt += 1
	dy_dx1 = df_dx1(x1)
	dy_dx2 = df_dx2(x2)
	x1 = x1 - 0.3*dy_dx1
	x2 = x2 - 0.3*dy_dx2

print(cnt)
	



	

#20번의 update를 통해 초기 x는 0.0346으로 update되어 x* = 0에 가까워짐