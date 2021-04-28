#Regresi Linear y = ax + b

from numpy import*
x = input("Masukkan x (dengan spasi) : ").split(' ')
y = input("Masukkan y (dengan spasi) : ").split(' ')
matx = []
for num in x :
    matx = matx + [float(num)]
maty = []
for num in y:
    maty = maty + [float(num)]

A = array([[0,0,0],
          [0,0,0]])
y2 = 0
i = 0
while i < len(matx):
    A[0,0] = A[0,0] + (matx[i])**2
    A[0,1] = A[0,1] + matx[i]
    A[1,0] = A[1,0] + matx[i]
    A[1,1] = i + 1

    A[0,2] = A[0,2] + matx[i]*maty[i]
    A[1,2] = A[1,2] + maty[i]
    y2 = y2 + maty[i]**2
    i = i + 1
print("\n matriks regresi :")
print(A)

A[0] = A[0]/A[0,0]                                  #Gauss
print("\nb1/", str(A[0, 0]))
print(A)
A[1] = A[1] - A[1,0]*A[0]
print("\nb2 - ", str(A[1, 0]), "b1")
print(A)
A[1] = A[1]/A[1,1]
print("\nb2/", str(A[1,1]))
print(A)
A[0] = A[0] - A[0,1]*A[1]
print("\nb1 - ", str(A[0, 1]), "b2")
print(A)

r = ((A[1,1]*A[0,2] - A[0,1]*A[1,2])**2)/((A[1,1]*A[0,0] - (A[0,1])**2)*((A[1,1]*y2 - (A[1,2])**2)))
print("\nRegresi Linear y = ax + b:")
print("a = ", str(A[0,2]), " b = ", str(A[1,2]))
print(A[0,2])
print("r (koef determinasi) = ", str(r))