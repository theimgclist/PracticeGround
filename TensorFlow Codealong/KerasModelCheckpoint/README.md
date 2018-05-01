[https://machinelearningmastery.com/check-point-deep-learning-models-keras/]  
Running a Deep Learning model can take time. Model training can stop for various reasons.  
It is a good practice to save the model weights from time to time so that training can be resumed from the learnt weights.  
I found a blog on machinelearningmastery which explains this process very well.  
One way to save the weights is to take a new snapshot whenver there is an improvement in the chosen metric.  
The other approach is to save the snapshot to the same file everytime there is an improvement.  
