'''HD_image_HVECTOR_CREATE
Used to generate the random hypervectors for the 50*50 template image
and store in file. This is done only once at the beginning of the process
From the file the vectors are then retrived and stored as a list for
use in the algorithm
'''
import numpy as np

l=50000                                                                           #size of Hvector
num_pixel =2500                                                                   #size of the image
fn = "cpixelvector_image.txt"                                                #file where stored

ch = input("Remake random vector ?")                                              #asks whether to remake the random vector initially
if(ch =='y'):
     var =[] 
     for i in range(0,num_pixel):
         var_i = np.random.randint(0,2,l)
         var.append(var_i)
       
     f = open(fn, "a")    
     for i in range(0,num_pixel):
         var_list = var[i].tolist()      
         for i in range(l):
             f.write(str(var_list[i]))                                            #writes vector to file 
         f.write("\n")
     f.close()
     
else:

     var_str = [] 
     f = open(fn, "r")                                                            #reads from file when algorithm runs
     var_str.append(f.readline(l))
     for x in f:
         var_str.append(f.readline(l))






          
                  
   



