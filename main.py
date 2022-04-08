def EUCLIDES(a, b):  
  if (b == 0):
    return a
  else:
    return EUCLIDES(b, a % b)

def EUEXT(a, b):  
  if (b == 0):
    return (a,1,0)
  else:
    aux = int(a/b)
    (d,x1,y1) = EUEXT(b, a % b)
    (x,y) = (y1, x1- (aux*y1))
    return (d,x,y)

a=int(input("Ingrese un número: "))
while a < 0:
    print("Ingrese números POSITIVOS")
    a=int(input("Ingrese un número: "))

b=int(input("Ingrese otro número: "))
while b < 0:
    print("Ingrese números POSITIVOS")
    b=int(input("Ingrese otro número: "))

print( EUCLIDES(a,b))
print( EUEXT(a,b))
m, x, y = EUEXT(a, b)
print("euclidesE(", a , "," , b, ") = ", "mcd: ",m, "valor de x: ",x,"valor de y: ",y)
