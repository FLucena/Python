def esBisiesto(x):
    try:   
        if (x%4==0):
            if (x%100==0):
                if (x%400==0):
                    return True
            else:
                return True
        return False        
    except:
        return False
  
print(esBisiesto(2400))