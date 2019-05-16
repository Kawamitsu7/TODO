import matplotlib.pyplot as plt
import numpy as np

def optimization(n_w1,n_w2,alpha,beta):	
	alpha_w1 = -1 * alpha * (n_w1 - n_w2 + 1)
	alpha_w2 = -1 * alpha * (n_w2 - n_w1 - 1)

	beta_w1 = -1 * beta * n_w1
	beta_w2 = -1 * beta * n_w2

	nplus1_w1 = n_w1 + alpha_w1
	nplus1_w2 = n_w2 + alpha_w2

	result_x.append(nplus1_w1)
	result_y.append(nplus1_w2)

	nplus1_w1 = nplus1_w1 + beta_w1
	nplus1_w2 = nplus1_w2 + beta_w2

	result_x.append(nplus1_w1)
	result_y.append(nplus1_w2)

	return nplus1_w1, nplus1_w2

#初期値
w_1 = 0
w_2 = -2

#学習率
alpha = 0.5
#忘却率
beta = 0.0001

result_x = []
result_y = []

for i in range (100000):
	w_1, w_2 = optimization(w_1,w_2,alpha,beta)

	if i % 10000 == 0:
		print(w_1,w_2)

plt.plot(result_x,result_y)
plt.xlabel("w_1")
plt.ylabel("w_2")

plt.show()

#print(w_1,w_2)