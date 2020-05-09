import numpy as np
n=input('enter the size of the matrix')
n=int(n)
flag=1
a=np.random.randint(1,101,size=(n,n))
a_transpose=a.transpose()
a_det=np.linalg.det(a)
a_trace=a.trace()
if(a_det==0):
    flag=0
else:
    flag=1
    a_inv=np.linalg.inv(a)
a_psuedoinv=np.linalg.pinv(a)
q, r = np.linalg.qr(a)
eig_val,eig_vec=np.linalg.eig(a)
print('matrix:\n',a)
print('transpose:',a_transpose)
print('Determinant:',a_det)
print('Trace:',a_trace)
if(flag==0):
    print("Inverse does not exist")
else:
    print('Inverse:',a_inv)
print('Pseudo inverse:',a_psuedoinv)
print('Q:',q)
print('R:',r)
print('Eigen values:',eig_val)
print('Eigen vectors:',eig_vec)
