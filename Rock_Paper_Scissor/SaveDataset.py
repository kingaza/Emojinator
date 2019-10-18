from imageio import imread
import numpy as np
import pandas as pd
import os
root = './RPS_data/' # or ‘./test’ depending on for which the CSV is being created

# go through each directory in the root folder given above
values = []
for directory, subdirectories, files in os.walk(root):
# go through each file in that directory
    print(directory, subdirectories)
    
    for file in files:
        # read the image file and extract its pixels
        if file == '.DS_Store':
            break
        #print(file)
        
        im = imread(os.path.join(directory,file))
        value = im.flatten()
        label = directory.split('/')[-1]
        value = np.hstack((label,value))
        values.append(value)
values = np.asarray(values).astype('int')
print(values.shape)

np.save('dataset.npy', values)