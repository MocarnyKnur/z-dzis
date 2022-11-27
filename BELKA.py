import numpy as np
from numpy.linalg import inv
l=200   #dl walka
podpora_poz=[[1,10], [0,190]]    #[[typ,pozycja]......] 0-podpora nieruchoma 1-podpora wolna
sila_poz=[[0,30,-100],[1,120,-10,50],[0,70,200]]    # 0-wektor sily [0,pozycja,wartosc] 1-rozklad sily [1,pozycja srodka, gestosc, dlugosc]
moment_poz=[[50,20]]    #[pozycja, wartosc]

#R = []  #przechowuje niewieadome tz. wartosc reakcji w podporze
A = []
A_temp = []
B = []

for k1 in range(len(podpora_poz)):
    B.append([0])
for k1 in range(len(podpora_poz)):
    A.append([])
    for k2 in range(len(podpora_poz)):
        A[k1].append(0)

for k1 in range(len(A)):
    A[0][k1] = 1
for k1 in range(len(A)-1):
    for k2 in range(len(A)):
        A[k1+1][k2] = podpora_poz[k2][1] - podpora_poz[k1][1]

for k1 in range(len(sila_poz)):
    if sila_poz[k1][0] == 0:
        B[0][0] = int(B[0][0]) - sila_poz[k1][2]
    elif sila_poz[k1][0] == 1:
        F_skup = sila_poz[k1][2] * sila_poz[k1][3]
        B[0][0] = int(B[0][0]) - F_skup

for k1 in range(len(B)-1):
    for k2 in range(len(sila_poz)):
        if sila_poz[k2][0] == 0:
            B[k1+1][0] = int(B[k1+1][0]) - sila_poz[k2][2]*(sila_poz[k2][1]-podpora_poz[k1][1])     # od R1
        elif sila_poz[k2][0] == 1:
            F_skup = sila_poz[k2][2]*sila_poz[k2][3]
            B[k1+1][0] = int(B[k1+1][0]) - F_skup*(sila_poz[k2][1]-podpora_poz[k1][1])

for k1 in range(len(B)-1):
    for k2 in range(len(moment_poz)):
        B[k1+1][0] = int(B[k1+1][0])-moment_poz[k2][1]

A = np.array(A)
B = np.array(B)

Ainv = inv(A)
R = np.matmul(Ainv, B)

print(R)