import numpy as np

x = 10
y = 10
z = 10 

while True:
    w = int(input("Значение X "))
    m = int(input("Значение Y "))
    u = int(input("Значение Z "))
    
    i = ((x-w)**2+(y-m)**2+(z-u)**2)
    if i == 0:
        print ("Bingo!")
        break
    elif i <= 5:
        print("Hight")
    else:
        print("Low")