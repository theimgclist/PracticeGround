[https://www.pyimagesearch.com/2018/04/09/how-to-quickly-build-a-deep-learning-image-dataset/]    
This is the first of the 3-part series on building a dataset, training a CNN model with Keras and deploying the model to run on mobile.   
[https://github.com/hardikvasa/google-images-download] --> an alternate for image scraping that was suggested in the comments.   
Bing Image Search API gives 30days of free trial.  
It's very easy to use since it avoids the manual web scraping.  
Once the data is collected, though most of the images returned from the API are relevant, it needs some searching.  
Search for any irrelevant images and also duplicates and remove if any such exist.  
This is important because the presence of any irrelevant data will effect model accuracy.  
Garbage in = Garbage out.  
The code is very informative - how to use an api key to get the data from URL, handling exceptions and downloaing the data.  
I can use this as a template for downloading image data for any practice projects.