
class Function1:
	def forward(self, x):
		z = x-2
		return z
	def not_self(x):
		return x
	
	def backward(self, dy_dz):
		dz_dx = 1
		dy_dx = dy_dz * dz_dx
		return dy_dx


# class Function2:
# 	#backward에서 z를 이용하기 위해 forward에서 저장해둬야 함
#     def forward(self, z): 
# 		self.z = z
#     	y = 2*(z ** 2)
# 		return y
        
	
# 	def backward(self):
#         dy_dz = 4 * self.z
# 		return dy_dz

func1 = Function1()
Function1.forward(func1, 3) # Function1.forward(func1, 3)
not_self = Function1.not_self(3)
print(id(func1))
print(not_self)

func2 = Function1()
print(id(func2))