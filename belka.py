#import numpy as np

l=200   #dl walka
podpora_poz=[[1,10],[0,190]]    #[[typ,pozycja]......] 0-podpora nieruchoma 1-podpora wolna
sila_poz=[[0,30,-100],[1,120,-10,50],[0,70,200]]    # 0-wektor sily [0,pozycja,wartosc] 1-rozklad sily [1,pozycja, gestosc, dlugosc]
moment_poz=[[50,20]]    #[pozycja, wartosc]

R = []  #przechowuje niewieadome tz. wartosc reakcji w podporze
A = []
B = [[0],[0]]


for k1 in range(len(sila_poz)):
    if sila_poz[k1][0] == 0:
        B[0][0] = int(B[0][0]) - sila_poz[k1][2]
    elif sila_poz[k1][0] == 1:
        B[0][0] = int(B[0][0]) - sila_poz[k1][2]*sila_poz[k1][3]

for k1 in range(len())


print(B)




