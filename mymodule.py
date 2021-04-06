def sum(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def factorial(x):
    if(x>1):
        z=x
        y=x-1
        while(y>=1):
            z=z*y
            y=y-1
        return z
        
    elif(x<0):
        return("Invalid")
    else:
        return 1