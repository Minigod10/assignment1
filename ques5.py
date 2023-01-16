"""Write a program that prints out the sine and cosine of the angles ranging
from 0 to 345◦ in 15◦ increments. Each result should be rounded to 4
decimal places. Sample output is shown below:"""
import math
for x in range(0,346,15):
    i=math.radians(x)
    angle_sin=round(math.sin(i),4)
    angle_cos=round(math.cos(i),4)
    print("sin(",x,")=",angle_sin,"and cos(",x,")=",angle_cos)
