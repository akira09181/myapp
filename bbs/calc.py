import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def simulate(top,bot,interval,value):
    bit = pd.read_csv('bitcoin.csv')
    bit=bit.iloc[::-1]
    itv=interval
    v=value
    x=bit.Id
    y=bit.Close
    plt.plot(x,y)


    plt.tight_layout()
    plt.show()
    bot=bot
    top=top
    total=0
    stock=0
    count=0
    high=0
    hstock=0
    for i in range(0,len(bit),itv+1):
        
        if bit.Close[len(bit)-i-1] <=bot:
            total-=(bit.Close[len(bit)-i-1])*v
            stock+=(1*v)
        elif bit.Close[len(bit)-i-1] >=top:
            total+=bit.Close[len(bit)-i-1]*stock
            stock=0
        else:
            pass
        count+=1
        
        if high>total:
            high=total
            hstock=stock
    total+=bit.Close[len(bit)-1]*stock
    stock=0
    print(str(int(total))+" "+str(int(high))+" "+str(hstock))

simulate(10000,8000,2,5)