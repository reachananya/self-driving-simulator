import pandas as pd
import numpy as np 
import os 
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
imprt matplotlib.images as mpimg

def getName(filePath):
    return filePath.split('\')[-1]
                          
def importDataInfo(path):
    columns = ['Center', 'Left', 'Right', 'Steering', 'Throttle', 'Brake', 'Speed']
    data = pd.read_csv(os.path.join(path, 'driving_log.csv'), names = columns)
    #### REMOVE FILE PATH AND GET ONLY FILE NAME
    #print(getName(data['center'][0]))
    data['Center']=data['Center'].apply(getName)
    #print(data.head())
    print('Total Images Imported',data.shape[0])
    return data

    
                         
 def balanceData(data,display=True):
    nBin = 31
    samplesPerBin = 500
    hist, bins = np.histogram(data['Steering'], nBin)
    if display:
        center = (bins[:-1] + bins[1:]) * 0.5
        plt.bar(center, hist, width=0.06)
        plt.plot((np.min(data['Steering']), np.max(data['Steering'])), (samplesPerBin, samplesPerBin))
        plt.show()
                          
 removeindexList = []
    for j in range(nBin):
        binDataList = []
        for i in range(len(data['Steering'])):
            if data['Steering'][i] >= bins[j] and data['Steering'][i] <= bins[j + 1]:
                binDataList.append(i)
        binDataList = shuffle(binDataList)
        binDataList = binDataList[samplesPerBin:]
        removeindexList.extend(binDataList)
 
    print('Removed Images:', len(removeindexList))
    data.drop(data.index[removeindexList], inplace=True)
    print('Remaining Images:', len(data))
                          
    if display:
         hist, _ = np.histogram(data['Steering'], (nBin))
         plt.bar(center, hist, width=0.06)
         plt.plot((np.min(data['Steering']), np.max(data['Steering'])), (samplesPerBin, samplesPerBin))
         plt.show()
    return data
                          
def loadData(path, data):
  imagesPath = []
  steering = []
  for i in range(len(data)):
    indexed_data = data.iloc[i]
    imagesPath.append(f'{path}/IMG/{indexed_data[0]}')
    steering.append(float(indexed_data[3]))
   imagesPath = np.asarray(imagesPath)
   steering = np.asarray(steering)
   return imagesPath, steering
   



def augmentImage(imgPath,steering):
    img =  mpimg.imread(imgPath)
    print(np.random.rand(),np.random.rand(),np.random.rand(),np.random.rand())
    #PAN
    if np.random.rand() < 0.5:
          pan = iaa.Affine(translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)})
          img = pan.augment_image(img)
    #ZOOM
    if np.random.rand() < 0.5: 
          zoom = iaa.Affine(scale=(1, 1.2))
          img = zoom.augment_image(img)
    #BRIGHTNESS
    if np.random.rand() < 0.5:
          brightness = iaa.Multiply((0.2, 1.2))
          img = brightness.augment_image(img)
    #FLIP
    if np.random.rand() < 0.5:
          img = cv2.flip(img, 1)
          steering = -steering
    return img, steering
