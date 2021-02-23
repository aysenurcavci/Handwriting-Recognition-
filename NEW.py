# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:41:35 2021

@author: aysenur
"""

import tflearn
import numpy as np
import scipy

import tflearn.datasets.mnist as mnist
from tensorflow import reset_default_graph
reset_default_graph()

X , Y , testX , testY = mnist.load_data(one_hot = True)

input_layer = tflearn.input_data(shape = [None,784])
hidden_layer1 = tflearn.fully_connected(input_layer , 128 , activation='relu' , regularizer = 'L2' , weight_decay = 0.001 )
dropout1 = tflearn.dropout(hidden_layer1 , 0.8)


hidden_layer2 = tflearn.fully_connected(dropout1 , 128 , activation='relu' , regularizer = 'L2' , weight_decay = 0.001 )
dropout2 = tflearn.dropout(hidden_layer2 , 0.8)

softmax = tflearn.fully_connected(dropout2, 10 ,activation = 'softmax')

sgd = tflearn.SGD(learning_rate=0.01 , lr_decay=0.96 , decay_step=1000)
top_k = tflearn.metrics.Top_k(3)
net  = tflearn.regression(softmax , optimizer=sgd , metric= top_k , loss = 'categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_verbose=0)
model.fit(X, Y, n_epoch=10, validation_set=(testX, testY), show_metric=True, run_id='dense_model')

cizim = np.vectorize(lambda x:255-x)(np.ndarray.flatten(scipy.ndimage.imread("deneme2.png" , flatten=True)))
cizim = np.array(cizim).reshape(1,784)

print (model.predict(cizim))
