# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt, matplotlib.image as mpimg
from sklearn.model_selection import train_test_split
from sklearn import svm

# Importing the dataset
labeled_images = pd.read_csv('Data/train.csv')
images = labeled_images.iloc[0:5000,1:]
labels = labeled_images.iloc[0:5000,:1]
train_images, test_images,train_labels, test_labels = train_test_split(images, labels, train_size=0.8, random_state=0)



clf = svm.SVC()
clf.fit(train_images, train_labels.values.ravel())
clf.score(test_images,test_labels) # gives accuracy of 10%

test_images[test_images>0]=1
train_images[train_images>0]=1

clf = svm.SVC()
clf.fit(train_images, train_labels.values.ravel())
clf.score(test_images,test_labels) # gives accuracy of 88%

         
test_data=pd.read_csv('Data/test.csv')
Xtest_images = labeled_images.iloc[0:5000,1:]
Xtest_labels = labeled_images.iloc[0:5000,:1]
test_data[test_data>0]=1 
clf.score(Xtest_images,Xtest_labels) 