#!/usr/bin/env python3
import sys
try:
    int(sys.argv[1])
except IndexError:
    print("Parameter loss")
    print("Example:")
    print("./calculator.py 3500")
    exit()
except ValueError:
    print("Parameter Error")
    exit()
#shui qian gong zi
sq = int(sys.argv[1])
if sq <= 3500:
    print(format(0,".2f"))
    exit()
elif sq >3500:
    #ying na shui 
    yns = int(sq - 3500)
if yns <= 1500:
    print(format(yns * 0.03,".2f"))
    exit()
elif yns > 1500 <= 4500:
    print(format(yns * 0.1 - 105,".2f"))
    exit()
elif yns > 4500 <= 9000:
    print(format(yns * 0.2 - 555,".2f"))
    exit()
elif yns > 9000 <= 35000:
    print(format(yns * 0.25 - 1005,".2f"))
    exit()
elif yns > 35000 <= 55000:
    print(format(yns * 0.3 - 2755,".2f"))
    exit()
elif yns > 55000 <= 80000:
    print(format(yns * 0.35 - 5505,".2f"))
    exit()
elif yns > 80000:
    print(format(yns * 0.45 - 13505,".2f"))
    exit()
