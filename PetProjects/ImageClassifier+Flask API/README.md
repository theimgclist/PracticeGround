[https://deeplearningsandbox.com/how-to-build-an-image-recognition-system-using-keras-and-tensorflow-for-a-1000-everyday-object-559856e04699]  

I tried to take the code and run it on Colab:
+ This has very easy to follow code, for image classification
+ If one of the features has a broad range of values, the distance will be governed by this particular feature. Therefore, the range of all features should be normalized so that each feature contributes approximately proportionately to the final distance. This is called data normalization
+ Zero-centering is subtracting mean from data (so that it’s mean is 0).
+ %matplotlib is a magic function in IPython -> this wont work when run through Python. It works in IPython or Jupyter
+ Jupiter Notebook has features that aren't part of the Python language itself. All the %-prefixed commands are special extensions, not regular Python statements.
+ !wget https://github.com/DeepLearningSandbox/DeepLearningSandbox/blob/master/image_recognition/classify.py -> use wget to download any files into Colab
+ !python neuralnet.py --image_url http://i.imgur.com/wpxMwsR.jpg -> this builds the model and classifies but doesnt display plots, since %matplotlib inline doesnt work with Python
+ %%writefile neuralnet.py -> use it at the top of cell to save the contents of the cell into the file neuralnet.py
+ https://stackoverflow.com/a/30250285/3464843
+ %run classify.py --image_url http://i.imgur.com/wpxMwsR.jpg -> runs the file as if its run as "python filename args" from shell
+ from IPython import get_ipython  CORRECTION - %matplotlib is not working with %run too. Using this alternate line of code fixed it
	``` get_ipython().run_line_magic('matplotlib', 'inline')```
+ Its working!!! Easy to code and understand. Perfect.


Note that ImageNet was not designed for face recognition. It is better to test with a picture of an elephant, a dog, or a cat.
