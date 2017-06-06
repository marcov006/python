from math import *

def f_gaussian(mu, sigma2, x):
    f_x = (1 / sqrt(2 * pi * sigma2)) * exp(-.5 * (pow((x - mu),2)) / sigma2)
    return f_x

mu = 10.
sigma2 = 4.
x = 10.

print('Function Gaussian : ', f_gaussian(mu, sigma2, x))


def update(mean1, var1, mean2, var2):

    new_mean = ((1./(var1 + var2))*(var2*mean1+var1*mean2))
    new_var = (1./((1./var1)+(1./var2)))

    return [new_mean, new_var]

g1=[10.,8.]
g2=[13.,2.]

n_gaussian = update(g1[0],g1[1], g2[0],g2[1])

print('new MEAN : ' , n_gaussian[0] , ' new VARIANCE : ', n_gaussian[1])

def predict(mean1, var1, mean2, var2):
    new_mean = mean1+mean2
    new_var =var1+var2
    return [new_mean, new_var]

print (predict(10., 4., 12., 4.))


# Write a program that will iteratively update and
# predict based on the location measurements
# and inferred motions shown below.

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 0.0000000001

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig].

# Insert code here

for i in range (len(measurements)):
    [mu, sig] = update(mu,sig,measurements[i],measurement_sig)
    #print('update: ', [mu, sig])
    [mu, sig] = predict(mu,sig,motion[i],motion_sig)
    #print('predict : ', [mu, sig])

print('## Last Values: ', [mu, sig])