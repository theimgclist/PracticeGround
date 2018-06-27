This is the first part of a 3 blog series from PyImageSearch[click here](https://www.pyimagesearch.com/2018/06/11/how-to-build-a-custom-face-recognition-dataset/).  
Before we can train our model to recognize faces in images and video streams we first need to gather the dataset of faces itself.  
If you are already using a pre-curated dataset, such as Labeled Faces in the Wild (LFW), then the hard work is done for you.  
* [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/), a database of face photographs designed for studying the problem of unconstrained face recognition. 
* The data set contains more than 13,000 images of faces collected from the web. 
* Each face has been labeled with the name of the person pictured. 
* 1680 of the people pictured have two or more distinct photos in the data set. 
* The only constraint on these faces is that they were detected by the Viola-Jones face detector.   
We need to gather examples of faces we want to recognize and then quantify them in some manner.  
This process is typically referred to as facial recognition enrollment. We call it “enrollment” because we are “enrolling” and “registering” the user as an example person in our dataset and application.  
**Method #1: Face enrollment via OpenCV and webcam**  
This first method to create your own custom face recognition dataset is appropriate when:  
* You are building an “on-site” face recognition system
* And you need to have physical access to a particular person to gather example images of their face  

