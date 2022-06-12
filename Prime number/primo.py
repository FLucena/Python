def esPrimo(x):
    try:
        for i in range(1,x-1):
            if (x%(i+1)==0):        
                return False
        return True        
    except:
        return (f'{x} no es un número entero.')
print(esPrimo(5))