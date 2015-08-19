#Name:          Tony Ranieri
#Created:       October 2014
#Modified:      August 2015

import numpy as np
import pylab as py
import matplotlib.pyplot as plt

def roots(f,df,a,b,niter,epsilon):
# Input
#   f: the function that we need to find roots for 
#   df: derivative of the function f 
#   a: initial left bracket x-coord
#   b: initial right bracket x-coord
#   niter: max number of iterations
#   epsilon: tolerance for the stopping rule
#
# Output
#   xstar: the root of f for given tolerance epsilon
  
# perform bisect
  fa=f(a)                   #define y-coord at a based on the given f
  fb=f(b)                   #define y-coord at b based on the given f
  if (fa*fb>0):             #test to see if there is a single root in the bracket
      print "There are either no roots in this bracket, or an even number of them. Please refine your bracket."
      return 1
  for i in range(niter):
      xstar=(a+b)/2           #define xstar as the midpoint of the current bracket  
      fxstar=f(xstar)         #set the value of our function at this new midpoint
      err=abs(b-a)
      if (fa*fxstar<0):       #test to see if root is in [fa,fxstar]
        b=xstar               #if yes, set our upper bound to now be xstar
        fb=fxstar             #update the guess and iterate
      elif (fb*fxstar<0):     #test to see if root is in [fxstar,fb]
        a=xstar               #if yes, set our lower bound to now be xstar
        fa=fxstar             #update the guess and iterate
      else:
        a=xstar
        b=xstar
        print "Check the results carefully! One of your endpoints may be a root or 0 might be a root."
      if (err<epsilon):  #test to see if our proposed root is "close enough" based on our tolerance level
        break                 #if it is, we're done here
  xstar_b=xstar
  fxstar_b=f(xstar_b)  
      
# perform Newton
  x0=(a+b)/2              #need an initial guess, midpoint seems decent enough
  fx0=f(x0)               #define y-coord at x0 based on the given f
  for i in range(niter):
      dfx0=df(x0)         #define derivative y-coord at x0 based on the given df
      if (dfx0==0):
          break
      xstar=x0-fx0/dfx0   #set xstar as defined by Newton's method
      err=abs(xstar-x0)
      fxstar=f(xstar)
      if (err<epsilon):   #test to see if our proposed root is "close enough" based on our tolerance level to the error
          x0=xstar            #update the initial guess and iterate
          fx0=fxstar
      if (i==niter):
          break
  xstar_n=xstar
  fxstar_n=f(xstar_n)
  
# perform Secant
  fa=f(a)                 #define y-coord at a based on the given f
  fb=f(b)                 #define y-coord at b based on the given f
  for i in range(niter):
      if (fb==fa):
          break
      xstar=b-((fb*(b-a))/(fb-fa))    #set xstar as defined by secant method
      err=abs(f(xstar))
      fxstar=f(xstar)
      if (err<epsilon):   #test to see if our proposed root is "close enough" based on our tolerance level to the error
          break    
      a=b                 #update the initial guess and iterate
      b=xstar             #update the initial guess and iterate
      fa=fb
      fb=fxstar
      if (i==niter) or (fb==fa):
          break
  xstar_s=xstar
  fxstar_s=f(xstar_s)
  
#find best estimate for root by testing proximity to zero
  if (abs(fxstar_b-0)<=abs(fxstar_n-0)):
    if (abs(fxstar_b-0)==abs(fxstar_n-0)):
      xstar=xstar_b
      print "Bisect method and Newton method came to the same conclusion."
    else:
      if (abs(fxstar_b-0)<=abs(fxstar_s-0)):
        if (abs(fxstar_b-0)==abs(fxstar_s-0)):
          xstar=xstar_b
          print "Bisect method and Secant method came to the same conclusion."
        else:
          xstar=xstar_b
          print "Bisect method is superior."
      else:
        xstar=xstar_s
        print "Secant method is superior."
  else:
    if (abs(fxstar_n-0)<=abs(fxstar_s-0)):
      if (abs(fxstar_n-0)==abs(fxstar_s-0)):
        xstar=xstar_n
        print "Newton method and Secant method came to the same conclusion."
      else:
        xstar=xstar_n
        print "Newton method is superior."
    else:
      xstar=xstar_s
      print "Secant method is superior."

#plot function with identified root
  #x=np.linspace(a, b, 200)
  #plt.plot(x, f(x))
  #plt.xlim(a-1, b+1)
  #plt.xticks(np.linspace(a, b, 10, endpoint=True))
  #plt.xlim(x.min()*1.1,x.max() * 1.1)
  #plt.ylim(-5, 5)
  #ax = plt.gca()  
  #ax.axes.get_yaxis().set_visible(False)
  #ax.spines['right'].set_color('none')
  #ax.spines['top'].set_color('none')
  #ax.spines['left'].set_color('none')
  #ax.xaxis.set_ticks_position('bottom')
  # ax.spines['bottom'].set_position(('data',0))
  #plt.show()
  print "output = (value, bisect, newton, secant)"
  return xstar, xstar_b, xstar_n, xstar_s

