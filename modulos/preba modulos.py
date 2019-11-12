#import modulo
#modulo.mi_print("Hola")

from modulo import *
from asciistuff import Banner
mi_print("hola de nuevo")
otro_print("otro print usado")
print(sumar(4,5))
print(restar(10,7))
import time
import sys
for i in range(10, 0, -1):
    print( i ," ... ")
    time.sleep(.5)
print(Banner("BOOOOOM !!!!!"))

print(sys.platform)

print(Banner("ICO fes aragon"))

for v in range(10,50,1):
    print(Banner("ICO fes aragon"))
