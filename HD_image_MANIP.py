'''HD_IMAGE_MANIPULATION_FUNCTION
Contains two functions for performing image manipulation of the images
HD_image_resize() is used to resize the image so the hand feature is visible and prominant
It cuts off the black area of the edges and resizes the image back to 50*50

HD_make_binary() converts all values to either 0 or 255
'''

import  cv2
import numpy as np
import csv

def HD_img_resize(ad,c):

     [row,col] = c.shape[0:2]        
                
     ind=np.array([1])
     ind =np.delete(ind,0)
         
     for i in range(row):
         count = np.count_nonzero(c[i]) 
         if (count < 3):
             ind = np.append(ind , i)           
         c = np.delete(c , ind ,0)

         ind=np.array([1])
         ind =np.delete(ind,0)
         [row,col] = c.shape[0:2]
         
         for i in range(col):
             count = np.count_nonzero(c[:,i]) 
             if (count < 3):
                 ind = np.append(ind , i)        
            
         c = np.delete(c , ind ,1)
         [row,col] = c.shape[0:2]
         
         c= cv2.resize(c,(50,50))
         [row,col] = c.shape[0:2]
         for i in range(row):    
             for j in range(col):
                 c[i,j]= 0 if (c[i,j]<120) else 255
         
         return(c) 


def HD_img_make_binary(gray_img):
     [row,col] = gray_img.shape[0:2]
     for i in range(row):    
         for j in range(col):
             gray_img[i,j]= 0 if (gray_img[i,j]<128) else 255
     return(gray_img)




