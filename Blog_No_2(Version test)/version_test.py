# This is a simple program to test versions of installed libraries in anaconda.
# Author : Onkar Kulkarni@ wdir='/home/NAIFE/github/Blog_Programs'.

# The main program starts from line no. 7 and ends on line no. 27.
# all other lines are comments.

import pandas
import scipy
import numpy
import nltk                     #natural language toolkit
import sklearn                  #scikit-learn
import cv2                      #openCV
import tensorflow

print('The pandas version is {}.'.format(pandas.__version__))

print('The scipy version is {}.'.format(scipy.__version__))

print('The numpy version is {}.'.format(numpy.__version__))

print('The nltk version is {}.'.format(nltk.__version__))

print('The scikit-learn version is {}.'.format(sklearn.__version__))

print('The openCV version is {}.'.format(cv2.__version__))

print('The tensorflow version is {}.'.format(tensorflow.__version__))

# The output should look like this:
'''
The pandas version is 0.20.3.
The scipy version is 0.19.1.
The numpy version is 1.12.1.
The nltk version is 3.2.4.
The scikit-learn version is 0.19.1.
The openCV version is 3.1.0.
The tensorflow version is 1.3.0.
'''