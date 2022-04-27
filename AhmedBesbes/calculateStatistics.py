import csv
import pandas as pd

data = pd.read_csv("dash/val_data.csv")
labels = data.loc[:,"labels"]
preds = data.loc[:,"preds"]
trueNegative = 0
truePositive = 0
falsePositive = 0
falseNegative = 0
for i in range(len(labels)):
    if labels[i] == 0.0 and preds[i] < 0.5:
        trueNegative+=1
    elif labels[i] == 0.0 and preds[i] >= 0.5:
        falsePositive +=1
    elif labels[i] == 1.0 and preds[i] >= 0.5:
        truePositive+=1
    elif labels[i] == 1.0 and preds[i] < 0.5:
        falseNegative+=1
sens = truePositive/(truePositive+falseNegative)
spec = trueNegative/(trueNegative+falsePositive)
print("Sensitivity score =",sens)
print("Specificity score =",spec)
