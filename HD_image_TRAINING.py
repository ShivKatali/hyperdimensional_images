'''TRAINING FILE
This is the training block it takes images from the pre processed image directory
and computes the classvector it can work with just one image per class
or several images per class which can be modified by changing the value
of num_pics to the required number of training images and uncommenting
the line A and commenting out B

Algorithm involves assigning a 10000 bit random Hvector to each pixel of a 50X50
image and performing cyclic rotation depending on if the pixel is white or black
(where white has no rotation and black is rotated once)
All the pixel vectors are accumulated and applied to a threshhold detector to get the picvector 
'''


import cv2
import numpy as np
import csv
import time
start_time = time.time() 

from HD_image_HVECTOR_CREATE import *
from HD_image_MANIP import *


               #####    address of the image file    ######
a="/home/adithya/Downloads/Gesture Image Pre-Processed Data/gesture/"                     #address of images
#a="/home/adithya/Downloads/Gesture Image Pre-Processed Data/gesture/"            #address of gestures

L=l                                                                           #vector size
num_pics=1                                                                        #number of images per class
num_class=8                                                                      #number of classes
num_pixel = 2500                                                                  #number of pixels (50*50)

var_10k =[]
for i in range(num_pixel):                                                        #stores hypervector for each pixel
     var_10k.append(np.fromiter(var_str[i], dtype=int))

start_time = time.time() 

for q in range(0,num_class):                                                      #to iterate over the classes 

     classvector=np.array([1])
     classvector =np.delete(classvector,0)                                        #define classvector
     for i in range(L):
         classvector=np.append(classvector,0)     
     
     b=str(q)
     classaddr=a+b+'/'
    
     piccounter=np.array([1])
     piccounter =np.delete(piccounter,0)                                          #define a counter to count multiple picture vactors
     for i in range(L):
         piccounter=np.append(piccounter,0)     
     
     for w in range(num_pics):                                                    #iterate over the pictures of a class
         picaddr= classaddr+str(w+1)+'.jpg'                                       #address of picture
         print(picaddr)
         gray = cv2.imread(picaddr)
         gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)                            #convert to grayscale if not  
         [row,col] = gray.shape[0:2]
         c = HD_img_make_binary(gray)                                             #grayscale is converted to binary ie only black(0) or white(255)
         c = HD_img_resize(a,c)                                                 #resize the image to make the required feature prominant

         picvector=np.array([1])                                                  #declare picvector
         picvector =np.delete(picvector,0)
         for i in range(L):
             picvector=np.append(picvector,0)
        
         subpiccounter=np.array([1])                                              #declare subpiccounter accumulating all pixelvectors in case of multiple images 
         subpiccounter =np.delete(subpiccounter,0) 
         for i in range(L):
             subpiccounter=np.append(subpiccounter,0)
   
         app=np.array([1])                                          
         app =np.delete(app,0)
         
         for i in range(0,row):     
             for j in range(0,col):
                 app=np.append(app,c[i,j])
        
         for i in range(len(app)):                                                #Performs cyclic shif based on pixel values
             s = np.fromiter(var_10k[i], dtype=int) 
             if(app[i] != 0 ):               
                 s = (np.roll(s , 1))
                           
             subpiccounter = subpiccounter+ s
          
         for i in range(L):
             if(subpiccounter[i] >int(num_pixel/2)):                              #majority function and threshholding
                 picvector[i]= 1
             elif(subpiccounter[i] <int(num_pixel/2)):
                 picvector[i]= 0
             else:
                 picvector[i]= np.random.randint(0,2)

         for k in range(L):                                                       #if multiple images are used a counter is needed 
             if(picvector[k] == 1):
                 piccounter[k]+=1
         
     for i in range(L):                                                           #calculate classvector from picvector
         #if(piccounter[i] >= int(num_pics/2)+1):                                 #this is if multiple pictures are used per class  ---------A
         if(picvector[i] ==1):                                                    #this is used if just a single image is used per class,----B
             classvector[i]= 1
         else:
             classvector[i]= 0
              
    
     print("trained")
     #print("classvector=",classvector)
     classvector=classvector.tolist()
     f = open("class_image.txt", "a")                                #Write classvector to txt file
     for i in range(L):
         f.write(str(classvector[i]))
     f.write("\n")  
     f.close()     




runtime= time.time() - start_time
rt= runtime/(num_pics * num_class)


print("######################################################## ") 
print("Time taken to run 1 sample image = " ,rt)  

