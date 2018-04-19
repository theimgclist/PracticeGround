[https://www.pyimagesearch.com/2018/04/16/keras-and-convolutional-neural-networks-cnns/]    
This is the second of the 3-part series on building a dataset, training a CNN model with Keras and deploying the model to run on mobile.   
Since we’re using the TensorFlow backend, we arrange the input shape with “channels last” data ordering, but if you want to use “channels first” (Theano, etc.) then it is handled automatically.  
Typically you’ll use a dropout of 40-50% in our fully-connected layers and a dropout with much lower rate, normally 10-25% in previous layers (if any dropout is applied at all).  
Sklearn's train_test_split will split the dataset into train data and test data. To include a validation set, do the following:  
You would use scikit-learn’s train_test_split function twice. The first time you split the data into two splits: training and testing. To split data into train/val/test using scikit  
You then split a second time on the training data, creating another two splits: training and validation.  
This process will leave you with three splits: training, testing, and validation.  
  
