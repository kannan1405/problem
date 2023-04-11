import numpy as np
n , m = map(int, input().split())
A = np.array([input().split() for i in range(n)], int,ndmin=2)
B = np.array([input().split() for i in range(n)], int,ndmin=2)
print(A+B,A-B,A*B,A//B,A%B,A**B,sep="\n")
