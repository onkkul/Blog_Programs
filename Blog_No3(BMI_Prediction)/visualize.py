#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 16:40:39 2018

@author: NAIFE
"""

from matplotlib import pyplot as plt


#daset of our model in the form of [height, weight] in inches and pounds respectivey
X = [[62, 100], [67, 105], [67, 115],[72, 120], [72, 135],[76, 145], [76, 150], [58, 91], [58, 115], [63, 107], [63, 135], [68, 125], [68, 158], [73, 144], [73, 182], [76, 156], [76, 197], [58, 119], [58, 138], [63, 141], [63, 163], [68, 164],[68, 190], [73, 189], [73, 219], [76, 205], [76, 238], [58, 143], [58, 186], [63, 169], [63, 220], [68, 197],[68, 256], [73, 227], [73, 295], [76, 246], [76, 320]]

#labels for the above dataset
Y = ['underweight', 'underweight', 'underweight', 'underweight', 'underweight', 'underweight', 'underweight', 'normal','normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'obese', 'obese', 'obese', 'obese', 'obese', 'obese', 'obese', 'obese', 'obese', 'obese']

def visual():
    for red in range(0,6):
        x = X[red][0]
        y = X[red][1]
        plt.plot(x, y, 'r+')

    for blue in range(7,16):
        x = X[blue][0]
        y = X[blue][1]
        plt.plot(x, y, 'bo')

    for green in range(17,26):
        x = X[green][0]
        y = X[green][1]
        plt.plot(x, y, 'gx')

    for black in range(27,36):
        x = X[black][0]
        y = X[black][1]
        plt.plot(x,y,'k^')

    plt.show()