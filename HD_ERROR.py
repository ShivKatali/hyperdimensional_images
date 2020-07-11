import numpy as np

fromc = "class_image.txt"
toc = "class_gesture_error.txt"

num_class =8
el= 3000
N=10000

f = open(fromc, "r")
g = open(toc, "a")

for i in range(0,num_class):
    K=  f.readline()
    K=K[:-1]
    C=np.fromiter(K,dtype=int)
    C= C[0:7000]
    var =[]
    var=np.array([1])
    var =np.delete(var,0)                                         #define classvector
    
    #for i in range(0,el):
    var_i = np.random.randint(0,2,el)
    var= np.append(var,var_i)

    D=np.concatenate([C,var])
    print(D)
    
    #g = open(toc, "a")    
    #for i in range(0,N):
    E = D.tolist()
    print(len(E))
       
    for i in range(N):
        g.write(str(E[i]))
        
    g.write("\n")

g.close()
f.close()    
