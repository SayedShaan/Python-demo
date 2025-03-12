'''
    Traffic Signal
'''
import time

def countdown(n):
    for i in range(n,0,-1):
        print(i)
        time.sleep(1)

def lightsignal():
    color="red"

    if(color=="red"):
        print("Color is red.Please stop!!!!!!!!")
        color="green"
        countdown(10)
        '''time.sleep(10)'''

      
    if(color=="green"):
         print("Color is green.Continue Driving!!!!!")
         color="yellow"
         countdown(10)
         '''time.sleep(10)'''
      
    if(color=="yellow"):
         print("Color is yellow.Slow Down and stop!!!!!")
         color="red"
         countdown(5)
         '''time.sleep(5)'''

lightsignal()
         



