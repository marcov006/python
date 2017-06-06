#Program a function that returns a new distribution
#q, shifted to the right by U units. If U=0, q should
#be the same as p.

p=[0, 1, 0, 0, 0]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


#Inaccurate motion
def move(p, U):
    print(p)
    #
    #ADD CODE HERE
    #
    q=[]

    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s += pOvershoot * p[(i-U-1) % len(p)]
        s += pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for i in range(1000):
    p = move(p, 1)

print (p)

