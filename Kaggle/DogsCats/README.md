I have been thinking for so long to try Kaggle's Dogs vs Cats problem.  
It is a classification problem in which we train a neural network to learn from 1000s of images of cats and dogs and then classify unseen images of dogs and cats correctly.  
I found [this](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html) very useful blog on Keras which uses this same problem as an example for Keras.  
I implemented the code from the blog as is to understand how it is done using Keras.  
The blog has few parts in it and I have tried only the first.  
It needed one correction:  
```  
model.add(Conv2D(32, (3, 3), input_shape=(3, 150, 150)))
```  
In the above code, input shape is of the form: number of channels, dimensions of the image.  
But with TensorFlow as backend, the number of channels should come at the end as :
```
model.add(Conv2D(32, (3, 3), input_shape=(150, 150,3)))
```  
In the first part of the blog, using only 2000 images for training and 800 images for validation, an accuracy of 81% was achieved.  
This can be further improved using transfer learning which will be the next part.  