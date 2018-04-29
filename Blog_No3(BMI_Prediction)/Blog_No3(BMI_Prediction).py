#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 18:34:05 2018

@author: NAIFE
"""

#classifier for BMI estimation
from sklearn import tree
import visualize

clf = tree.DecisionTreeClassifier()    #create object(model) of classifier

#daset of our model in the form of [height, weight] in inches and pounds respectivey
X = [[62, 100], [67, 105], [67, 115],[72, 120], [72, 135],[76, 145], [76, 150], [58, 91], [58, 115], [63, 107], [63, 135], [68, 125], [68, 158], [73, 144], [73, 182], [76, 156], [76, 197], [58, 119], [58, 138], [63, 141], [63, 163], [68, 164],[68, 190], [73, 189], [73, 219], [76, 205], [76, 238], [58, 143], [58, 186], [63, 169], [63, 220], [68, 197],[68, 256], [73, 227], [73, 295], [76, 246], [76, 320]]

#labels for the above dataset
Y = ['underweight', 'underweight', 'unnderweight', 'underweight', 'underweight', 'underweight', 'underweight', 'normal','normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'normal', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'overweight', 'obese', 'obese', 'obese', 'obese', 'obese', 'obese', 'obese', 'obese', 'obese', 'obese']

clf = clf.fit(X, Y)     #train the model

cm = int(input("Enter the height in cm"))   #We take input from user in centimeter
kg = int(input("Enter the weight in kg"))
inch = cm*0.39370   #as our model is trained on [inches, pound] we make our input compatible to our system
pounds = kg*2.20463
accept = [inch, pounds]    #accept the value for input

prediction = clf.predict([accept]) #pass input to the model for prediction
print(prediction)





#   would you like to see how our training data looks like?? Just uncomment the following line!! ps: do not forget to close the image to proceed
#visualize.visual()



##################OUTPUT##########################
"""
[NAIFE@localhost python]$ python prediction.py
Enter the height145
Enter the weight46
['underweight']
[NAIFE@localhost python]$ python prediction.py
Enter the height192
Enter the weight82
['normal']
[NAIFE@localhost python]$ python prediction.py
Enter the height136
Enter the weight92
['obese']
[NAIFE@localhost python]$
"""
