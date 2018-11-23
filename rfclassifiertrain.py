# Random Forest Classifier Deployed

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# load data
iris = load_iris()
X= iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    random_state = 42,
                                                    test_size = 0.5)
# Build model
classifier = RandomForestClassifier(n_estimators = 10)
classifier.fit(X_train, y_train)

predicted = classifier.predict(X_test)

# check accuracy
print(accuracy_score(predicted, y_test))

import pickle 
# create binary file of python object for reuse later in our api
with open('D:\Data Science Class Files\ML Deployment\\rf.pkl','wb') as model_pkl: # write binary
    pickle.dump(classifier,model_pkl) # need to include file name and double forward slash before
                                        # file name
