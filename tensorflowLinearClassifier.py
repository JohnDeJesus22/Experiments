import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
from os import chdir

chdir('D:\\Data Science Class Files\\TensorFlow\\02-TensorFlow-Basics')

# import data
data = pd.read_csv('census_data.csv')

# encode classes into zeros and ones
labelencoder_brackets = LabelEncoder()
data['income_bracket'] = labelencoder_brackets.fit_transform(data['income_bracket'])

# split data
x_data = data.drop('income_bracket',axis=1)
y_val = data['income_bracket']

x_train, x_test,y_train, y_test = train_test_split(x_data, y_val,
                                                    test_size =0.3, random_state=1)

# feature scale numeric data
continuous_features = ['age','education_num','capital_gain','capital_loss','hours_per_week']

scaler = MinMaxScaler()
scaler.fit(x_train[continuous_features])
x_train[continuous_features] = pd.DataFrame(data=scaler.transform(x_train[continuous_features]),
       columns = continuous_features,index=x_train.index)
x_test[continuous_features] = pd.DataFrame(data=scaler.transform(x_test[continuous_features]),
      columns = continuous_features,index=x_test.index)

# set up tf.estimator inputs

# continuous variables
age = tf.feature_column.numeric_column('age')
education_num = tf.feature_column.numeric_column('education_num')
capital_gain = tf.feature_column.numeric_column('capital_gain')
capital_loss = tf.feature_column.numeric_column('capital_loss')
hours_per_week = tf.feature_column.numeric_column('hours_per_week')

# categorical variables
workclass = tf.feature_column.categorical_column_with_hash_bucket('workclass',
                                        hash_bucket_size = len(data.workclass.unique()))
education = tf.feature_column.categorical_column_with_hash_bucket('education',
                                        hash_bucket_size = len(data.education.unique()))
marital_status = tf.feature_column.categorical_column_with_hash_bucket('marital_status',
                                        hash_bucket_size = len(data.marital_status.unique()))
relationship = tf.feature_column.categorical_column_with_hash_bucket('relationship',
                                        hash_bucket_size = len(data.relationship.unique()))
race = tf.feature_column.categorical_column_with_hash_bucket('race',
                                        hash_bucket_size = len(data.race.unique()))
gender = tf.feature_column.categorical_column_with_hash_bucket('gender',
                                        hash_bucket_size = 2 )
native_country = tf.feature_column.categorical_column_with_hash_bucket('native_country',
                                        hash_bucket_size = len(data.native_country.unique()))

# List of features
feat_columns = [age, education_num, capital_gain, capital_loss, hours_per_week,
                workclass, education, marital_status, relationship, race,
                gender, native_country]

# Intiate Estimator
estimator = tf.estimator.LinearClassifier(feature_columns = feat_columns, n_classes = 2)

# Set up imput and test functions
train_input_func = tf.estimator.inputs.pandas_input_fn(x = x_train, y = y_train, batch_size = 100,
                                                num_epochs = 1000, shuffle = True)

test_input_func = tf.estimator.inputs.pandas_input_fn(x = x_test, y= y_test, batch_size = 100,
                                                num_epochs = 1, shuffle = False)

# train the classifier
estimator.train(input_fn = train_input_func,steps = 10000)

# get results
results = estimator.evaluate(test_input_func)
'''
{'accuracy': 0.81625551,
 'accuracy_baseline': 0.7728529,
 'auc': 0.8354404,
 'auc_precision_recall': 0.61268145,
 'average_loss': 0.41177276,
 'global_step': 1000,
 'label/mean': 0.2271471,
 'loss': 4.1173062,
 'precision': 0.64077026,
 'prediction/mean': 0.2791642,
 'recall': 0.43488058}
'''

# test classifier
predict = estimator.predict(test_input_func)

# get test results
classifications = list(predict)

final_classifications = []
for pred in classifications: 
    final_classifications.append(pred['class_ids'][0])
    
# get accuracy score
accuracy_score(y_test,final_classifications)
# 0.8279250690961204

# get classification report
classification_report(y_test, final_classifications)
'''
            precision    recall  f1-score   support
         0       0.85      0.94      0.89      7550
         1       0.69      0.44      0.54      2219
     total       0.81      0.83      0.81      9769'
'''

