
#___________________________________3. Logistic Regression____________________________
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split 
#------------------------------------------ dataset
ntotal=100
iris = datasets.load_iris()
data= iris.data[:ntotal, :2] 
label= iris.target[:ntotal]

X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.40, random_state=42)

# function defination
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def derivatives_sigmoid(z):
    return sigmoid(z) * (1 - sigmoid(z))

def loss(h, y):
    Error=1/2*pow(h-y,2)
    return Error  

def predict_prob(X):    
        return sigmoid(np.dot(X, weight))
    
def predict(X, threshold):
    return predict_prob(X) >= threshold

def accuracy(pred,acutal):
    count=0
    for i in range(len(acutal)):
        if (pred[i]==acutal[i]):
            count=count+1
    acc=(count/len(acutal))*100
    return acc   

# weights initialization
weight= np.random.uniform(0,1,X_train.shape[1])
lr=0.01
E_threshold=0.01

z = np.dot(X_train, weight)
h = sigmoid(z)
Err=loss(h,y_train).mean()
print("Loss with random weights",Err)
##______________________________________weight learning phase__________________________ 
count=0
while(Err > E_threshold):
    count=count+1
    z = np.dot(X_train, weight)
    h = sigmoid(z)
    Err = loss(h,y_train).mean()
    print("loss in",count,"th itration","is:-",Err)
    gradient = np.dot(X_train.T, (h - y_train)*derivatives_sigmoid(z)) 
    weight = weight- lr * gradient
  
#________________________________________testing phase__________________
# predict probability of test instances 
pred_y_prob=predict_prob(X_test)
# predict class label of test instances 
threshold=0.5
pred_y=1*(predict(X_test, threshold))

# Acuuray 
acc=accuracy(pred_y,y_test)
print('logistic regression accuracy with iris dataset',acc)
        