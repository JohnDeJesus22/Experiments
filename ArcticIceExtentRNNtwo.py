# test from mapr blog of rnn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# generate data
arctic_ice = pd.read_excel('https://query.data.world/s/nru6ghqqozkuhofruvudxegtcbveg3')

# make the Date column in index and then drop the date column.
arctic_ice.index = pd.to_datetime(arctic_ice['Date'])
arctic_ice=arctic_ice.drop(['Date'],axis=1)

arctic_ice.columns = ['Extent (million sq km)']

# convert data for batches
measurements = arctic_ice.loc[:,'Extent (million sq km)'].values
measurements = np.array(measurements)
num_periods = 12
f_horizon = 1

ms_length = len(measurements)
x_data = measurements[:(ms_length-(ms_length % num_periods))]
x_batches = x_data.reshape(-1, num_periods, 1)

y_data = measurements[1:(ms_length-(ms_length % num_periods)) + f_horizon]
y_batches = y_data.reshape(-1, num_periods, 1)
print(len(x_batches))

# create test data
def test_data(series, forecast, num_periods):
    test_x_setup = measurements[-(num_periods + forecast):]
    testX = test_x_setup[:num_periods].reshape(-1,num_periods,1)
    testY = measurements[-(num_periods):].reshape(-1,num_periods,1)
    return testX, testY

X_test, y_test = test_data(measurements,f_horizon, num_periods)


# set up rnn
tf.reset_default_graph()
inputs = 1
hidden = 100
learning_rate = 0.001
output = 1

X = tf.placeholder(tf.float32,[None, num_periods, inputs])
y = tf.placeholder(tf.float32,[None, num_periods, inputs])

basic_cell1 = tf.nn.rnn_cell.BasicRNNCell(num_units = hidden, activation = tf.nn.relu)
rnn_output, states = tf.nn.dynamic_rnn(basic_cell1, X, dtype = tf.float32)
#basic_cell2 = tf.nn.rnn_cell.BasicRNNCell(num_units = hidden, activation = tf.nn.relu)
#rnn_output, states = tf.nn.bidirectional_dynamic_rnn(basic_cell1, basic_cell2,
                                                     #X, dtype = tf.float32)

stacked_rnn_output = tf.reshape(rnn_output, [-1, hidden])
stacked_outputs = tf.layers.dense(stacked_rnn_output, output)
outputs = tf.reshape(stacked_outputs, [-1, num_periods, output])

loss = tf.reduce_sum(tf.square(outputs-y))
optimizer = tf.train.AdamOptimizer(learning_rate = learning_rate)
training_op = optimizer.minimize(loss)

init = tf.global_variables_initializer()

saver = tf.train.Saver()

# run session and make predictions
epochs = 1000

with tf.Session() as sess:
    
    init.run()
    
    for ep in range(epochs):
        sess.run(training_op, feed_dict={X: x_batches, y: y_batches})
        
        if ep % 100 == 0:
            mse = loss.eval(feed_dict={X: x_batches, y: y_batches})
            print(ep, "\tMSE:", mse)
    saver.save(sess, './arctic_ice_rnn_model_improvement')
    
    y_pred = sess.run(outputs, feed_dict={X: X_test})
    print(y_pred)

    
    
# plot results
plt.title('Forecast vs Actual', fontsize = 14)
plt.plot(pd.Series(np.ravel(y_test)),markersize=10,label = 'Actual')
plt.plot(pd.Series(np.ravel(y_pred)),markersize=10, label = 'Forecast')
plt.legend()
plt.xlabel('Time Periods',fontsize = 12)
plt.show()