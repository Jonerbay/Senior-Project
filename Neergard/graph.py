import csv
import matplotlib.pyplot as plt
import numpy as np
file = open("values.csv","r")
alllines = file.readlines()
lines = [[],[],[],[]]
i = 0
for line in alllines:
    values = line.split(',')
    for l in values:
        if l[-1] == '\n':
            l = l[:-1]
        lines[i].append(float(l))
    i+=1
trainLoss = lines[0]
trainAUC = lines[1]
validLoss = lines[2]
validAUC = lines[3]
epochs = np.arange(1,len(trainLoss)+1)

plt.plot(epochs,trainAUC)
plt.plot(epochs,validAUC)
plt.title('model\'s AUC ')
plt.ylabel('AUC')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(epochs,trainLoss)
plt.plot(epochs,validLoss)
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
