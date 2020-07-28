# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:31:25 2020

@author: Zakaria Farhati baby :D
"""

# First I'm gonna call my favourites libraries

import matplotlib.pyplot as plt # Math Plotting library
import numpy as np              # Numerical Python Library


#Let's make some inital variables :)
learning_rate = 0.0001
totalError = 0
# Importing my data using numpy.genfromtxt function
points = np.genfromtxt('dataTraining.csv',delimiter=";")
x = [] # X axis data list
y = [] # Y axis data list
h = [] # The predicted data 

