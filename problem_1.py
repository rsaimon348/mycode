import os  


l = list()

def subDir(dirName):
    for path,dname,fname in os.walk(dirName,topdown=True):
        #print (os.path.basename(path),end=',')
        l.append(os.path.basename(path))
        for d in dname:
            subDir(d)
        
if __name__ == "__main__":
    
    path = input ("please enter a path:")
    
    if os.path.exists(path):
        subDir(path)
        print (','.join(l))
    else:
        print ("directory does not exist")    
    
    
    # for item in l:
    #     print(item,end=',')
    # #print (l)

       