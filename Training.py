# -*- coding: utf-8 -*-
"""DMP_TRAINING_VALIDATION_TESTING.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15t2z-esOVzygVLkJqX9RG01AMsSdeGQq
"""

import numpy as np

from PIL import Image, ImageOps

import matplotlib.pyplot as plt

import h5py

from datetime import datetime

import tensorflow as tf

tf.config.get_visible_devices('GPU')

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics



P = []*0

TRAINDATA, TESTDATA = "A:\\Arima\\PROJECTS\\Outbox\\Anitha Akka\\Animals\\DMP\\DMP_GPU\\Train_data.h5", "A:\\Arima\\PROJECTS\\Outbox\\Anitha Akka\\Animals\\DMP\\DMP_GPU\\Test_data.h5"

files = h5py.File(DIR, 'r')

predcat, predsubcat = "c2", "031_002"

#predimg = np.array([1])

predimg = np.array(files["c2"]["031_002"][:, :, :-1].flatten()) #100:201, 100:200

labels = []*0

x_rgb, y_label = []*0, []*0

for category in files.keys():

    for subcategory in files[category].keys():         

        if subcategory[:3] not in labels:

            labels.append(subcategory[:3])

        #dmpimg = np.array([1])

        dmpimg = np.array(files[category][subcategory][:, :, :-1].flatten())    #100:201, 100:200
        
        x_rgb.append(dmpimg)
        
        y_label.append(files[category][subcategory][:, :, -1][-1][-1])    #100:201, 100:200

x_rgb = np.array(x_rgb, dtype = np.uint8)

x_rgb2 = x_rgb

y_label = np.array(y_label)

from sklearn.utils import shuffle

x_rgb2 = shuffle(x_rgb2, random_state=0)

x_test = x_rgb2[:50]

y_test = []*0

for i in x_test:

    for j in range(x_rgb.shape[0]):

        if np.array_equal(i, x_rgb[j]) == True:

            y_test.append(y_label[j])

            break

print(x_test.shape[0], len(y_test))

regressor = LinearRegression()  
regressor.fit(x_rgb, y_label)

#To retrieve the intercept:
print(regressor.intercept_)

#For retrieving the slope:
print(regressor.coef_)

y_pred = regressor.predict(x_rgb)
y_pred = np.round(y_pred)

print(np.array(list(zip(y_label, y_pred))))

y_pred = regressor.predict(x_test)
y_pred = np.round(y_pred)
print(np.array(list(zip(y_test, y_pred))))

"""#PREDICTION/CONFUSION MATRIX"""

from sklearn.metrics import confusion_matrix,classification_report

predictions = regressor.predict(x_test)

y_pred = np.round(predictions)

true_classes = y_test

class_labels = y_pred

print(class_labels)

print(confusion_matrix(true_classes, y_pred))

report = classification_report(true_classes, y_pred, zero_division=1)

print(report)