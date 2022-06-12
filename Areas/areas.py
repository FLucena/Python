import math

def areaTriangulo(altura, base):
    areaT = base * altura / 2
    return areaT

print("El área del triángulo es de",areaTriangulo(2,3))

def areaCirculo(radio):
    areaC = math.pi * radio **2
    return areaC

print("El área del círculo es de",areaCirculo(3))