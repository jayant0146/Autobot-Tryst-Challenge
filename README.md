# TAB-015
Here is the code for the Auto Bot Challenge round 1 organised by IITD

Here is the link of the modified dataset by us  :https://drive.google.com/drive/folders/1PJsilddU8IkRs8yWibiREoeccWnBLXh7?usp=sharing

In the above link we have dataset combined of all the five categories and the video of the lane.



main.ipynb : 
1.  We have copied the dataset of all the 5 folders (animals, person, cones, traffic Lights, stop) into a single folder named datset.
2.  And in this folder dataset we have renamed all the images of people dataset as people (1), people (2) etc... Similarly with the other classes we have done this renaming.
3.  Then we have divided the total datset into a training and testing part. 
4.  Then trained the model and 
5.  Further then saved the trained model under the folder Saved_Model with the name **model.h5**




lane_detection.py:
1. Firstly imported the required Libraries like cv2, numpy, matplotlib.pylab etc..
2. Then defined the function to get the interested region named as the region of interest 
3. And defined the function for the edged lines
4. Then tested the provided video 


