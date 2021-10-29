import numpy as np
import pandas as pd
from sklearn import datasets


from sklearn import preprocessing
sx = preprocessing.MinMaxScaler()
sy = preprocessing.MinMaxScaler()
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt
from sklearn.datasets import load_wine

wine = datasets.load_wine()
wine.feature_names
data = pd.DataFrame(wine.data)

# normalize the dataset
max_val=max(data.max())
data =data/max_val

data.columns = wine.feature_names
data
wine.target.shape
data['target'] = wine.target

# number of classes
print("number of classes",len(pd.unique(data['target'])))

data
train, test = np.split(data.sample(frac=1),[int(.7*len(data))])

#Trainig dataset
train_X =train.drop('target',axis='columns').values

train_X
train_Y = train['target'].values
train_Y

#test dataset
test_X =test.drop('target',axis='columns').values
test_X
test_Y = test['target'].values
test_Y

y1 , y2 , y3 = oneHotEncoding(train_Y)

def train_SLP(X , y1 , y2 , y3 , epoch, rho):
  lr = 0.01
  number_of_features = X.shape[1]
  
  w1 = np.ones(shape=(number_of_features))*0.1
  b1 = 0.1
  
  w2 = np.ones(shape=(number_of_features))*0.1
  b2 = 0.1
  
  w3 = np.ones(shape=(number_of_features))*0.1
  b3 = 0.1
  
  error = []
  for i in range(epoch ):
    errorItr = 0;
    for j in range(len(X)):
       d1 = np.dot(w1, X[j].T) + b1
       d1 = 1 if d1 > 0 else 0
       d2 = np.dot(w2, X[j].T) + b3
       d2 = 1 if d2 > 0 else 0
       d3 = np.dot(w3, X[j].T) + b3
       d3 = 1 if d3 > 0 else 0
       
       errorItr = errorItr + ((d1- y1[j])*(d1 - y1[j]) + (d2- y2[j])*(d2 - y2[j]) + (d3- y3[j])*(d3 - y3[j]))/2
        
      #  print(w1) 
       w1 = w1 + lr*(y1[j] - d1)*X[j].T
      #  print(w1)
       b1 = b1 + (y1[j] - d1)
       
      #  print(w2)
       w2 = w2 + lr*(y2[j]- d2)*X[j].T
      #  print(w2)
       b2 = b2 + (y2[j]- d2)
       
      #  print(w3)
       w3 = w3 + lr*(y3[j]- d3)*X[j].T
      #  print(w3)
       b3 = b3 + (y3[j]- d3)
      
    if (errorItr < rho):
      return w1 , b1, w2 , b2 , w3 , b3
   
    
  return w1 , b1, w2 , b2 , w3 , b3   
       
  
def predict_Y(w1 , b1, w2 ,b2 , w3, b3 , X):
  y = []
  
  for i in range(len(X)):
    d1 = np.dot(w1, X[i].T) + b1
    
    d2 = np.dot(w2, X[i].T) + b3
  
    d3 = np.dot(w3, X[i].T) + b3
    
  
    if (d1 > d2 and d1 > d3):
      y.append(0)
    elif (d2 > d1 and d2 > d3):
      y.append(1)
    else :
      y.append(2)
   
  return y


from sklearn.metrics import accuracy_score
w1 , b1, w2 , b2 , w3 , b3   = train_SLP(train_X , y1 , y2, y3, 1000, 0.00001)
y_predicted = predict_Y(w1 , b1, w2 , b2 , w3 , b3 , test_X)
y_predicted = np.array(y_predicted)
print(y_predicted)
print(accuracy_score(  test_Y , y_predicted ))
