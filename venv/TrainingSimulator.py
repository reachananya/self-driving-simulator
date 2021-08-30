from utils import *

path = 'myData'
data = importDataInfo(path)

data = balanceData(date, display=False)

imagesPath, steering = loadData(path, data)


xTrain, xVal, yTrain, yVal = train_test_split(imagesPath, steerings, test_size=0.2,random_state=10)
print('Total Training Images: ',len(xTrain))
print('Total Validation Images: ',len(xVal))