def bisect(f,a,b,niter,epsilon):
# Input
#   f: the function that we need to find roots for 
#   a: initial left bracket x-coord
#   b: initial right bracket x-coord
#   niter: max number of iterations
#   epsilon: tolerance for the stopping rule
#
# Output
#   xstar: the root of f for given tolerance epsilon
#   err: error at convergence
#   fxstar: the value of f at xstar (should be very close to zero as we are expecting a root)
#   i: the number of iterations taken to get to the tolerance
#   xseq: the values of {x_n} to see convergence
  fa=f(a)                   #define y-coord at a based on the given f
  fb=f(b)                   #define y-coord at b based on the given f
  xseq=np.zeros(niter)
  if (fa*fb>0):             #test to see if there is a single root in the bracket
      print "There are either no roots in this bracket, or an even number of them. Please refine your bracket."
      return 1
  for i in range(niter):
      xstar=(a+b)/2           #define xstar as the midpoint of the current bracket  
      xseq[i]=xstar           #add the value of xstar to this convergent sequence
      fxstar=f(xstar)         #set the value of our function at this new midpoint
      err=abs(b-a)
      if (fa*fxstar<0):       #test to see if root is in [fa,fxstar]
          b=xstar               #if yes, set our upper bound to now be xstar
          fb=fxstar             #update the guess and iterate
      elif (fb*fxstar<0):     #test to see if root is in [fxstar,fb]
          a=xstar               #if yes, set our lower bound to now be xstar
          fa=fxstar             #update the guess and iterate
      else:
          a=xstar
          b=xstar
          print "Check the results carefully! One of your endpoints may be a root."
      if (err<epsilon):  #test to see if our proposed root is "close enough" based on our tolerance level
          break                 #if it is, we're done here
  xstar=(a+b)/2
  fxstar=f(xstar)
  return xstar, err, fxstar, i+1, xseq[0:i]

def newton(f,df,x0,niter,epsilon):
# Input
#   f: the function that we need to find roots for 
#   df: the derivative of the function f
#   x0: initial guess for a root
#   niter: max number of iterations 
#   epsilon: tolerance for the stopping rule
#    
# Output
#   xstar: the root of f for given tolerance epsilon
#   err: error at convergence
#   fxstar:  the value of f at xstar (should be very close to zero as we are expecting a root)  
#   i: the number of iterations taken to get to the tolerance
#   xseq: the values of {x_n} to see convergence
    fx0=f(x0)               #define y-coord at x0 based on the given f
    xseq=np.zeros(niter+1)  #need +1 as we already know the first entry is x0
    xseq[0]=x0
    for i in range(niter):
        dfx0=df(x0)         #define derivative y-coord at x0 based on the given df
        xstar=x0-fx0/dfx0   #set xstar as defined by Newton's method
        xseq[i+1]=xstar
        err=abs(xstar-x0)
        fxstar=f(xstar)
        if (err<epsilon):   #test to see if our proposed root is "close enough" based on our tolerance level to the error
            break
        x0=xstar            #update the initial guess and iterate
        fx0=fxstar
        if (i==niter):
            print "Newton's method failed to converge given the number of iterations."
            break
    return xstar, err, fxstar, i+1, xseq[0:(i+2)]
    
def secant(f,a,b,niter,epsilon):
# Input
#   f: the function of interest 
#   a: initial left bracket x-coord
#   b: initial right bracket x-coord
#   niter: max number of iterations 
#   epsilon: tolerance for the stopping rule
#    
# Output
#   xstar: the root of f for given tolerance epsilon
#   err: error at convergence
#   fxstar:  the value of f at xstar (should be very close to zero as we are expecting a root)  
#   i: the number of iterations taken to get to the tolerance
#   xseq: the values of {x_n} to see convergence
    fa=f(a)                 #define y-coord at a based on the given f
    fb=f(b)                 #define y-coord at b based on the given f
    xseq=np.zeros(niter+1)     #need +1 as we already know the first entry is x0
    xseq[0]=a
    xseq[1]=b
    for i in range(niter):
        xstar=b-((fb*(b-a))/(fb-fa))    #set xstar as defined by secant method
        xseq[i+2]=xstar                 #+2 as we alreqady defined the first 2
        err=abs(f(xstar))
        fxstar=f(xstar)
        if (err<epsilon):   #test to see if our proposed root is "close enough" based on our tolerance level to the error
            break    
        a=b                 #update the initial guess and iterate
        b=xstar             #update the initial guess and iterate
        fa=fb
        fb=fxstar
        if (i==niter):
            print "Secant's method failed to converge given the number of iterations."
            break
    return xstar, err, fxstar, i+1, xseq[0:(i+2)]
