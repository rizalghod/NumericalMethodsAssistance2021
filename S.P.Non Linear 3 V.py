from numpy import*                                              #import fungsi-fungsi numpy
from math import*                                               #import fungsi-fungsi math

def f1 (x1, x2, x3):                                                # Definisi Fungsi 1
    a = 3*x1 - cos(x1*x3) - 0.5
    return a
def f2 (x1, x2, x3):                                                # Definisi Fungsi 2
    b = x1**2 - 81*(x2 + 0.1)**2 + sin(x3) + 1.06
    return b
def f3 (x1, x2, x3):                                                # Definisi Fungsi 3
    c = exp(-x1*x2) + 20*x3 + 9.472
    return c

def Gauss(X):                                                   # Definisi operasi Gauss Jordan
    X[0] = X[0] / X[0][0]
    X[1] = X[1] - X[1][0] * X[0]
    X[2] = X[2] - X[2][0] * X[0]
    X[1] = X[1] / X[1][1]
    X[2] = X[2] - X[2][1] * X[1]
    X[2] = X[2] / X[2][2]
    X[1] = X[1] - X[1][2] * X[2]
    X[0] = X[0] - X[0][1] * X[1] - X[0][2] * X[2]
    return X[0,3], X[1,3], X[2,3]

x1 = 4                                                          # Nilai tembakan x1
x2 = 4                                                          # Nilai tembakan x2
x3 = 4                                                          # Nilai tembakan x3
x1lama = 0
while abs(x1-x1lama)>0.000000000001 :                           # Eror harus kurang dari 10.E11, iterasi dimulai
    f11 = (f1((x1*(1+0.0000001)),x2,x3) - f1(x1,x2,x3))/(x1*0.0000001)              # df1/dx1
    f12 = (f1(x1, x2*(1+0.0000001), x3) - f1(x1,x2,x3))/(x2*0.0000001)              #df1/dx2
    f13 = (f1(x1, x2, x3*(1+0.0000001)) - f1(x1,x2,x3))/(x3*0.0000001)              #df1/dx3
    f21 = (f2(x1*(1+0.0000001), x2, x3) - f2(x1,x2,x3))/(x3*0.0000001)              #df2/dx1
    f22 = (f2(x1,x2*(1+0.0000001),x3) - f2(x1,x2,x3))/(x3*0.0000001)                #df2/dx2
    f23 = (f2(x1, x2, x3*(1+0.0000001)) - f2(x1,x2,x3))/(x3*0.0000001)              #df2/dx3
    f31 = (f3((x1 * (1 + 0.0000001)), x2, x3) - f3(x1, x2, x3)) / (x1 * 0.0000001)  # df3/dx1
    f32 = (f3(x1, x2 * (1 + 0.0000001), x3) - f3(x1, x2, x3)) / (x2 * 0.0000001)    # df3/dx2
    f33 = (f3(x1, x2, x3 * (1 + 0.0000001)) - f3(x1, x2, x3)) / (x3 * 0.0000001)    # df3/dx3

    X = array([[f11, f12, f13, f1(x1,x2,x3)],                   # Augmented matriks untuk persamaan di atas
                [f21, f22, f23, f2(x1,x2, x3)],
               [f31, f32, f33, f3(x1, x2, x3)]])
    a = Gauss(X)                                                # Augmented matriks diselesaikan dengan
                                                                # Eliminasi gauss jordan
    x1lama = x1
    x1 = x1 - a[0]                                              # x1 baru
    x2 = x2 - a[1]                                              # x2 baru
    x3 = x3 - a[2]                                              # x3 baru

print("x1 = ", str(x1))
print("x2 = ", str(x2))
print("x3 = ", str(x3))
