# tensorflow experimentation

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from os import chdir

chdir('D:\\Data Science Class Files\\TensorFlow\\02-TensorFlow-Basics')

data = pd.read_csv('cal_housing_clean.csv')

# clean/set up data
features = ['housingMedianAge', 'totalRooms', 'totalBedrooms', 'population',
       'households', 'medianIncome']

x_data = data.drop('medianHouseValue',axis=1)
y_val = data['medianHouseValue']

# split data
x_train, x_test,y_train, y_test = train_test_split(x_data, y_val,
                                                    test_size =0.3, random_state=1)

# feature scale data
scaler = MinMaxScaler()
scaler.fit(x_train)# do this separately from transform, do not do fit_transform
x_train = pd.DataFrame(data=scaler.transform(x_train),columns = x_train.columns,index=x_train.index)
x_test = pd.DataFrame(data=scaler.transform(x_test),columns = x_test.columns,index=x_test.index)

# set up tf.estimator inputs and outputs
age = tf.feature_column.numeric_column(key='housingMedianAge',dtype=tf.float64)
room = tf.feature_column.numeric_column(key='totalRooms',dtype=tf.float64)
pop = tf.feature_column.numeric_column(key='population',dtype=tf.float64)
bedrooms = tf.feature_column.numeric_column(key='totalBedrooms',dtype=tf.float64)
households =tf.feature_column.numeric_column(key='households',dtype=tf.float64)
income = tf.feature_column.numeric_column(key='medianIncome',dtype=tf.float64)
feature_columns = [age, room, bedrooms, pop, households, income]

# intiate estimator

estimator = tf.estimator.DNNRegressor(hidden_units = [6,6,6],feature_columns = feature_columns)

# create input functions
train_input_func = tf.estimator.inputs.pandas_input_fn(x=x_train,y= y_train,
                                                 batch_size = 10, num_epochs = 100,
                                                 shuffle = True)

test_input_func = tf.estimator.inputs.pandas_input_fn(x=x_test,
                                                 batch_size = 10, num_epochs = 100,
                                                 shuffle = False)

# train the model
estimator.train(input_fn = train_input_func,steps = 20000)

# test the model
predict = estimator.predict(test_input_func)

# get predictions
predictions = list(predict)

final_predictions = []
for pred in predictions[613008:]: #split predictions due to number of epochs
    final_predictions.append(pred['predictions'])
    
# determine the mean squared error
mean_squared_error(y_test,final_predictions)**0.5

# plot mse over epochs
all_predictions = []
for pred in predictions: 
    all_predictions.append(pred['predictions'])
    

mses = []
epoch = [i for i in range(1,101)]
for i in range(0,len(predictions)-6192,6192):
    prediction_set = all_predictions[i:i+6192]
    mses.append(mean_squared_error(y_test,prediction_set)**0.5)
    
plt.plot(mses)
plt.title('Mean Square Errors on Test Set of DNNRegressor')
plt.xlabel('Epoch Number')
plt.ylabel('MSE')
plt.show()
    
