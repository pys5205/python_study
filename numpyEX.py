import numpy as np

a=np.array([1, 2, 3, 4])
b=np.array([5,6,7,8])
A = np.reshape(a, [2,2])
B = np.reshape(b, [2,2])

print(A)
print(B)

result3_1 = np.matmul(A,B)
result3_2 = np.matmul(B,A)

print(result3_1)
print(result3_2)

su1 = 3
su2 = 4
rep_cnt = 4
abcd = np.repeat(su1, rep_cnt)
abcde = np.repeat(su2, rep_cnt)
res = np.concatenate((abcd, abcde))
print(res)

arr3 = ([1, 2, 3, 4, 5, 6])
res1 = np.reshape(arr3, [2, 3])
print(res1)
res1 = np.reshape(arr3, [3, 2])
print(res1)

