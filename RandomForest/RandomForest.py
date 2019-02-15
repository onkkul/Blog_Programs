# -*- coding: utf-8 -*-
"""
Random Forest using ScikitLearn Binary Tree

Created on Sat Feb 15 17:05:38 2019


@author: onkarkul

-->Step 1 : Import Libraries            (LineNo. 19)
-->Step 2 : Load Data_Set               (LineNo. 40)
-->Step 3 : Clean Data_Set              (LineNo. 50)
-->Step 4 : Form Subsets                (LineNo. 59)
-->Step 5 : Create Forest from Tree     (LineNo. 68)
-->Step 6 : Predict                     (LineNo. 73)

"""

from sklearn import tree  #for building forest

import random             #for creating the "randomness" in >RANDOM< forest.

from csv import reader    #to read CSV file (our data file)

Data_Set = list()        #Init the Data_Set as a double list (Matrix) for our usage.
Data_Indices = list()    #Index list of row numbers that we will pass to the individual trees.
Local_Data = list()      #This will store data from those above rows in index list for individual trees(bags).
Local_Labels = list()    #This will store labels from those above rows in index list for individual trees.
TreeNames= list()        #The list that will contain the Trees using their names(we will name them on line no. 35)
Result = list()          #List to store result of each tree(26 results in total).
check_accuracy =  list() #List used to check accuracy.

for Tree_Name in range (0,45):
    TreeNames.append(Tree_Name)     #Naming our trees in forest(26 trees named 0 through 25)

for each_name in TreeNames:     #Creating the index of >RANDOMLY< selected row numbers for each tree
    RowNumbers_of_DataPoints_for_One_Tree = random.sample(range(0,1000),50)  #We are "RANDOMLY" selecting datapoints for each tree. (Reason we call it "random forest".)
    Data_Indices.append(RowNumbers_of_DataPoints_for_One_Tree)     #These are nothing but the row numbers in Data_Set


def load_csv(filename):     # Load a CSV file
    with open(filename, 'r') as file:   #open it as a readable file
        csv_reader = reader(file)   #init the csv reader
        for row in csv_reader:  #for every row in the csv file
            if not row:
                continue    #do it till rows end.
            Data_Set.append(row)     #add that row as an element in our Data_Set list (2D Matrix of values)   
    return Data_Set  #return in-memory data matrix


def Cleanse(Data_Set):   #convert the strinig Data_Set into int Data_Set.
    for row,column in enumerate(Data_Set):
        del Data_Set[row][-1]   #delete that null entry
    for row in range(0,1000):
        for column in range(0,25):
            Data_Set[row][column]=int(Data_Set[row][column])    #Convert str to int
    return Data_Set


def Load_Data_for_One_Tree(Tree_No):    #fetch data for individual trees(Sampling).
    Local_Data.clear()      #Clear Data from pervious tree
    Local_Labels.clear()    #Clear Labels from pervious tree
    for every_row_number_assigned_for_one_tree in Data_Indices[Tree_No]:     #fetch rows from the index. 
        Local_Data.append(Data_Set[every_row_number_assigned_for_one_tree][0:-1])      #use that index to load actual data from the Data_Set(all columns except the last).
        Local_Labels.append(Data_Set[every_row_number_assigned_for_one_tree][-1])     #use same index to load actual labels from the Data_Set(the remaining last column).
    return Local_Data, Local_Labels
    

def Create_Predict(number): #Main code of random forest
    for each_tree in TreeNames:   #for every tree we named in TreeNames
        Load_Data_for_One_Tree(each_tree)            #Create local data
        each_tree = tree.DecisionTreeClassifier()    #Create(Init) decision tree here
        each_tree.fit(Local_Data,Local_Labels)       #feed local data (bags) to train forest        
        Individual_Prediction = each_tree.predict([Data_Set[number][:-1]]) #feed our new data point to each tree so as to predict result
        Result.append(int(Individual_Prediction))    #Store result of each tree prediction.

    if Result.count(1) > Result.count(2):    #Display the most common result.
        check_accuracy.append(1)
        print("Approve Loan\n","Trees In favour:\t",Result.count(1),"\tTrees against:\t", Result.count(2))
    elif Result.count(1) < Result.count(2):
        check_accuracy.append(2)
        print("Dont Approve Loan\n","Trees In favour:\t",Result.count(1),"\tTrees against:\t", Result.count(2))
    else:
        check_accuracy.append(0)
        print("Can not predict, No clear mandate\n")


#def accuracy():                            #Uncomment this function, if you wish to see each tree in training proccess and accuracy at the end.
#    acc = 0                                #Increases execution time considerably though
#    for x in range(0,1000):
#        Result.clear()
#        Create_Predict(x)
#        if check_accuracy[x] == Data_Set[x][-1]:
#            acc = acc + 1
#    acc_per = acc/10
#    print("accuracy percentage:\t",acc_per)
    
        

load_csv('Document.csv')
Cleanse(Data_Set)
#accuracy()             #The above funciton of accuracy is called here.
while True:
    Result.clear()
    Create_Predict(int(input("Enter a row number\t")))
