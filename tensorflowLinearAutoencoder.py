#Linear Autoenconder for dimensionality reduction

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.contrib.layers import fully_connected


# setup data with 30 features and two output classes
data = make_blobs(n_samples = 100, n_features = 30, centers = 2, random_state = 2)

# feature scale data
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data[0])

# defining numbers for layera
num_inputs = 30
num_hidden = 2
num_outputs = num_inputs
learning_rate = 0.05

# setup place holder
X = tf.placeholder(tf.float32,shape = [None, num_inputs])

# setup hidden layer 
hidden = fully_connected(X,num_hidden, activation_fn = None)

# setup output layer
outputs = fully_connected(hidden, num_outputs, activation_fn = None)

# setup loss with mse
loss = tf.reduce_mean(tf.square(outputs-X))

# setup optimizer
optimizer = tf.train.AdamOptimizer(learning_rate)
train = optimizer.minimize(loss)

# initiate global variables
init = tf.global_variables_initializer()


# initate number of steps
num_steps = 1000

# run session
with tf.Session() as sess:
    
    # run init
    sess.run(init)
    
    # iterate
    for step in range(num_steps):
        sess.run(train, feed_dict ={X:scaled_data})
        
    # get output
    output_2d = hidden.eval(feed_dict = {X:scaled_data})
    
# plot new features
plt.scatter(x = output_2d[:,0], y = output_2d[:,1], c = data[1])
plt.title('Plot of New Autoencoded Features')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# classes where clearly separated. defintely linearly separable..

