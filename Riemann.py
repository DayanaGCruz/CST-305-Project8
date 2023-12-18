# Dayana Gonzalez Cruz
# CST-307: Principles of Modeling and Simulation
# WF1100A Dr. Citro
# 12-17-2023
# Project 8: Numerical Integration

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import time 

#------------------------------------------------------------------------------------
# Part 1 
#------------------------------------------------------------------------------------

def Riemann(a,b,func,n):
	start = time.time() # Get start time of computation 
	ms = 5 # Define marker size to be 0 when n > 50 for graph clarity
	if(n> 50):
		ms = 0
	xi = (b-a)/n # Subinterval/rectangle width
	xs = np.linspace(a,b, n + 1) # n + 1 points, n subintervals/rectangles
	ys = func(xs)
	# Identify left-hand endpoints
	lnxs = xs[:-1] 
	lnh = ys[:-1] # Height at point

	lnarea = np.sum(xi * lnh) # Calculate approximate area using Riemann summation c_i * height + c_(i+1) * height
	print('Left Riemann Approx. Area = {}'.format(lnarea))
	# Identify right-hand endpoints
	rnxs = xs[1:] 
	rnh = ys[1:]	

	rnarea = np.sum(xi * rnh)
	print('Right Riemann Approx. Area = {}'.format(rnarea))
	# Identify midpoints
	mnxs = (xs[:-1] + xs[1:])/2 
	mnh = func(mnxs)

	mnarea = np.sum(xi * mnh) 
	print('Mid Riemann Approx. Area = {}'.format(mnarea)) 
	# Midpoint with granularity n = 1000 is the best approximate of actual area as n approaches infinity

	# Plot and label rectangles with left-hand end points
	plt.figure(1,figsize = (8,18))
	plt.subplot(3,2,1)
	plt.text(3, 0.7, 'Approx. Area = {}'.format(lnarea))
	plt.title('Left-Hand Endpoint Reimann Sum with {} rectangles'.format(n))
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.plot(xs, ys, color = 'pink', marker = 'o', markersize = ms, markerfacecolor = '#ff5ba3')
	plt.bar(lnxs, lnh, width = xi, alpha = 0.1, align = 'edge', color = 'green') 
	plt.grid(True)
	#---------------------------
	# (b)
	#---------------------------
	# Plot and label rectangles with right-hand end points
	plt.subplot(3,2,3)
	plt.text(3, 0.7, 'Approx. Area = {}'.format(rnarea))
	plt.plot(xs, ys,  color = 'pink', marker = 'o', markersize = ms, markerfacecolor = '#ff5ba3')
	plt.bar(rnxs, rnh, width = -xi, alpha = 0.1, align = 'edge', color = 'green') # Negative xi, so that the bar orients left
	plt.title('Right-Hand Endpoint Reimann Sum with {} rectangles'.format(n))
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.grid(True)
	#---------------------------
	# (c)
	#---------------------------
	# Plot and label rectangles with midpoints
	plt.subplot(3,2,5)
	plt.text(3, 0.7, 'Approx. Area = {}'.format(mnarea))
	plt.title('Midpoint Reimann Sum with {} rectangles'.format(n))
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.plot(xs,ys, color = 'pink', marker = 'o', markersize = ms, markerfacecolor = '#ff5ba3')
	plt.bar(mnxs, mnh, width = xi, alpha = 0.1, align = 'edge', color = 'green') 
	plt.grid(True)
	end = time.time() # Get end time ofcomputation
	ctime = end - start
	print("Computation Time: {} seconds".format(ctime)) # Display

	plt.show()

# Riemann(a,b,func,n)
# a - Lower Limit of Interval
# b - Upper Limit of Interval
# f - function 
# n - number of subintervals/rectangles

#---------------
# a.
#---------------

print('Part 1: a.')
# Define the function
def f(x):
    return np.sin(x) + 1

# [-π,π] [a,b] 
Riemann(-np.pi,np.pi,f,4)
Riemann(-np.pi,np.pi,f,200)
Riemann(-np.pi,np.pi,f,1000)

print('Part 1: b.')
#---------------
# b.
#---------------

def k(x):
	return 3*x + 2 * (x**2)
Riemann(0,1, k, 1000)

print('Part 1: c1.')
#---------------
# c1. 

def g(x):
	return np.log(x)

Riemann(1, np.e, g, 1000)

print('Part 1: c2.')
#---------------
# c2. 
#---------------

def j(x):
	return x**2 - x**3

Riemann(-1, 0, j, 1000)

#------------------------------------------------------------------------------------
# Part 2 
#------------------------------------------------------------------------------------
print('Part 2:')
# Mean Download rate noted over the interval of [0,30] minutes
def R(t):
	return 34.9*t


# Call Riemann Sum function to Calculate Riemann Sum & Total Amount of Data Compressed in the Interval 
# Minutes: [0, 30]
Riemann(0,30, R,1000)
 