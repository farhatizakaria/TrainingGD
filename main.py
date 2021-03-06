# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:31:25 2020

@author: Zakaria Farhati baby :D
"""

# First I'm gonna call my favourites libraries

# Math Plotting library
import matplotlib.pyplot as plt
# Numerical Python Library 
import numpy as np


#Let's make some inital variables :)
learning_rate = 0.0001
totalError = 0
# Importing my data using numpy.genfromtxt function
points = np.genfromtxt('dataTraining.csv',delimiter=";")
m = len(points)
x = [] # X axis data list
y = [] # Y axis data list
h = [] # The predicted data 

# And we need some inital values which're theta0 and theta1
init_theta0 = 2
init_theta1 = 1 

# After Gradient Descent we goona got new theta0 and theta1
new_theta0, new_theta1 = 0, 0

def setup():
    """
    This function has only role which's setup the module 
    to be ready for analyzing the data ...
    """
    print('Setup the module :D')
    
    # I'm gonna use a loop to fill in the X, Y and H 
    # from dataTraining.csv
    
    for point in range(m):
        x.append(points[point,0])
        y.append(points[point,1])
        h.append(points[point,2])


def jCost(totalError=0):
    """ 
    The role of the jCost function is calculating the
    different between H value and Y value
    """
    for point in range(m):
        totalError = totalError + (h[point] - y[point]) ** 2
        # I incrementing the value of totalError
        # Such as the summation operator sigmma Ʃ
    return totalError / (2*m)



def gradientDescenet(learning_rate,init_theta0,init_theta1):
    """
    For optimizing the Hypothesis line equation H
    """
    
    
def plottingData():
    """Only for plotting the data and the Hypothesis line"""
    fig = plt.figure()
    # I'll draw the origin x and y axis for clear view
    fig, ax = plt.subplots()
    ax.axhline(y=0, color='k',linewidth=1)
    ax.axvline(x=0, color='k',linewidth=1)
    # Plotting the Hypo line
    plt.plot(x,h,label="The Hypothesis line H")
    # Scattering the Data
    plt.scatter(x,y,color="red",label="The data")
    # Grid => make some squares
    plt.grid()
    plt.legend()
    plt.title('The main figure baby!')
    plt.xlabel('The X axis')
    plt.ylabel('The Y axis')
    plt.show()
        

if __name__ == '__main__':
    setup()
    # To show up Jcost value
    print('The value of Jcost equal {}'.format(jCost())) 
    # Plotting the main figure baby!
    plottingData()
    
    

