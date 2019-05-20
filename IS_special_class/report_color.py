import matplotlib.pyplot as plt
import numpy as np

def optimization(n_w1,n_w2,alpha,beta):	
	alpha_w1 = -1 * alpha * (n_w1 - n_w2 + 1)
	alpha_w2 = -1 * alpha * (n_w2 - n_w1 - 1)

	beta_w1 = -1 * beta * n_w1
	beta_w2 = -1 * beta * n_w2

	nplus1_w1 = n_w1 + alpha_w1
	nplus1_w2 = n_w2 + alpha_w2

	opt_x.append(nplus1_w1)
	opt_y.append(nplus1_w2)

	nplus1_w1 = nplus1_w1 + beta_w1
	nplus1_w2 = nplus1_w2 + beta_w2

	obl_x.append(nplus1_w1)
	obl_y.append(nplus1_w2)

	return nplus1_w1, nplus1_w2

#初期値
w_1 = 0
w_2 = -2

init_w1 = w_1
init_w2 = w_2

#学習率 (100000回計算では0.5でいい感じ)
alpha = 0.2
#忘却率 (100000回計算では0.0001でいい感じ)
#最終的にこの値幅で解が振動しだす
beta = 0.001

opt_x = []
opt_y = []

obl_x = []
obl_y = []

obl_x.append(init_w1)
obl_y.append(init_w2)

for i in range (10000):
	w_1, w_2 = optimization(w_1,w_2,alpha,beta)
	#お遊び : alphaを徐々に変えてみる
	#alpha = alpha * 0.9999

	if i % 1000 == 0:
		print(w_1,w_2)

print(len(opt_x))

for i in range (len(opt_x)):
	if i % 100 == 0:
		print(i)
	plt.plot([obl_x[i], opt_x[i]],[obl_y[i], opt_y[i]], color = 'orange')
	plt.plot([opt_x[i], obl_x[i+1]],[opt_y[i], obl_y[i+1]], color = 'green')


plt.xlabel("w_1")
plt.ylabel("w_2")

plt.show()

#print(w_1,w_2)