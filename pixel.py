from machine import Pin
from neopixel import NeoPixel
import time
import math

text=[
   0x00,0x00,0x00,0x00,0x00,0x18,0x3C,0x7E,
0xFF,0x3C,0x3C,0x3C,0x3C,0x3C,0x3C,0x3C,
0x3C,0x3C,0x3C,0x3C,0x3C,0x3C,0x3C,0x3C,
0x3C,0x00,0x00,0x00,0x00,0x00,0x00,0x00,


    ]
 
def init(data_pin, leds_num):
    global np
 
    dp = Pin(data_pin, Pin.OUT)
    np = NeoPixel(dp, leds_num)
    clear()
def demo0():
    j=k=l=50
    for i in range(0,np.n):
       np[i] = (j,k,l)
    np.write()


 
# 按红、绿、蓝、白显示灯带
def demo1():
    j=k=l=0
    for i in range(0,np.n):
       np[i] = (j,k,l)
       j=j+40
       if(j>50):
           j=0
           k=k+20
       if(k>50):
            k=0
            l=l+20 
       if(l>50):
            l=0 
    np.write()
    while(1):
        n1=np
        n=np.n
        for i in range(n):
            if((n-i)<=1):
                np[i]=n1[1-(n-i)]
            else:
                np[i]=n1[i+1]
        np.write()
        time.sleep_ms(300)
        
def ByteOpera1(num,dat):
    byte= [0x01,0x02,0x04,0x8,0x10,0x20,0x40,0x80]
    if dat&byte[num]:
        return 1
    else:
        return 0

def ByteOpera2(num,dat):
    byte= [0x80,0x40,0x20,0x10,0x8,0x4,0x2,0x01]
    if dat&byte[num]:
        return 1
    else:
        return 0
    
def show_text():
    for i in range(32):
        for line in range(2):
            for b in range(8):
                if(line==0):
                    temp=ByteOpera1(b,text[i])
                else:
                    temp=ByteOpera2(b,text[i])
                if(temp):
                    np[i*8+b]=(1,1,1)
                else:
                    np[i*8+b]=(0,0,0)
    np.write()
    A=B=C=0
    while(1):
        n1=np
        n=np.n
        A=A+30
        
        if(A>50):
           A=5
           B=B+20
        if(B>50):
            B=5
            C=C+20
        if(C>50):
            C=5
        for i in range(n):
            if((n-i)<=8):
                np[i]=n1[8-(n-i)]
            else:
                np[i]=n1[i+8]
            if(np[i]!=(0,0,0)):
                np[i]=(A,B,C)
        np.write()
        

def clear():
    n = np.n
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
