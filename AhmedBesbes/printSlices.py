import matplotlib.pyplot as plt
import numpy as np
import sys


if len(sys.argv) != 4:
    raise Exception("No arguments are presented")
numberOfSlices = int(sys.argv[3])
axe = str(sys.argv[1])
fileNum = str(sys.argv[2])
axes = ["sagittal","axial","coronal"]

if axe not in axes:
    raise Exception("Right axe is not present")

path = "/home/snake/Desktop/mrnet/data/train/" + axe + "/" + fileNum + ".npy"

series = np.load(path)

if numberOfSlices > len(series):
    raise Exception("Number of slices greater than in file %d vs %d" % (numberOfSlices,len(series)))
series = series[:numberOfSlices]

fig = plt.figure(figsize=(20, 6))
for i in range(numberOfSlices):
    for _,image in enumerate(series[i:i+1]):
        plt.imshow(image,cmap='gray')
        plt.savefig("images/Slice" + str(i) + "-" + axe +"-"+fileNum+".png",bbox_inches='tight')
plt.clf()
for i, image in enumerate(series):
    ax = fig.add_subplot(1, numberOfSlices, i + 1, xticks=[], yticks=[])
    plt.imshow(image, cmap='gray')
    plt.axis('off');
plt.show()
