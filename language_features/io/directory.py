import os
 
def main():
    
    # Create directory
    dirName = 'tempDir'
    
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")        
    
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")
    
    # Delete directory
    if os.path.exists(dirName):
        os.removedirs(dirName)
        print("Directory " , dirName ,  " deleted ")
    
    dirName = 'tempDir2/temp2/temp'
    
    # Create target directory & all intermediate directories if don't exists
    try:
        os.makedirs(dirName)    
        print("Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")  
        
    
    # Create target directory & all intermediate directories if don't exists
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")    
    
    # Delete directory
    if os.path.exists(dirName):
        os.removedirs(dirName)
        print("Directory " , dirName ,  " deleted ")
    
if __name__ == '__main__':
    main()