# UNIFORM DISTRIBUTION

# Modify the empty list, p, so that it becomes a UNIFORM probability
# distribution over five grid cells, as expressed in a list of 
# five probabilities.

p = [0.2, 0.2, 0.2, 0.2, 0.2]
print (p)

# GENERAL UNIFORM DISTRIBUTION
#  Modify your code to create probability vectors, p, of arbitrary
#  size, n. Use n=5 to verify that your new solution matches
#  the previous one.

p=[]
n=5

for i in range(n):
    p.append(1/n)

print (p)

#After Sense
p = [0.2, 0.2, 0.2, 0.2, 0.2]
pHit = 0.6
pMiss = 0.2
p[0] = p[0]*pMiss
p[1] = p[1]*pHit
p[2] = p[2]*pHit
p[3] = p[3]*pMiss
p[4] = p[4]*pMiss
print (p)

#Normalization
norm=sum(p)
print(norm)

for i in range(len(p)):
    p[i]=p[i]/norm

print (p)

#Sense function
#Modify the code below so that the function sense, which
#takes p and Z as inputs, will output the NON-normalized
#probability distribution, q, after multiplying the entries
#in p by pHit or pMiss according to the color in the
#corresponding cell in world.

p = [0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for wenum in enumerate(world):
        print("")
        print('idx is: ' + repr(wenum[0]))
        print('p@idx is: ' + repr(p[wenum[0]]) )
        print('world @ idx is: ' + repr(wenum[1]))
        print('Measurement Z is: ' + repr(Z))

        hit = (Z == wenum[1])
        q.append(p[wenum[0]]*hit*pHit + p[wenum[0]]* (1-hit)*pMiss)
        print(q[wenum[0]])

    print(q)
    norm = sum(q)
    print("" "norm is: " + repr(norm))

    for i in range(len(q)):
        q[i]=q[i]/norm

    print("")
    return q

for k in range(len(measurements)):
    p = sense(p,measurements[k])

print(p)

