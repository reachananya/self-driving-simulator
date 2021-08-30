from utils import *

path = 'myData'
data = importDataInfo(path)

data = balanceData(date, display=False)

loadData(path,data)
