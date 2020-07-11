'''TESTING AND VERIFICATION
This is the testing block
Its just like image training block but it compares the generated test vectors with the classvectors using xor
and outputs the class which is most similar ie where the hamming distance is least
'''
import cv2
import numpy as np
import csv
from HD_image_HVECTOR_CREATE import *
from HD_image_MANIP import *

import time
start_time = time.time()                                                          #To find running time

L=l
width =50
num_pics= 700
num_class=8
num_pixel = 2500
pic_start_num = 200
correct =0

var_10k =[]
for i in range(num_pixel):
     var_10k.append(np.fromiter(var_str[i], dtype=int))


     
############     Address of the images    ##########    
#a="/home/adithya/Downloads/Gesture Image Pre-Processed Data/"                     #address of signlanguages
a="/home/adithya/Downloads/Gesture Image Pre-Processed Data/gesture/"            #address of gestures

for q in range(0,num_class):                                                      #classes 

     classvector=np.array([1])
     classvector =np.delete(classvector,0)      
     for i in range(L):
         classvector=np.append(classvector,0)     
     
     b=str(q)
     classaddr=a+b+'/'
    
     piccounter=np.array([1])
     piccounter =np.delete(piccounter,0)      
     for i in range(L):
         piccounter=np.append(piccounter,0)     
         
     for w in range(pic_start_num,pic_start_num + num_pics):
         picaddr= classaddr+str(w+1)+'.jpg'
         print(picaddr)
         gray = cv2.imread(picaddr)
         gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
         [row,col] = gray.shape[0:2]
         c = HD_img_make_binary(gray)
         c = HD_img_resize(a,c)
                
         app=np.array([1])
         app =np.delete(app,0)

         picvector=np.array([1])
         picvector =np.delete(picvector,0)
         for i in range(L):
             picvector=np.append(picvector,0)
     
         for i in range(0,row):    
             for j in range(0,col):
                 app=np.append(app,c[i,j])
                  
         subpiccounter=np.array([1])
         subpiccounter =np.delete(subpiccounter,0)
         for i in range(L):
             subpiccounter=np.append(subpiccounter,0)

                  
         for i in range(len(app)):
             if(app[i] == 0 ):                        
                 s = np.fromiter(var_10k[i], dtype=int) 
                 s = (np.roll(s , 0))                         
             else :
                 s = np.fromiter(var_10k[i], dtype=int) 
                 s = (np.roll(s , 1))
             subpiccounter = subpiccounter+ s
         
         for i in range(L):
             if(subpiccounter[i] >int(num_pixel/2)):                        
                 picvector[i]= 1
             elif(subpiccounter[i] <int(num_pixel/2)):
                 picvector[i]= 0
             else:
                 picvector[i]= np.random.randint(0,2)

         f = open("class_image.txt", "r")
         f.seek(0) 
    
         discounter=np.array([1])
         discounter =np.delete(discounter,0)
         for i in range(num_class):
             discounter=np.append(discounter,0)

         for i in range(num_class):
             K=  f.readline()                                                     #read class vectors from file
             K=K[:-1]
             C=np.fromiter(K,dtype=int)
             distance= picvector ^ C                                              #Xor is done to find the places where vectors differ
             for k in range(len(picvector)):
                 if(distance[k] == 1):                                            #this is done over all the class vectors 
                     discounter[i]+=1
         print(discounter)            
         result = np.where(discounter == np.amin(discounter))                     #checks to see if predicted value is same as actual value
         print("Predicted = ",result[0][0],"     ","Actual = " , q)
         if(result[0][0]== q):
             correct +=1

print("####################################################### ")    
print("Accuracy = " ,(correct/(num_pics*num_class))*100)                          #shows accuracy as percent
runtime= time.time() - start_time
rt= runtime/(num_pics * num_class)

#print("Time taken to run 1 sample image = " ,rt)                                  #shows average time to run one image
    
    
 
             
