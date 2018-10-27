# Tensorflow RNN practice

# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from os import chdir
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error 

# change directory
chdir('D:\\Data Science Class Files\\TensorFlow\\04-Recurrent-Neural-Networks')

# load data with index set to 'Month'
data = pd.read_csv('monthly-milk-production.csv', index_col = 'Month')

# change index to datetime
data.index = pd.to_datetime(data.index)

# plot the data
plt.plot(data, label = 'Milk Production')
plt.show()

# split data so that test set is the last 12 months of milk productions
training_set = data.head(156)
test_set = data.tail(12)

# feature scale the data by fitting to the training set
scaler = MinMaxScaler()
train_scaled = scaler.fit_transform(training_set)
test_scaled = scaler.transform(test_set)

# create batch function to input batches into model
def next_batch_function(training_data, batch_size, steps):
    
    '''
    initiate a random starting point in the data.
    index the data and reshape.
    return batches reshaped for RNN (current minus the last point and prediction
    without the first data pt).
    '''
    rand_start = np.random.randint(0,len(training_data)-steps)
    
    y_batch = np.array(training_data[rand_start:rand_start+steps+1]).reshape(1,steps+1)
    
    return y_batch[:,:-1].reshape(-1,steps,1), y_batch[:,1:].reshape(-1,steps,1)
    
# setup constant values
num_inputs = 1
num_time_steps = 12
num_neurons_per_layer = 200
num_outputs = 1
learning_rate = 0.04
num_iterations = 4000
batch_size = 1

# initiate placeholders
X = tf.placeholder(tf.float32,[None,num_time_steps, num_inputs])
y = tf.placeholder(tf.float32,[None,num_time_steps, num_outputs])

# create RNN layer, had to update dask to remove an attribute error with pandas.core
rnn_layer = tf.nn.rnn_cell.LSTMCell(name='basic_lstm_cell',
                                    num_units = num_neurons_per_layer,
                                         activation = tf.nn.relu)
cell = tf.contrib.rnn.OutputProjectionWrapper(rnn_layer,output_size = num_outputs)

# setup dynamic_rnn
output, states = tf.nn.dynamic_rnn(cell, X, dtype = tf.float32)

# setup loss of mse
loss = tf.reduce_mean(tf.square(output-y))

# setup optimizer
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate)
training = optimizer.minimize(loss)


# initiate variables
init = tf.global_variables_initializer()

# initiate saver
saver = tf.train.Saver()

# session
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.9)
with tf.Session(config=tf.ConfigProto(gpu_options=gpu_options)) as sess:
    
    sess.run(init)
    
    for iteration in range(num_iterations):
        
        X_batch, y_batch = next_batch_function(train_scaled,batch_size, num_time_steps)
        sess.run(training, feed_dict={X: X_batch, y: y_batch})
        
        if iteration % 100 ==0:
            mse = loss.eval(feed_dict={X: X_batch,y:y_batch})
            print(iteration, '\tMSE', mse)
            
        
    saver.save(sess, './john_rnn_milk_model2')
    
# showing testset
plt.plot(test_set,label = 'Last Year of Productions')
plt.show()

# restore saved session (model designed for single step predictions, not 12 step)
with tf.Session() as sess:
    saver.restore(sess,'./john_rnn_milk_model2')
    
    train_list = list(train_scaled[-12:])
    
    for iteration in range(12):
        X_new = np.array(train_list[-num_time_steps:]).reshape(1,num_time_steps,1)
        y_pred = sess.run(output,feed_dict={X: X_new})
        
        train_list.append(y_pred[0,-1,0])

# inverse transform test and results
results = scaler.inverse_transform(np.array(train_list[12:]).reshape(12,1))
test_reversed = scaler.inverse_transform(np.array(test_scaled))

# Append the results to the dataframe
test_set['Generated'] = results

# plot the results to the original
test_set.plot()

# evaluate model (want as close to zero as possible)
error = mean_squared_error(test_set['Milk Production'],test_set['Generated'])
